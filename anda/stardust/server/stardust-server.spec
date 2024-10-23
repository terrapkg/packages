%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$
#global build_rustflags -Copt-level=3 -Cdebuginfo=2 -Ccodegen-units=1 -Cstrip=none -Cforce-frame-pointers=yes --cap-lints=warn -Cdebug-assertions=true
%define __strip /bin/true
%global debug_package %{nil}

Name:           stardust-server
Version:        0.45.1
Release:        1%?dist
Summary:        Usable Linux display server that reinvents human-computer interaction for all kinds of XR.
URL:            https://github.com/StardustXR/server
Source0:        %url/archive/refs/tags/%version.tar.gz
License:        GPL-2.0-only

BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros gcc-c++
BuildRequires:  glx-utils fontconfig-devel glibc libxcb-devel wayland-devel
BuildRequires:  openxr-devel libglvnd-devel libglvnd-gles mesa-libgbm-devel
BuildRequires:  libwayland-egl libX11-devel libXfixes-devel
BuildRequires:  mesa-libEGL-devel libxkbcommon-devel

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Usable Linux display server that reinvents human-computer interaction for all kinds of XR, from putting 2D/XR apps into various 3D shells for varying uses to SDF-based interaction.

%prep
%autosetup -n server-%version

%build
LDFLAGS="" RUSTFLAGS="" CXXFLAGS="" CFLAGS="" cargo build --release --locked

%install
install -Dm755 target/release/stardust-xr-server %buildroot%_bindir/stardust-xr-server


%files
%_bindir/stardust-xr-server
%license LICENSE
%doc README.md

%changelog
* Sat Sep 14 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR Server
