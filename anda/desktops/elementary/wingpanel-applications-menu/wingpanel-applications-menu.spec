%global srcname applications-menu
%global appname io.elementary.wingpanel.applications-menu

%global __provides_exclude_from ^%{_libdir}/(wingpanel|%{appname})/.*\\.so$

Name:           wingpanel-applications-menu
Summary:        Lightweight and stylish app launcher
Version:        2.11.1
Release:        2%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/applications-menu
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.32.1


BuildRequires:  appstream-vala

BuildRequires:  pkgconfig(appstream) >= 0.10.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 6.1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libhandy-1) >= 0.83.0
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       redhat-menus

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}

%description
The lightweight and stylish app launcher from elementary.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson -Dwith-zeitgeist=false
%meson_build


%install
%meson_install
%find_lang slingshot


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f slingshot.lang
%doc README.md
%license COPYING

%{_libdir}/%{appname}/
%{_libdir}/wingpanel/libslingshot.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.applications-menu.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 2.11.0-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
