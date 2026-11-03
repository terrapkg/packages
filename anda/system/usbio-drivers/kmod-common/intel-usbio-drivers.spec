%global commit 8f22aca95f3426f93fff0cd84f4962635ffddcfc
%global shortcommit %{sub %{commit} 1 7}
%global commit_date 20261103
%global debug_package %{nil}

Name:          intel-usbio
Version:       0^%{commit_date}git.%{shortcommit}
Release:       1%{?dist}
Summary:       Common files for the USBIO drivers
License:       GPL-2.0-only
URL:           https://github.com/intel/usbio-drivers
Source0:       %{url}/archive/%{commit}.tar.gz#/usbio-drivers-%{shortcommit}.tar.gz
BuildRequires: anda-srpm-macros
Provides:      intel-usbio-kmod-common = %{evr}
Requires:      intel-ipu6-kmod-common
BuildArch:     noarch
Packager:      Gilver E. <roachy@fyralabs.com>

%description
This package contains the common files for the UBSIO kernel modules.

%prep
%autosetup -p1 -n usbio-drivers-%{commit}

%build
# Hi, I'm empty.

%install
# Hi, I'm also empty!

%files
%doc README.md
%doc SECURITY.md
%license LICENSE.txt

%changelog
* Mon Jun 16 2025 Gilver E. <rockgrub@disroot.org> - 0^20250312git4fb690c
- Initial package
