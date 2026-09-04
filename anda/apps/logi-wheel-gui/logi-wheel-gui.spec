Name:           logi-wheel-gui
Version:        0.39.2
Release:        1%{?dist}
Summary:        Graphical settings app for the Logitech racing wheel driver
License:        GPL-3.0-or-later
URL:            https://github.com/mescon/logitech-trueforce-linux-driver
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        com.github.logi-wheel-gui.metainfo.xml
Packager:       Luan Oliveira <luanv.oliveira@outlook.com>
ExclusiveArch:  x86_64

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rustc
BuildRequires:  cargo-rpm-macros
# owns the hicolor icon directories during the post-build filelist check
BuildRequires:  hicolor-icon-theme
# logi-tf-sim's build.rs compiles the in-repo libtrueforce.a via make+gcc
# and links it statically (no runtime dependency).
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtrueforce-devel
BuildRequires:  libtrueforce-static
# logi-wheel-gui's yeslogic-fontconfig-sys dependency links fontconfig/freetype
# at build time (build.rs calls pkg_config::find_library, no dlopen), so the
# devel package and pkg-config must be present or `cargo build` panics and
# aborts the whole %build. pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fontconfig)

Requires:       logi-wheel
# Owns the hicolor icon directories the GUI's launcher icon lands in.
Requires:       hicolor-icon-theme
# Renamed from logi-dd-gui (0.20.0); see logi-wheel's subpackage for why.
Provides:       logi-dd-gui = %{version}-%{release}
Obsoletes:      logi-dd-gui < %{version}-%{release}

Requires:       libwayland-client
Requires:       libwayland-cursor
Requires:       libwayland-egl
Requires:       libxkbcommon
Requires:       libxkbcommon-x11
Requires:       libX11
Requires:       libX11-xcb
Requires:       libxcb
Requires:       libXcursor
Requires:       libXi
Requires:       libXrender
Requires:       mesa-libEGL
Requires:       mesa-libGL
Requires:       fontconfig
Requires:       freetype

%description
logi-wheel-gui, a graphical settings app (GPL-3.0-or-later, with a desktop
menu entry) for the Logitech direct-drive wheel driver: wheel settings,
LIGHTSYNC, response curves, game-helper setup pages, and a test section.


%package -n    logi-wheel
Summary:        Terminal tools for the Logitech racing wheel driver
License:        GPL-2.0-only

Requires:     logitech-trueforce
# The shim installer edits the wine prefix registry with python3.
Recommends:     python3
# Renamed from logi-dd (0.20.0): "dd" meant direct-drive, but the app
# configures every supported wheel, including the gear-driven G923. These
# move an existing logi-dd install onto this package automatically.
Provides:       logi-dd = %{version}-%{release}
Obsoletes:      logi-dd < %{version}-%{release}

%description -n logi-wheel
The complete headless toolset for the Logitech direct-drive wheel driver:
logi-wheel, a terminal settings UI, logi-ffb, a DirectInput force-feedback
proxy, logi-tf-sim, a simulated-TrueForce daemon driven by game telemetry,
and logi-shim, the TrueForce SDK shim installer for
Proton prefixes.

%prep
%autosetup -n logitech-trueforce-linux-driver-%{version}
cd userspace/logi-wheel
%cargo_prep_online

%build
cd userspace/logi-wheel
%cargo_build
cd ../..
# logi-rpm-bridge: the small C bridge that feeds relayed game RPM to the
# driver's kernel texture merge; logi-launch starts and stops it around a
# game session.
gcc %{optflags} -o tools/logi-rpm-bridge tools/logi-rpm-bridge.c

%install
# Headless toolset (the logi-wheel subpackage).
install -D -m 0755 userspace/logi-wheel/target/release/logi-wheel \
    %{buildroot}%{_bindir}/logi-wheel
install -D -m 0755 userspace/logi-wheel/target/release/logi-ffb \
    %{buildroot}%{_bindir}/logi-ffb
install -D -m 0755 userspace/logi-wheel/target/release/logi-tf-sim \
    %{buildroot}%{_bindir}/logi-tf-sim
# Transitional symlink: scripts and habits built around the old logi-dd
# binary name keep working.
ln -s logi-wheel %{buildroot}%{_bindir}/logi-dd
# TrueForce-in-Proton shim installer (no-op without the proprietary SDK DLLs).
install -D -m 0755 tools/install-tf-shim.sh \
    %{buildroot}%{_bindir}/logi-shim
# The rotation proxy that installer stages with --range-proxy. Prebuilt: it
# is a Windows DLL and its users run Linux without a cross-compiler.
install -D -m 0644 tools/tf-range-proxy.dll \
    %{buildroot}%{_datadir}/logitech-trueforce/tf-range-proxy.dll
# The dinput8 escape proxy logi-launch stages into an SDK game's own
# directory: it answers the SDK's range getters and relays the game's RPM
# telemetry for the kernel texture merge. Prebuilt, same reason.
install -D -m 0644 tools/dinput8-escape.dll \
    %{buildroot}%{_datadir}/logitech-trueforce/dinput8-escape.dll
# The RPM feed for the kernel texture merge; logi-launch starts and stops
# it around a game session.
install -D -m 0755 tools/logi-rpm-bridge \
    %{buildroot}%{_bindir}/logi-rpm-bridge
install -D -m 0644 userspace/logi-wheel/target/release/liblogi_tf_scs.so \
    %{buildroot}%{_datadir}/logitech-trueforce/liblogi_tf_scs.so
# A Windows executable: it runs inside the game's Proton prefix.
# Prebuilt because no distro builder ships a Rust Windows target.
install -D -m 0644 tools/logi-tf-relay.exe \
    %{buildroot}%{_datadir}/logitech-trueforce/logi-tf-relay.exe
# The recorded TrueForce init burst logi-launch replays when LOGI_TF_REARM
# is set. Without it that recovery path silently cannot work here alone.
install -D -m 0644 tools/tf-init.bin \
    %{buildroot}%{_datadir}/logitech-trueforce/tf-init.bin
# G923 Xbox mode-switch helper, dispatched by udev rule 73.
install -D -m 0755 tools/xbox-modeswitch.sh \
    %{buildroot}%{_bindir}/logi-wheel-modeswitch
# Rebinds a wheel that another driver claimed, which the settings apps'
# diagnostics offer as a fix. Kept as a script rather than a command in the
# app because a wheel presents several HID interfaces and all of them have
# to be moved.
install -D -m 0755 tools/rebind-wheel.sh \
    %{buildroot}%{_bindir}/logi-rebind-wheel
# Steam launch-options wrapper: starts an in-prefix Windows helper
# (logi-tf-relay, or a telemetry bridge) after the game is up. Useless
# unless it is on PATH, because the whole point is that a user types
# `logi-launch %command%` and nothing else.
install -D -m 0755 tools/logi-launch.sh \
    %{buildroot}%{_bindir}/logi-launch
# Transitional symlink for the pre-v0.22.0 name.
ln -s logi-shim %{buildroot}%{_bindir}/logitech-trueforce-install-shim
# The GUI + its desktop integration (the logi-wheel-gui subpackage).
install -D -m 0755 userspace/logi-wheel/target/release/logi-wheel-gui \
    %{buildroot}%{_bindir}/logi-wheel-gui
install -D -m 0644 desktop/logi-wheel-gui.desktop \
    %{buildroot}%{_datadir}/applications/logi-wheel-gui.desktop
install -D -m 0644 desktop/logi-wheel-gui.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/logi-wheel-gui.svg
# Transitional symlink: scripts and habits built around the old
# logi-dd-gui binary name keep working.
ln -s logi-wheel-gui %{buildroot}%{_bindir}/logi-dd-gui

install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/com.github.logi-wheel-gui.metainfo.xml

%files
%license COPYING
%{_bindir}/logi-wheel-gui
%{_bindir}/logi-dd-gui
%{_datadir}/applications/logi-wheel-gui.desktop
%{_datadir}/icons/hicolor/scalable/apps/logi-wheel-gui.svg
%{_datadir}/metainfo/com.github.logi-wheel-gui.metainfo.xml

%files -n logi-wheel
%license COPYING
%{_bindir}/logi-wheel
%{_bindir}/logi-dd
%{_bindir}/logi-ffb
%{_bindir}/logi-tf-sim
%{_bindir}/logi-shim
%dir %{_datadir}/logitech-trueforce
%{_datadir}/logitech-trueforce/tf-range-proxy.dll
# These two lines had drifted into %%install as bare paths (a latent shell
# error there and unpackaged files here); they belong in this list.
%{_datadir}/logitech-trueforce/liblogi_tf_scs.so
%{_datadir}/logitech-trueforce/logi-tf-relay.exe
%{_datadir}/logitech-trueforce/tf-init.bin
%{_datadir}/logitech-trueforce/dinput8-escape.dll
%{_bindir}/logi-rpm-bridge
%{_bindir}/logi-wheel-modeswitch
%{_bindir}/logi-rebind-wheel
%{_bindir}/logi-launch
%{_bindir}/logitech-trueforce-install-shim

%changelog
* Fri Sep 4 2026 luan Oliveira <luanv.oliveira@outlook.com> - 0.39.2-1
- ported to terra

* Sun Jul 26 2026 mescon <5875228+mescon@users.noreply.github.com> - 0.20.0-1
- Renamed the userspace subpackages: logi-dd -> logi-wheel, logi-dd-gui ->
  logi-wheel-gui ("dd" meant direct-drive, but the app now also covers the
  gear-driven G923). Provides/Obsoletes on the old names move existing
  installs over automatically.

* Mon Jul 20 2026 mescon <5875228+mescon@users.noreply.github.com> - 0.16.1-1
- Build the Rust workspace offline against vendored crate dependencies
  (new Source1 tarball produced by the publish workflow): OBS builders
  have no network access, so the previous cargo build failed to resolve
  index.crates.io and the repository kept serving stale binaries.

* Sat Jul 18 2026 mescon <5875228+mescon@users.noreply.github.com> - 0.15.0-1
- Ship the userspace ecosystem as layered subpackages: logi-dd (settings
  TUI, logi-ffb DirectInput force-feedback proxy, logi-tf-sim
  simulated-TrueForce daemon, and the TrueForce SDK shim installer;
  requires the driver package, which now carries both udev rules) and
  logi-dd-gui (graphical settings app, GPL-3.0-or-later, with desktop
  entry, icon, and the GUI's windowing/rendering runtime dependencies;
  requires logi-dd). Built from the userspace/logi-dd Rust workspace.
