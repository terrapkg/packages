Name:             libde265
Summary:          Open H.265 video codec implementation
Version:          1.0.15
Release:          1%{?dist}
License:          LGPLv3+
URL:              https://www.libde265.org/
Source0:          https://github.com/strukturag/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    gcc
BuildRequires:    libtool
BuildRequires:    pkgconfig(libswscale)
BuildRequires:    pkgconfig(Qt5Core)
BuildRequires:    pkgconfig(Qt5Gui)
BuildRequires:    pkgconfig(sdl)

%description
%{name} is an open source implementation of the H.265 video codec.

%package devel
Summary:    Open H.265 video codec implementation - development files
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
%{name} is an open source implementation of the H.265 video codec.

The development headers for compiling programs that use %{name} are provided
by this package.

%package tools
License:    GPLv3+
Summary:    Open H.265 video codec implementation - examples
Obsoletes:  %{name}-samples < %{version}-%{release}
Provides:   %{name}-samples%{?_isa} = %{version}-%{release}

%description tools
%{name} is an open source implementation of the H.265 video codec.

Various sample and test applications using %{name} are provided by this package.

%prep
%autosetup

%build
autoreconf -vif
%configure --disable-silent-rules --disable-static --enable-encoder
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%{?ldconfig_scriptlets}

%files
%license COPYING
%doc AUTHORS
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.1.8

%files devel
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%doc README.md
%{_bindir}/acceleration_speed
%{_bindir}/bjoentegaard
%{_bindir}/block-rate-estim
%{_bindir}/dec265
%{_bindir}/enc265
%{_bindir}/gen-enc-table
%{_bindir}/rd-curves
%{_bindir}/sherlock265
%{_bindir}/tests
%{_bindir}/yuv-distortion

%changelog
%autochangelog
