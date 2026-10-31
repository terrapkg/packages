%global appid org.waywallen.waywallen

Name:           waywallen
Version:        0.5.0
Release:        1%{?dist}
License:        MIT
Summary:        Wallpaper Manager for Linux
URL:            https://github.com/waywallen/waywallen
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  anda-srpm-macros
BuildRequires:  rust
BuildRequires:  lito >= 0.8.1
BuildRequires:  cargo
BuildRequires:  clang >= 22
BuildRequires:  cmake >= 3.28
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(vulkan) >= 1.1
BuildRequires:  llvm
BuildRequires:  lld
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  protobuf-compiler
BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(Qt6WebSockets) >= 6.10
BuildRequires:  cmake(Qt6Protobuf) >= 6.10
BuildRequires:  cmake(Qt6LinguistTools) >= 6.10
BuildRequires:  cmake(Qt6ShaderTools) >= 6.10
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  sqlite-devel
BuildRequires:  glslang
BuildRequires:  git-lfs

Requires:       waywallen-display
Requires:       waywallen-libs
Requires:       vulkan-loader >= 1.1
Requires:       qt6-qtgrpc >= 6.10

Recommends:     open-wallpaper-engine

Packager:       L1oly <lid2011@ukr.net>

%description
Waywallen is a dynamic wallpaper solution for Linux desktops.
It started life as a Wallpaper Engine plugin for KDE.

%package devel
%pkg_devel_files
%exclude %{_libdir}/libwaywallen-bridge.so

%package libs
Summary:        Libs of Wallpaper Manager for Linux (waywallen-libs)
%description libs
%{summary}.
# had problems with pkg_libs_files

%prep
%autosetup

%conf
%if 0%{?fedora} >= 45
export CXXFLAGS="${CXXFLAGS//-Wp,-D_FORTIFY_SOURCE=3/}"
%endif
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
export ZSTD_SYS_USE_PKG_CONFIG=1
export RUSTFLAGS="%{build_rustflags} -C link-arg=-fuse-ld=lld"

%build
lito build --profile release

%install
lito install --prefix %{buildroot}%{_prefix} --profile release
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/lib/* %{buildroot}%{_libdir}/
rmdir %{buildroot}%{_prefix}/lib

%terra_appstream

%files
%license LICENSE
%doc README.md
%{_bindir}/waywallen
%{_bindir}/waywallen-i18n
%{_bindir}/waywallen-image-renderer
%{_bindir}/waywallen-ui
%{_bindir}/waywallen-video-renderer
%{_appsdir}/%{appid}.desktop
%{_scalableiconsdir}/%{appid}.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%dir %{_datadir}/waywallen
%{_datadir}/waywallen/

%files libs
%{_libdir}/libwaywallen-bridge.so

%changelog
* Thu Oct 29 2026 L1oly <lid2011@ukr.net>
- Initial commit
