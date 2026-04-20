%global commit 56c3cc0748cc66220487aaa63dc621aa1076994d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260418
%global ver 0

Name:           sc0710
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Elgato 4K60 Pro MK.2 / 4K Pro capture card driver common files
License:        GPL-2.0-only
URL:            https://github.com/Nakildias/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      noarch
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>

%description
Elgato 4K60 Pro MK.2 / 4K Pro capture card driver common files.

%prep
%autosetup -p1 -n %{name}-%{commit}

%install

%files
%license LICENSE
%doc README.md

%changelog
* Fri Apr 03 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
