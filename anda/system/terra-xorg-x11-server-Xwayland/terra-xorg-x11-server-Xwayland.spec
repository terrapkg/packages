%global commit 9a55c402aa803fb10e39ab4fd18a709d0cd06fd4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

#global gitdate 20230426
%global pkgname %{?gitdate:xserver}%{!?gitdate:xwayland}

%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"

Summary:   Xwayland with gaming patches
Name:      terra-xorg-x11-server-Xwayland
Version:   24.1.13
Release:   1%{?dist}
Packager:  Kyle Gospodnetich <me@kylegospodneti.ch>

URL:       http://www.x.org
%if 0%{?gitdate}
Source0:   https://gitlab.freedesktop.org/xorg/%{pkgname}/-/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
%else
Source0:   https://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.xz
%endif

License:   MIT

## Steam OS Patches
Patch0:    0001-Revert-xwayland-Restrict-allow-commit-to-the-window-.patch
Patch1:    0002-Revert-xwayland-present-Check-allow_commits-in-xwl_p.patch

# Nobara Patches
Patch2:    xwayland-pointer-warp-fix.patch

Provides:  xorg-x11-server-Xwayland = %{evr}
Conflicts: xorg-x11-server-Xwayland

Requires: xkeyboard-config
Requires: xkbcomp
Requires: libEGL
Requires: libepoxy >= 1.5.5

BuildRequires: gcc
BuildRequires: git-core
BuildRequires: meson

BuildRequires: wayland-devel
BuildRequires: desktop-file-utils

BuildRequires: pkgconfig(wayland-client) >= 1.21.0
BuildRequires: pkgconfig(wayland-protocols) >= 1.34

BuildRequires: pkgconfig(epoxy) >= 1.5.5
BuildRequires: pkgconfig(fontenc)
BuildRequires: pkgconfig(libdrm) >= 2.4.89
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libtirpc)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xfont2)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xres)
BuildRequires: pkgconfig(xshmfence) >= 1.1
BuildRequires: pkgconfig(xtrans) >= 1.3.2
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xv)
BuildRequires: pkgconfig(libxcvt)
BuildRequires: pkgconfig(libdecor-0) >= 0.1.1
BuildRequires: pkgconfig(liboeffis-1.0) >= 1.0.0
BuildRequires: pkgconfig(libei-1.0) >= 1.0.0
BuildRequires: xorg-x11-proto-devel >= 2025.1-1

BuildRequires: mesa-libGL-devel >= 9.2
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libgbm-devel

BuildRequires: audit-libs-devel
BuildRequires: libselinux-devel >= 2.0.86-1

# libunwind is Exclusive for the following arches
%ifarch aarch64 %{arm} hppa ia64 mips ppc ppc64 %{ix86} x86_64
%if !0%{?rhel}
BuildRequires: libunwind-devel
%endif
%endif

BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-renderutil)

%description
Xwayland is an X server for running X clients under Wayland.

%package devel
Summary: Development package
Provides: xorg-x11-server-Xwayland-devel = %{evr}
Conflicts: xorg-x11-server-Xwayland-devel
Requires: pkgconfig
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The development package provides the developmental files which are
necessary for developing Wayland compositors using Xwayland.

%prep
%autosetup -S git_am -n %{pkgname}-%{?gitdate:%{commit}}%{!?gitdate:%{version}}

%build
%meson \
	%{?gitdate:-Dxwayland=true -D{xorg,xnest,xvfb,udev}=false} \
        -Ddefault_font_path=%{default_font_path} \
        -Dbuilder_string="Build ID: %{name} %{version}-%{release}" \
        -Dxkb_output_dir=%{_localstatedir}/lib/xkb \
        -Dserverconfigdir=%{_datadir}/xwayland \
        -Dxcsecurity=true \
        -Dglamor=true \
        -Ddri3=true

%meson_build

%install
%meson_install

# Remove unwanted files/dirs
rm $RPM_BUILD_ROOT%{_mandir}/man1/Xserver.1*
rm -Rf $RPM_BUILD_ROOT%{_includedir}/xorg
rm -Rf $RPM_BUILD_ROOT%{_datadir}/aclocal

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%dir %{_datadir}/xwayland
%{_bindir}/Xwayland
%{_mandir}/man1/Xwayland.1*
%{_datadir}/applications/org.freedesktop.Xwayland.desktop
%{_datadir}/xwayland/protocol.txt

%files devel
%{_datadir}/pkgconfig/xwayland.pc

%changelog
* Wed Oct 07 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 26.0.99.903-1
- Initial release of terra-xorg-x11-server-Xwayland