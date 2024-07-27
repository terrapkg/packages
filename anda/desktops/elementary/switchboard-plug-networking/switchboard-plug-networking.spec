%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-network

%global plug_type network
%global plug_name networking
%global plug_rdnn io.elementary.settings.network

Name:           switchboard-plug-networking
Summary:        Switchboard Networking plug
Version:        8.0.0
Release:        1%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/switchboard-plug-network
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0
BuildRequires:  fdupes

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
#BuildRequires:  pkgconfig(granite)
#BuildRequires:  pkgconfig(gthread-2.0)
#BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma-gtk4)
#BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-3)

Requires:       network-manager-applet%{?_isa}
Requires:       switchboard%{?_isa}
Requires:       NetworkManager%{?_isa}

Supplements:    (switchboard%{?_isa} and NetworkManager%{?_isa})

%description
A switchboard plug for configuring available networks.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%fdupes %buildroot%_datadir/locale/
%find_lang %{plug_rdnn}


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_rdnn}.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard-3/%{plug_type}/libnetwork.so

%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%changelog
* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 2.4.4-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
