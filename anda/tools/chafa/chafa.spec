Name:          terra-chafa
Version:        1.18.1
Release:        1%?dist
Summary:        Terminal graphics for the 21st century
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
URL:            https://hpjansson.org/chafa/
Source0:        https://github.com/hpjansson/chafa/archive/refs/tags/%version.tar.gz

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libavif-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  libpng-devel
BuildRequires:  anda-srpm-macros
Requires:       %{name}-libs%{?_isa} = %{evr}
Provides:       chafa = %{evr}

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Chafa is a command-line utility that converts all kinds of images, including
animated image formats like GIFs, into ANSI/Unicode character output that can
be displayed in a terminal.

It is highly configurable, with support for alpha transparency and multiple
color modes and color spaces, combining a range of Unicode characters for
optimal output.

%package libs
%pkg_libs_files

%package devel
Requires:       %{name}-libs%{?_isa} = %{evr}
%pkg_devel_files
%{_libdir}/chafa/include/chafaconfig.h

%package static
%pkg_static_files

%prep
%autosetup -n chafa-%{version}

%build
autoreconf -ivf
%configure --disable-rpath
%make_build

%install
%make_install
%if 0%{?rhel}
find %{buildroot} -name "*.la" -delete
%endif

%files
%doc AUTHORS COPYING.LESSER README* NEWS
%license COPYING.LESSER COPYING
%{_bindir}/chafa
%{_mandir}/man1/chafa.1*

%changelog
* Fri Feb 20 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
