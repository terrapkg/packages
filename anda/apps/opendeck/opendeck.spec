%undefine __brp_mangle_shebangs

%global appid               opendeck
%global name_pretty         OpenDeck
%global appstream_component desktop-application
%global developer           Aman Khanna
# Tauri resolves its resource directory relative to the binary, i.e. /usr/bin/../lib/opendeck.
# This is /usr/lib even on 64-bit, so %%_libdir must not be used here.
%global opendeck_libdir     %{_prefix}/lib/%{name}

Name:           opendeck
Version:        2.14.0
Release:        1%{?dist}
Summary:        Use stream controllers
URL:            https://github.com/nekename/OpenDeck
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        opendeck.desktop

SourceLicense:  GPL-3.0-or-later
License:        GPL-3.0-or-later AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 AND ISC) AND (Apache-2.0 AND MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CDLA-Permissive-2.0 AND ISC AND (ISC AND (Apache-2.0 OR ISC)) AND (ISC AND (Apache-2.0 OR ISC) AND OpenSSL) AND MIT AND (MIT OR Apache-2.0) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)

BuildRequires:  %{tauri_buildrequires}
# The frontend and the bundled starter pack plugin are built with Deno.
BuildRequires:  deno
# reqwest pulls in native-tls -> openssl-sys, which refuses to build against
# OpenSSL 4.0. openssl3-devel provides openssl-devel and conflicts with >= 4.0,
# so it replaces the default. Drop this once openssl-sys supports OpenSSL 4.
BuildRequires:  openssl3-devel
BuildRequires:  anda-srpm-macros
BuildRequires:  terra-appstream-helper
# Detected from src-tauri/Cargo.lock
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  javascriptcoregtk4.1-devel
BuildRequires:  libsoup3-devel
# hidapi (hidraw backend) needs libudev, the Tauri process needs libdbus
BuildRequires:  systemd-devel
BuildRequires:  dbus-devel
# font-loader -> servo-fontconfig-sys, active-win-pos-rs/enigo -> X11 and Wayland
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  expat-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  wayland-devel
# aws-lc-sys and libgit2-sys build native code
BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  perl
BuildRequires:  zlib-devel

# Optional plugin runtimes, see the upstream README
Recommends:     nodejs
Suggests:       wine

Packager:       NichSchlagen <tim-rosenhagen@web.de>

%description
OpenDeck is a desktop application for using stream controller devices like the
Elgato Stream Deck. OpenDeck supports plugins made for the original Stream Deck
SDK, allowing many plugins made for the Elgato software ecosystem to be used.

%prep
%autosetup -n OpenDeck-%{version}
%tauri_prep

%build
%deno_build
%{tauri_cargo_license_summary}
%{tauri_cargo_license} > LICENSE.dependencies

%install
install -Dpm755 src-tauri/target/rpm/%{name}   %{buildroot}%{_bindir}/%{name}
%desktop_file_install                          %{SOURCE1}
install -Dpm644 src-tauri/icons/icon.png       %{buildroot}%{_hicolordir}/512x512/apps/%{name}.png
install -Dpm644 src-tauri/bundle/40-streamdeck.rules \
                                               %{buildroot}%{_udevrulesdir}/40-streamdeck.rules
install -Dpm644 src-tauri/bundle/%{name}.metainfo.xml \
                                               %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

# The starter pack plugin is built by src-tauri/build.rs and would normally be
# copied in by the Tauri bundler, which we do not run.
mkdir -p %{buildroot}%{opendeck_libdir}
cp -a src-tauri/target/plugins %{buildroot}%{opendeck_libdir}/plugins
# `cargo install` bookkeeping, not needed at runtime
find %{buildroot}%{opendeck_libdir} \( -name '.crates.toml' -o -name '.crates2.json' \) -delete

%terra_appstream

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{name}.desktop

%files
%license LICENSE.md
%license LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}
%{_appsdir}/%{name}.desktop
%{_hicolordir}/512x512/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml
%{_udevrulesdir}/40-streamdeck.rules
%dir %{opendeck_libdir}
%{opendeck_libdir}/plugins

%changelog
* Sat Jul 25 2026 NichSchlagen <tim-rosenhagen@web.de>
- Initial package
