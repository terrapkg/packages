%global         majorminor 1.0

Name:           gstreamer1-plugins-ugly
Version:        1.26.0
Release:        1%{?dist}
Epoch:          1
Summary:        GStreamer streaming media framework "ugly" plugins
License:        LGPL-2.0-or-later and LGPL-2.0-only
URL:            http://gstreamer.freedesktop.org/

Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.xz

BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}

BuildRequires:  a52dec-devel >= 0.7.3
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel >= 0.17
BuildRequires:  libdvdread-devel
BuildRequires:  libid3tag-devel >= 0.15.0
BuildRequires:  meson >= 0.48.0
BuildRequires:  orc-devel >= 0.4.16
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(libcdio) >= 0.76
BuildRequires:  pkgconfig(libmpeg2) >= 0.5.1
BuildRequires:  pkgconfig(mad) >= 0.15
BuildRequires:  pkgconfig(x264) >= 0.120

Obsoletes:      %{name}-free < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free%{?_isa} = %{?epoch}:%{version}-%{release}

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This module contains a set of plugins that have good quality and correct
functionality, but distributing them might pose problems. The license on either
the plugins or the supporting libraries might not be how we'd like. The code
might be widely known to present patent problems. Distributors should check if
they want/can ship these plugins.

%prep
%autosetup -n gst-plugins-ugly-%{version}

%build
%meson \
  -D package-name="Fedora GStreamer-plugins-ugly package" \
  -D package-origin="https://negativo17.org" \
  -D a52dec=enabled \
  -D asfdemux=enabled \
  -D cdio=enabled \
  -D doc=disabled \
  -D dvdlpcmdec=enabled \
  -D dvdread=enabled \
  -D dvdsub=enabled \
  -D gpl=enabled \
  -D mpeg2dec=enabled \
  -D realmedia=enabled \
  -D sidplay=disabled \
  -D x264=enabled \
  -D x264_libraries=libx264_main10.so

%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -delete
%find_lang gst-plugins-ugly-%{majorminor}

%files -f gst-plugins-ugly-%{majorminor}.lang
%license COPYING
%doc AUTHORS NEWS README.md REQUIREMENTS
%{_datadir}/gstreamer-%{majorminor}/presets/*.prs
%{_libdir}/gstreamer-%{majorminor}/libgstasf.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdlpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdsub.so
%{_libdir}/gstreamer-%{majorminor}/libgsta52dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdio.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdread.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstrealmedia.so
%{_libdir}/gstreamer-%{majorminor}/libgstx264.so

%changelog
%autochangelog
