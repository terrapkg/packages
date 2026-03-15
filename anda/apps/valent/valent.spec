%global commit 1b540bb7562206d33a3646b698fba899e50ba29d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260315

Name:               valent
Version:            0~%{commit_date}git.%{shortcommit}
Release:            1%{?dist}
Summary:            Connect, control and sync devices
License:            GPL-3.0-or-later
URL:                https://github.com/andyholmes/valent
Source0:            %{url}/archive/%{commit}/valent-%{commit}.tar.gz
Source1:            https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/archive/master/libgnome-volume-control-master.tar.gz

Provides:           bundled(gvc)
BuildRequires:      desktop-file-utils
BuildRequires:      evolution-data-server-devel
BuildRequires:      gcc
BuildRequires:      gcc-c++
BuildRequires:      libphonenumber-devel
BuildRequires:      meson
BuildRequires:      pkgconfig(glycin-2)
BuildRequires:      pkgconfig(glycin-gtk4-2)
BuildRequires:      pkgconfig(gnutls)
BuildRequires:      pkgconfig(gstreamer-1.0)
BuildRequires:      pkgconfig(json-glib-1.0)
BuildRequires:      pkgconfig(libadwaita-1)
BuildRequires:      pkgconfig(libpeas-2)
BuildRequires:      pkgconfig(libpipewire-0.3)
BuildRequires:      pkgconfig(libportal-gtk4)
BuildRequires:      pkgconfig(libpulse)
BuildRequires:      pkgconfig(tracker-sparql-3.0)

%description
%{summary}.

%package devel
Summary:           Development files for building against %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          evolution-data-server-devel
Requires:          libphonenumber-devel
Requires:          pkgconfig(glycin-2)
Requires:          pkgconfig(glycin-gtk4-2)
Requires:          pkgconfig(gnutls)
Requires:          pkgconfig(gstreamer-1.0)
Requires:          pkgconfig(json-glib-1.0)
Requires:          pkgconfig(libadwaita-1)
Requires:          pkgconfig(libpeas-2)
Requires:          pkgconfig(libpipewire-0.3)
Requires:          pkgconfig(libportal-gtk4)
Requires:          pkgconfig(libpulse)
Requires:          pkgconfig(tracker-sparql-3.0)

%description devel
Development files needed for building things which link against %{name}.
 
%package langpacks
Summary:           Translations for %{name}
BuildArch:         noarch
Requires:          %{name} = %{version}-%{release}
 
%description langpacks
This package contains translations for %{name}.

%prep
%autosetup -n valent-%{commit} -p1
rm -r subprojects/gvc*
tar -xf %{SOURCE1} -C subprojects
mv subprojects/libgnome-volume-control* subprojects/gvc

%conf
%meson

%build
%meson_build

%install
%meson_install

%files langpacks
%{_datadir}/locale

%files devel
%{_datadir}/vala/vapi/libvalent-1.deps
%{_datadir}/vala/vapi/libvalent-1.vapi
%{_includedir}/libvalent-1
%{_libdir}/libvalent-1.so
%{_libdir}/libvalent-1.so.0
%{_libdir}/libvalent-1.so.1.0.0
%{_libdir}/pkgconfig/libvalent-1.pc

%files
%license LICENSE
%doc README.md
%{_bindir}/valent
%{_datadir}/applications/ca.andyholmes.Valent.desktop
%{_datadir}/dbus-1/services/ca.andyholmes.Valent.service
%{_datadir}/gir-1.0/Valent-1.gir
%{_datadir}/glib-2.0/schemas/ca.andyholmes.Valent.Plugin.battery.gschema.xml
%{_datadir}/glib-2.0/schemas/ca.andyholmes.Valent.Plugin.clipboard.gschema.xml
%{_datadir}/glib-2.0/schemas/ca.andyholmes.Valent.Plugin.connectivity_report.gschema.xml
%{_datadir}/glib-2.0/schemas/ca.andyholmes.Valent.Plugin.contacts.gschema.xml
%{_datadir}/glib-2.0/schemas/ca.andyholmes.Valent.Plugin.notification.gschema.xml
%{_datadir}/glib-2.0/schemas/ca.andyholmes.Valent.Plugin.runcommand.gschema.xml
%{_datadir}/glib-2.0/schemas/ca.andyholmes.Valent.Plugin.sftp.gschema.xml
%{_datadir}/glib-2.0/schemas/ca.andyholmes.Valent.Plugin.share.gschema.xml
%{_datadir}/glib-2.0/schemas/ca.andyholmes.Valent.Plugin.systemvolume.gschema.xml
%{_datadir}/glib-2.0/schemas/ca.andyholmes.Valent.Plugin.telephony.gschema.xml
%{_datadir}/glib-2.0/schemas/ca.andyholmes.Valent.Plugin.xdp.gschema.xml
%{_datadir}/glib-2.0/schemas/ca.andyholmes.Valent.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/ca.andyholmes.Valent.svg
%{_datadir}/icons/hicolor/symbolic/apps/ca.andyholmes.Valent-symbolic.svg
%{_datadir}/metainfo/ca.andyholmes.Valent.metainfo.xml
%{_libdir}/girepository-1.0/Valent-1.typelib
%{_sysconfdir}/xdg/autostart/ca.andyholmes.Valent-autostart.desktop

%changelog
* Sun Mar 15 2026 Tulip Blossom <tulilirockz@outlook.com>
- Initial commit
