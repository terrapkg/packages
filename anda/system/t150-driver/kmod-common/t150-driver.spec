%global commit f7ecb30c65ee5f7870e921bc0a2354df8e1e8100
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250225
%global ver 1.0

Name:           t150-driver
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        2%{?dist}
Summary:        Thrustmaster T150 steering wheel driver common files
License:        GPL-2.0-only
URL:            https://github.com/scarburato/t150_driver
Source0:        %{url}/archive/%{commit}.tar.gz#/t150_driver-%{shortcommit}.tar.gz
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      noarch

%description
Linux driver for Thrustmaster T150 Steering Wheel USB. This package contains
common files shared between the akmod and dkms variants.

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      akmod-%{name}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.

%prep
%autosetup -p1 -n t150_driver-%{commit}

echo hid-t150 > %{name}.conf

%install
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}

%files
%license LICENSE
%doc README.md

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
* Thu Apr 02 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
