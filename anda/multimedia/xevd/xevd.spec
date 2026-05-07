Name:           xevd
Epoch:          1
Version:        0.5.0
Release:        1%{?dist}
Summary:        eXtra-fast Essential Video Decoder, MPEG-5 EVC (Essential Video Coding)
License:        BSD-3-Clause
URL:            https://github.com/mpeg5/xevd

Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-fix-build-on-non-x86.patch
# https://github.com/mpeg5/xevd/commit/4087f635624cf4ee6ebe3f9ea165ff939b32117f
# But also for src_main:
Patch1:         xevd-link-libm.patch

BuildRequires:  cmake
BuildRequires:  gcc

%description
The eXtra-fast Essential Video Decoder (XEVD) is an opensource and fast MPEG-5
EVC decoder.

MPEG-5 Essential Video Coding (EVC) is a video compression standard of ISO/IEC
Moving Picture Experts Group (MPEG). The main goal of the EVC is to provide a
significantly improved compression capability over existing video coding
standards with timely publication of terms. The EVC defines two profiles,
including "Baseline Profile" and "Main Profile". The "Baseline profile" contains
only technologies that are older than 20 years or otherwise freely available for
use in the standard. In addition, the "Main profile" adds a small number of
additional tools, each of which can be either cleanly disabled or switched to
the corresponding baseline tool on an individual basis.

%package        libs
Summary:        MPEG-5 EVC encoder %{name} libraries

%description    libs
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}. This package contains the shared libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
echo "v%{version}" > version.txt

%build
%cmake -DSET_PROF=MAIN
%cmake_build

%install
%cmake_install

# Static library
rm -fr %{buildroot}%{_libdir}/%{name}

%files
%{_bindir}/%{name}_app

%files libs
%license COPYING
%doc README.md
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.5

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
