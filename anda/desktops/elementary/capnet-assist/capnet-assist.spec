%global appid io.elementary.capnet-assist

Name:           capnet-assist
Version:        8.0.2
Release:        1%?dist
Summary:        Captive Network Assistant automatically opens to help you get connected
License:        GPL-3.0-only
URL:            https://github.com/elementary/capnet-assist
Source0:        %url/archive/refs/tags/%version.tar.gz
BuildRequires:  meson gettext vala desktop-file-utils
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7) >= 7.0.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0.0
BuildRequires:  pkgconfig(webkitgtk-6.0)

%description
Log into captive portals—like Wi-Fi networks at coffee shops, airports, and trains—with ease. Captive Network Assistant automatically opens to help you get connected.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%terra_appstream -o %buildroot%_metainfodir/%appid.metainfo.xml
%find_lang %appid

%check
%desktop_file_validate %buildroot%_appsdir/%appid.desktop

%files -f %appid.lang
%doc README.md
%license COPYING
%_bindir/%appid
%_appsdir/%appid.desktop
%_datadir/glib-2.0/schemas/%appid.gschema.xml
%_hicolordir/*/apps/%appid.svg
%_metainfodir/%appid.metainfo.xml

%changelog
* Tue Apr 07 2026 madonuko <mado@fyralabs.com> - 8.0.2-1
- Initial package.
