Name:           cglm
Version:        0.9.6
Release:        1%{?dist}
Summary:        Highly Optimized Graphics Math (glm) for C
Packager:       Jan200101 <sentrycraft123@gmail.com>

License:        MIT
URL:            https://github.com/recp/cglm
Source0:        %{url}/archive/v%{version}.tar.gz#/cglm-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: cmake

%description
Highly optimized 2D|3D math library, also known as OpenGL Mathematics
(glm) for `C`.
cglm provides lot of utils to help math operations to be fast and
quick to write. It is community friendly, feel free to bring any
issues, bugs you faced.

%package devel
Summary:        Development package for %{name}
Requires:       %{name} = %{version}

%description devel
Development package for %{name}.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libcglm.so.%{version}

%files devel
%{_libdir}/libcglm.so
%{_libdir}/libcglm.so.0
%{_includedir}/cglm/
%{_libdir}/cmake/cglm/
%{_libdir}/pkgconfig/cglm.pc

%changelog
* Mon Jun 29 2026 Jan200101 <sentrycraft123@gmail.com>
- Initial package
