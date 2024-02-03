Name:           unl0kr
Version:        2.0.3
Release:        %autorelease
Summary:        Disk unlocker for the initramfs based on LVGL.

License:        GPL-v3.0
URL:            https://gitlab.com/postmarketOS/buffybox

BuildRequires:  pkgconfig(inih) pkgconfig(libinput) pkgconfig(libudev) pkgconfig(xkbcommon) pkgconfig(libdrm) pkgconfig(scdoc) git meson gcc
Requires:       inih libxkbcommon libinput systemd libdrm cryptsetup
Conflicts:      osk-sdl

%description
Unl0kr is an osk-sdl clone written in LVGL and rendering directly to the Linux framebuffer. As a result, it doesn't depend on GPU hardware acceleration.

%prep
git clone --recursive --shallow-submodules --branch unl0kr-%version %url.git .


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license    COPYING
%doc        doc/*
%{_bindir}/unl0kr
%{_sysconfdir}/unl0kr.conf
%{_mandir}/man1/unl0kr.1.gz
%{_mandir}/man5/unl0kr.conf.5.gz


%changelog
* Fri Feb 2 2024 infinitebash <infinitebash@fyralabs.com>
- Initial package
%autochangelog
