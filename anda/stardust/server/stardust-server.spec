%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-server
Version:        0.45.1
Release:        1%?dist
Summary:        Usable Linux display server that reinvents human-computer interaction for all kinds of XR.
URL:            https://github.com/StardustXR/server
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        GPLv2

BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros mold g++
BuildRequires:  glx-utils fontconfig-devel glibc libxcb-devel wayland-devel
BuildRequires:  openxr-devel libglvnd-devel libglvnd-gles mesa-libgbm-devel
BuildRequires:  libwayland-egl libX11-devel libXfixes-devel lld clang
BuildRequires:  mesa-libEGL-devel libxkbcommon-devel

Requires:       libxkbcommon libstdc++ openxr-libs libX11 libXfixes
Requires:       libglvnd-egl mesa-libgbm fontconfig libgcc glibc jsoncpp libxcb libglvnd
Requires:       libwayland-server libdrm expat libxcb freetype libxml2 libXau libXau
Requires:       libffi zlib-ng-compat bzip2-libs libpng harfbuzz libbrotli xz-libs
Requires:       glib2 graphite2 libbrotli pcre2

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Usable Linux display server that reinvents human-computer interaction for all kinds of XR, from putting 2D/XR apps into various 3D shells for varying uses to SDF-based interaction.

%prep
%autosetup -n server-%version
%cargo_prep_online

%build

%install
%define __cargo_common_opts %{?_smp_mflags} -Z avoid-dev-deps --locked
%cargo_install

%files
%_bindir/stardust-xr-server
%license LICENSE
%doc README.md

%changelog
* Sat Sep 14 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR Server
