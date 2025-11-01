%global commit0 1fd04917cff50fac72ae23e45f82ca6fd9130bd8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20230223

Name:       uavs3d
Summary:    AVS3 decoder library
Version:    1.2.0
Release:    4%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
License:    BSD
URL:        https://github.com/uavs3/uavs3d

Source0:    https://github.com/uavs3/uavs3d/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch0:     %{name}-soname.patch
%ifarch %ix86
Patch1:     i686-build-fix.patch
%endif

BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  git

%description
Opensource and cross-platform AVS3 decoder that supports AVS3-P2 baseline
profile.

%package libs
Summary:    AVS3 decoder library

%description libs
Opensource and cross-platform AVS3 decoder that supports AVS3-P2 baseline
profile.

%package devel
Summary:    Header files for uavs3d library
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{commit0} -p1
%ifnarch %ix86
   sed -i '/libdir/ s/"lib"/"%{_lib}"/' source/CMakeLists.txt
%endif

%build
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
    -DCMAKE_SKIP_RPATH:BOOL=YES \
    -DCOMPILE_10BIT:BOOL=ON

%cmake_build

%install
%cmake_install
install -p -m 755 -D %{__cmake_builddir}/uavs3dec %{buildroot}%{_bindir}/uavs3dec

%files
%{_bindir}/uavs3dec

%files libs
%license COPYING
%doc README.md
%{_libdir}/libuavs3d.so.1
%{_libdir}/libuavs3d.so.%{version}

%files devel
%{_includedir}/%{name}.h
%{_libdir}/libuavs3d.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
