%global commit 2092db19f7b40854e0427a1b2e39eda9f8d0c3cd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250528
%global ver 0.5.0

Name:           new-lg4ff
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Logitech force feedback driver common files
License:        GPL-2.0-only
URL:            https://github.com/berarma/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Requires:       (akmod-%{name} = %{?epoch:%{epoch}:}%{version} or dkms-%{name} = %{?epoch:%{epoch}:}%{version})
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      noarch

%description
Experimental Logitech force feedback module for Linux. This package contains
common files shared between the akmod and dkms variants.

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      akmod-%{name}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.

%prep
%autosetup -p1 -n %{name}-%{commit}

echo hid-logitech-new > %{name}.conf

%install
# Akmods modules
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}

%files
%license LICENSE
%doc README.md

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
* Thu Apr 02 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
