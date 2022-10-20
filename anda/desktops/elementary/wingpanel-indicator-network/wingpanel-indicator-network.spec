%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-network
%global appname io.elementary.wingpanel.network

Name:           wingpanel-indicator-network
Summary:        Network Indicator for wingpanel
Version:        2.3.3
Release:        %autorelease
License:        GPLv3+

URL:            https://github.com/elementary/wingpanel-indicator-network
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       network-manager-applet%{?_isa}
Requires:       wingpanel%{?_isa}

Supplements:    wingpanel%{?_isa}


%description
A network indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang network-indicator


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f network-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libnetwork.so

%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
