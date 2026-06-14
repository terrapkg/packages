%global modulename xpadneo

Name:           dkms-%{modulename}
Version:        0.10.2
Release:        1%{?dist}
%if 0%{?fedora} <= 45
Epoch:          1
%endif
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad
License:        GPL-2.0-only AND GPL-3.0-or-later
URL:            https://atar-axis.github.io/%{modulename}
Source0:        https://github.com/atar-axis/xpadneo/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.conf
Source2:        no-weak-modules.conf
BuildRequires:  sed
Provides:       %{modulename}-kmod
Requires:       bluez
Requires:       bluez-tools
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Conflicts:      akmod-%{modulename}
Provides:       %{modulename}-kmod
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%description
Advanced Linux Driver for Xbox One Wireless Gamepad.

%prep
%autosetup -p1 -n %{modulename}-%{version}


cp -f %{SOURCE1} hid-xpadneo/src/dkms.conf

sed -i -e 's/__VERSION_STRING/%{version}/g' hid-xpadneo/src/dkms.conf
sed -i -e 's/$(VERSION)/v%{version}/g' hid-xpadneo/src/Makefile

%build

%install
# Create empty tree:
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
cp -fr hid-xpadneo/src/* %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

%if %{defined fedora}
# Do not enable weak modules support in Fedora (no kABI):
install -Dpm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%post
dkms add -m %{modulename} -v %{version} -q --rpm_safe_upgrade || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{modulename} -v %{version} -q || :
dkms install -m %{modulename} -v %{version} -q --force || :

%preun
# Remove all versions from DKMS registry:
dkms remove -m %{modulename} -v %{version} -q --all --rpm_safe_upgrade || :

%files
%{_usrsrc}/%{modulename}-%{version}
%if %{defined fedora}
%{_sysconfdir}/dkms/%{modulename}.conf
%endif

%changelog
* Sat Apr 11 2026 Gilver E. <roachy@fyralabs.com> - 1:0.10.2-1
- Initial stable package
