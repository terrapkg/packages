%global commit f7bf935f0e534434d41e159d695f4a6c81e19fe9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260106
%global ver 0.2.2

Name:           hid-fanatecff
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Fanatec force feedback driver common files
License:        GPL-2.0-only
URL:            https://github.com/gotzl/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      noarch

%description
Driver to support Fanatec input devices, in particular force feedback of
various wheel-bases. This package contains common files shared between the
akmod and dkms variants.

%package       akmod-modules
Summary:       Modules for Akmods
Requires:      akmod-%{name}
BuildArch:     noarch

%description   akmod-modules
Akmods modules for the akmod-%{name} package.

%prep
%autosetup -p1 -n %{name}-%{commit}

echo hid-fanatec > %{name}.conf

%install
# UDev rules:
install -Dpm644 fanatec.rules %{buildroot}%{_udevrulesdir}/99-fanatec.rules

# Akmods modules
install -Dm644 %{name}.conf -t %{buildroot}%{_modulesloaddir}

%files
%license LICENSE
%doc README.md
%{_udevrulesdir}/99-fanatec.rules

%files akmod-modules
%{_modulesloaddir}/%{name}.conf

%changelog
* Thu Apr 02 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
