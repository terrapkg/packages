%bcond_with check

# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$
# Use Mold as the linker
%global build_rustflags %build_rustflags -C link-arg=-fuse-ld=mold

%global crate zed
%global app_id dev.zed.Zed

Name:           zed
Version:        0.145.1
Release:        1%?dist
Summary:        Zed is a high-performance, multiplayer code editor

License:        MIT
URL:            https://zed.dev/
Source0:        https://github.com/zed-industries/zed/archive/refs/tags/v%{version}.tar.gz

Conflicts:      zed
Provides:       zed

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  anda-srpm-macros
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  clang
BuildRequires:  mold
BuildRequires:  alsa-lib-devel
BuildRequires:  fontconfig-devel
BuildRequires:  wayland-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  libzstd-devel
BuildRequires:  perl-FindBin
BuildRequires:  perl-IPC-Cmd
BuildRequires:  perl-File-Compare
BuildRequires:  perl-File-Copy
BuildRequires:  perl-lib
BuildRequires:  vulkan-loader
BuildRequires:  libcurl-devel

%description
Code at the speed of thought - Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

export DO_STARTUP_NOTIFY="true"
export APP_ID="%app_id"
export APP_ICON="%app_id"
export APP_NAME="Zed Editor"
export APP_CLI="zed"
export APP="%{_libexecdir}/zed-editor"
export APP_ARGS="%U"
export ZED_UPDATE_EXPLANATION="Run dnf up to update Zed from Terra."
export ZED_RELEASE_CHANNEL=stable
export BRANDING_LIGHT="#e9aa6a"
export BRANDING_DARK="#1a5fb4"

echo "StartupWMClass=$APP_ID" >> crates/zed/resources/zed.desktop.in
envsubst < "crates/zed/resources/zed.desktop.in" > $APP_ID.desktop # from https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=zed-git#n52

envsubst < "crates/zed/resources/flatpak/zed.metainfo.xml.in" > $APP_ID.metainfo.xml

%build
export ZED_UPDATE_EXPLANATION="Run dnf up to update Zed from Terra."
echo "stable" > crates/zed/RELEASE_CHANNEL

%cargo_build -- --package zed --package cli
script/generate-licenses

%install
install -Dm755 target/rpm/zed %{buildroot}%{_libexecdir}/zed-editor
install -Dm755 target/rpm/cli %{buildroot}%{_bindir}/zed

install -Dm644 %app_id.desktop %{buildroot}%{_datadir}/applications/%app_id.desktop
install -Dm644 crates/zed/resources/app-icon.png %{buildroot}%{_datadir}/pixmaps/%app_id.png

install -Dm644 %app_id.metainfo.xml %{buildroot}%{_metainfodir}/%app_id.metainfo.xml

%if %{with check}
%check
%cargo_test
%endif

%files
%{_libexecdir}/zed-editor
%{_bindir}/zed
%{_datadir}/applications/%app_id.desktop
%{_datadir}/pixmaps/%app_id.png
%{_metainfodir}/%app_id.metainfo.xml
%license assets/licenses.md

%changelog
%autochangelog
