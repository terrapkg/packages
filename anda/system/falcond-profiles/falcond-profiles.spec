%global commit 0f87c748cf34a9bcbc4351ad051bcef8cce79158
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260101

Name:           falcond-profiles
Version:        0^%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        Profiles for falcond
License:        MIT
URL:            https://github.com/PikaOS-Linux/falcond-profiles
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Requires:       falcond
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

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

%files
%doc README.md
%license LICENSE
%{_datadir}/falcond/system.conf
%{_datadir}/falcond/profiles/*.conf
%{_datadir}/falcond/profiles/handheld/*.conf
%{_datadir}/falcond/profiles/htpc/*.conf

%changelog
* Thu Jun 19 2025 Gilver E. <rockgrub@disroot.org> - 0^20250613git.96c2cdf-1
- Initial package
