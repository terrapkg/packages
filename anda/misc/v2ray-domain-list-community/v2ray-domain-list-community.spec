%global debug_package %{nil}
# Disabled

%global commit  6bb4a68f2f1323998c84754ba56341f8e31efc26
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 20260309041918
%global commit_date 20260309

%global goipath         github.com/v2fly/domain-list-community
Version:                %{ver}^%{commit_date}git.%{shortcommit}

%global golicenses      LICENSE
%global godocs          README.md

Name:           v2ray-domain-list-community
Release:        1%?dist
Summary:        Community managed domain list (geosite.dat) for V2Ray
License:        MIT
Packager:       veuxit <erroor234@gmail.com>
URL:            https://github.com/v2fly/domain-list-community

Source0:        %{url}/archive/%{commit}/%{ver}-%{commit}.tar.gz

BuildRequires:  golang
BuildRequires:  go-rpm-macros go-srpm-macros anda-srpm-macros

%description
%summary.

%gopkg

%prep
%goprep_online -Ae
%autosetup -n domain-list-community-%{commit}

%build
go run main.go

%install
install -Dm644 dlc.dat %{buildroot}%{_datadir}/v2ray/geosite.dat

%files
%license LICENSE
%{_datadir}/v2ray/geosite.dat

%changelog
* Mon Mar 9 2026 veuxit <erroor234@gmail.com> - 20260309041918^20260309git.6bb4a68-1
- Initial package release