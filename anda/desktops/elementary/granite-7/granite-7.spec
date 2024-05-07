%global common_description %{expand:
Granite is a companion library for GTK+ and GLib. Among other things, it
provides complex widgets and convenience functions designed for use in
apps built for elementary.}

Name:           granite-7
Summary:        Elementary companion library for GTK+ and GLib
Version:        7.5.0
Release:        1%?dist
License:        LGPL-3.0-or-later

URL:            https://github.com/elementary/granite
Source0:        %{url}/archive/%{version}/granite-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.48.2
BuildRequires:  vala >= 0.48
BuildRequires:  fdupes

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.4
BuildRequires:  sassc

# granite relies on org.gnome.desktop.interface for the clock-format setting
Requires:       gsettings-desktop-schemas

# granite provides and needs some generic icons
Requires:       hicolor-icon-theme

%description %{common_description}


%package        devel
Summary:        Granite Toolkit development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

This package contains the development headers.


%prep
%autosetup -n granite-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%fdupes %buildroot%_datadir/icons/hicolor/
%fdupes %buildroot%_datadir/locale/

%find_lang granite-7

%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/io.elementary.granite-7.demo.desktop

%dnl appstream-util validate-relax --nonet \
%dnl     %{buildroot}/%{_datadir}/metainfo/granite-7.metainfo.xml


%files -f granite-7.lang
%doc README.md
%license COPYING

%{_libdir}/libgranite-7.so.7
%{_libdir}/libgranite-7.so.7.*
%{_libdir}/girepository-1.0/Granite-7.0.typelib

%{_datadir}/metainfo/granite-7.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/io.elementary.granite-7.svg
%{_datadir}/themes/Granite/


%files devel
%doc README.md
%license COPYING
%{_bindir}/granite-7-demo

%{_libdir}/libgranite-7.so
%{_libdir}/pkgconfig/granite-7.pc

%{_includedir}/granite-7/granite-7.h

%{_datadir}/applications/io.elementary.granite-7.demo.desktop
%{_datadir}/gir-1.0/Granite-7.0.gir
%{_datadir}/vala/vapi/granite-7.deps
%{_datadir}/vala/vapi/granite-7.vapi

%changelog
* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 7.1.0-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
