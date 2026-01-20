%global commit ee221ecae757d43ab3fb39433f389373b2026109
%global shortcommit %{sub %{commit} 1 7}
%global commit_date 20251031
%global debug_package %{nil}
%global modulename intel-usbio

Name:       dkms-%{modulename}
Version:    0^%{commit_date}git.%{shortcommit}
Release:    1%?dist
Summary:    Kernel drivers for the USBIO Extension
License:    GPL-2.0-only
URL:        https://github.com/intel/usbio-drivers
Source0:    %{url}/archive/%{commit}.tar.gz#/usbio-drivers-%{shortcommit}.tar.gz
Source2:    %{name}.conf
Provides:   %{modulename}-kmod = %{version}
Requires:   dkms
Requires:   dkms-intel-ipu6
BuildArch:  noarch
Packager:   Gilver E. <rockgrub@disroot.org>

%description
This package enables USBIO Extension drivers on Intel Alder Lake, Raptor Lake, Meteor Lake and Lunar Lake platforms.

%prep
%autosetup -p1 -n usbio-drivers-%{commit}
rm -fr .github

cp -f %{SOURCE2} dkms.conf

%build

%install
# Create empty tree:
mkdir -p %{buildroot}%{_usrsrc}/%{modulename}-%{version}/
cp -fr * %{buildroot}%{_usrsrc}/%{modulename}-%{version}/

%post
dkms add -m %{modulename} -v %{version} -q || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{modulename} -v %{version} -q || :
dkms install -m %{modulename} -v %{version} -q --force || :

%preun
# Remove all versions from DKMS registry:
dkms remove -m %{modulename} -v %{version} -q --all || :

%files
%{_usrsrc}/%{modulename}-%{version}

%changelog
* Mon Jun 16 2025 Gilver E. <rockgrub@disroot.org> - 0^20250312git4fb690c
- Initial package

