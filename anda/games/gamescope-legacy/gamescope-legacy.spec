%if 0%{?fedora} >= 41
%global libliftoff_minver 0.5.0
%else
%global libliftoff_minver 0.4.1
%endif
%global reshade_commit 4245743a8c41abbe3dc73980c1810fe449359bf1
%global reshade_shortcommit %(c=%{reshade_commit}; echo ${c:0:7})
%global _default_patch_fuzz 2


# =============================================================================
# IMPORTANT: This package should *not* have an update script, at least not one that
# tracks upstream Gamescope from Valve. This package is intended to be a legacy
# build for Polaris and older GPUs from AMD, and should not be updated to the
# latest version.
# 
# This package however, should be obsoleted once https://github.com/ValveSoftware/gamescope/issues/1218
# is finally resolved, and Gamescope's Wayland backend has a fallback for GPUs without Vulkan DRM modifiers.
# =============================================================================


Name:           gamescope-legacy
Version:        3.14.2
Release:        1%{?dist}
Summary:        Legacy builds of gamescope, a micro-compositor for video games on Wayland
Packager:       Cappy Ishihara <cappy@fyralabs.com>
License:        BSD
URL:            https://github.com/ValveSoftware/gamescope

# Create stb.pc to satisfy dependency('stb')
Source1:        stb.pc
Source2:        https://github.com/Joshua-Ashton/reshade/archive/%{reshade_commit}/reshade-%{reshade_shortcommit}.tar.gz

Patch0:         0001-cstdint.patch

# https://hhd.dev/
Patch1:         v2-0001-always-send-ctrl-1-2-to-steam-s-wayland-session.patch

# ChimeraOS
Patch2:         legacy-720p.patch

# System wlroots
Patch4:         wlroots-pc.patch
BuildRequires:  git-core
BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  google-benchmark-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXcursor-devel
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  (pkgconfig(wlroots) >= 0.17.0 with pkgconfig(wlroots) < 0.18)
BuildRequires:  (pkgconfig(libliftoff) >= %{libliftoff_minver} with pkgconfig(libliftoff) < 0.6)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  spirv-headers-devel
# Enforce the the minimum EVR to contain fixes for all of:
# CVE-2021-28021 CVE-2021-42715 CVE-2021-42716 CVE-2022-28041 CVE-2023-43898
# CVE-2023-45661 CVE-2023-45662 CVE-2023-45663 CVE-2023-45664 CVE-2023-45666
# CVE-2023-45667
BuildRequires:  stb_image-devel >= 2.28^20231011gitbeebb24-12
# Header-only library: -static is for tracking per guidelines
BuildRequires:  stb_image-static
BuildRequires:  stb_image_resize-devel
BuildRequires:  stb_image_resize-static
BuildRequires:  stb_image_write-devel
BuildRequires:  stb_image_write-static
BuildRequires:  vkroots-devel
BuildRequires:  /usr/bin/glslangValidator

# libliftoff hasn't bumped soname, but API/ABI has changed for 0.2.0 release
Requires:       libliftoff%{?_isa} >= %{libliftoff_minver}
Requires:       xorg-x11-server-Xwayland

Requires:       terra-gamescope-libs
Requires:       terra-gamescope-libs(x86-32)

Recommends:     mesa-dri-drivers
Recommends:     mesa-vulkan-drivers

%description
%{name} is the micro-compositor optimized for running video games on Wayland. This is a legacy build primarily intended for use by Polaris GPUs.

%prep
git clone --depth 1 --branch %{version} %{url}.git gamescope
cd gamescope
git submodule update --init --recursive
# Install stub pkgconfig file
mkdir -p pkgconfig
cp %{SOURCE1} pkgconfig/stb.pc

# Replace spirv-headers include with the system directory
sed -i 's^../thirdparty/SPIRV-Headers/include/spirv/^/usr/include/spirv/^' src/meson.build

tar -xvf %{SOURCE2}

# Push in reshade from sources instead of submodule
rm -rf src/reshade && mv reshade-%{reshade_commit} src/reshade

%autopatch -p1

%build
cd gamescope
export PKG_CONFIG_PATH=pkgconfig
%meson -Dpipewire=enabled -Denable_gamescope_wsi_layer=false -Denable_openvr_support=false -Dforce_fallback_for=[]
%meson_build

%install
cd gamescope
%meson_install
# Rename to not conflict with the base package
mv %{buildroot}%{_bindir}/gamescope %{buildroot}%{_bindir}/gamescope-legacy

%files
%license LICENSE
%doc README.md
%{_bindir}/gamescope-legacy

%changelog
%autochangelog

