%global appid org.opengamingcollective.cardwire
%bcond rust_nightly 1
%global cardwire_toolchain nightly-2026-08-04
%define _cargo_home %{rpmbuilddir}%{?buildsubdir:/%{buildsubdir}}/.cargo
%global _rustup_home %{rpmbuilddir}/.rustup
%define __cargo /usr/bin/env CARGO_HOME=%{_cargo_home} RUSTUP_HOME=%{_rustup_home} RUSTFLAGS='%{terra_rustflags}' %{_cargo_home}/cardwire-cargo
%define __rustc %{_cargo_home}/cardwire-rustc
%define __rustdoc %{_cargo_home}/cardwire-rustdoc

Name:           cardwire
Version:        0.12.1
Release:        1%{?dist}
Summary:        A GPU Manager for linux that uses eBPF LSM hooks to block GPUs
URL:            https://opengamingcollective.github.io/cardwire/
Source0:        https://github.com/OpenGamingCollective/cardwire/archive/refs/tags/v%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/OpenGamingCollective/cardwire/v%{version}/assets/%{appid}.metainfo.xml
# Cargo.lock for the pinned Rust nightly's rust-src component.
Source2:        https://raw.githubusercontent.com/rust-lang/rust/504869653/library/Cargo.lock
SourceLicense:  GPL-3.0-or-later
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND Unlicense AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND GPL-3.0 AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND BSL-1.0 AND ISC AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Provides:       switcheroo-control
Conflicts:      switcheroo-control
BuildRequires:  cargo-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd-devel
BuildRequires:  libbpf-devel
BuildRequires:  clang-devel
BuildRequires:  pkgconfig(xcb)
BuildRequires:  rustup

Requires: hwdata
Requires: upower

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%package        gui
Summary:        GUI for cardwire
Requires:       %{name} = %{evr}

%description    gui
%{summary}.

%prep
%autosetup
# Set up a private Rustup environment without the distro macro, whose
# _cargo_home guard conflicts with Fedora's caching macros.
%{__rm} -rf %{_cargo_home} %{_rustup_home}
%{__mkdir} -p %{_cargo_home}
/usr/bin/env CARGO_HOME=%{_cargo_home} RUSTUP_HOME=%{_rustup_home} \
    RUSTUP_INIT_SKIP_PATH_CHECK=yes rustup-init --default-toolchain none -y -q --no-modify-path
. %{_cargo_home}/env
# cardwire v0.12.0 pins this toolchain because the prebuilt bpf-linker is
# LLVM-version-sensitive.
rustup toolchain install %{cardwire_toolchain} --profile minimal --component rust-src
rustup default %{cardwire_toolchain}
cardwire_cargo=$(rustup which cargo --toolchain %{cardwire_toolchain})
cardwire_rustc=$(rustup which rustc --toolchain %{cardwire_toolchain})
cardwire_rustdoc=$(rustup which rustdoc --toolchain %{cardwire_toolchain})
cat > %{_cargo_home}/cardwire-cargo <<EOF
#!/bin/sh
exec "$cardwire_cargo" "\$@"
EOF
cat > %{_cargo_home}/cardwire-rustc <<EOF
#!/bin/sh
exec "$cardwire_rustc" "\$@"
EOF
cat > %{_cargo_home}/cardwire-rustdoc <<EOF
#!/bin/sh
exec "$cardwire_rustdoc" "\$@"
EOF
cat > %{_cargo_home}/rustup <<EOF
#!/bin/sh
if test "\$1" = run && test "\$2" = %{cardwire_toolchain}; then
    command=\$3
    shift 3
    exec %{_cargo_home}/cardwire-\$command "\$@"
fi
exec %{_cargo_home}/bin/rustup "\$@"
EOF
chmod 0755 %{_cargo_home}/cardwire-cargo %{_cargo_home}/cardwire-rustc %{_cargo_home}/cardwire-rustdoc %{_cargo_home}/rustup
# This pinned rust-src component may omit the lockfile required by -Z build-std.
rust_src=%{_rustup_home}/toolchains/%{cardwire_toolchain}-x86_64-unknown-linux-gnu/lib/rustlib/src/rust
install -Dpm0644 %{SOURCE2} "$rust_src/library/Cargo.lock"
test -f "$rust_src/library/Cargo.lock"
%cargo_prep_online

%build
# The Rustup environment from %prep is not retained by RPM.
export PATH=%{_cargo_home}:%{_cargo_home}/bin:$PATH
export CARGO_HOME=%{_cargo_home}
export RUSTUP_HOME=%{_rustup_home}
export RUSTUP_TOOLCHAIN=%{cardwire_toolchain}
# Aya's eBPF build uses the unstable -Z build-std=core option.
export RUSTC_BOOTSTRAP=1

# bpf-linker is not packaged by Fedora; install cargo-binstall and the linker
# as private build tools. Keep helper-tool Cargo separate from the pinned
# nightly Cargo configuration used by Aya.
rm -rf %{_builddir}/tool-cargo-home
CARGO_HOME=%{_builddir}/tool-cargo-home RUSTUP_TOOLCHAIN=stable \
    /usr/bin/cargo install --locked --root %{_builddir}/cargo-binstall cargo-binstall
export PATH=%{_builddir}/cargo-binstall/bin:$PATH
CARGO_HOME=%{_builddir}/tool-cargo-home RUSTUP_TOOLCHAIN=stable \
    cargo binstall --no-confirm --install-path %{_builddir}/bpf-linker/bin bpf-linker
export PATH=%{_builddir}/bpf-linker/bin:$PATH
%cargo_build

%install
install -Dm0755 target/rpm/cardwire             %{buildroot}%{_bindir}/cardwire
install -Dm0755 target/rpm/cardwired            %{buildroot}%{_bindir}/cardwired
install -Dm0644 assets/cardwired.service        %{buildroot}%{_unitdir}/cardwired.service
install -Dm0644 assets/%{appid}.conf            %{buildroot}%{_datadir}/dbus-1/system.d/%{appid}.conf
install -Dm0755 target/release/cardwire-gui     %{buildroot}%{_bindir}/cardwire-gui
install -Dm0644 assets/cardwire-gui.desktop     %{buildroot}%{_appsdir}/cardwire-gui.desktop
install -Dm0644 assets/%{appid}.metainfo.xml    %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
for icon in assets/icons/*.svg; do
	install -Dm644 "$icon" %{buildroot}%{_scalableiconsdir}/$(basename "$icon")
done

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%terra_appstream -o %{S:1}

%post
%systemd_post cardwired.service

%preun
%systemd_preun cardwired.service

%postun
%systemd_postun_with_restart cardwired.service

%files
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/cardwire
%{_bindir}/cardwired
%{_unitdir}/cardwired.service
%config %{_datadir}/dbus-1/system.d/%{appid}.conf

%files gui
%{_scalableiconsdir}/*.svg
%{_bindir}/cardwire-gui
%{_appsdir}/cardwire-gui.desktop
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sun Aug 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Update for 0.12.0

* Sat Aug 01 2026 Owen Zimmerman <owen@fyralabs.com>
- Add cardwire-gui subpackage

* Wed May 06 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
