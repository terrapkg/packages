%global commit 7d705d0a65c027bb39825bf428fe7c5316411197
%global commit_date 20251014
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           piclone
Version:        %commit_date.git~%shortcommit
Release:        2%?dist
Summary:        Utility to back up Pi to an SD card reader
License:        BSD-3-Clause
URL:            https://github.com/raspberrypi-ui/piclone
Source0:        %url/archive/%commit.tar.gz

BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: gtk3-devel
BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: vala
BuildRequires: pkgconfig
BuildRequires: gcc

Requires: parted dosfstools e2fsprogs coreutils util-linux-core uuid dbus-x11 gtk3

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
SD Card backup program for Raspberry Pi.
This is a GTK application to copy the contents of SD cards and other USB
drives. It mirrors the partition layout of the source device onto the
target device, with the exception of the last partition, which is created
to be the largest which will fit onto the target device.
Files are then copied between all partitions - the result should be a
bootable card with an image of the source device.

%prep
%autosetup -n piclone-%commit

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README
%license debian/copyright
%{_bindir}/piclone
%{_datadir}/applications/piclone.desktop
%{_datadir}/locale/de/LC_MESSAGES/piclone.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/piclone.mo
%{_datadir}/locale/hy/LC_MESSAGES/piclone.mo
%{_datadir}/locale/it/LC_MESSAGES/piclone.mo
%{_datadir}/locale/ko/LC_MESSAGES/piclone.mo
%{_datadir}/locale/nb/LC_MESSAGES/piclone.mo
%{_datadir}/locale/sk/LC_MESSAGES/piclone.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/piclone.mo
%{_datadir}/piclone/piclone.ui

%changelog
* Thu Aug 07 2025 Owen Zimmerman <owen@fyralabs.com>
- Package piclone
