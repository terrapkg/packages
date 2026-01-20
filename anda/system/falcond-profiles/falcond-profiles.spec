%global commit f52c3445a9b9aa18401b7c8e9bf532c37758e585
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260119

Name:           falcond-profiles
Version:        0^%{commit_date}git.%{shortcommit}
Release:        2%{?dist}
Summary:        Profiles for falcond
License:        MIT
URL:            https://github.com/PikaOS-Linux/falcond-profiles
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Requires:       falcond
Suggests:       falcond-gui
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%description
This package contains the profiles needed for falcond.

%prep
%autosetup -n %{name}-%{commit}

%build
# Hi, I'm empty!

%install
install -Dm644 usr/share/falcond/system.conf -t %{buildroot}%{_datadir}/falcond/
install -Dm644 usr/share/falcond/profiles/*.conf -t %{buildroot}%{_datadir}/falcond/profiles/
install -Dm644 usr/share/falcond/profiles/handheld/* -t %{buildroot}%{_datadir}/falcond/profiles/handheld/
install -Dm644 usr/share/falcond/profiles/htpc/* -t %{buildroot}%{_datadir}/falcond/profiles/htpc/

install -dm2775 %{buildroot}%{_datadir}/falcond/profiles/user

%files
%doc README.md
%license LICENSE
%dir %{_datadir}/falcond
%{_datadir}/falcond/system.conf
%{_datadir}/falcond/profiles/*.conf
%{_datadir}/falcond/profiles/handheld/*.conf
%{_datadir}/falcond/profiles/htpc/*.conf
%attr(2775, root, falcond) %dir %{_datadir}/falcond/profiles/user

%changelog
* Thu Jan 1 2026 Gilver E. <roachy@fyralabs.com> - 0^20260101git.0f87c74-2
- Added new user profiles directory
- Added weak dep on falcond-gui
* Thu Jun 19 2025 Gilver E. <rockgrub@disroot.org> - 0^20250613git.96c2cdf-1
- Initial package
