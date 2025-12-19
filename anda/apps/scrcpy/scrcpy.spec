%global __requires_exclude_from %{_datadir}/%{name}/.*
%bcond_without server_prebuilt

%global appid com.genymobile.scrcpy
%global org com.genymobile
%global appstream_component desktop-application

# NOTE: We only do this on aarch64 to avoid
# duplicate build artifacts on x86_64
# 
# If you are building this package locally,
# set --with server to cross-compile/bundle the server APK subpackage.
# 
# The server APK is architecture independent.
%ifarch aarch64
%bcond_without server
%else
%bcond_with server
%endif

Name:			scrcpy
Version:		3.3.4
Release:		1%?dist
Summary:		Display and control your Android device
License:		Apache-2.0 AND Proprietary
URL:			https://github.com/Genymobile/scrcpy
Source0:		%url/archive/refs/tags/v%version.tar.gz
Source1:    https://developer.android.com/studio/terms.html
%if %{with server_prebuilt}
Source10:       https://github.com/Genymobile/scrcpy/releases/download/v%{version}/scrcpy-server-v%{version}
%endif
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
Requires:       %{name}-server
# Gradle here really wants Java 21-23 to work properly
# Java 25 breaks the build
BuildRequires:  java-21-openjdk-devel
BuildConflicts:	dkms-nvidia akmod-nvidia
Requires:       android-tools

%description
This application mirrors Android devices (video and audio) connected via USB or TCP/IP and allows control using the computer's keyboard and mouse. It does not require root access or an app installed on the device. It works on Linux, Windows, and macOS.

%if %{with server}
%package server
# This package is architecture independent, it's
# an Android APK file.
Summary:	Android server for %{name}
BuildArch:	noarch
%description server
Android server for %{name}
%endif


%pkg_completion -Bz

%prep
%autosetup
mkdir -p /tmp/android_sdk
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk
export PATH=$JAVA_HOME/bin:$PATH
export ANDROID_SDK_ROOT=/tmp/android_sdk
sdkmanager --install tools --sdk_root /tmp/android_sdk
echo y | sdkmanager --license

%build
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk
export PATH=$JAVA_HOME/bin:$PATH
export WORK_DIR=$PWD/work
export OUTPUT_DIR=$PWD/output
%dnl #export CFLAGS="$(echo $CFLAGS | sed 's/-D_GNU_SOURCE[=1]*//g')"
%dnl #export CPPFLAGS="$(echo $CPPFLAGS | sed 's/-D_GNU_SOURCE[=1]*//g')"
export VERSION=v%version
export ANDROID_SDK_ROOT=/tmp/android_sdk

# TODO: Gradle 8.9 seems to have problems with Java
# 21-25, so we can't build the APK here at all
# For now, let's use the prebuilt server
# https://github.com/gradle/gradle/issues/35111
%if %{with server}
  %if %{with server_prebuilt}
%meson -Dprebuilt_server=%{SOURCE10}
  %else
%meson -Dcompile_server=true
  %endif
%else
%meson -Dcompile_server=false
%endif

%meson_build

rm -rf /tmp/android_sdk

%install
pushd "%_vpath_builddir"
%ninja_install
popd
ls -la

%if %{with server}
install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/licenses/LICENSE.android-sdk-license
%endif

%terra_appstream

%files
%doc README.md
%license LICENSE
%_bindir/scrcpy
%_datadir/applications/scrcpy-console.desktop
%_datadir/applications/scrcpy.desktop
%_datadir/bash-completion/completions/scrcpy
%_iconsdir/hicolor/*/apps/scrcpy.png
%_metainfodir/%{appid}.metainfo.xml
%_mandir/man1/scrcpy.1.*

%if %{with server}
%files server
%license %{_datadir}/licenses/LICENSE.android-sdk-license
%_datadir/scrcpy/scrcpy-server
%endif

%changelog
* Thu Oct 02 2025 june-fish <june@fyralabs.com>
- fix android sdk bug
