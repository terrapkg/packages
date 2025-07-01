## NVIDIA DKMS package, based on the work of Negativo17 with tweaks for Terra.

%global debug_package %{nil}
%global modulename nvidia

Name:           dkms-%{modulename}-open
Version:        575.64.03
Release:        1%?dist
Summary:        NVIDIA display driver kernel module
Epoch:          3
License:        NVIDIA License
URL:            https://www.nvidia.com/object/unix.html
Source0:        https://download.nvidia.com/XFree86/Linux-%{_arch}/%{version}/NVIDIA-Linux-%{_arch}-%{version}.run
Source1:        %{name}.conf
BuildRequires:  sed
Provides:       %{modulename}-open-kmod = %{?epoch:%{epoch}:}%{version}
Requires:       %{modulename}-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Conflicts:      akmod-nvidia
# Unlike most DKMS packages, this package is NOT noarch!
ExclusiveArch:  x86_64 aarch64

%description
This package provides the NVIDIA kernel driver modules.

%prep
sh %{SOURCE0} -x --target dkms-nvidia-%{version}-%{_arch}
%setup -T -D -n dkms-nvidia-%{version}-%{_arch}
%autopatch -p1

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
%autochangelog
