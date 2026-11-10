%global __brp_mangle_shebangs %{nil}

%global commit 6aca9202fb8dfd6f31241c3f98b72df4a775c1a1
%global commit_date 20261109
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver v0.84.0

Name:           inputplumber-nightly
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Open source input router and remapper daemon for Linux
License:        GPL-3.0-or-later
URL:            https://github.com/ShadowBlip/InputPlumber
Source0:        %{url}/archive/%{commit}/InputPlumber-%{commit}.tar.gz
Patch0:         make-install-dont-build.patch
Patch1:         gpd_fixup.patch
Patch2:         generic-hidraw.patch
Patch3:         legion-go2-gyro.patch
Patch4:         evdev-capability-translations.patch
Patch5:         udev-device-lifecycle.patch
BuildRequires:  libevdev-devel libiio-devel git make cargo libudev-devel llvm-devel clang-devel
BuildRequires:  rust-packaging cargo-rpm-macros rpm_macro(cargo_prep_online) systemd-rpm-macros
Requires:       libevdev libiio
Recommends:     steam gamescope-session linuxconsoletools
Packager:       madonuko <mado@fyralabs.com>
Provides:       inputplumber = %{version}-%{release}
Conflicts:      inputplumber hhd

%description
InputPlumber is an open source input routing and control daemon for Linux. It
can be used to combine any number of input devices (like gamepads, mice, and
keyboards) and translate their input to a variety of virtual device formats.

%prep
%autosetup -n InputPlumber-%{commit} -S git_am -p1
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
%_udevhwdbdir/60-inputplumber-autostart.hwdb
%_udevrulesdir/90-inputplumber-autostart.rules
%{_modulesloaddir}/inputplumber-hrtimer.conf
%_datadir/dbus-1/system.d/org.shadowblip.InputPlumber.conf
%_datadir/inputplumber/
%{_udevrulesdir}/99-inputplumber-device-setup.rules
%{_udevrulesdir}/60-inputplumber-uaccess.rules
%{_udevrulesdir}/55-8bitdo-u2-controller.rules
%{_datadir}/polkit-1/actions/org.shadowblip.InputPlumber.policy
%{_datadir}/polkit-1/rules.d/org.shadowblip.InputPlumber.rules

%changelog
* Sun Nov 08 2026 Kyle Gospo <kyle@fyralabs.com>
- Add nightly package with all downstream patches
