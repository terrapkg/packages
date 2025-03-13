%global __brp_mangle_shebangs %{nil}

Name:           inputplumber
Version:        0.49.4
Release:        1%?dist
Summary:        Open source input router and remapper daemon for Linux
License:        GPL-3.0-or-later
URL:            https://github.com/ShadowBlip/InputPlumber
Source0:        %{url}/archive/refs/tags/v%version.tar.gz
BuildRequires:  libevdev-devel libiio-devel git make cargo libudev-devel llvm-devel clang-devel
BuildRequires:  rust-packaging cargo-rpm-macros mold rpm_macro(cargo_prep_online)
Requires:       libevdev libiio
Recommends:     steam gamescope-session linuxconsoletools
Packager:       madonuko <mado@fyralabs.com>
Provides:       inputplumber
Conflicts:      hhd

%description
InputPlumber is an open source input routing and control daemon for Linux. It
can be used to combine any number of input devices (like gamepads, mice, and
keyboards) and translate their input to a variety of virtual device formats.

%prep
%autosetup -n InputPlumber-%version
%cargo_prep_online

%build
%cargo_build

%install
%make_install BUILD_TYPE=rpm PREFIX=%buildroot%_prefix

%post
%systemd_post inputplumber.service

%preun
%systemd_preun inputplumber.service

%postun
%systemd_postun_with_restart inputplumber.service

%files
%doc README.md
%license LICENSE
%_bindir/inputplumber
%_unitdir/inputplumber.service
%_unitdir/inputplumber-suspend.service
%_udevhwdbdir/59-inputplumber.hwdb
%_datadir/dbus-1/system.d/org.shadowblip.InputPlumber.conf
%_datadir/inputplumber/
