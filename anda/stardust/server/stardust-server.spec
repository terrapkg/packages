%global commit 3e31905b5bc9bd78e285099ed94a4b31fdc6810b
%global commit_date 20250402
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

Name:           stardust-xr-server
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Usable Linux display server that reinvents human-computer interaction for all kinds of XR.
URL:            https://github.com/StardustXR/server
Source0:        %url/archive/%commit/server-%commit.tar.gz
License:        GPL-2.0-only

BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros gcc-c++ mold
BuildRequires:  glx-utils fontconfig-devel glibc libxcb-devel wayland-devel
BuildRequires:  openxr-devel libglvnd-devel libglvnd-gles mesa-libgbm-devel
BuildRequires:  libwayland-egl libX11-devel libXfixes-devel
BuildRequires:  mesa-libEGL-devel libxkbcommon-devel
Provides:       stardust-server
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Usable Linux display server that reinvents human-computer interaction for all kinds of XR, from putting 2D/XR apps into various 3D shells for varying uses to SDF-based interaction.

%prep
%autosetup -n server-%commit
%cargo_prep_online

%build
export CXXFLAGS=""
%cargo_build

%install
install -Dm755 target/rpm/stardust-xr-server %buildroot%_bindir/stardust-xr-server


%files
%_bindir/stardust-xr-server
%license LICENSE
%doc README.md

%changelog
* Sat Sep 14 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR Server
