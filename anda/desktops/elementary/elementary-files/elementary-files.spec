%global srcname files
%global appname io.elementary.files

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

Name:           elementary-files
Summary:        File manager from elementary
Version:        7.0.0
Release:        1%?dist
License:        GPL-3.0

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

# contracts for compressing/uncompressing files with file-roller
Source1:        file-roller-compress.contract
Source2:        file-roller-extract-here.contract

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.50.0
BuildRequires:  vala >= 0.48.2
BuildRequires:  fdupes

BuildRequires:  pkgconfig(cloudproviders) >= 0.3.0
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.40
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.40
BuildRequires:  pkgconfig(gobject-2.0) >= 2.40
BuildRequires:  pkgconfig(granite) >= 6.1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.25
BuildRequires:  pkgconfig(libcanberra) >= 0.30
BuildRequires:  pkgconfig(libgit2-glib-1.0)
BuildRequires:  pkgconfig(libhandy-1) >= 0.83.0
BuildRequires:  pkgconfig(libnotify) >= 0.7.2
BuildRequires:  pkgconfig(pango) >= 1.1.2
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(systemd) >= 206
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)

Requires:       contractor
Requires:       file-roller

%description
The simple, powerful, and sexy file manager from elementary.


%package        portal
Summary:        File manager from elementary (flatpak file chooser portal)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       xdg-desktop-portal

%description    portal
The simple, powerful, and sexy file manager from elementary.

This package contains a file chooser portal implementation for flatpak.


%package        devel
Summary:        File manager from elementary (development headers)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The simple, powerful, and sexy file manager from elementary.

This package contains the development headers.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
CFLAGS="$CFLAGS -Wno-implicit-function-declaration"
%meson -Dwith-zeitgeist=disabled
%meson_build


%install
%meson_install

%find_lang %{appname}

# install file-roller contracts
mkdir -p %{buildroot}/%{_datadir}/contractor
cp -pav %{SOURCE1} %{buildroot}/%{_datadir}/contractor/
cp -pav %{SOURCE2} %{buildroot}/%{_datadir}/contractor/


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%post portal
%systemd_user_post %{appname}.xdg-desktop-portal.service

%preun portal
%systemd_user_preun %{appname}.xdg-desktop-portal.service


%files -f %{appname}.lang
%doc AUTHORS README.md
%license COPYING

%{_bindir}/%{appname}
%{_bindir}/%{appname}-daemon
%{_bindir}/%{appname}-pkexec

%{_libdir}/%{appname}/
%{_libdir}/libpantheon-files-core.so.6*

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/contractor/*.contract
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/dbus-1/services/%{appname}.Filemanager1.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/polkit-1/actions/%{appname}.policy

%files portal
%{_libexecdir}/%{appname}.xdg-desktop-portal
%{_userunitdir}/%{appname}.xdg-desktop-portal.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.elementary.files.service
%{_datadir}/xdg-desktop-portal/portals/io.elementary.files.portal

%files devel
%{_includedir}/pantheon-files-core/

%{_libdir}/libpantheon-files-core.so
%{_libdir}/pkgconfig/pantheon-files-core.pc

%{_datadir}/vala/vapi/pantheon-files-core.vapi


%changelog
* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 6.2.1-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
