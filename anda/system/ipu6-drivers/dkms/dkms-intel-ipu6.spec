%global debug_package %{nil}
%global commit 9bff73689ea2502f6e3bc34769fd699cde3ffeea
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250627
%global modulename intel-ipu6
# Actual "release" version, currently unused as the release versions are back and forth on if on if they use 1.0.0 or 1.0.1
%global ver 1.0.1

Name:           dkms-%{modulename}
Summary:        DKMS module for %{modulename}
Version:        0^%{commit_date}git.%{shortcommit}
Release:        1%?dist
License:        GPL-2.0-or-later
URL:            https://github.com/intel/ipu6-drivers
Source0:        %{url}/archive/%{commit}.tar.gz#/ipu6-drivers-%{shortcommit}.tar.gz
Source1:        %{name}.conf
BuildRequires:  elfutils-libelf-devel
BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros
Provides:       %{modulename}-kmod
Requires:       %{modulename}-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       dkms
Requires:       dkms-usbio-drivers
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

%description
This package enables the Intel IPU6 image processor.

%prep
%autosetup -p1 -n ipu6-drivers-%{commit}
# Pre-apply patch listed in dkms.conf:
patch -p1 -i patches/*.patch
rm -fr patch* .github

cp -f %{SOURCE1} dkms.conf

%build

%install
# Create empty tree:
mkdir -p %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
cp -fr * %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/

%post
dkms add -m %{dkms_name} -v %{version} -q || :
# Rebuild and make available for the currently running kernel:
dkms build -m %{dkms_name} -v %{version} -q || :
dkms install -m %{dkms_name} -v %{version} -q --force || :

%preun
# Remove all versions from DKMS registry:
dkms remove -m %{dkms_name} -v %{version} -q --all || :

%files
%{_usrsrc}/%{dkms_name}-%{version}

%changelog
* Thu Apr 24 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
