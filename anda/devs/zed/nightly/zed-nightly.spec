%global commit 4668aeb7284780cca830ba1173c4d3eb8bd11e2b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20260301
%global ver 0.227.0

%bcond_with check
%bcond_with debug_no_build
%bcond nightly 1

%if 0%{?with_debug_no_build}
%global debug_package %{nil}
%endif

# Exclude input files from mangling
%global __brp_mangle_shebangs_exclude_from ^/usr/src/.*$

%global crate zed
%global appid dev.zed.Zed-Nightly
%global appstream_component desktop-application

%global rustflags_debuginfo 0

Name:           zed-nightly
Version:        %ver^%commit_date.%shortcommit
Release:        1%?dist
Summary:        Zed is a high-performance, multiplayer code editor
SourceLicense:  AGPL-3.0-only AND Apache-2.0 AND GPL-3.0-or-later
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 AND ISC) AND AGPL.3.0-only AND AGPL-3.0-or-later AND (Apache-2.0 OR BSL-1.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR MIT OR Apache-2.0) AND BSD-2-Clause AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND (CC0-1.0 OR Apache-2.0) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CC0-1.0 AND GPL-3.0-or-later AND (ISC AND (Apache-2.0 OR ISC) AND OpenSSL) AND (ISC AND (Apache-2.0 OR ISC)) AND ISC AND (MIT AND (MIT OR Apache-2.0)) AND (MIT AND BSD-3-Clause) AND (MIT OR Apache-2.0 OR CC0-1.0) AND (MIT OR Apache-2.0 OR NCSA) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Zlib
URL:            https://zed.dev/
Source0:        https://github.com/zed-industries/zed/archive/%{commit}.tar.gz
Source1:        override.xml

Conflicts:      zed
Conflicts:      zed-preview

%ifarch x86_64
# BUG: fedora rustc missing this dep
BuildRequires:  libedit(x86-64)
%endif
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  anda-srpm-macros
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-envsubst
BuildRequires:  clang
BuildRequires:  mold
BuildRequires:  cmake
BuildRequires:  alsa-lib-devel
BuildRequires:  fontconfig-devel
BuildRequires:  wayland-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  openssl-devel
%if 0%{?fedora}
BuildRequires:  openssl-devel-engine
%endif
BuildRequires:  libzstd-devel
BuildRequires:  perl-FindBin
BuildRequires:  perl-IPC-Cmd
BuildRequires:  perl-File-Compare
BuildRequires:  perl-File-Copy
BuildRequires:  perl-lib
%if %{with nightly}
BuildRequires:  rustup
%endif
BuildRequires:  vulkan-loader
Requires: (%name-cli-compat-zfs if zfs else %name-cli)
Suggests: %name-cli

%description
Code at the speed of thought - Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.

%package cli
Summary: Provides the /usr/bin/zed binary
Conflicts: zfs
Supplements: (%name unless zfs)

%description cli
This package provides the /usr/bin/zed binary. If you use zfs, install %name-cli-compat-zfs instead.

%package cli-compat-zfs
Summary: Rename zed to zeditor to prevent collision with zfs
Provides: %name-cli
Conflicts: %name-cli
Obsoletes: %{name}-rename-zeditor <= 0.217.3
Supplements: (%name and zfs)
RemovePathPostFixes: .zeditor

%description cli-compat-zfs
This package provides the %_bindir/zeditor binary instead of %_bindir/zed. This avoids conflicts with the zfs package.
The normal package is %name-cli.

%prep
%autosetup -n %{crate}-%{commit} -p1
%if %{without debug_no_build}
%if %{with nightly}
%rustup_nightly
%endif
%cargo_prep_online
%endif

export DO_STARTUP_NOTIFY="true"
export APP_ID="%appid"
export APP_ICON="%appid"
export APP_NAME="Zed Nightly"
export APP_CLI="zed"
export APP="%{_libexecdir}/zed-editor"
export APP_ARGS="%U"
export ZED_UPDATE_EXPLANATION="Run dnf up to update Zed Nightly from Terra."
export ZED_RELEASE_CHANNEL=nightly
export BRANDING_LIGHT="#e9aa6a"
export BRANDING_DARK="#1a5fb4"

envsubst < "crates/zed/resources/zed.desktop.in" > %{appid}.desktop # from https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=zed-git#n52
sed -i "s|@release_info@||g" "crates/zed/resources/flatpak/zed.metainfo.xml.in"

envsubst < "crates/zed/resources/flatpak/zed.metainfo.xml.in" > %{appid}.metainfo.xml

%build
%if %{without debug_no_build}
export ZED_UPDATE_EXPLANATION="Run dnf up to update Zed Nightly from Terra."
echo "nightly" > crates/zed/RELEASE_CHANNEL

%cargo_build -- --package zed --package cli
ALLOW_MISSING_LICENSES=1 script/generate-licenses
%endif

%install
%if %{without debug_no_build}
install -Dm755 target/rpm/zed %{buildroot}%{_libexecdir}/zed-editor
install -Dm755 target/rpm/cli %{buildroot}%{_bindir}/zeditor
install -Dm755 target/rpm/cli %{buildroot}%{_bindir}/zed

%__cargo clean
%endif

install -Dm644 %appid.desktop %{buildroot}%{_datadir}/applications/%appid.desktop
sed 's/Exec=zed/Exec=zeditor/' %appid.desktop > %appid.desktop.zeditor
install -Dm644 %appid.desktop.zeditor -t %buildroot%_datadir/applications/
install -Dm644 crates/zed/resources/app-icon-nightly.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%appid.png

install -Dm644 %appid.metainfo.xml %{buildroot}%{_metainfodir}/%appid.metainfo.xml

# The license generation script doesn't generate licenses for ALL compiled dependencies, just direct deps of Zed, and it does not "group" licenses
# Zed also needs a special approach to fetch the dep licenses
%if %{without debug_no_build}
%{__cargo} tree                                                             \
    -Z avoid-dev-deps                                                       \
    --workspace                                                             \
    --edges no-build,no-dev,no-proc-macro                                   \
    --target all                                                            \
    %{__cargo_parse_opts %{-n} %{-a} %{-f:-f%{-f*}}}                        \
    --prefix none                                                           \
    --format "{l}: {p}"                                                     \
    | sed -e "s: ($(pwd)[^)]*)::g" -e "s: / :/:g" -e "/\/.*:/{s/\// OR /}"  \
    | sed -e '/.*(\*).*/d' -e '/^: pet/ s/./MIT&/'                          \
    | sort -u                                                               \
> LICENSE.dependencies
%endif
mv assets/icons/LICENSES LICENSE.icons
mv assets/themes/LICENSES LICENSE.themes
mv assets/fonts/ibm-plex-sans/license.txt LICENSE.fonts
%terra_appstream -o %{SOURCE1}

%if %{with check}
%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%appid.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%appid.desktop

%if %{without debug_no_build}
%cargo_test
%endif
%endif

%files
%doc CODE_OF_CONDUCT.md
%doc README.md
%license LICENSE-AGPL
%license LICENSE-APACHE
%license LICENSE-GPL
%if %{without debug_no_build}
%license LICENSE.dependencies
%endif
%license LICENSE.fonts
%license LICENSE.icons
%license LICENSE.themes
%if %{without debug_no_build}
%license assets/licenses.md
%endif
%if %{without debug_no_build}
%{_libexecdir}/zed-editor
%endif

%files cli
%if %{without debug_no_build}
%_bindir/zed
%endif
%{_datadir}/icons/hicolor/512x512/apps/%appid.png
%{_datadir}/applications/%appid.desktop
%{_metainfodir}/%appid.metainfo.xml

%files cli-compat-zfs
%if %{without debug_no_build}
%_bindir/zeditor
%endif
%{_datadir}/icons/hicolor/512x512/apps/%appid.png
%_datadir/applications/%appid.desktop.zeditor
%{_metainfodir}/%appid.metainfo.xml

%changelog
%autochangelog
