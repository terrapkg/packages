Name:           gpu-screen-recorder-notification
Version:        1.3.4
Release:        1%{?dist}
Summary:        Notification in the style of ShadowPlay

License:        GPL-3.0-or-later

URL:            https://git.dec05eba.com/%{name}/about

Source:         https://dec05eba.com/snapshot/%{name}.git.%{version}.tar.gz

BuildRequires:  gcc gcc-c++
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glx)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(pango)
BuildRequires:  rpm_macro(buildsystem_meson_conf)
BuildSystem:    meson

Packager:       madonuko <mado@fyralabs.com>

%description
%summary.

%files
%license LICENSE
%doc README.md
%_bindir/gsr-notify
%_datadir/gsr-notify

%changelog
* Tue Aug 18 2026 madonuko <mado@fyralabs.com> - 1.3.4-1
- Initial package
