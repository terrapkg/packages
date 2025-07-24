# Metadata.
Name:           amdvlk
Version:        2025.Q2.1
Release:        1%?dist
Summary:        AMD Open Source Driver For Vulkan 
License:        MIT
Packager:       libffi <contact@ffi.lol>

# Project URL.
URL:            https://github.com/GPUOpen-Drivers/AMDVLK

# Files.
Patch0:         fix-remove-non-compiling-assignment-operator.patch

# Build dependencies - tooling.
BuildRequires:  gcc-c++ >= 9
BuildRequires:  cmake >= 3.21
BuildRequires:  ninja-build
BuildRequires:  python3
BuildRequires:  repo
BuildRequires:  git

# Build dependencies - python libraries.
BuildRequires:  python3-jinja2
BuildRequires:  python3-ruamel-yaml

# Build dependencies - native libraries.
BuildRequires:  curl
BuildRequires:  openssl-devel
BuildRequires:  glibc-devel
BuildRequires:  libstdc++-devel
# BUILD_SHARED_LIBS=off requires statically linking with libstdc++.
BuildRequires:  libstdc++-static
BuildRequires:  libxcb-devel
BuildRequires:  libX11-devel
BuildRequires:  libxshmfence-devel
BuildRequires:  libXrandr-devel
BuildRequires:  wayland-devel

# Build dependencies - shader compilers.
BuildRequires:  DirectXShaderCompiler
BuildRequires:  glslang
 
%description
Potentially unstable. Use at your own risk!

The AMD Open Source Driver for Vulkan® is an open-source Vulkan driver for
Radeon™ graphics adapters on Linux®. It is built on top of AMD's
Platform Abstraction Library (PAL), a shared component that is designed to
encapsulate certain hardware and OS-specific programming details for many of
AMD's 3D and compute drivers. Leveraging PAL can help provide a consistent
experience across platforms, including support for recently released GPUs
and compatibility with AMD developer tools.
 
%prep
# Set up git.
git config --global user.name dummy
git config --global user.email dummy
# Clone sources.
repo init -u https://github.com/GPUOpen-Drivers/AMDVLK.git -b refs/tags/v-%{version}
repo sync
%patch 0 -p 1 -d drivers/pal/shared/devdriver/third_party/rapidjson/
 
%build
# Shared libs are not built because otherwise it can not link with it's own
# LLVM.
%cmake -G Ninja -S drivers/xgl -DBUILD_WAYLAND_SUPPORT=ON \
    -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
 
%install
%cmake_install --component icd
# _docdir only containts the license, which is made redundant by %license.
rm %{buildroot}/%{_docdir}/ -r
 
%files
# Files are globbed for reasons of potentially being built for 32-bit systems.
%{_sysconfdir}/vulkan/icd.d/amd_icd*.json
%{_sysconfdir}/vulkan/implicit_layer.d/amd_icd*.json
%{_libdir}/amdvlk*.so
%license drivers/xgl/LICENSE.txt
 
%changelog
* Thu Jul 24 2025 libffi <contact@ffi.lol>
- Initial release.
