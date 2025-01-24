%global commit0 b41cf117452e2d73d827f02d3e30aa20f1c721ac
%global date 20220903
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       davs2
Version:    1.6
Release:    5%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Summary:    An open-source decoder of AVS2-P2/IEEE1857.4 video coding standard
URL:        https://github.com/pkuvcl/%{name}
License:    GPLv2

%if "%{?shortcommit0}"
Source0:    https://github.com/pkuvcl/%{name}/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%else
Source0:    https://github.com/pkuvcl/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildRequires:  gcc-c++
%ifarch x86_64
BuildRequires:  nasm >= 2.13
%endif

%description
davs2 is an open-source decoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the command line decoder.

%package libs
Summary:    AVS2-P2/IEEE1857.4 decoder library

%description libs
davs2 is an open-source decoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the shared library.

%package devel
Summary:    AVS2-P2/IEEE1857.4 decoder library development files
Requires:   %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
davs2 is an open-source decoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the shared library development files.

%prep
# Use flat condition or it fails on EPEL 7
%if "%{?shortcommit0}"
%autosetup -n %{name}-%{commit0}
%else
%autosetup
%endif

%build
cd build/linux
%configure \
    --bit-depth='8' \
    --chroma-format='all' \
%ifarch aarch64 %ix86
    --disable-asm \
%endif
    --disable-static \
    --enable-pic \
    --enable-shared

# Remove hardcoded CFLAGS on generated file containing variables
sed -i \
    -e 's|CFLAGS=.*%{optflags}|CFLAGS=%{optflags}|g' \
    config.mak

%make_build

%install
cd build/linux
%make_install

%ldconfig_scriptlets libs

%files
%{_bindir}/%{name}

%files libs
%license COPYING
%{_libdir}/lib%{name}.so.16

%files devel
%doc README.md
%{_includedir}/%{name}.h
%{_includedir}/%{name}_config.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
