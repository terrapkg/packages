%global commit eae1e8b9d12468059bdd7dee893508e470fa83d8
%global commit_date 20190422
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       xavs2
Version:    1.4
Release:    1%{?shortcommit:.%{commit_date}git%{shortcommit}}%{?dist}
Summary:    An open-source encoder of AVS2-P2/IEEE1857.4 video coding standard
URL:        https://github.com/pkuvcl/%{name}
License:    GPLv2

%if "%{?shortcommit}"
Source0:    https://github.com/pkuvcl/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
%else
Source0:    https://github.com/pkuvcl/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildRequires:  gcc
%ifarch x86_64
BuildRequires:  nasm >= 2.13
%endif

%description
xavs2 is an open-source encoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the command line encoder.

%package libs
Summary:    AVS2-P2/IEEE1857.4 encoder library

%description libs
davs2 is an open-source encoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the shared library.

%package devel
Summary:    AVS2-P2/IEEE1857.4 encoder library development files
Requires:   %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
davs2 is an open-source encoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the shared library development files.

%prep
%if "%{?shortcommit}"
%autosetup -n %{name}-%{commit}
%else
%autosetup 
%endif

%build
cd build/linux
export CFLAGS="%{optflags} -Wno-incompatible-pointer-types"
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

find %{buildroot} -name "*a" -delete

%ldconfig_scriptlets libs

%files
%{_bindir}/%{name}

%files libs
%license COPYING
%{_libdir}/lib%{name}.so.13

%files devel
%doc README.md
%{_includedir}/%{name}.h
%{_includedir}/%{name}_config.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Mar 21 2024 Simone Caronni <negativo17@gmail.com> - 1.3-5.20190422giteae1e8b
- Fix build on Fedora 40.

* Sat May 23 2020 Simone Caronni <negativo17@gmail.com> - 1.3-4.20190422giteae1e8b
- Disable ASM for aarch64.

* Sun Mar 15 2020 Simone Caronni <negativo17@gmail.com> - 1.3-3.20190422giteae1e8b
- Update to latest snapshot.

* Sun Jun 09 2019 Simone Caronni <negativo17@gmail.com> - 1.3-2.20181229gitf45c340
- Update to latest snapshot to fix various bugs.

* Sat Jun 08 2019 Simone Caronni <negativo17@gmail.com> - 1.3-1
- First build.
