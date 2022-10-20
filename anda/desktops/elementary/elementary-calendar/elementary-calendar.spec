%global srcname calendar
%global appname io.elementary.calendar

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

Name:           elementary-calendar
Summary:        Desktop calendar app designed for elementary
Version:        6.1.1
Release:        %autorelease
License:        GPLv3+

URL:            https://github.com/elementary/calendar
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 6.2.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libhandy-1) >= 0.90.0
BuildRequires:  pkgconfig(libical-glib)
BuildRequires:  pkgconfig(libsoup-2.4)

Requires:       hicolor-icon-theme

%description
A slim, lightweight calendar app that syncs and manages multiple
calendars in one place, like Google Calendar, Outlook and CalDAV.


%package        devel
Summary:        The official elementary calendar (devel files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
A slim, lightweight calendar app that syncs and manages multiple
calendars in one place, like Google Calendar, Outlook and CalDAV.

This package contains the development files.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}-daemon.desktop

%{_bindir}/%{appname}

%{_libdir}/lib%{name}.so.0*
%{_libdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml

%files devel
%{_includedir}/%{name}/

%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%{_datadir}/vala/vapi/%{name}.deps
%{_datadir}/vala/vapi/%{name}.vapi


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
