Name:			hyprlock
Version:		0.8.2
Release:		1%?dist
Summary:		Hyprland's GPU-accelerated screen locking utility
License:		BSD-3-Clause
URL:			https://github.com/hyprwm/%name
Source0:		%url/archive/refs/tags/v%version.tar.gz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	cmake
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(hyprgraphics)
BuildRequires:	pkgconfig(hyprland-protocols)
BuildRequires:	pkgconfig(hyprlang)
BuildRequires:	pkgconfig(hyprutils)
BuildRequires:	pkgconfig(hyprwayland-scanner)
BuildRequires:	mesa-libgbm-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	pkgconfig(pam)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(sdbus-c++)

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
