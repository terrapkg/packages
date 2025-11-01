Name:           mpvpaper
Version:        1.8
Release:        1%?dist
Summary:        A video wallpaper program for wlroots based wayland compositors
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://github.com/GhostNaN/mpvpaper
Source:         %url/archive/%version.tar.gz
BuildRequires:  meson
BuildRequires:  mpv-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  wayland-protocols-devel
BuildRequires:  wlroots-devel
BuildRequires:  gcc
Requires:       mpv

%description
%summary.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
install -Dm644 %name.man %buildroot%_mandir/man1/%name.1

%files
%license LICENSE
%doc README.md
%_bindir/mpvpaper
%_bindir/mpvpaper-holder
%_mandir/man1/mpvpaper.1.gz

%changelog
* Fri Dec 20 2024 madonuko <mado@fyralabs.com> - 1.7-1
- Initial package
