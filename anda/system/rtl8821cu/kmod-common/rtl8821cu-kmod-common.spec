%global commit 7f63a9da2e8ed83403f6f920e9b1628a37b38ef4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20251215
%global ver 5.12.0.4
%global modulename rtl8821cu
%global git_name 8821cu-20210916
%global debug_package %{nil}

Name:           %{modulename}-kmod-common
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        2%{?dist}
Summary:        Common files and documentation for the rtl8821cu driver
License:        GPL-2.0-only
URL:            https://github.com/morrownr/8821cu-20210916
Source0:        %{url}/archive/%{commit}.tar.gz#/%{git_name}-%{shortcommit}.tar.gz
BuildRequires:  systemd-rpm-macros
Requires:       rtl8821cu-kmod = %{version}
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%description
Necessary files for the %{modulename} driver.

%package -n     %{modulename}-doc
Summary:        Docs for the rtl8821cu driver

%description -n %{modulename}-doc
Documentation files for the Linux rtl8821cu driver.

%prep
%autosetup -n %{git_name}-%{commit}

%build
# Empty build section for RPM reasons

%install
install -Dm644 8821cu.conf -t %{buildroot}%{_modprobedir}

%files
%doc README.md
%license LICENSE
%{_modprobedir}/8821cu.conf

%files -n %{modulename}-doc
%doc FAQ.md
%doc supported-device-IDs
%doc docs/*

%changelog
* Wed May 28 2025 Gilver E. <rockgrub@disroot.org> - 5.12.0.4^20250508git.d74134a-1
- Initial package
