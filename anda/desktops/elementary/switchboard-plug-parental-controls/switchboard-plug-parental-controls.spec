%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-parental-controls

%global plug_type system
%global plug_name parental-controls
%global plug_rdnn io.elementary.switchboard.parental-controls

Name:           switchboard-plug-parental-controls
Summary:        Switchboard Screen Time & Limits Plug
Version:        6.0.1
Release:        2%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/%name
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.46.1
BuildRequires:  vala

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(libhandy-1) >= 0.90.0
BuildRequires:  pkgconfig(malcontent-0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  polkit-devel
BuildRequires:  switchboard-devel

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
%summary.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{plug_name}-plug

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml

%_sysconfdir/pantheon-parental-controls/daemon.conf
%_bindir/pantheon-parental-controls-daemon
%_libexecdir/pantheon-parental-controls-client
%_datadir/applications/pantheon-parental-controls-client.desktop
%_datadir/dbus-1/system-services/org.pantheon.ParentalControls.service
%_datadir/dbus-1/system.d/org.pantheon.ParentalControls.conf
%_datadir/polkit-1/actions/io.elementary.switchboard.screentime-limits.policy
/usr/lib/systemd/system/pantheon-parental-controls.service

%changelog
* Tue Jun 13 2023 windowsboy111 <windowsboy111@fyralabs.com> - 6.0.1-1
- Initial package.
