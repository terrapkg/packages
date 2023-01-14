Name:           blackbox-terminal
Version:        0.13.0
Release:        %autorelease
Summary:        A beautiful GTK 4 terminal
License:        GPLv3
URL:            https://gitlab.gnome.org/raggesilver/blackbox
BuildRequires:  vala meson gettext 
BuildRequires:  pkgconfig(gtk4) >= 4.6.2
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(libadwaita-1) >= 1.1
BuildRequires:  marble-gtk >= 42
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= 0.69.0
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.4.4
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.12
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.54.0
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gee-0.8)
Source0:        %{url}/-/archive/v%{version}/blackbox-v%{version}.tar.gz

%description
%{summary}.

%prep
%autosetup -n blackbox-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING
/usr/bin/blackbox
/usr/lib/debug/*
/usr/share/applications/com.raggesilver.BlackBox.desktop
/usr/share/appdata/com.raggesilver.BlackBox.appdata.xml
/usr/share/blackbox/*
/usr/share/glib-2.0/schemas/com.raggesilver.BlackBox.gschema.xml
/usr/share/icons/hicolor/scalable/actions/com.raggesilver.BlackBox-fullscreen-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/com.raggesilver.BlackBox-show-headerbar-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/external-link-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/settings-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/com.raggesilver.BlackBox.svg
/usr/share/locale/*/LC_MESSAGES/blackbox.mo


%changelog
* Sun Oct 23 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
