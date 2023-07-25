Name:           blackbox-terminal
Version:        0.14.0
Release:        1%{?dist}
Summary:        A beautiful GTK 4 terminal
License:        GPL-3.0
URL:            https://gitlab.gnome.org/raggesilver/blackbox
BuildRequires:  vala meson gettext 
BuildRequires:  pkgconfig(gtk4) >= 4.6.2
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  libadwaita-devel >= 1.1
BuildRequires:  pkgconfig(pqmarble) >= 2
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= 0.69.0
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.4.4
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.12
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.54.0
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  desktop-file-utils libappstream-glib cmake
Source0:        %url/-/archive/v%version/blackbox-v%version.tar.gz

%description
%{summary}.

%prep
%autosetup -p1 -n blackbox-v%version

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING
%_bindir/blackbox
%_datadir/applications/com.raggesilver.BlackBox.desktop
%_datadir/appdata/com.raggesilver.BlackBox.appdata.xml
%_datadir/blackbox/*
%_datadir/glib-2.0/schemas/com.raggesilver.BlackBox.gschema.xml
%_datadir/icons/hicolor/scalable/actions/com.raggesilver.BlackBox-fullscreen-symbolic.svg
%_datadir/icons/hicolor/scalable/actions/com.raggesilver.BlackBox-show-headerbar-symbolic.svg
%_datadir/icons/hicolor/scalable/actions/external-link-symbolic.svg
%_datadir/icons/hicolor/scalable/actions/settings-symbolic.svg
%_datadir/icons/hicolor/scalable/apps/com.raggesilver.BlackBox.svg
%_datadir/locale/*/LC_MESSAGES/blackbox.mo


%changelog
* Sun Oct 23 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
