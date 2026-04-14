## NVIDIA DKMS package, based on the work of Negativo17 with tweaks for Terra.

%global debug_package %{nil}
%global modulename nvidia

Name:           dkms-%{modulename}
Version:        595.58.03
Release:        1%{?dist}
Summary:        NVIDIA display driver kernel module
Epoch:          3
License:        NVIDIA License
URL:            https://www.nvidia.com/object/unix.html
Source0:        https://github.com/NVIDIA/open-gpu-kernel-modules/archive/%{version}/open-gpu-kernel-modules-%{version}.tar.gz
Source1:        %{name}.conf
Patch0:         https://github.com/CachyOS/open-gpu-kernel-modules/commit/211f012865b8ea2ba62c3422f5519cb32395c3e0.patch
Patch1:         https://github.com/CachyOS/open-gpu-kernel-modules/commit/92789a5709f64008bee34bb044e33a3de9702eb7.patch
BuildRequires:  sed
Requires:       %{modulename}-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Provides:       %{modulename}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-open = %{?epoch:%{epoch}:}%{version}
Obsoletes:      %{name}-open < %{?epoch:%{epoch}:}%{version}
Conflicts:      akmod-%{modulename}
Conflicts:      %{modulename}-kmod-580xx
# Unlike most DKMS packages, this package is NOT noarch!
ExclusiveArch:  x86_64 aarch64
Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
This package provides the NVIDIA kernel driver modules.

%prep
%autosetup -p1 -n open-gpu-kernel-modules-%{version}

cp -f %{SOURCE1} dkms.conf

sed -i -e 's/__VERSION_STRING/%{version}/g' dkms.conf

%build

%install
# Create empty tree:
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
cp -fr * %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
rm -f %{buildroot}%{_usrsrc}/%{modulename}-%{version}/*/dkms.conf

%post
dkms add -m %{modulename} -v %{version} -q --rpm_safe_upgrade || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{modulename} -v %{version} -q --force
dkms install -m %{modulename} -v %{version} -q --force

%preun
# Remove all versions from DKMS registry:
dkms remove -m %{modulename} -v %{version} -q --all --rpm_safe_upgrade || :

%files
%{_usrsrc}/%{modulename}-%{version}

%changelog
* Mon Apr 13 2026 Gilver E. <roachy@fyralabs.com> - 3:595.58.03-1
- Update patches for DSC functionality
- Update spec for Terra packaging team
