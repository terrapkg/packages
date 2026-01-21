%global snapshot r1245.8e82100

Name:           gpu-screen-recorder
Version:        5.12.1
Release:        1%?dist
Summary:        A shadowplay-like screen recorder for Linux

License:        GPL-3.0-or-later

URL:            https://git.dec05eba.com/%{name}/about

Source:         https://dec05eba.com/snapshot/%{name}.git.%{snapshot}.tar.gz

BuildRequires:  gcc
BuildRequires:  (gcc-g++ or gcc-c++)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  (ffmpeg-free-devel or ffmpeg-devel or ffmpeg-7-mini-devel) 
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libglvnd)
Requires(post): libcap
BuildRequires:  systemd-rpm-macros

Packager:       Willow Reed <willow@willowidk.dev>

%description
Shadowplay-like screen recorder for Linux. Uses GPU acceleration to record in H.264, HEVC, AV1, VP8, or VP9.

%prep
%autosetup -c

%build
%meson -Dcapabilities=false
%meson_build

%install
%meson_install

%check
%meson_test

%post
%systemd_user_post gpu-screen-recorder.service

%preun
%systemd_user_preun gpu-screen-recorder.service

%postun
%systemd_user_postun gpu-screen-recorder.service

%files
%license LICENSE
%doc README.md
%{_bindir}/gpu-screen-recorder
%caps(cap_sys_admin+ep) %{_bindir}/gsr-kms-server
%{_includedir}/gsr/plugin.h
%{_userunitdir}/%{name}.service
%{_modprobedir}/gsr-nvidia.conf
%{_mandir}/man1/gsr-kms-server.1*
%{_mandir}/man1/gpu-screen-recorder.1*

%changelog
* Fri Jan 02 2026 Willow Reed <willow@willowidk.dev>
- Initial commit