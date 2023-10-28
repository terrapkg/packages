Name: kairos
Version: 0.1.0
Release: %autorelease
Summary: Check the weather outside
URL: https://github.com/tau-OS/kairos
Source0: %url/archive/refs/tags/v%{version}.tar.gz
License: GPL-3.0

BuildRequires: meson
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: cmake
BuildRequires: vala
BuildRequires: ninja-build
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(libgeoclue-2.0)
BuildRequires: pkgconfig(geocode-glib-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libbismuth-1)
BuildRequires: pkgconfig(libhelium-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gweather4)
Requires: libhelium
BuildRequires: desktop-file-utils

%description
%{summary}.

%prep
%forgeautosetup

%build
%meson
%meson_build

%install
%meson_install

%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :

%files
%license COPYING
%{_bindir}/com.fyralabs.Kairos
%{_datadir}/applications/com.fyralabs.Kairos.desktop
%{_datadir}/dbus-1/services/com.fyralabs.Kairos.service
%{_datadir}/icons/hicolor/*/apps/com.fyralabs.Kairos*
%{_datadir}/metainfo/com.fyralabs.Kairos.appdata.xml
%{_datadir}/glib-2.0/schemas/com.fyralabs.Kairos.gschema.xml


%changelog
%autochangelog