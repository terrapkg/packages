%global libver  1.0.4

# replace - with ~
%global libver_format %(v=%{libver}; sed -e 's/-/~/' <<< $v)

Name:           libappimage


Version:        %{libver_format}
Release:        1%{?dist}
Summary:        Implements functionality for dealing with AppImage files

License:        MIT
URL:            https://github.com/AppImageCommunity/libappimage
Source0:        %{url}/archive/refs/tags/v%{libver}.tar.gz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  cairo-devel
BuildRequires:  xz-devel
BuildRequires:  libarchive-devel
BuildRequires:  fuse-devel
BuildRequires:  squashfuse-devel
BuildRequires:  git-core
BuildRequires:  librsvg2-devel
BuildRequires:  boost-devel


%description
Implements functionality for dealing with AppImage files. It is written in C++ and is using Boost.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{libver}
echo "#include <cstdint>" > a.h
cat src/libappimage/utils/hashlib.h >> a.h
mv a.h src/libappimage/utils/hashlib.h


%build
%cmake \
 -DBUILD_TESTING:bool=False \
 -DUSE_SYSTEM_SQUASHFUSE=ON \
 -DUSE_SYSTEM_XZ=ON \
 -DUSE_SYSTEM_LIBARCHIVE=ON \
 -DUSE_SYSTEM_BOOST=ON
%cmake_build


%install
%cmake_install
#find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%{?ldconfig_scriptlets}


%files
%license LICENSE
%doc docs
%{_libdir}/*.so.*
%{_libdir}/*.a

%files devel
%doc docs
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/%{name}/*.cmake




%changelog
* Tue Oct 25 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial package.
