## NVIDIA DKMS package, based on the work of Negativo17 with tweaks for Terra.

# RPM inexplicably thinks this package deps on a version of libcrypto it does not?
%global __requires_exclude (libcrypto\\.so\\.1\\.1.*)$
%global debug_package %{nil}
%global modulename nvidia-580xx

Name:           dkms-%{modulename}
Version:        580.142
Release:        1%{?dist}
Summary:        NVIDIA display driver kernel module
Epoch:          3
License:        NVIDIA License
URL:            https://www.nvidia.com/object/unix.html
Source0:        https://download.nvidia.com/XFree86/Linux-%{_arch}/%{version}/NVIDIA-Linux-%{_arch}-%{version}.run
Source1:        dkms-nvidia.conf
Patch0:         0001-Enable-atomic-kernel-modesetting-by-default.patch
BuildRequires:  sed
Requires:       %{modulename}-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Provides:       %{modulename}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-580-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       dkms-nvidia-580 = %{evr}
Conflicts:      akmod-nvidia-580xx
Conflicts:      nvidia-kmod
# Unlike most DKMS packages, this package is NOT noarch!
ExclusiveArch:  x86_64 aarch64
Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
This package provides the proprietary NVIDIA kernel driver modules.

%prep
sh %{SOURCE0} -x --target dkms-nvidia-%{version}-%{_arch}
%setup -T -D -n dkms-nvidia-%{version}-%{_arch}

pushd kernel-open
%autopatch -p1
popd

cp -f %{SOURCE1} dkms.conf

sed -i -e 's/__VERSION_STRING/%{version}/g' dkms.conf

%build

%install
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
cp -fr * %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
rm -f %{buildroot}%{_usrsrc}/%{modulename}-%{version}/*/dkms.conf

%post
dkms add -m %{modulename} -v %{version} -q --rpm_safe_upgrade || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{modulename} -v %{version} -q || :
dkms install -m %{modulename} -v %{version} -q --force || :
dracut --regenerate-all --force --quiet

%preun
# Remove all versions from DKMS registry:
dkms remove -m %{modulename} -v %{version} -q --all --rpm_safe_upgrade || :
if [ "$1" == 0 ]; then
    dracut --regenerate-all --force --quiet
fi

%files
%{_usrsrc}/%{modulename}-%{version}

%changelog
* Mon Apr 13 2026 Gilver E. <roachy@fyralabs.com> - 3:580.142-1
- Update spec for Terra packaging team
