%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-applications

%global plug_type personal
%global plug_name applications
%global plug_rdnn io.elementary.settings.%{plug_name}

Name:           switchboard-plug-applications
Summary:        Switchboard Applications plug
Version:        8.0.0
Release:        1%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/switchboard-plug-applications
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
#BuildRequires:  vala >= 0.22.0
BuildRequires:  fdupes

#BuildRequires:  pkgconfig(flatpak) >= 1.1.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.34
#BuildRequires:  pkgconfig(granite)
#BuildRequires:  pkgconfig(gtk+-3.0)
#BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(switchboard-3)
#BuildRequires:  pkgconfig(libhandy-1)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
The applications plug is a section in the Switchboard (System Settings)
that allows the user to manage application settings.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%fdupes %buildroot%_datadir/locale/
mv %buildroot%_datadir/metainfo/%plug_rdnn.metainfo.xml %buildroot%_datadir/metainfo/%plug_rdnn.metainfo.xml || true
%find_lang %{plug_rdnn}

# remove the specified stock icon from metainfo (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_rdnn}.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard-3/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/io.elementary.settings.applications.svg


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
