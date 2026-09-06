%global appid com.jaoushingan.WaydroidHelper
%define debug_package %{nil}

Name:           waydroid-helper
Version:        0.2.9
Release:        1%?dist
Summary:        User-friendly way to configure Waydroid and install extensions
License:        GPL-3.0-or-later
URL:            https://github.com/waydroid-helper/waydroid-helper
Source0:        %url/archive/refs/tags/v%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>

# https://github.com/waydroid-helper/waydroid-helper/blob/main/waydroid-helper.spec

Recommends:     bindfs
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  libadwaita-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  systemd
BuildRequires:  desktop-file-utils

%description
Waydroid Helper is a graphical user interface application written in Python using PyGObject. It provides a user-friendly way to configure Waydroid and install extensions, including Magisk and ARM translation.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%terra_appstream
%find_lang %name

%post
%systemd_post waydroid-mount.service
%systemd_user_post waydroid-monitor.service

%preun
%systemd_preun waydroid-mount.service
%systemd_user_preun waydroid-monitor.service

%postun
%systemd_postun_with_restart waydroid-mount.service
%systemd_user_postun_with_restart waydroid-monitor.service

%files -f %name.lang
%license COPYING
%doc README.md
%_bindir/waydroid-helper
%_bindir/waydroid-cli
%_datadir/waydroid-helper/
%_datadir/applications/%appid.desktop
%_scalableiconsdir/%appid.svg
%_iconsdir/hicolor/symbolic/apps/%appid-symbolic.svg
%_datadir/metainfo/%appid.metainfo.xml
%_datadir/glib-2.0/schemas/%appid.gschema.xml
%_datadir/polkit-1/actions/%appid.policy
%_datadir/dbus-1/system.d/id.waydro.Mount.conf
%_datadir/dbus-1/system-services/id.waydro.Mount.service
%_unitdir/waydroid-mount.service
%_userunitdir/waydroid-monitor.service

%changelog
* Mon Mar 05 2026 madonuko <mado@fyralabs.com> - 0.2.9-1
- Initial package
