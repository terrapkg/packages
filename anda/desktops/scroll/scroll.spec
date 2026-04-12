Name:           scroll
Version:        1.12.8
Release:        1%{?dist}
Summary:        i3-compatible Wayland compositor (sway) with a PaperWM layout like niri or hyprscroller
License:        MIT
URL:            https://github.com/dawsers/scroll
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
# https://aur.archlinux.org/cgit/aur.git/tree/?h=sway-scroll
Source1:        50-systemd-user.conf
Source2:        scroll-portals.conf

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libliftoff)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)

Provides:       sway-scroll

%description
%{summary}.

%prep
%autosetup

%pkg_completion -B scroll scrollbar scrollmsg
%pkg_completion -f scroll scrollmsg scrollnag
%pkg_completion -z scroll scrollmsg

%build
%meson -D sd-bus-provider=libsystemd
%meson_build

%install
%meson_install
install -Dm644 %{S:1} %{buildroot}%{_sysconfdir}/scroll/config.d/50-systemd-user.conf
install -Dm644 %{S:2} %{buildroot}%{_datadir}/xdg-desktop-portal/scroll-portals.conf

%files
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/scroll
%{_bindir}/scrollbar
%{_bindir}/scrollmsg
%{_bindir}/scrollnag
%{_sysconfdir}/scroll/config
%{_sysconfdir}/scroll/config.d/50-systemd-user.conf
%{_datadir}/backgrounds/scroll/*png
%{_datadir}/xdg-desktop-portal/scroll-portals.conf
%{_iconsdir}/scroll.png
%{_mandir}/man1/scroll.1.*
%{_mandir}/man1/scrollmsg.1.*
%{_mandir}/man1/scrollnag.1.*
%{_mandir}/man5/scroll-bar.5.*
%{_mandir}/man5/scroll-input.5.*
%{_mandir}/man5/scroll-output.5.*
%{_mandir}/man5/scroll.5.*
%{_mandir}/man5/scrollnag.5.*
%{_mandir}/man7/scroll-ipc.7.*
%{_mandir}/man7/scrollbar-protocol.7.*
%{_datadir}/wayland-sessions/scroll.desktop

%changelog
* Sun Apr 12 2026 Owen Zimmerman <owen@fyralabs.com> - 1.12.8-1
- Initial commit
