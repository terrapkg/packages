# Metadata.
Name:           DirectXShaderCompiler
Version:        1.8.2502
Release:        1%?dist
Summary:        A Direct X Shader compiler.
License:        MIT
Packager:       libffi <contact@ffi.lol>

# Source and Project URLs.
URL:            https://github.com/microsoft/DirectXShaderCompiler
Source0:        https://github.com/microsoft/DirectXShaderCompiler/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/KhronosGroup/SPIRV-Headers/archive/aa6cef192b8e693916eb713e7a9ccadf06062ceb.tar.gz
Source2:        https://github.com/KhronosGroup/SPIRV-Tools/archive/a62abcb402009b9ca5975e6167c09f237f630e0e.tar.gz
Source3:        https://github.com/microsoft/DirectX-Headers/archive/980971e835876dc0cde415e8f9bc646e64667bf7.tar.gz

# Build dependencies - tooling.
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.17.2
BuildRequires:  python3
BuildRequires:  git

%description
The DirectX Shader Compiler project includes a compiler and related tools used
to compile High-Level Shader Language (HLSL) programs into DirectX Intermediate
Language (DXIL) representation. Applications that make use of DirectX for
graphics, games, and computation can use it to generate shader programs.
 
%prep
%autosetup
%setup -D -C -a 1
%setup -D -C -a 2
%setup -D -C -a 3
rm -rf external/DirectX-Headers
rm -rf external/SPIRV-Headers
rm -rf external/SPIRV-Tools
mv DirectX-Headers-980971e835876dc0cde415e8f9bc646e64667bf7 external/DirectX-Headers
mv SPIRV-Headers-aa6cef192b8e693916eb713e7a9ccadf06062ceb external/SPIRV-Headers
mv SPIRV-Tools-a62abcb402009b9ca5975e6167c09f237f630e0e external/SPIRV-Tools
 
# Attribution: https://github.com/gentoo/guru/blob/master/dev-util/DirectXShaderCompiler/DirectXShaderCompiler-1.8.2407.ebuild
%build
%cmake \
    -C ./cmake/caches/PredefinedParams.cmake \
    -DSPIRV_WERROR=0 \
    -DLLVM_BUILD_DOCS=0 \
    -DLLVM_BUILD_TOOLS=0 \
    -DSPIRV_BUILD_TESTS=0 \
    -DLLVM_ENABLE_WERROR=0 \
    -DBUILD_SHARED_LIBS=OFF \
    -DLLVM_VERSION_SUFFIX=dxc \
    -DSPIRV_WARN_EVERYTHING=0 \
    -DCMAKE_INSTALL_PREFIX="%{_libdir}/%{name}" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
 
%install
%cmake_install
mkdir %{buildroot}%{_bindir} -p
for BINARY in dxa dxc dxl dxopt dxr dxv; do
ln -s %{_libdir}/%{name}/bin/$BINARY %{buildroot}%{_bindir}/$BINARY;
done

%check
%ctest
 
%files
%{_libdir}/%{name}
%{_bindir}/dxa
%{_bindir}/dxc
%{_bindir}/dxl
%{_bindir}/dxopt
%{_bindir}/dxr
%{_bindir}/dxv
 
%changelog
* Wed Apr 30 2025 libffi <contact@ffi.lol>
- Initial build.
