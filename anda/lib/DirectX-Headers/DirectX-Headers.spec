%global mingw_build_ucrt64 1
%{?mingw_package_header}

# Disable debug as this package only provides a static archive (and no shared object).
# debuginfo will be made available via consumer (mesa) instead.
%global debug_package %{nil}
%global __strip /bin/true

# There is no LTO in mesa, so drop that in stub archives also
# see mesa comment:
# We've gotten a report that enabling LTO for mesa breaks some games. See
# https://bugzilla.redhat.com/show_bug.cgi?id=1862771 for details.
# Disable LTO for now
%define _lto_cflags %{nil}

Name:           DirectX-Headers
Version:        1.618.1
Release:        1%{?dist}
Summary:        Official Direct3D 12 headers

License:        MIT
URL:            https://github.com/microsoft/DirectX-Headers
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
# Test assumes the build is under WSL, which is unlikely
%{?_with_test:BuildRequires: gtest-devel}

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++

BuildRequires: ucrt64-filesystem
BuildRequires: ucrt64-gcc-c++


%description
Official Direct3D 12 headers

%package        devel
Summary:        Development files for %{name}
# This only provides -static files, so only
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n mingw32-directx-headers
Summary:        Official DirectX headers available under an open source license

%description -n mingw32-directx-headers
Official DirectX headers available under an open source license

%package -n mingw64-directx-headers
Summary:        Official DirectX headers available under an open source license

%description -n mingw64-directx-headers
Official DirectX headers available under an open source license

%package -n ucrt64-directx-headers
Summary:        Official DirectX headers available under an open source license

%description -n ucrt64-directx-headers
Official DirectX headers available under an open source license


%prep
%autosetup -p1
# Change EOL encoding
for i in LICENSE README.md ; do
  sed -i -e 's/\r$//' ${i}
  touch -r SECURITY.md ${i}
done


%build
%meson \
 %{?!_with_test:-Dbuild-test=false}

%meson_build

%mingw_meson
%mingw_ninja


%install
%meson_install

%mingw_ninja_install

%check
%{?_with_test:
%meson_test
}


%files devel
%license LICENSE
%doc README.md SECURITY.md
%{_includedir}/composition
%{_includedir}/directx
%{_includedir}/dxguids
%{_includedir}/wsl
%{_libdir}/libDirectX-Guids.a
%{_libdir}/libd3dx12-format-properties.a
%{_libdir}/pkgconfig/DirectX-Headers.pc

%files -n mingw32-directx-headers
%doc README.md SECURITY.md
%license LICENSE
%{mingw32_libdir}/pkgconfig/DirectX-Headers.pc
%{mingw32_libdir}/libDirectX-Guids.a
%{mingw32_libdir}/libd3dx12-format-properties.a
%{mingw32_includedir}/composition
%{mingw32_includedir}/wsl/
%{mingw32_includedir}/dxguids/
%{mingw32_includedir}/directx/

%files -n mingw64-directx-headers
%doc README.md SECURITY.md
%license LICENSE
%{mingw64_libdir}/pkgconfig/DirectX-Headers.pc
%{mingw64_libdir}/libDirectX-Guids.a
%{mingw64_libdir}/libd3dx12-format-properties.a
%{mingw64_includedir}/composition
%{mingw64_includedir}/wsl/
%{mingw64_includedir}/dxguids/
%{mingw64_includedir}/directx/

%files -n ucrt64-directx-headers
%doc README.md SECURITY.md
%license LICENSE
%{ucrt64_libdir}/pkgconfig/DirectX-Headers.pc
%{ucrt64_libdir}/libDirectX-Guids.a
%{ucrt64_libdir}/libd3dx12-format-properties.a
%{ucrt64_includedir}/composition
%{ucrt64_includedir}/wsl/
%{ucrt64_includedir}/dxguids/
%{ucrt64_includedir}/directx/


%changelog
%autochangelog
