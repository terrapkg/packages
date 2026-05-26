## NVIDIA DKMS package, based on the work of Negativo17 with tweaks for Terra.

%global debug_package %{nil}
%global modulename nvidia

Name:           dkms-%{modulename}
Version:        610.43.02
Release:        1%{?dist}
Summary:        NVIDIA display driver kernel module
Epoch:          3
License:        NVIDIA License
URL:            https://www.nvidia.com/object/unix.html
Source0:        https://download.nvidia.com/XFree86/NVIDIA-kernel-module-source/NVIDIA-kernel-module-source-%{version}.tar.xz
Source1:        %{name}.conf
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
%autosetup -p1 -n NVIDIA-kernel-module-source-%{version}

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
