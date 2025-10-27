%global debug_package %{nil}

%global commit c9e76f327376c8bb6ab4e4cc5187954aa8cdc538
%global commit_date 20251020
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global rustflags -Clink-arg=-Wl,-z,relro,-z,now

Name:           asusctl
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        A control daemon, CLI tools, and a collection of crates for interacting with ASUS ROG laptops
URL:            https://gitlab.com/asus-linux/asusctl
Source0:        %url/-/archive/%commit/asusctl-%commit.tar.gz
License:        MPL-2.0
Patch0:         fix-makefile.patch
BuildRequires:  anda-srpm-macros cargo-rpm-macros systemd-rpm-macros mold rust-udev-devel clang-devel 
BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  rust
BuildRequires:  rust-std-static
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libzstd)
ExclusiveArch:  x86_64

Packager:       Metcya <metcya@gmail.com>

%description
%summary.

%package rog-gui
Summary:    An experimental gui for %name
Requires:   %name

%description rog-gui
A one-stop-shop GUI tool for asusd/asusctl. It aims to provide most controls,
a notification service, and ability to run in the background.

%prep
%autosetup -p1 -n asusctl-%commit
%cargo_prep_online

%build
%cargo_build

%install
export RUSTFLAGS="%{rustflags}"
mkdir -p "%{buildroot}/%{_bindir}" "%{buildroot}%{_docdir}"
%make_install

install -D -m 0644 rog-anime/data/diagonal-template.png %{buildroot}/%{_docdir}/%{name}/diagonal-template.png

desktop-file-validate %{buildroot}/%{_datadir}/applications/rog-control-center.desktop

%files
%license LICENSE
%doc README.md rog-anime/README.md
%{_bindir}/asusd
%{_bindir}/asusd-user
%{_bindir}/asusctl
%{_unitdir}/asusd.service
%{_userunitdir}/asusd-user.service
%{_udevrulesdir}/99-asusd.rules
%dnl %{_sysconfdir}/asusd/
%{_datadir}/dbus-1/system.d/asusd.conf
%{_datadir}/icons/hicolor/512x512/apps/asus_notif_*.png
%{_datadir}/icons/hicolor/scalable/status/gpu-*.svg
%{_datadir}/icons/hicolor/scalable/status/notification-reboot.svg
%{_datadir}/asusd/

%files rog-gui
%{_bindir}/rog-control-center
%{_datadir}/applications/rog-control-center.desktop
%{_datadir}/icons/hicolor/512x512/apps/rog-control-center.png
%{_datadir}/rog-gui


%changelog
* Sun Oct 26 2025 Metcya <metcya@gmail.com>
- Package asusctl
