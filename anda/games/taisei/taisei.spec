Name:           taisei
Version:        1.4.5
Release:        1%{?dist}
Summary:        A free and open-source Touhou Project fangame
Packager:       Jan200101 <sentrycraft123@gmail.com>

License:        MIT AND CC-BY-4.0 AND CC0-1.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/taisei-project/taisei
Source0:        %{url}/releases/download/v%{version}/taisei-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc gcc-c++
BuildRequires:  pkgconfig(libwebpdecoder)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(cglm)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  python3-zstandard
BuildRequires:  pkgconfig(gamemode)
BuildRequires:  pkgconfig(mimalloc)
BuildRequires:  pkgconfig(libunibreak)
# shader validation
BuildRequires:  glslc
# documentation
BuildRequires:  python3-docutils

Requires: hicolor-icon-theme
Requires: %{name}-data = %{version}

%package data
Summary:        game data for %{name}
BuildArch:      noarch

%description data
required game data for %{name}

%description
Taisei Project is an open source fan-game set in the world of Tōhō Project.
It is a top-down vertical-scrolling curtain fire shooting game (STG),
also known as a "bullet hell" or "danmaku."
STGs are fast-paced games focused around pattern recognition and mastery
through practice.

Taisei Project is highly portable, and is written in C11, using SDL3 with
an OpenGL renderer.
It is officially supported on Windows, Linux, macOS, and through WebGL-enabled
browsers such as Firefox and Chromium-based browsers (Chrome, Edge, etc).
It can also be compiled for a number of other operating systems.

%prep
%autosetup -n taisei-%{version}

# the build defaults force strip on and there is no way to disable it via flags
sed -i "/'strip=true'/d" meson.build

%conf
%meson \
    -Dallocator=mimalloc \
    -Dpackage_data=enabled \
    -Dinstall_relocatable=disabled \
    -Dinstall_freedesktop=enabled \
    -Dshader_transpiler=disabled \
    -Dshader_transpiler_dxbc=disabled \
    -Dvalidate_glsl=enabled \
    -Dinstall_macos_bundle=disabled \
    -Dgamemode=enabled

%build
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING.txt
%{_bindir}/taisei
%{_appsdir}/org.taisei_project.Taisei.desktop
%{_appsdir}/org.taisei_project.Taisei.tsr.desktop
%{_hicolordir}/*/apps/taisei.png
%{_hicolordir}/*/apps/org.taisei_project.Taisei.png
%{_hicolordir}/*/mimetypes/org.taisei_project.Taisei.tsr.png
%{_hicolordir}/*/mimetypes/taisei-replay.png
%{_datadir}/mime/packages/org.taisei_project.Taisei.xml
%{_metainfodir}/org.taisei_project.Taisei.appdata.xml
%{_docdir}/taisei

%files data
%license COPYING.txt
%{_datadir}/taisei

%changelog
* Mon Jun 29 2026 Jan200101 <sentrycraft123@gmail.com>
- Initial package
