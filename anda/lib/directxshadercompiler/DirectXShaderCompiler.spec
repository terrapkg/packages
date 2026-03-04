# Disable in-source build.
%undefine __cmake_in_source_build

# Metadata.
Name:           DirectXShaderCompiler
Version:        1.9.2602
Release:        1%?dist
Summary:        A Direct X Shader compiler.
License:        MIT
Packager:       libffi <contact@ffi.lol>

# Project URL.
URL:            https://github.com/microsoft/DirectXShaderCompiler

# Build dependencies - tooling.
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.17.2
BuildRequires:  python3
BuildRequires:  git

Provides:       dxc = %{version}-%{release}
Requires:       %{name}-libs

# Sub-packages.

%package devel
Summary: Development files for %{name}.
Requires: %{name}-libs
Requires: %{name}-static

%package libs
Summary: Runtime shared libraries for %{name}.

%package static
Summary: Static libraries for %{name}.

# Descriptions.

%description
The DirectX Shader Compiler project includes a compiler and related tools used
to compile High-Level Shader Language (HLSL) programs into DirectX Intermediate
Language (DXIL) representation. Applications that make use of DirectX for
graphics, games, and computation can use it to generate shader programs.

%description devel
This package contains library and header files needed to develop new native
programs that use %{name}.

%description libs
This package contains runtime shared libraries needed to link with native
programs that use %{name}.

Provided files include:
* libdxcompiler.so, a .so providing a componentized compiler, assembler,
disassembler, and validator.
* and some other ones!

%description static
Static libraries / binaries to link with applications at compile-time
for %{name}.

# Prepare.
 
%prep
%git_clone %{url} v%{version}
 
# Build.
# Attribution: https://github.com/gentoo/guru/blob/master/dev-util/DirectXShaderCompiler/DirectXShaderCompiler-1.8.2407.ebuild
# Attribution: https://github.com/negativo17/DirectXShaderCompiler/blob/master/DirectXShaderCompiler.spec
%build
%cmake \
    -C ./cmake/caches/PredefinedParams.cmake \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -DSPIRV_BUILD_TESTS=OFF \
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_BUILD_TYPE=Fedora

%cmake_build
 
# Install.
# Attribution: https://github.com/negativo17/DirectXShaderCompiler/blob/master/DirectXShaderCompiler.spec
%install
mkdir %{buildroot}%{_bindir} -p
# Binaries.
install -m755 %{_vpath_builddir}/bin/dx{a,c,l,opt,r,v} \
    %{buildroot}%{_bindir}/

# Static libraries.
mkdir -p %{buildroot}%{_libdir}
for STATIC in libdxclib libdxcvalidator; do
install -m644 %{_vpath_builddir}/lib/$STATIC.a \
    %{buildroot}%{_libdir}/; done

# Shared libraries.
install -m755 %{_vpath_builddir}/lib/*.so \
    %{buildroot}%{_libdir}/

# Headers.
mkdir -p %{buildroot}%{_includedir}/dxc
install -m644 include/dxc/*.h \
    %{buildroot}%{_includedir}/dxc/

# Test.
%check
%ctest
 
# Files.
%files
%license LICENSE.TXT
%doc CONTRIBUTING.md README.md SECURITY.md ThirdPartyNotices.txt
%{_bindir}/dxa
%{_bindir}/dxc
%{_bindir}/dxl
%{_bindir}/dxopt
%{_bindir}/dxr
%{_bindir}/dxv

%files libs
%{_libdir}/libdxcompiler.so
%{_libdir}/libdxil.so
%{_libdir}/libdxildll.so

%files static
%{_libdir}/*.a

%files devel
%{_includedir}/dxc/*.h

# Changelog.
%changelog
* Sun Jul 20 2025 libffi <contact@ffi.lol> - 1.8.2505.1-5
- Removed support for building with external libraries.
- Internal changes to the build process.

* Fri Jul 18 2025 libffi <contact@ffi.lol> - 1.8.2505.1-4
- Remove the `tools` and `cmake-utils` subpackages.
- Make the package provide the `dxc` package.
- Add license and some docs.
- Internal package changes.
- Bump upstream.

* Mon May 5 2025 libffi <contact@ffi.lol> - 1.8.2502-3
- Provide unsupported build conditional for building with(out)
  external libraries.

* Sun May 4 2025 libffi <contact@ffi.lol> - 1.8.2502-2
- Refactor.
- Use subpackages.

* Wed Apr 30 2025 libffi <contact@ffi.lol> - 1.8.2502-1
- Initial build.
