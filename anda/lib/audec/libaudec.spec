%global _desc %{expand:
libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and
libsamplerate for reading and resampling audio files.
}

Name:           libaudec
Version:        0.3.4
Release:        1%?dist
Summary:        libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files
License:        AGPL-3.0-or-later
URL:            https://git.sr.ht/~alextee/libaudec
Source0:        %url/archive/v%version.tar.gz
Patch0:         libaudec.patch
BuildRequires:  cmake meson ninja-build gcc
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  ffmpeg-free-devel

%description %_desc

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel %_desc
This package contains the development files for the %name package.

%prep
%setup -q -n libaudec-v%{version}
%ifarch %{ix86} %{arm}
%autopatch -p1
rm -r tests
%endif

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING COPYING.GPL3
%_bindir/audec

%files devel
%_includedir/audec/audec.h
%_libdir/libaudec.a
%_libdir/pkgconfig/audec.pc
%_libdir/libaudec.so
