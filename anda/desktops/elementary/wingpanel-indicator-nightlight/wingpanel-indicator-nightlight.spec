%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-nightlight
%global appname io.elementary.wingpanel.nightlight

Name:           wingpanel-indicator-nightlight
Summary:        Night Light Indicator for wingpanel
Version:        2.1.2
Release:        1%{?dist}
License:        GPL-2.0-or-later

URL:            https://github.com/elementary/wingpanel-indicator-nightlight
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0


BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       wingpanel%{?_isa}
Supplements:    wingpanel%{?_isa}


%description
A wingpanel indicator for Night Light.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang nightlight-indicator


%check
%dnl appstream-util validate-relax --nonet \
%dnl     %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f nightlight-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libnightlight.so

%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
* Thu Oct 20 2022 windowsboy111 <wboy111@outlook.com> - 2.1.1-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
