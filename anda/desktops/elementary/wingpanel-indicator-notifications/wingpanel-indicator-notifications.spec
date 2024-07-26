%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-notifications
%global appname io.elementary.wingpanel.notifications

Name:           wingpanel-indicator-notifications
Summary:        Notifications Indicator for wingpanel
Version:        7.1.0
Release:        1%{?dist}
License:        LGPL-2.0-or-later

URL:            https://github.com/elementary/wingpanel-indicator-notifications
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0


BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A notifications indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang notifications-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f notifications-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libnotifications.so

%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml


%changelog
* Thu Oct 20 2022 windowsboy111 <wboy111@outlook.com> - 6.0.7-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
