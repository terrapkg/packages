Name:           stardust-server
Version:        0.44.1
Release:        1%?dist
Summary:        Usable Linux display server that reinvents human-computer interaction for all kinds of XR.
URL:            https://github.com/StardustXR/server
Source0:        %url/archive/refs/tags/0.44.1.tar.gz
License:        GPLv2
BuildRequires:  cargo cmake anda-srpm-macros rust-srpm-macros
Requires:       libxkbcommon libstdc++ openxr-libs libX11 libXfixes libglvnd-egl mesa-libgbm fontconfig libgcc glibc jsoncpp libxcb libglvnd libwayland-server libdrm expat libxcb freetype libxml2 libXau libXau libffi zlib-ng-compat bzip2-libs libpng harfbuzz libbrotli xz-libs glib2 graphite2 libbrotli pcre2
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
/usr/bin/stardust-xr-server
%license LICENSE
%doc README.md

%changelog
* Tue Sep 10 2024 Owen-sz <owen@fyralabs.com>
- Package StardustXR Server
