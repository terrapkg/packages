%global commit 46474a4a86692b7c38ecdb4f135bee7badbfa8b0
%global commit_date 20250116
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          geteltorito
Version:       %{commit_date}.%{shortcommit}
Release:       2%?dist
Summary:       An El Torito boot image extractor
License:       GPL-3.0-only
Packager:      Owen Zimmerman <owen@fyralabs.com>
Url:           https://github.com/rainer042/geteltorito
Source0:       %{url}/archive/%{commit}.tar.gz
BuildArch:     noarch
Requires:      perl

%description
%summary.

%prep
%autosetup -n geteltorito-%commit

%install
install -Dm 755 geteltorito.pl %buildroot%{_bindir}/geteltorito

%files
%license LICENSE
%doc README
%{_bindir}/geteltorito

%changelog
* Sat Feb 01 2025 Owen Zimmerman <owen@fyralabs.com>
- Package geteltorito