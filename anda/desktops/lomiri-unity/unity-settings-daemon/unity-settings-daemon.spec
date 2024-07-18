Name:           unity-settings-daemon
Version:        15.04.1+21.10.20220802
Release:        2%?dist
Summary:        Daemon handling for Unity session settings

License:        GPL-2.0 AND LGPL-2.0-or-later
URL:            https://launchpad.net/unity-settings-daemon
Source0:        http://archive.ubuntu.com/ubuntu/pool/universe/u/unity-settings-daemon/unity-settings-daemon_%{version}.orig.tar.gz
Source1:        unity-settings-daemon.service
Source2:        unity-settings-daemon.1

BuildRequires: automake libtool gnome-common
BuildRequires: intltool
BuildRequires: make
BuildRequires: gcc
BuildRequires: g++
BuildRequires: systemd-rpm-macros
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: pkgconfig(lcms2)
BuildRequires: libnotify-devel
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xi)
BuildRequires: libXext-devel
BuildRequires: xorg-x11-server-devel
BuildRequires: gperf
BuildRequires: ibus-devel
BuildRequires: accountsservice-devel
BuildRequires: pkgconfig(xkbfile)
BuildRequires: xkeyboard-config-devel
BuildRequires: pkgconfig(fcitx-config)
BuildRequires: pkgconfig(fcitx-gclient)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pulseaudio-libs-devel
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: alsa-lib-devel
BuildRequires: libXrandr-devel
BuildRequires: upower-devel
BuildRequires: pkgconfig(colord)
BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(xorg-wacom)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(packagekit-glib2)
BuildRequires: NetworkManager-libnm-devel
BuildRequires: gsettings-ubuntu-touch-schemas
Requires:      hwdata
Requires:      gsettings-ubuntu-touch-schemas

%description
The settings daemon used in Unity. It is based on GNOME Settings Daemon 3.8.6.1.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%autosetup -n unity-settings-daemon-%{version}

# Requires internet so manually installing manpage
rm -rf man
sed -i '/man\/Makefile/d' "configure.ac"
sed -i '/man/d' Makefile.am

%build
# Some flag fixes an issue
export LDFLAGS="$LDFLAGS -Wl,-O1 -Wl,-z,defs -Wl,--warn-unresolved-symbols -Wl,--as-needed"

NOCONFIGURE=1 \
./autogen.sh

%configure --disable-static --enable-packagekit --enable-ibus --enable-fcitx --enable-network-manager

%make_build

%install
%make_install
rm -fv %{buildroot}%{_libdir}/unity-settings-daemon-1.0/*.la %{buildroot}%{_libdir}/*.la

pushd %{buildroot}
mkdir -m 755 -p .%{_bindir}
ln -fs %{_libexecdir}/unity-settings-daemon .%{_bindir}/unity-settings-daemon
popd

# Install this
mkdir -m 755 -p %{buildroot}%{_userunitdir}
install -m 644 %{SOURCE1} -t %{buildroot}%{_userunitdir}

# Requires internet so manually installing
mkdir -m 755 -p %{buildroot}%{_mandir}/man1
install -m 644 %{SOURCE2} -t %{buildroot}%{_mandir}/man1

# This conflicts
rename 61-gnome-settings-daemon-rfkill.rules 60-gnome-settings-daemon-rfkill.rules %{buildroot}%{_prefix}/lib/udev/rules.d/61-gnome-settings-daemon-rfkill.rules

%find_lang %{name}

%files -f %{name}.lang
%license COPYING COPYING.LIB
%config %{_sysconfdir}/xdg/autostart/*.desktop
%{_bindir}/unity-settings-daemon
%{_prefix}/lib/udev/rules.d/60-gnome-settings-daemon-rfkill.rules
%{_userunitdir}/unity-settings-daemon.service
%{_libdir}/libunity-settings-daemon.so.*
%{_libdir}/unity-settings-daemon-1.0/
%{_libexecdir}/check_gl_texture_size
%{_libexecdir}/gnome-update-wallpaper-cache
%{_libexecdir}/gsd-test-rfkill
%{_libexecdir}/unity-*
%{_libexecdir}/usd-*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*
%{_mandir}/man1/unity-settings-daemon.1.gz
%{_datadir}/polkit-1/actions/*.policy
%dir %{_datadir}/unity-settings-daemon
%dir %{_datadir}/unity-settings-daemon/icons
%dir %{_datadir}/unity-settings-daemon/icons/hicolor
%dir %{_datadir}/unity-settings-daemon/icons/hicolor/64x64
%dir %{_datadir}/unity-settings-daemon/icons/hicolor/64x64/devices
%{_datadir}/unity-settings-daemon/icons/hicolor/64x64/devices/*.png
%dir %{_datadir}/unity-settings-daemon-1.0
%{_datadir}/unity-settings-daemon-1.0/input-device-example.sh

%files devel
%{_libdir}/libunity-settings-daemon.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/unity-settings-daemon-1.0
%dir %{_includedir}/unity-settings-daemon-1.0/libunity-settings-daemon
%{_includedir}/unity-settings-daemon-1.0/libunity-settings-daemon/*.h
%dir %{_includedir}/unity-settings-daemon-1.0/unity-settings-daemon
%{_includedir}/unity-settings-daemon-1.0/unity-settings-daemon/*.h

%changelog
%autochangelog
