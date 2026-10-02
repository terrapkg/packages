%global commit  2c892a618f4e23c549d28edd0f3f75407521b1aa
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 20261002050024
%global commit_date 20261002

Name:           v2ray-domain-list-community
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Community managed domain list (geosite.dat) for V2Ray
License:        MIT
Packager:       veuxit <erroor234@gmail.com>
URL:            https://github.com/v2fly/domain-list-community
BuildArch:      noarch

Source0:        %{url}/archive/%{commit}/%{ver}-%{commit}.tar.gz

BuildRequires:  golang
BuildRequires:  go-rpm-macros go-srpm-macros anda-srpm-macros

%description
%summary.

%prep
%autosetup -n domain-list-community-%{commit}
go run main.go

%install
install -Dm644 dlc.dat %{buildroot}%{_datadir}/v2ray/geosite.dat

%files
%doc README.md
%license LICENSE
%{_datadir}/v2ray/geosite.dat

%changelog
* Mon Mar 9 2026 veuxit <erroor234@gmail.com> - 20260309041918^20260309git.6bb4a68-1
- Initial package release
