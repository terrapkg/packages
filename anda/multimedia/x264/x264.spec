%global commit 0480cb05fa188d37ae87e8f4fd8f1aea3711f7ee
%global commit_date 20250910
%global api_version 165
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%ifarch %{ix86}
%global _pkg_extra_ldflags "-Wl,-z,notext"
%endif

%bcond_with bootstrap

Name:           x264
Version:        0^%{commit_date}git%{shortcommit}
Release:        1%{?dist}
Epoch:          1
Summary:        H264/AVC video streams encoder
License:        GPL-2.0-or-later
URL:            https://www.videolan.org/developers/x264.html

BuildRequires:  gcc
BuildRequires:  nasm >= 2.13
BuildRequires:  pkgconfig(bash-completion)
%if %{without bootstrap}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
%endif
Requires:       bash-completion
Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
%{name} is a free software library and application for encoding video streams into
the H.264/MPEG-4 AVC compression format. This package contains the command line
encoder.

%package libs
Summary:        Library for encoding H264/AVC video streams

%description libs
%{name} is a free software library and application for encoding video streams into
the H.264/MPEG-4 AVC compression format. This package contains the shared
libraries.

%package devel
Summary:        Development files for the x264 library
Requires:       %{name}-libs%{?_isa} = %{evr}
Requires:       pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%pkg_completion -B


%prep
%git_clone https://code.videolan.org/videolan/x264.git %{commit}

%conf
%configure \
    --enable-bashcompletion \
    --enable-debug \
    --enable-pic \
    --enable-shared \
    --bit-depth=all \
    --system-libx264

%build
%make_build

%install
%make_install

%ldconfig_scriptlets libs

%files
%license COPYING
%doc AUTHORS
%{_bindir}/%{name}

%files libs
%license COPYING
%doc AUTHORS
%{_libdir}/lib%{name}.so.*

%files devel
%doc doc/*
%{_includedir}/%{name}.h
%{_includedir}/%{name}_config.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Jun 1 2026 Gilver E. <roachy@fyralabs.com> - 0^20250910git0480cb0-1
- Fix i686 builds
- Update versioning scheme to modern Fedora snapshot guidelines
