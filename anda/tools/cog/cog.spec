Name:           cog
Version:        0.18.5
Release:        2%{?dist}
Summary:        Small single "window" launcher for the WebKit WPE port

License:        MIT
URL:            https://github.com/Igalia/cog
Source0:        https://wpewebkit.org/releases/cog-%{version}.tar.xz
# libwpe dlopen()s the backend, use the runtime soname instead of the -devel symlink
Patch0:         cog-wpebackend-fdo-soname.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(manette-0.2)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wpe-1.0)
BuildRequires:  pkgconfig(wpe-webkit-2.0)
BuildRequires:  pkgconfig(wpebackend-fdo-1.0)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(gbm)

Requires:       %{name}-libs%{?_isa} = %{evr}

Packager: Cypress Reed <cypress@fyralabs.com>

%description
Cog is a small single "window" launcher for the WebKit WPE port. It is
small, provides no user interface, and is suitable to be used as a Web
application container. The "window" may be fullscreen depending on the
WPE backend being used.

%package       libs
Summary:       Core library and platform plug-ins for %{name}

Requires:      wpebackend-fdo%{?_isa}

%description   libs
The %{name}-libs package contains the libcogcore library and the platform
plug-ins used by %{name} and applications embedding it.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}-libs%{?_isa} = %{evr}

%description   devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.

%prep
%autosetup -n cog-%{version} -p1

%conf
%meson \
    -Dplatforms=drm,headless,wayland,gtk4,x11 \
    -Dwpe_api=2.0 \
    -Dlibmanette=enabled

%build
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/cog
%{_bindir}/cogctl
%{_mandir}/man1/cog.1*
%{_mandir}/man1/cogctl.1*

%files libs
%license COPYING
%{_libdir}/libcogcore.so.9
%{_libdir}/libcogcore.so.9.*
%dir %{_libdir}/cog
%dir %{_libdir}/cog/modules
%{_libdir}/cog/modules/libcogplatform-drm.so
%{_libdir}/cog/modules/libcogplatform-gtk4.so
%{_libdir}/cog/modules/libcogplatform-headless.so
%{_libdir}/cog/modules/libcogplatform-wl.so
%{_libdir}/cog/modules/libcogplatform-x11.so

%files devel
%{_includedir}/cog
%{_libdir}/libcogcore.so
%{_pkgconfigdir}/cogcore.pc

%changelog
* Fri Oct 30 2026 Cypress Reed <cypress@fyralabs.com>
- Load wpebackend-fdo by its runtime soname and require it

* Sat Oct 17 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
