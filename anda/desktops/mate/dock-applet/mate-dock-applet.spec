%define debug_package %nil

Name:           mate-dock-applet
Version:        21.10.0
Release:        1%?dist
Summary:        Application dock for the MATE panel
License:        GPL-3.0-or-later
URL:            https://github.com/ubuntu-mate/mate-dock-applet
Source0:        %url/archive/refs/tags/%version.tar.gz
BuildRequires:  automake make
BuildRequires:  python3 python3-xlib python3-pillow glib2-devel python3-cairo bamf-daemon bamf python3-distro gettext-devel
Requires:       bamf libnotify mate-panel python3-cairo python3-dbus python3-gobject python3-pillow python3-xdg python3-xlib
Packager:       madonuko <mado@fyralabs.com>

%description
%summary.

%prep
%autosetup
autoreconf -fi

%build
%configure --with-gtk3
%make_build

%install
%make_install

%files
%doc README.md
%license COPYING
%_libdir/mate-applets/%name/
%_datadir/dbus-1/services/org.mate.panel.applet.DockAppletFactory.service
%_datadir/glib-2.0/schemas/org.mate.panel.applet.dock.gschema.xml
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_datadir/mate-panel/applets/org.mate.panel.DockApplet.mate-panel-applet
