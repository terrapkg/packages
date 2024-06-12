%global srcname photos
%global appname io.elementary.%{srcname}

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

Name:           elementary-photos
Summary:        Photo manager and viewer from elementary
Version:        8.0.0
Release:        1%?dist
License:        LGPL-2.0-or-later

URL:            https://github.com/elementary/photos
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.46.0
BuildRequires:  vala
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  cmake

BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gexiv2) >= 0.4.90
BuildRequires:  pkgconfig(gio-2.0) >= 2.20
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.20
BuildRequires:  pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.24.0
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.6.0
BuildRequires:  pkgconfig(gudev-1.0) >= 145
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libgphoto2) >= 2.4.2
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libraw) >= 0.13.2
BuildRequires:  pkgconfig(libwebp) >= 0.4.4
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)

Requires:       hicolor-icon-theme

%description
The elementary continuation of Shotwell, originally written by Yorba
Foundation.


%prep
%autosetup -n %{srcname}-%{version} -N


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

%fdupes %buildroot%_datadir/icons/hicolor/
%fdupes %buildroot%_datadir/locale/


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}-viewer.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_libdir}/%{appname}/

%{_libexecdir}/%{appname}/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/applications/%{appname}-viewer.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/icons/hicolor/*/apps/%{appname}-viewer.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com> - 2.7.5-1
- Repackaged for Terra
