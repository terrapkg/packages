Name:			scrcpy
Version:		3.3.2
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

%description
This application mirrors Android devices (video and audio) connected via USB or TCP/IP and allows control using the computer's keyboard and mouse. It does not require root access or an app installed on the device. It works on Linux, Windows, and macOS.

%prep
%autosetup

%build
export WORK_DIR=$PWD/work
export OUTPUT_DIR=$PWD/output
export VERSION=v%version

%meson \
	-Dcompile_server=false \
	-Dportable=false \
	-Dstatic=false
%meson_build

%install
%meson_install

%files
%doc READMD.md
%license LICENSE
