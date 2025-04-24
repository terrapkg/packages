%global commit 0558d54cdbc563706d44671ba7d846fc12b96485
%global date 20250324
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global tag %{version}

Name:           egl-x11
Version:        1.0.1%{!?tag:~%{date}git%{shortcommit}}
Release:        6%{?dist}
Summary:        NVIDIA XLib and XCB EGL Platform Library
License:        Apache-2.0
URL:            https://github.com/NVIDIA/egl-x11

%if 0%{?tag:1}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
%endif
# Allow building with an older meson:
Patch0:         egl-x11-meson-0.58.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.2
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 21.2.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.99
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
# Minimum version 1.17.0 for explicit sync support (Fedora 40+):
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)

# Required for directory ownership
Requires:       libglvnd-egl%{?_isa}

%description
This is an EGL platform library for the NVIDIA driver to support XWayland via
xlib (using EGL_KHR_platform_x11) or xcb (using EGL_EXT_platform_xcb).

%prep
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit}
%endif

%build
%meson \
  -D xcb=true \
  -D xlib=enabled
%meson_build

%install
%meson_install

rm -fv %{buildroot}%{_libdir}/*.so

%files
%license LICENSE
%doc README.md
%{_libdir}/libnvidia-egl-xcb.so.1
%{_libdir}/libnvidia-egl-xcb.so.1.0.1
%{_libdir}/libnvidia-egl-xlib.so.1
%{_libdir}/libnvidia-egl-xlib.so.1.0.1
%{_datadir}/egl/egl_external_platform.d/20_nvidia_xcb.json
%{_datadir}/egl/egl_external_platform.d/20_nvidia_xlib.json

%changelog
%autochangelog
