Name:           xeve
Epoch:          1
Version:        0.5.1
Release:        2%{?dist}
Summary:        eXtra-fast Essential Video Encoder, MPEG-5 EVC (Essential Video Coding)
License:        BSD-3-Clause
URL:            https://github.com/mpeg5/xeve

Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         xeve-fix-build-on-non-x86.patch
# https://github.com/mpeg5/xeve/commit/bc45faa2e8d22bf33b0d15c025662f2a8de61fbc
# But also for src_main:
Patch1:         xeve-link-libm.patch
Patch2:         xeve-fix-build-i386.patch

BuildRequires:  cmake
BuildRequires:  gcc
%ifarch aarch64
BuildRequires:  sse2neon-devel
%endif

%description
The eXtra-fast Essential Video Encoder (XEVE) is an opensource and fast MPEG-5
EVC encoder.

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
rm src_base/neon/sse2neon.h

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
