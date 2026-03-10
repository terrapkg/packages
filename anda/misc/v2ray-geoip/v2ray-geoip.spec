%global commit  7a6498ae1cacdc6ec3356ad29d9566d7f0242f56
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 202603050223
%global commit_date 20260122

%global year %{gsub %commit_date %%d%%d%%d%%d$ %{quote:}}
%global month %{gsub %commit_date %%d%%d%%d%%d(%%d%%d)%%d%%d %%1}

Name:           v2ray-geoip
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%?dist
Summary:        GeoIP for V2Ray
License:        CC-BY-SA-4.0
Packager:       veuxit <erroor234@gmail.com>
URL:            https://github.com/v2fly/geoip
BuildArch:      noarch

Source0:        %{url}/archive/%{commit}/%{ver}-%{commit}.tar.gz
Source1:        https://download.db-ip.com/free/dbip-country-lite-%year-%month.mmdb.gz

BuildRequires:  golang

%description
%summary.

%prep
%autosetup -n geoip-%{commit}
mkdir -p db-ip
gzip -d %SOURCE1 -c > ./db-ip/dbip-country-lite.mmdb

%build
go run ./ -c ./config.json

%install
install -Dm644 output/geoip.dat %{buildroot}%{_datadir}/v2ray/geoip.dat

%files
%license LICENSE
%{_datadir}/v2ray/geoip.dat

%changelog
* Mon Mar 9 2026 veuxit <erroor234@gmail.com> - 202603050223^20260122git.7a6498a-1
- Initial package release
