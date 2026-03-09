%global debug_package %{nil}
# Disabled

%global commit  7a6498ae1cacdc6ec3356ad29d9566d7f0242f56
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 202603050223
%global commit_date 20260122

%global goipath         github.com/v2fly/domain-list-community
Version:                %{ver}^%{commit_date}git.%{shortcommit}

%global golicenses      LICENSE
%global godocs          README.md

Name:           v2ray-geoip
Release:        1%?dist
Summary:        GeoIP for V2Ray
License:        CC-BY-SA-4.0
Packager:       veuxit <erroor234@gmail.com>
URL:            https://github.com/v2fly/geoip

Source0:        %{url}/archive/%{commit}/%{ver}-%{commit}.tar.gz

BuildRequires:  golang
BuildRequires:  go-rpm-macros go-srpm-macros anda-srpm-macros

%description
%summary.

%gopkg

%prep
%goprep_online -Ae
%autosetup -n geoip-%{commit}

%build
export TAG_NAME=$(date +%Y%m%d%H%M)
export RELEASE_NAME=$(date +%Y%m%d%H%M)
export YEAR=$(date +%Y)
export MONTH=$(date +%m)

curl -L -o dbip-country-lite.mmdb.gz "https://download.db-ip.com/free/dbip-country-lite-$YEAR-$MONTH.mmdb.gz"
gzip -d dbip-country-lite.mmdb.gz
mkdir -p db-ip
mv dbip-country-lite*.mmdb ./db-ip/dbip-country-lite.mmdb

go run ./ -c ./config.json

%install
install -Dm644 output/geoip.dat %{buildroot}%{_datadir}/v2ray/geoip.dat

%files
%license LICENSE
%{_datadir}/v2ray/geoip.dat

%changelog
* Mon Mar 9 2026 veuxit <erroor234@gmail.com> - 
- Initial package release