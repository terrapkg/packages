%define debug_package %{nil}
# no matter what i did build makes no debug info

Name:           open-wallpaper-engine
Version:        0.3.2
Release:        1%{?dist}
License:        GPL-2.0-only
Summary:        Open source wallpaper engine implement mostly for linux (waywallen plugin)
URL:            https://github.com/waywallen/open-wallpaper-engine
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake >= 4.0
BuildRequires:  lito >= 0.3.0
BuildRequires:  clang >= 22
BuildRequires:  ninja-build
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  cef-devel
BuildRequires:  quickjs-ng-devel
BuildRequires:  waywallen-devel
BuildRequires:  waywallen-libs
BuildRequires:  glslang

Requires:       waywallen
Requires:       cef

Packager:       L1oly <lid2011@ukr.net>

%description
%{summary}.

%prep
%autosetup
#lito fetch --all-features
mkdir -p .lito
cat > .lito/config.toml <<'EOF'
[tools.cmake.overrides.Eigen3]
source = "installed"

[tools.cmake.overrides.glslang]
source = "installed"

[tools.cmake.overrides.qjs]
source = "installed"

[tools.cmake.overrides.CEF]
source = "installed"
EOF

%build
lito build --profile release --package owe-sceneviewer --package owe-webviewer --package owe-waywallen-scene-renderer --package owe-waywallen-web-renderer

%install
lito install --prefix %{buildroot}%{_prefix} --profile release
lito install --prefix %{buildroot}%{_prefix} --profile release --package owe-waywallen-plugin
rm -rf %{buildroot}%{_prefix}/lib
rm -rf %{buildroot}%{_bindir}
install -Dm 755 build/release/bin/owe-sceneviewer/SceneViewer                             %{buildroot}%{_libdir}/open-wallpaper-engine/SceneViewer
install -Dm 755 build/release/bin/owe-webviewer/WebViewer                                 %{buildroot}%{_libdir}/open-wallpaper-engine/WebViewer
install -Dm 755 build/release/bin/owe-waywallen-scene-renderer/waywallen-wescene-renderer %{buildroot}%{_bindir}/waywallen-wescene-renderer
install -Dm 755 build/release/bin/owe-waywallen-web-renderer/waywallen-weweb-renderer     %{buildroot}%{_bindir}/waywallen-weweb-renderer

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_libdir}/*
%{_datadir}/waywallen/plugins/org.waywallen.open-wallpaper-engine

%changelog
* Thu Oct 29 2026 L1oly <lid2011@ukr.net>
- Initial commit
