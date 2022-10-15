%global __provides_exclude_from ^%{_libdir}/gala/.*\\.so$

Name:           gala
Summary:        Gala window manager
Version:        6.3.1
Release:        %autorelease
License:        GPLv3+

URL:            https://github.com/elementary/gala
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# patch some default settings to better match Fedora
Patch0:         0000-Modify-default-settings-for-Fedora.patch

# upstream patches for better support of mutter 42 / libmutter-10
Patch1:         %{url}/commit/60861a4.patch
Patch2:         %{url}/commit/9641704.patch
Patch3:         %{url}/commit/f9008e4.patch
Patch4:         %{url}/commit/1e223b3.patch
Patch5:         %{url}/commit/e86a951.patch
Patch6:         %{url}/commit/e009541.patch
Patch7:         %{url}/commit/890f78d.patch
Patch8:         %{url}/commit/fc838d7.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.50.0
BuildRequires:  vala >= 0.28.0

BuildRequires:  mesa-libEGL-devel

BuildRequires:  pkgconfig(clutter-1.0) >= 1.12.0
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon) >= 3.15.2
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(mutter-clutter-10)
BuildRequires:  pkgconfig(mutter-cogl-10)
BuildRequires:  pkgconfig(mutter-cogl-pango-10)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# gala provides a generic icon (apps/multitasking-view)
Requires:       hicolor-icon-theme

# gala's multitasking view is activated via dbus
Requires:       dbus-tools

# gala relies on the new notification server
Requires:       elementary-notifications

%description
Gala is Pantheon's Window Manager, part of the elementary project.


%package        libs
Summary:        Gala window manager libraries

%description    libs
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the shared libraries.


%package        devel
Summary:        Gala window manager development files
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the development headers.


%prep
%autosetup -p1


%build
%meson -Dsystemd=false
%meson_build


%install
%meson_install

%find_lang gala


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/gala-daemon.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/gala*.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml


%files -f gala.lang
%config(noreplace) %{_sysconfdir}/xdg/autostart/gala-daemon.desktop

%{_bindir}/gala
%{_bindir}/gala-daemon

%{_libdir}/gala/plugins/*

%{_datadir}/applications/gala*.desktop
%{_datadir}/glib-2.0/schemas/20_elementary.pantheon.wm.gschema.override
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.gala.gschema.xml
%{_datadir}/icons/hicolor/*/apps/multitasking-view.svg
%{_datadir}/metainfo/%{name}.appdata.xml

%files libs
%doc AUTHORS README.md
%license COPYING

%dir %{_libdir}/gala
%dir %{_libdir}/gala/plugins

%{_libdir}/libgala.so.0*

%files devel
%{_includedir}/gala/

%{_libdir}/libgala.so
%{_libdir}/pkgconfig/gala.pc

%{_datadir}/vala/vapi/gala.deps
%{_datadir}/vala/vapi/gala.vapi


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
