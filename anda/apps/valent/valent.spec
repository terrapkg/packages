%global commit df82168bc37ad1ec700c66b0f0f5dfd7a07be485
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260316

Name:               valent
Version:            0~%{commit_date}git.%{shortcommit}
Release:            1%{?dist}
Summary:            Connect, control and sync devices
License:            GPL-3.0-or-later
URL:                https://github.com/andyholmes/valent
Source0:            %{url}/archive/%{commit}/valent-%{commit}.tar.gz
Source1:            https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/archive/master/libgnome-volume-control-master.tar.gz
Packager:           Tulip Blossom <tulilirockz@outlook.com>

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
%pkg_devel_files
%{_datadir}/vala/vapi/libvalent-1.deps
%{_datadir}/vala/vapi/libvalent-1.vapi
%{_libdir}/libvalent-1.so.0
%{_libdir}/libvalent-1.so.1.0.0

%package langpacks
Summary:           Translations for %{name}
BuildArch:         noarch
Requires:          %{name} = %{evr}

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
