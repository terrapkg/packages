Name:       gstreamer1-plugin-libav
Version:    1.26.0
Release:    1%?dist
Summary:    GStreamer Libav plugin
License:    LGPLv2+
URL:        https://gstreamer.freedesktop.org/modules/gst-libav.html

Source0:    https://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz

BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  libtool
BuildRequires:  meson >= 0.62
BuildRequires:  orc-devel >= 0.4.16
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec) >= 58
BuildRequires:  pkgconfig(libavutil)

Obsoletes:      gstreamer1-libav < 1:1.20.3-4
Provides:       gstreamer1-libav = 1:%{version}-%{release}
Provides:       gstreamer1-libav%{?_isa} = 1:%{version}-%{release}

%ifarch %{ix86} x86_64
BuildRequires:  yasm
%endif

%description
GStreamer plugin containing libav library code.

%prep
%autosetup -p1 -n gst-libav-%{version}

%build
%meson \
  -D package-name="Fedora GStreamer-plugins-ugly package" \
  -D package-origin="https://gstreamer.freedesktop.org" \
  -D doc=disabled
%meson_build

%install
%meson_install
find %{buildroot} -name "*.la" -delete

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/gstreamer-1.0/libgstlibav.so

%changelog
%autochangelog
