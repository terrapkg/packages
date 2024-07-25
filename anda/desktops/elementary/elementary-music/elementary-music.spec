%global srcname music
%global appname io.elementary.music

%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$

%global common_description %{expand:
Music is a fast and beautiful GTK3 audio player with a focus on music
and libraries. It handles external devices, CDs, and album art. Music
utilizes Granite for a consistent and slick UI.}

Name:           elementary-music
Summary:        Music player and library from elementary
Version:        8.0.0
Release:        1%?dist
License:        LGPL-2.0-or-later

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

# meson: remove deprecated positional arguments from i18n.merge_file calls
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  libappstream-glib
BuildRequires:  vala >= 0.26
BuildRequires:  fdupes

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7) >= 7.0.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libgda-5.0)
BuildRequires:  pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libhandy-1) >= 0.83.0
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(taglib_c)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       hicolor-icon-theme

# elementary-music explicitly requires the sqlite libgda database provider
Requires:       libgda-sqlite%{?_isa}

# Last.FM plugin was dropped in Fedora 34
Obsoletes:      elementary-music-plugin-lastfm < 5.0.5-5
# iPod plugin was merged into the main package in Fedora 34
Obsoletes:      elementary-music-plugin-ipod < 5.0.5-5
Provides:       elementary-music-plugin-ipod  = %{version}-%{release}

%description %{common_description}


%package        devel
Summary:        The official elementary music player (development headers)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

This package contains files needed for developing with Music.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{appname}

%fdupes %buildroot%_datadir/icons/hicolor/


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%doc README.md
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/locale/*/LC_MESSAGES/%{appname}.mo

%files devel

%changelog
* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 7.0.0-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
