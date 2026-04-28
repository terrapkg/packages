Name:           vvenc
Version:        1.14.0
Release:        1%?dist
Summary:        VVenC, the Fraunhofer Versatile Video Encoder
License:        BSD-3-Clause
URL:            https://github.com/fraunhoferhhi/%{name}

Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{url}/commit/ebce395254d9d7be7dc00cec7b49c7ed1d9eebec.patch
Patch1:         %{url}/commit/982fcaac22488415899ae6c6ef7977a728a88e94.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

# Define this after the version is defined
%global vvenc_majorminor %(v=%{version}; echo ${v:0:4})

%description
VVenC, the Fraunhofer Versatile Video Encoder, is a fast and efficient software
H.266/VVC encoder implementation with the following main features:

- Easy to use encoder implementation with five predefined quality/speed presets;
- Perceptual optimization to improve subjective video quality, based on the
  XPSNR visual model;
- Extensive frame-level and task-based parallelization with very good scaling;
- Frame-level single-pass and two-pass rate control supporting variable bit-rate
  (VBR) encoding.

%package        libs
Summary:        VVenC, the Fraunhofer Versatile Video Encoder %{name} libraries

%description    libs
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}. This package contains the shared libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
export CXXFLAGS="%{optflags} -Wno-error=maybe-uninitialized -Wno-error=uninitialized"
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH=OFF \
    -DVVENC_INSTALL_FULLFEATURE_APP=ON
%cmake_build

%install
%cmake_install

%files
%{_bindir}/%{name}app
%{_bindir}/%{name}FFapp

%files libs
%license LICENSE.txt
%doc README.md changelog.txt
%{_libdir}/lib%{name}.so.%{vvenc_majorminor}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/%{name}*.cmake
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
%autochangelog
