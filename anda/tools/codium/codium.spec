Name:			codium
Version:		1.77.0.23090
Release:		%autorelease
Summary:		Code editing. Redefined.
License:		MIT
URL:			https://vscodium.com/
Source0:		https://github.com/VSCodium/vscodium/archive/refs/tags/%version.tar.gz
BuildRequires:	pkgconfig(libx11-dev) pkgconfig(libxkbfile-dev) pkgconfig(libsecret-1-dev) pkg-config
BuildRequires:	make gcc nodejs20 yarnpkg jq git
Requires:		alsa-lib at-spi2-atk cairo cups-libs dbus-libs expat gtk3 xrandr mesa-libgbm nspr nss nss-util xdg-utils

%description
VSCodium is a new choice of tool that combines the simplicity of a code editor with what developers need for the core edit-build-debug cycle.

%prep
%autosetup

%build
export RELEASE_VERSION="%version"
export MS_TAG=$(echo $RELEASE_VERSION | egrep -o '([0-9]+\.){2}[0-9]+')
./build/build.sh

%install

%files

%changelog
* Sun Apr 1 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package.

