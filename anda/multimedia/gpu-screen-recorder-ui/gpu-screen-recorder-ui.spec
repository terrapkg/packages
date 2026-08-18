Name:           gpu-screen-recorder-ui
Version:        1.13.5
Release:        1%{?dist}
Summary:        A fullscreen overlay UI for GPU Screen Recorder in the style of ShadowPlay

License:        GPL-3.0-or-later

URL:            https://git.dec05eba.com/%{name}/about

Source:         https://dec05eba.com/snapshot/%{name}.git.%{version}.tar.gz

BuildRequires:  meson gcc gcc-c++
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glx)
BuildRequires:  pkgconfig(egl)
BuildRequires:  kernel-headers
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  rpm_macro(buildsystem_meson_conf)
BuildSystem:    meson

Packager:       madonuko <mado@fyralabs.com>

%description
%summary.

%post
setcap cap_setuid+ep /usr/bin/gsr-global-hotkeys

%files
%license LICENSE
%doc README.md
%_appsdir/gpu-screen-recorder.desktop
%_bindir/gsr-game-tracker
%_bindir/gsr-global-hotkeys
%_bindir/gsr-gnome-helper
%_bindir/gsr-kwin-helper
%_bindir/gsr-ui
%_bindir/gsr-ui-cli
%_bindir/gsr-wayland-bridge
%_datadir/gsr-ui
%_hicolordir/*/apps/gpu-screen-recorder.png
%_mandir/man1/gsr-ui-cli.1.*
%_mandir/man1/gsr-ui.1.*
