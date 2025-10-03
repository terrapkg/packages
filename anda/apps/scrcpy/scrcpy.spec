Name:			scrcpy
Version:		3.3.3
Release:		1%?dist
Summary:		Display and control your Android device
License:		Apache-2.0
URL:			https://github.com/Genymobile/scrcpy
Source0:		%url/archive/refs/tags/v%version.tar.gz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	meson ninja-build cmake nasm gcc
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavdevice)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libswresample)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	cmake(VulkanHeaders)
BuildRequires:	vulkan-loader
BuildRequires:	OpenCL-ICD-Loader
BuildConflicts:	dkms-nvidia akmod-nvidia
Requires:       android-tools

%description
This application mirrors Android devices (video and audio) connected via USB or TCP/IP and allows control using the computer's keyboard and mouse. It does not require root access or an app installed on the device. It works on Linux, Windows, and macOS.

%pkg_completion -Bz

%prep
%autosetup

%build
export WORK_DIR=$PWD/work
export OUTPUT_DIR=$PWD/output
%dnl #export CFLAGS="$(echo $CFLAGS | sed 's/-D_GNU_SOURCE[=1]*//g')"
%dnl #export CPPFLAGS="$(echo $CPPFLAGS | sed 's/-D_GNU_SOURCE[=1]*//g')"
export VERSION=v%version

%meson \
	-Dcompile_server=true \
	-Dportable=false \
	-Dstatic=false
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%_bindir/scrcpy
%_datadir/applications/scrcpy-console.desktop
%_datadir/applications/scrcpy.desktop
%_datadir/scrcpy/scrcpy-server
%_datadir/bash-completion/completions/scrcpy
%_iconsdir/hicolor/*/apps/scrcpy.png
%_mandir/man1/scrcpy.1.*
