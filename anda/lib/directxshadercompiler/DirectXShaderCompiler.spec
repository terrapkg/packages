# Commit hashes.
%global SPIRV_Headers_HASH aa6cef192b8e693916eb713e7a9ccadf06062ceb
%global SPIRV_Tools_HASH a62abcb402009b9ca5975e6167c09f237f630e0e
%global DirectX_Headers_HASH 980971e835876dc0cde415e8f9bc646e64667bf7

# Build parameters.
%bcond external_libraries 1

# Metadata.
Name:           DirectXShaderCompiler
Version:        1.8.2502
Release:        3%?dist
Summary:        A Direct X Shader compiler.
License:        MIT
Packager:       libffi <contact@ffi.lol>

# Source and Project URLs.
URL:            https://github.com/microsoft/DirectXShaderCompiler
Source0:        https://github.com/microsoft/DirectXShaderCompiler/archive/refs/tags/v%{version}.tar.gz

# Libraries - building with libraries with a different version / git reference
# is not supported by upstream.
Source1:        https://github.com/KhronosGroup/SPIRV-Headers/archive/%{SPIRV_Headers_HASH}.tar.gz
Source2:        https://github.com/KhronosGroup/SPIRV-Tools/archive/%{SPIRV_Tools_HASH}.tar.gz
Source3:        https://github.com/microsoft/DirectX-Headers/archive/%{DirectX_Headers_HASH}.tar.gz

# Build dependencies - tooling.
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.17.2
BuildRequires:  python3
BuildRequires:  git

# External libraries - BuildRequires.
%if %{!with external_libraries}
    BuildRequires: DirectX-Headers-devel
    BuildRequires: spirv-tools-devel
    BuildRequires: spirv-headers-devel
%endif

# Sub-packages.

%package devel
Summary: Development files for %{name}.
Requires: %{name}-libs
Requires: %{name}-static

%package libs
Summary: Runtime shared libraries for %{name}.

%package static
Summary: Static libraries for %{name}.

%package cmake-utils
Summary: CMake files for %{name}. Theoretically useless.

%package tools
Summary: Binaries of %{name}, such as the compiler/optimizer.
Requires: %{name}-libs

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

%description tools
This package contains runtime binaries of %{name} that could be used in
scripts.

Provided files include:
* dxc, a command-line tool that can compile HLSL programs for SM6.0 or later.
* dxv, a command-line tool for validating the DXIL bytecode/compiled binaries.
* and some other ones!

%description cmake-utils
This package contains CMake scripts of %{name}.
Theoretically internal usage only, likely no usage at all.

%description static
Static libraries / binaries to link with applications at compile-time
for %{name}.

# Prepare.
 
%prep
%autosetup
# Are we building with external libraries?
%if %{with external_libraries}
    # If so, extract and prepare them.
    %setup -D -C -a 1 -q
    %setup -D -C -a 2 -q
    %setup -D -C -a 3 -q
    rm -rf external/DirectX-Headers
    rm -rf external/SPIRV-Headers
    rm -rf external/SPIRV-Tools
    mv DirectX-Headers-%{DirectX_Headers_HASH} external/DirectX-Headers
    mv SPIRV-Headers-%{SPIRV_Headers_HASH} external/SPIRV-Headers
    mv SPIRV-Tools-%{SPIRV_Tools_HASH} external/SPIRV-Tools
%else
    # Warn :P.
    %{warn: Building without external libraries is unsupported by upstream!}
    %{warn: You are likely to run into compilation failures this way.}
    # Otherwise, nuke external libraries as a whole.
    rm -rf external/
%endif
 
# Build.
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
 
# Install.

%install
%cmake_install
mkdir %{buildroot}%{_bindir} -p
# Link binaries.
for BINARY in dxa dxc dxl dxopt dxr dxv; do
ln -s ../%{lib}/%{name}/bin/$BINARY %{buildroot}%{_bindir}/$BINARY;
done

# Test.
%check
%ctest
 
# Files.
%files tools
%{_libdir}/%{name}/bin/
%{_bindir}/dxa
%{_bindir}/dxc
%{_bindir}/dxl
%{_bindir}/dxopt
%{_bindir}/dxr
%{_bindir}/dxv

%files libs
%{_libdir}/%{name}/lib/libdxcompiler.so
%{_libdir}/%{name}/lib/libdxil.so

%files static
%{_libdir}/%{name}/lib/libHLSLTestLib.a
%{_libdir}/%{name}/lib/libLLVMAnalysis.a
%{_libdir}/%{name}/lib/libLLVMAsmParser.a
%{_libdir}/%{name}/lib/libLLVMBitReader.a
%{_libdir}/%{name}/lib/libLLVMBitWriter.a
%{_libdir}/%{name}/lib/libLLVMCore.a
%{_libdir}/%{name}/lib/libLLVMDXIL.a
%{_libdir}/%{name}/lib/libLLVMDxcBindingTable.a
%{_libdir}/%{name}/lib/libLLVMDxcSupport.a
%{_libdir}/%{name}/lib/libLLVMDxilCompression.a
%{_libdir}/%{name}/lib/libLLVMDxilContainer.a
%{_libdir}/%{name}/lib/libLLVMDxilDia.a
%{_libdir}/%{name}/lib/libLLVMDxilHash.a
%{_libdir}/%{name}/lib/libLLVMDxilPIXPasses.a
%{_libdir}/%{name}/lib/libLLVMDxilPdbInfo.a
%{_libdir}/%{name}/lib/libLLVMDxilRootSignature.a
%{_libdir}/%{name}/lib/libLLVMDxilValidation.a
%{_libdir}/%{name}/lib/libLLVMDxrFallback.a
%{_libdir}/%{name}/lib/libLLVMHLSL.a
%{_libdir}/%{name}/lib/libLLVMIRReader.a
%{_libdir}/%{name}/lib/libLLVMInstCombine.a
%{_libdir}/%{name}/lib/libLLVMLinker.a
%{_libdir}/%{name}/lib/libLLVMMSSupport.a
%{_libdir}/%{name}/lib/libLLVMOption.a
%{_libdir}/%{name}/lib/libLLVMPassPrinters.a
%{_libdir}/%{name}/lib/libLLVMPasses.a
%{_libdir}/%{name}/lib/libLLVMProfileData.a
%{_libdir}/%{name}/lib/libLLVMScalarOpts.a
%{_libdir}/%{name}/lib/libLLVMSupport.a
%{_libdir}/%{name}/lib/libLLVMTableGen.a
%{_libdir}/%{name}/lib/libLLVMTarget.a
%{_libdir}/%{name}/lib/libLLVMTransformUtils.a
%{_libdir}/%{name}/lib/libLLVMVectorize.a
%{_libdir}/%{name}/lib/libLLVMipa.a
%{_libdir}/%{name}/lib/libLLVMipo.a
%{_libdir}/%{name}/lib/libclang.a
%{_libdir}/%{name}/lib/libclangAST.a
%{_libdir}/%{name}/lib/libclangASTMatchers.a
%{_libdir}/%{name}/lib/libclangAnalysis.a
%{_libdir}/%{name}/lib/libclangBasic.a
%{_libdir}/%{name}/lib/libclangCodeGen.a
%{_libdir}/%{name}/lib/libclangDriver.a
%{_libdir}/%{name}/lib/libclangEdit.a
%{_libdir}/%{name}/lib/libclangFormat.a
%{_libdir}/%{name}/lib/libclangFrontend.a
%{_libdir}/%{name}/lib/libclangFrontendTool.a
%{_libdir}/%{name}/lib/libclangIndex.a
%{_libdir}/%{name}/lib/libclangLex.a
%{_libdir}/%{name}/lib/libclangParse.a
%{_libdir}/%{name}/lib/libclangRewrite.a
%{_libdir}/%{name}/lib/libclangRewriteFrontend.a
%{_libdir}/%{name}/lib/libclangSPIRV.a
%{_libdir}/%{name}/lib/libclangSema.a
%{_libdir}/%{name}/lib/libclangTooling.a
%{_libdir}/%{name}/lib/libclangToolingCore.a
%{_libdir}/%{name}/lib/libdxclib.a
%{_libdir}/%{name}/lib/libdxcvalidator.a

%files devel
%{_libdir}/%{name}/include/

%files cmake-utils
%{_libdir}/%{name}/share/llvm/cmake

# Changelog.
%changelog
* Sun May 5 2025 libffi <contact@ffi.lol> - 1.8.2502-3
- Provide unsupported build conditional for building with(out)
external libraries.

* Sun May 4 2025 libffi <contact@ffi.lol> - 1.8.2502-2
- Refactor.
- Use subpackages.

* Wed Apr 30 2025 libffi <contact@ffi.lol> - 1.8.2502-1
- Initial build.
