Name:           polychromatic
Version:        0.9.8
Release:        1%{?dist}
Summary:        RGB lighting management software for OpenRazer

License:        GPL-3.0-or-later
URL:            https://github.com/polychromatic/polychromatic
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Packager:       ammix <maxim@ammix.dev>

BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

Requires:       python3-colorama
Requires:       python3-colour
Requires:       python3-requests
Requires:       python3-setproctitle
Requires:       python3-pyqt6
Requires:       python3-pyqt6-webengine
Requires:       qt6-qtsvg
Requires:       python3-gobject
Requires:       gtk3
Requires:       libayatana-appindicator-gtk3
Requires:       hicolor-icon-theme
Recommends:     python3-openrazer

%description
Polychromatic is a front-end for configuring Razer peripherals: keyboards,
mice, keypads, headsets, laptops and more!

%prep
%autosetup
# Fix duplicate key in the desktop file. Already fixed upstream, drop after 0.9.8
sed -i 's/^GenericName\[pl_PL\]=Konfiguruj/Comment[pl_PL]=Konfiguruj/' sources/launchers/polychromatic.desktop

%conf
%meson

%build
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{name}.desktop

%files -f %{name}.lang
%license LICENSE
%doc CHANGELOG README.md
%{_bindir}/polychromatic-*
%{_mandir}/man1/polychromatic-*.1.*
%{_datadir}/%{name}/
%{_hicolordir}/*/apps/%{name}.*
%{_appsdir}/%{name}.desktop
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%{_metainfodir}/app.polychromatic.controller.metainfo.xml
%{python3_sitelib}/%{name}/

%changelog
* Sat Oct 03 2026 ammix <maxim@ammix.dev>
- Initial package
