%global commit d469a80f12e286c0e937d8b93c01dfc2d55dca8f
%global commit_date 20260504
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: fx-autoconfig
Version: 0~%{commit_date}git.%{shortcommit}
Release: 1%{?dist}
Summary: Firefox userChrome.js manager
Packager: Anna Simmons <anna@simmons.ovh>

License: MPL-2.0
URL: https://github.com/MrOtherGuy/fx-autoconfig
Source0: https://github.com/MrOtherGuy/fx-autoconfig/archive/%commit.tar.gz
Requires: firefox
BuildArch: noarch

%description
%{summary}.

%prep
%autosetup -n fx-autoconfig-%commit

%build

%install
mkdir -p %{buildroot}%{_libdir}/firefox

install -Dm644 program/config.js %{buildroot}%{_libdir}/firefox/
cp -pr program/defaults %{buildroot}%{_libdir}/firefox/defaults

%files
%license LICENSE
%doc readme.md
%{_libdir}/firefox/config.js
%{_libdir}/firefox/defaults/

%changelog
* Thu May 21 2026 Anna Simmons <anna@simmons.ovh>
- Initial package build
