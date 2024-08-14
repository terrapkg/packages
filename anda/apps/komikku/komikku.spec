%global appname Komikku
%global uuid    info.febvre.%{appname}
%global gtk4_version        4.14.4
%global libadwaita_version  1.5.1
%global pure_protobuf_version 2.0.0

Name:           komikku
Version:        1.53.0
%forgemeta
Release:        1%?dist
Summary:        A manga reader for GNOME

BuildArch:      noarch

License:        GPL-3.0-or-later
URL:            https://valos.gitlab.io/Komikku
Source0:        https://codeberg.org/valos/%{appname}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.59.0
BuildRequires:  python3-devel >= 3.8
BuildRequires:  blueprint-compiler

BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}

Requires:       hicolor-icon-theme
Requires:       gtk4 >= %{gtk4_version}
Requires:       libadwaita >= %{libadwaita_version}
Requires:       libnotify
Requires:       webkitgtk6.0
Requires:       python3-beautifulsoup4
Requires:       python3-brotli
Requires:       python3-colorthief
Requires:       python3-dateparser  %dnl >= 1.1.4 | https://bugzilla.redhat.com/show_bug.cgi?id=2115204
Requires:       python3-emoji
Requires:       python3-gobject
Requires:       python3-keyring >= 21.6.0
Requires:       python3-lxml
Requires:       python3-natsort
Requires:       python3-file-magic
Requires:       python3-piexif
Requires:       python3-pillow
Requires:       python3-pillow-heif
Requires:       python3-pure-protobuf >= %{pure_protobuf_version}
Requires:       python3-rarfile
Requires:       python3-requests
Requires:       python3-unidecode

%description
Komikku is a manga reader for GNOME. It focuses on providing a clean, intuitive
and adaptive interface.

Keys features

* Online reading from dozens of servers
* Offline reading of downloaded comics
* Categories to organize your library
* RTL, LTR, Vertical and Webtoon reading modes
* Several types of navigation:
  * Keyboard arrow keys
  * Right and left navigation layout via mouse click or tapping
    (touchpad/touch screen)
  * Mouse wheel
  * 2-fingers swipe gesture (touchpad)
  * Swipe gesture (touch screen)
* Automatic update of comics
* Automatic download of new chapters
* Reading history
* Light and dark themes

%prep
%autosetup -n %{name} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/


%changelog
* Thu Jul 11 2024 Trung Lê <8@tle.id.au> - 1.51.1-0
- Initial RPM package
