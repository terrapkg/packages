Name:           budgie-extras
Version:        2.2.3
Release:        3%{?dist}

License:        GPL-3.0-or-later
Summary:        Additional Budgie Desktop enhancements for user experience
URL:            https://ubuntubudgie.org/

Source0:        https://github.com/UbuntuBudgie/budgie-extras/releases/download/v%{version}/budgie-extras-%{version}.tar.xz

BuildRequires:  rpm_macro(fdupes)
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  intltool

BuildRequires:  pkgconfig(budgie-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libxfce4windowing-0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)

BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(zeitgeist-2.0)

Requires:       budgie-applet-app-launcher
Requires:       budgie-applet-applications-menu
Requires:       budgie-applet-brightness-controller
Requires:       budgie-applet-clockworks
Requires:       budgie-applet-countdown
Requires:       budgie-applet-dropby
Requires:       budgie-applet-fuzzyclock
Requires:       budgie-applet-kangaroo
Requires:       budgie-applet-network-manager
Requires:       budgie-applet-quicknote
Requires:       budgie-applet-recentlyused
Requires:       budgie-applet-screencast
Requires:       budgie-applet-showtime
Requires:       budgie-applet-takeabreak
Requires:       budgie-applet-visualspace
Requires:       budgie-applet-wallstreet
Requires:       budgie-applet-weathershow
Requires:       budgie-applet-wswitcher
# Fix for https://github.com/UbuntuBudgie/budgie-extras/issues/233, don't know how stenstorp did not notice this
Requires:       xinput

%description
This is part of a suite of python3 and Vala based applets for the Budgie
Desktop that provide additional user orientated capabilities.
The applets can be used individually or as a set.

%package        common
Requires:       budgie-desktop
Summary:        Shared component of budgie-extras applets
BuildArch:      noarch
%description	  common
The shared component provides for capabilities that are utilised between
budgie-extra applets.

%package        daemon
Summary:        Manages keyboard shortcuts
Requires:       budgie-extras-common
%description    daemon
This on logon process manages keyboard shortcuts delivered via .bde files for
various extras-plugins.

%package -n	budgie-applet-app-launcher
Requires:       budgie-extras-common
Summary:        Applet to provide an alternative means to launch applications
%description -n	budgie-applet-app-launcher
The app-launcher applet allows the ability to add favorite apps to the
panel as well as finding and launching applications.  The list of
applications listed can be easily configured to be visible or hidden.

%package -n	budgie-applet-applications-menu
Requires:       budgie-extras-common
Summary:        Lightweight and stylish app launcher
%description -n	budgie-applet-applications-menu
%{summary}

%package -n	budgie-applet-brightness-controller
Requires:       budgie-extras-common
Summary:        A Budgie Desktop applet for productivity
%description -n	budgie-applet-brightness-controller
%{summary}

%package -n	budgie-applet-clockworks
Requires:       budgie-extras-common
Summary:        Applet to display clock across multiple time zones
%description -n	budgie-applet-clockworks
The Clockworks applet displays the current time across multiple
time zones.

%package -n	budgie-applet-countdown
Requires:       budgie-extras-common
Summary:        Applet providing a countdown capability on the Budgie Desktop
%description -n	budgie-applet-countdown
The Countdown applet provides the user the ability to start an
action when the countdown reaches 0 seconds. Actions include flashing
an icon in the panel, opening a notification window, sounding a
bell or running a custom command.

%package -n	budgie-applet-dropby
Requires:       budgie-extras-common
Summary:        Applet to popup when a USB device is connected
%description -n	budgie-applet-dropby
The DropBy applet pops up in the panel when connecting a usb device.
The applet subsequently offers the option(s) to mount, unmount/eject
and in case of a flash drive, to make a local copy of the drive's
content. The info shows the free space on the volume.

%package -n	budgie-applet-fuzzyclock
Requires:       budgie-extras-common
Summary:        Shows the time in a Fuzzy Way
%description -n	budgie-applet-fuzzyclock
%{summary}

%package -n	budgie-applet-kangaroo
Requires:       budgie-extras-common
Summary:        Applet to allow quick file-browsing
%description -n	budgie-applet-kangaroo
The kangaroo applet allows for quick & easy browsing, across
(possibly) many directory layers, without having to do a single mouse
click.

%package -n	budgie-applet-network-manager
Requires:       budgie-extras-common
Summary:        A fork of Wingpanel Network Indicator, ported to budgie desktop
%description -n	budgie-applet-network-manager
%{summary}

%package -n	budgie-applet-quicknote
Requires:       budgie-extras-common
Summary:        Applet providing simple notes capability for the Budgie Desktop
%description -n	budgie-applet-quicknote
The quicknote applet allows a user to record a text based note.
The applet supports multiple undo and redo capabilities.

%package -n	budgie-applet-recentlyused
Requires:       budgie-extras-common
Summary:        Applet displays files recently accessed for the Budgie Desktop
%description -n	budgie-applet-recentlyused
The recentlyused applet displays the users files that have been opened
or created within a configurable period of time.

%package -n	budgie-applet-screencast
Requires:       budgie-extras-common
Summary:        Applet wrapper around wf-recorder
%description -n	budgie-applet-screencast
Applet wrapper around wf-recorder. Allows recording of whole screen displays or areas.

%package -n	budgie-applet-showtime
Requires:       budgie-extras-common
Summary:        Applet displaying date and time on the Budgie Desktop
%description -n	budgie-applet-showtime
The ShowTime applet is a digital desktop clock, showing time and/or
date.  Text color of both the displayed time and date can be set
separately from the applet's menu

%package -n	budgie-applet-takeabreak
Requires:       budgie-extras-common
Summary:        A pomodoro-like applet, to make sure to take regular breaks from working
%description -n	budgie-applet-takeabreak
Budgie TakeaBreak is a pomodoro- like applet, to make sure to take regular
breaks from working. Options from Budgie Settings include turning the screen
upside down, dim the screen, lock screen or show a countdown message on break
time. The applet can be accessed quickly from the panel to temporarily switch
it off.

%package -n	budgie-applet-visualspace
Requires:       budgie-extras-common
Summary:        Shows the current workspace(s), as bullet(s)
%description -n	budgie-applet-visualspace
Budgie VisualSpace shows the current workspace(s), as bullet(s). The applet
includes a menu to navigate to either one of the windows or their
corresponding workspace.

%package -n	budgie-applet-wallstreet
Requires:       budgie-extras-common
Summary:        A mini-app to switch wallpapers on regular intervalls
%description -n	budgie-applet-wallstreet
Budgie WallStreet is a mini-app to switch wallpapers on regular intervalls.

%package -n	budgie-applet-weathershow
Requires:       budgie-extras-common
Summary:        Applet to display the weather and forecast
%description -n	budgie-applet-weathershow
The weathershow applet displays daily and three hourly weather
forecasts on both the desktop and a Popover.

%package -n	budgie-applet-wswitcher
Requires:       budgie-extras-common
Requires:       budgie-extras-daemon
Summary:        An applet to show a different wallpaper on each of the workspaces
%description -n	budgie-applet-wswitcher
Budgie Wallpaper Workspace Switcher is an application (applet) to show a
different wallpaper on each of the workspaces. Usage is simple: add the applet
to the panel and set wallpapers on each of the workspaces in the way you are
used to. The applet will remember what wallpaper was set on each of the
workspaces.

%prep
%autosetup -p1

find . -name "meson.build" -exec sed -i "s/dependency('budgie-1.0')/dependency('budgie-3.0')/g" {} +
find . -name "meson.build" -exec sed -i "s/dependency('libpeas-1.0')/dependency('libpeas-2')/g" {} +
find . -name "meson.build" -exec sed -i "s/dependency('libpeas-gtk-1.0')/dependency('libpeas-2')/g" {} +

%conf
%meson -Dfor-wayland=true

%build
%meson_build

%install
%meson_install

%fdupes %{buildroot}%{_datadir}/budgie-desktop/budgie-weathershow/weather_icons

%post

%files

%files common
%{_datadir}/locale
%{_datadir}/glib-2.0/schemas/20_budgie-extras.gschema.override

%files daemon
%config %{_sysconfdir}/xdg/autostart/budgie-extras-daemon.desktop
%{_bindir}/budgie-extras-daemon
%{_libdir}/budgie-extras-daemon/invoke.py
%{_datadir}/budgie-desktop/layouts/*.layout
%{_mandir}/man1/budgie-extras-daemon.1.gz

%files -n budgie-applet-app-launcher
%{_datadir}/pixmaps/budgie-app-launcher*.svg
%{_libdir}/budgie-desktop/plugins/budgie-app-launcher
%{_metainfodir}/org.ubuntubudgie.applauncher.metainfo.xml

%files -n budgie-applet-applications-menu
%{_libdir}/budgie-desktop/plugins/applications-menu
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-appmenu.gschema.xml

%files -n budgie-applet-brightness-controller
%{_libdir}/budgie-desktop/plugins/budgie-brightness-controller
%{_datadir}/pixmaps/budgie-brightness-controller-1-symbolic.svg
%{_metainfodir}/org.ubuntubudgie.brightnesscontroller.metainfo.xml

%files -n budgie-applet-clockworks
%{_libdir}/budgie-desktop/plugins/budgie-clockworks
%{_datadir}/glib-2.0/schemas/*budgie-clockworks*.xml
%{_datadir}/pixmaps/budgie-clockworks*.svg
%{_metainfodir}/org.ubuntubudgie.clockworks.metainfo.xml

%files -n budgie-applet-countdown
%{_libdir}/budgie-desktop/plugins/budgie-countdown
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-countdown.gschema.xml
%{_datadir}/pixmaps/budgie-countdown-symbolic.svg
%{_datadir}/pixmaps/cr_*.png
%{_metainfodir}/org.ubuntubudgie.countdown.metainfo.xml

%files -n budgie-applet-dropby
%{_libdir}/budgie-desktop/plugins/budgie-dropby
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-dropby.gschema.xml
%{_datadir}/pixmaps/budgie-dropby*.svg
%{_metainfodir}/org.ubuntubudgie.dropby.metainfo.xml

%files -n budgie-applet-fuzzyclock
%{_libdir}/budgie-desktop/plugins/budgie-fuzzyclock
%{_metainfodir}/org.ubuntubudgie.fuzzyclock.metainfo.xml

%files -n budgie-applet-kangaroo
%{_libdir}/budgie-desktop/plugins/budgie-kangaroo
%{_datadir}/pixmaps/budgie-foldertrack-symbolic.svg
%{_metainfodir}/org.ubuntubudgie.kangaroo.metainfo.xml

%files -n budgie-applet-network-manager
%{_libdir}/budgie-desktop/plugins/budgie-network-manager

%files -n budgie-applet-quicknote
%{_libdir}/budgie-desktop/plugins/budgie-quicknote
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.quicknote.gschema.xml
%{_datadir}/pixmaps/budgie-quicknote-symbolic.svg
%{_metainfodir}/org.ubuntubudgie.quicknote.metainfo.xml

%files -n budgie-applet-recentlyused
%{_libdir}/budgie-desktop/plugins/budgie-recentlyused
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-recentlyused.gschema.xml
%{_metainfodir}/org.ubuntubudgie.recentlyused.metainfo.xml

%files -n budgie-applet-screencast
%{_libdir}/budgie-desktop/plugins/budgie-screencast/BudgieScreencast.plugin
%{_libdir}/budgie-desktop/plugins/budgie-screencast/libbudgie-screencast.so
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.budgie-screencast.gschema.xml
%{_datadir}/pixmaps/budgie-screencast-symbolic.svg

%files -n budgie-applet-showtime
%{_libdir}/budgie-desktop/raven-plugins/org.ubuntubudgie.raven.widget.budgie-showtime/*
%{_datadir}/pixmaps/showtimenew-symbolic.svg
%{_metainfodir}/org.ubuntubudgie.showtime.metainfo.xml

%files -n budgie-applet-takeabreak
%{_libdir}/budgie-desktop/plugins/budgie-takeabreak
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.takeabreak.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.raven.widget.budgie-showtime.gschema.xml
%{_datadir}/pixmaps/takeabreak*.svg
%{_metainfodir}/org.ubuntubudgie.takeabreak.metainfo.xml

%files -n budgie-applet-visualspace
%config %{_sysconfdir}/xdg/autostart/visualspace-autostart.desktop
%{_libdir}/budgie-desktop/plugins/budgie-visualspace
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-visualspace.gschema.xml
%{_datadir}/pixmaps/visualspace-symbolic.svg
%{_metainfodir}/org.ubuntubudgie.visualspace.metainfo.xml

%files -n budgie-applet-wallstreet
%config %{_sysconfdir}/xdg/autostart/wallstreet-autostart.desktop
%{_libdir}/budgie-wallstreet/wallstreet*
%{_datadir}/applications/org.ubuntubudgie.wallstreetcontrol.desktop
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.budgie-wallstreet.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.ubuntubudgie.wallstreet-control.svg
%{_datadir}/metainfo/org.ubuntubudgie.wallstreetcontrol.metainfo.xml

%files -n budgie-applet-weathershow
%{_libdir}/budgie-desktop/plugins/budgie-weathershow
%{_datadir}/budgie-desktop/budgie-weathershow/cities
%{_datadir}/budgie-desktop/budgie-weathershow/weather_icons/*
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.weathershow.gschema.xml
%{_datadir}/pixmaps/budgie-wticon-symbolic.svg
%{_metainfodir}/org.ubuntubudgie.weathershow.metainfo.xml

%files -n budgie-applet-wswitcher
%{_libdir}/budgie-desktop/raven-plugins/org.ubuntubudgie.raven.widget.budgie-wswitcher/*
%{_datadir}/glib-2.0/schemas/org.ubuntubudgie.plugins.budgie-wswitcher.gschema.xml
%{_datadir}/pixmaps/budgie-wsw-symbolic.svg
%{_metainfodir}/org.ubuntubudgie.wswitcher.metainfo.xml

%changelog
* Tue Jun 02 2026 Owen Zimmerman <owen@fyralabs.com> - 2.2.3-1
- Update for 2.2.3

* Thu Jun 09 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 1.4.0-1
- Updated to 1.4.0
- Added requirements for Workspace Overview

* Fri Apr 16 2021 Thomas Batten <stenstorpmc@gmail.com> - 1.2.0-1
- Initial Build
