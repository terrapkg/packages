Name:			hyprlock
Version:		0.8.2
Release:		1%?dist
Summary:		Hyprland's GPU-accelerated screen locking utility
License:		BSD-3-Clause
URL:			https://github.com/hyprwm/%name
Source0:		%url/archive/refs/tags/v%version.tar.gz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	cmake gcc gcc-c++
BuildRequires:	pkgconfig(cairo)
BuildRequires:	(pkgconfig(hyprgraphics) with hyprgraphics.nightly-devel)
BuildRequires:	pkgconfig(hyprland-protocols)
BuildRequires:	(pkgconfig(hyprlang) with hyprlang.nightly-devel)
BuildRequires:	pkgconfig(hyprutils)
BuildRequires:	(pkgconfig(hyprwayland-scanner) with hyprwayland-scanner.nightly-devel)
BuildRequires:	mesa-libgbm-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	pkgconfig(pam)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(sdbus-c++) >= 2.0.0
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(libmagic)

%description
%summary.

%prep
%autosetup

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%_bindir/%name
%_pam_confdir/%name
%_datadir/hypr/%name.conf
