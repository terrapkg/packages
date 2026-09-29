%global appid org.openboardview.openboardview
%global appstream_component desktop-application
%global name_pretty OpenBoardView
%global developer OpenBoardView
%global org org.openboardview
%global appstream_description Software for viewing PCB, laptop, and motherboard layouts.

Name:           openboardview
Version:        10.0.0
Release:        1%{?dist}
Summary:        Viewer for PCB layouts
# OpenBoardView, Dear ImGui, and glad are MIT. glad also ships Khronos
# specifications under Apache-2.0. mpc is BSD-3-Clause. utf8.h is Unlicense.
# stb is MIT OR Unlicense.
License:        MIT AND Apache-2.0 AND BSD-3-Clause AND Unlicense AND (MIT OR Unlicense)
URL:            https://github.com/OpenBoardView/OpenBoardView
# System SQLite is detected as SQLite3_FOUND, but the build checks SQLITE3_FOUND
# and then fails while aliasing the bundled static library.
Patch0:         sqlite-found-variable.patch

Packager:       Utkarsh Verma <hi@utkarshverma.com>

BuildRequires:  anda-srpm-macros
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  python3
# glad generates its OpenGL loader with a bundled Python module that imports jinja2.
BuildRequires:  python3-jinja2
BuildRequires:  SDL2-devel
BuildRequires:  sqlite-devel
BuildRequires:  terra-appstream-helper
BuildRequires:  zlib-ng-devel

Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       libglvnd-glx
Recommends:     evince

# Header-only or generated sources pinned as git submodules.
Provides:       bundled(glad) = 73db193f853e2ee079bf3ca8a64aa2eaf6459043
Provides:       bundled(imgui) = 8936b58fe26e8c3da834b8f60b06511d537b4c63
Provides:       bundled(mpc) = 65f20a1a0b3249a475efa8ecb7b5ecd2c1c071c4
Provides:       bundled(stb) = f54acd4e13430c5122cab4ca657705c84aa61b08
Provides:       bundled(utf8.h) = 3e9e3ec15c7bf129664ab2a113eb03b54ee0b584

%description
OpenBoardView is a viewer for PCB, laptop, and motherboard layout files.
It reads FZ, BRD, BRD2, BDV, and BV boardview formats, and can annotate
parts, nets, pins, and locations.

%prep
%git_clone %{url} %{version}
%autopatch -p1

%conf
# Fedora's %%cmake defaults to shared libraries. glad follows that and
# produces libglad_gl.so, which is not installed. Keep bundled libraries static.
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF

%build
%cmake_build

%install
%cmake_install
# Upstream metadata uses a legacy component id and a screenshot URL that
# does not point at an image. Generate Terra metadata from the installed files.
rm -f %{buildroot}%{_metainfodir}/openboardview.appdata.xml
%terra_appstream

# Several bundled components ship a file named LICENSE. Install them under
# distinct names so they do not overwrite each other.
install -Dm0644 LICENSE %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE
install -Dm0644 src/glad/LICENSE %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE.glad
install -Dm0644 src/imgui/LICENSE.txt %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE.imgui
install -Dm0644 src/stb/LICENSE %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE.stb
install -Dm0644 src/utf8/LICENSE %{buildroot}%{_defaultlicensedir}/%{name}/LICENSE.utf8

%check
%desktop_file_validate %{buildroot}%{_appsdir}/openboardview.desktop

%files
%license %{_defaultlicensedir}/%{name}/LICENSE
%license %{_defaultlicensedir}/%{name}/LICENSE.glad
%license %{_defaultlicensedir}/%{name}/LICENSE.imgui
%license %{_defaultlicensedir}/%{name}/LICENSE.stb
%license %{_defaultlicensedir}/%{name}/LICENSE.utf8
%doc README.md
%{_bindir}/openboardview
%{_appsdir}/openboardview.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_datadir}/mime/packages/openboardview.xml
%{_scalableiconsdir}/openboardview.svg

%changelog
* Tue Sep 29 2026 Utkarsh Verma <hi@utkarshverma.com> - 10.0.0-1
- Initial package
