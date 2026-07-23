Name:           vvdec
Version:        3.1.0
Release:        1%?dist
Summary:        VVdeC, the Fraunhofer Versatile Video Decoder
License:        BSD-3-Clause
URL:            https://github.com/fraunhoferhhi/%{name}

Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
VVdeC, the Fraunhofer Versatile Video Decoder, is a fast software H.266/VVC
decoder implementation supporting all features of the VVC Main10 profile.

%package        libs
Summary:        VVdeC, the Fraunhofer Versatile Video Encoder %{name} libraries

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
%cmake \
%ifarch %{ix86}
	-DVVDEC_ENABLE_X86_SIMD=OFF \
%endif
	-DVVDEC_INSTALL_VVDECAPP=ON
%cmake_build

%install
%cmake_install

%files
%{_bindir}/%{name}app

%files libs
%license LICENSE.txt
%doc README.md
%{_libdir}/lib%{name}.so.3
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/%{name}*.cmake
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
%autochangelog
