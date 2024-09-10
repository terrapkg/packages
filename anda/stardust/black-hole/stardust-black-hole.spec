Name:           stardust-server
Version:        0.44.1
Release:        1%?dist
Summary:        Usable Linux display server that reinvents human-computer interaction for all kinds of XR.
URL:            https://github.com/StardustXR/server
Source0:        %url/archive/refs/tags/0.44.1.tar.gz
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
%cargo_install

%files
/usr/bin/stardust-server
%license LICENSE
%doc README.md

%changelog
* Tue Sep 10 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR Server
