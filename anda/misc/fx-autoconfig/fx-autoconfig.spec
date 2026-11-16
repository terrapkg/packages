%global commit dfdab5684faffc112b76ccb1d8cab7f75da0102c
%global commit_date 20260723
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: fx-autoconfig
Version: 0~%{commit_date}git.%{shortcommit}
Release: 2%{?dist}
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
mkdir -p %{buildroot}%{_prefix}/lib64/firefox

install -Dm644 program/config.js %{buildroot}%{_prefix}/lib64/firefox/
cp -pr program/defaults %{buildroot}%{_prefix}/lib64/firefox/defaults

%files
%license LICENSE
%doc readme.md
%{_prefix}/lib64/firefox/config.js
%{_prefix}/lib64/firefox/defaults/

%changelog
* Sun Nov 15 2026 Anna Simmons <anna@simmons.ovh> - 2
- Fix install location to lib64 from lib

* Thu May 21 2026 Anna Simmons <anna@simmons.ovh> - 1
- Initial package build
