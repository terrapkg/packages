Name:			hypridle
Version:		0.1.6
Release:		1%?dist
Summary:		Hyprland's idle daemon
License:		BSD-3-Clause
URL:			https://github.com/hyprwm/hypridle
Source0:		%url/archive/refs/tags/v%version.tar.gz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	cmake
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(hyprland-protocols)
BuildRequires:	(pkgconfig(hyprlang) >= 0.6.0 with hyprlang.nightly-devel)
BuildRequires:	pkgconfig(sdbus-c++)
BuildRequires:	(pkgconfig(hyprwayland-scanner) with hyprwayland-scanner.nightly-devel)
BuildRequires:	pkgconfig(hyprutils) >= 0.2.0

%description
%summary.

%prep
%autosetup

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%install
%cmake_install

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun_with_restart %name.service

%files
%_userunitdir/%name.service
