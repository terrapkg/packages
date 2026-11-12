%global appid com.github.ShadowBlip.ayaneo-platform

Name:           ayaneo-platform
Version:        0.3.5
Release:        1%{?dist}
Summary:        Platform driver for AYANEO x86 handhelds
License:        GPL-2.0-or-later
URL:            https://github.com/ShadowBlip/%{name}
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        com.github.ShadowBlip.ayaneo-platform.metainfo.xml
BuildArch:      noarch

Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}

%description
Platform driver for AYANEO x86 handhelds, exposing RGB LED control and
bypass charging through sysfs. This package contains common files shared
between the akmod and DKMS variants.

%prep
%autosetup -n %{name}-%{version}

%install
install -D -m 0644 %{SOURCE1} \
    %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
%terra_appstream

%files
%license LICENSE
%doc README.md
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Thu Oct 22 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.3.5-1
- Initial package
