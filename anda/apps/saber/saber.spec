%global appid   com.adilhanney.saber

Name:           saber
Version:        1.37.2
Release:        2%{?dist}
Summary:        The cross-platform notes app built for handwriting
License:        GPL-3.0-only
URL:            https://github.com/saber-notes/saber

Packager:       Adil Hanney <adilhanney@disroot.org>

BuildRequires:  anda-srpm-macros
BuildRequires:  terra-appstream-helper
BuildRequires:  desktop-file-utils
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  egl-utils
BuildRequires:  gtk3-devel
BuildRequires:  java-latest-openjdk-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libcurl-devel
BuildRequires:  libsecret-devel
BuildRequires:  ninja-build
BuildRequires:  patchelf
BuildRequires:  rustup
BuildRequires:  webkit2gtk4.1-devel

Requires:       jsoncpp
Requires:       zenity

%ifarch x86_64
%global bundle_path build/linux/x64/release/bundle
%elifarch aarch64
%global bundle_path build/linux/arm64/release/bundle
%endif

# Don't expose private libraries like "libapp.so"
%global __provides_exclude_from ^/%{_datadir}/%{name}/lib/.*$
# These must be manually listed: https://docs.fedoraproject.org/en-US/packaging-guidelines/AutoProvidesAndRequiresFiltering/#_private_libraries
%global __requires_exclude ^(libapp|libdartjni|libflutter_linux_gtk|libpdfium|libpdfrx_pdfium_gate|libsuper_native_extensions_native|lib.*_plugin)\\.so.*$

%description
%{summary}.

%prep
# Flutter version is pinned as a submodule
%git_clone %{url} v%{version}
# Restore Flutter tags
git -C submodules/flutter fetch --depth=1 origin '+refs/tags/*:refs/tags/*'

# Some dependencies require rustup (not just rust)
rustup-init -y

./patches/pre/remove_permission_handler.sh
./patches/pre/remove_proprietary_dependencies.sh

./submodules/flutter/bin/flutter config --no-cli-animations
./submodules/flutter/bin/flutter pub get

%build
# Remove gcc-specific specs as they trip up [-Werror,-Wunused-command-line-argument] with clang.
export CFLAGS="${CFLAGS//-specs=\/usr\/lib\/rpm\/redhat\/redhat-hardened-cc1/}"
export CFLAGS="${CFLAGS//-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1/}"
export CXXFLAGS="${CXXFLAGS//-specs=\/usr\/lib\/rpm\/redhat\/redhat-hardened-cc1/}"
export CXXFLAGS="${CXXFLAGS//-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1/}"

./submodules/flutter/bin/flutter build linux --no-pub --verbose

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a %{bundle_path}/* %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
ln -sr %{buildroot}/%{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
%desktop_file_install flatpak/%{appid}.desktop
install -Dm644 flatpak/%{appid}.metainfo.xml -t %{buildroot}%{_metainfodir}
install -Dm644 assets/icon/icon_linux.svg %{buildroot}%{_scalableiconsdir}/%{appid}.svg
%terra_appstream

# Fix the rpaths of bundled libraries. Similar to `anda/apps/localsend-bin/localsend-bin.spec`
for so in %{buildroot}/%{_datadir}/%{name}/lib/*.so; do
    patchelf --set-rpath '$ORIGIN' "$so"
done

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%license LICENSE.md
%{_bindir}/%{name}
/%{_datadir}/%{name}
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg

%changelog
* Fri Nov 20 2026 Adil Hanney <adilhanney@disroot.org>
- Initial package
