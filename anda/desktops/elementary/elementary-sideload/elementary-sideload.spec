%global srcname sideload
%global appname io.elementary.sideload
 
Name:           elementary-sideload
Summary:        Sideload flatpaks on Pantheon
Version:        6.2.2
Release:        1%?dist
License:        GPL-3.0-or-later
 
URL:            https://github.com/elementary/sideload
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
 
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  fdupes
 
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7) >= 7.0.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libxml-2.0)
 
Requires:       hicolor-icon-theme
 
%description
Sideload is a simple application that lets users install flatpaks on
Pantheon without needing to use a command line application.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build

%install
%meson_install

%fdupes %buildroot%_datadir/icons/hicolor/
%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop
 
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license LICENSE
%doc README.md

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
* Tue Nov 22 2022 Lleyton Gray <lleyton@fyralabs.com> - 6.1.0-1
- Repackaged for Terra
