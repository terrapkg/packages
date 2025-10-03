Name:			scrcpy
Version:		3.3.3
Release:		1%?dist
Summary:		Display and control your Android device
License:		Apache-2.0 AND Proprietary
URL:			https://github.com/Genymobile/scrcpy
Source0:		%url/archive/refs/tags/v%version.tar.gz
Source1:    https://developer.android.com/studio/terms.html
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
BuildRequires:  python3-sdkmanager
BuildRequires:  java-25-openjdk-devel
BuildConflicts:	dkms-nvidia akmod-nvidia
Requires:       android-tools

%description
This application mirrors Android devices (video and audio) connected via USB or TCP/IP and allows control using the computer's keyboard and mouse. It does not require root access or an app installed on the device. It works on Linux, Windows, and macOS.

%pkg_completion -Bz

%prep
%autosetup
mkdir -p /tmp/android_sdk
export ANDROID_SDK_ROOT=/tmp/android_sdk
sdkmanager --install tools --sdk_root /tmp/android_sdk
echo y | sdkmanager --license

%build
export WORK_DIR=$PWD/work
export OUTPUT_DIR=$PWD/output
%dnl #export CFLAGS="$(echo $CFLAGS | sed 's/-D_GNU_SOURCE[=1]*//g')"
%dnl #export CPPFLAGS="$(echo $CPPFLAGS | sed 's/-D_GNU_SOURCE[=1]*//g')"
export VERSION=v%version
export ANDROID_SDK_ROOT=/tmp/android_sdk

%meson \
	-Dcompile_server=true \
	-Dportable=false \
	-Dstatic=false

%meson_build

rm -rf /tmp/android_sdk

%install
pushd "%_vpath_builddir"
%ninja_install
popd
ls -la
install -Dm 644 ${SOURCES}/terms.html %{buildroot}%{_licensedir}/LICENSE.android-sdk-license

%files
%doc README.md
%license LICENSE
%license %{SOURCE1}
%_bindir/scrcpy
%_datadir/applications/scrcpy-console.desktop
%_datadir/applications/scrcpy.desktop
%_datadir/scrcpy/scrcpy-server
%_datadir/bash-completion/completions/scrcpy
%_iconsdir/hicolor/*/apps/scrcpy.png
%_mandir/man1/scrcpy.1.*

%changelog
* Thu Oct 02 2025 june-fish <june@fyralabs.com>
- fix android sdk bug
