%global commit 36e917c383a333caa43e187c06c0aed0c30c0421
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20250221
%global ver 12.12
%global base_name steamtinkerlaunch
%global _description %{expand:
Steam Tinker Launch is a Linux wrapper tool for use with the Steam client which allows customizing and start tools and options for games quickly on the fly.}

Name:           %{base_name}-git
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Wrapper tool for use with the Steam client for custom launch options
License:        GPL-3.0-or-later
URL:            https://github.com/sonic2kk/steamtinkerlaunch
Source0:        %{url}/archive/%{commit}/%{base_name}-%{commit}.tar.gz
BuildRequires:  make
BuildRequires:  sed
Requires:       bash
Requires:       gawk
Requires:       git
Requires:       procps-ng
Requires:       tar
Requires:       unzip
Requires:       vim-common
Requires:       wget
Requires:       xdotool
Requires:       xprop
Requires:       xrandr
Requires:       xwininfo
Requires:       xxd
Requires:       yad >= 7.2
# Weak deps for various optional features
Recommends:     gamemode
Recommends:     gameconqueror
# Default to terra-gamescope if available as Fedora's Gamescope package is notoriously broken, otherwise recommend Fedora's
Recommends:     (terra-gamescope or gamescope)
Recommends:     ImageMagick
Recommends:     innoextract
Recommends:     jq
Recommends:     mangohud
Recommends:     net-toolsa
Recommends:     p7zip
Recommends:     rsync
Recommends:     scummvm
Recommends:     strace
Recommends:     usbutils
Recommends:     vkBasalt
# Default to whatever WINE source the user has
Recommends:     (winehq-staging or wine)
Recommends:     winetricks
Recommends:     xdg-utils
# Terra tag policy
Provides:       %{base_name}.git
Conflicts:      %{base_name}
BuildArch:      noarch
Packager:       Gilver E. <rockgrub@disroot.org>

%description %_description

%prep
%autosetup -p1 -n %{base_name}-%{commit}
# We only want the install commands from the Makefile
sed -i 's/.*sed.*//g' Makefile
# Let RPM handle the doc files
sed -i 's/.*doc.*//g' Makefile

%build

%install
%make_install PREFIX=%{buildroot}%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/steamtinkerlaunch
%{_datadir}/steamtinkerlaunch
%{_datadir}/applications/steamtinkerlaunch.desktop
%{_datadir}/icons/hicolor/scalable/apps/steamtinkerlaunch.svg

%changelog
* Wed Mar 26 2025 Gilver E. <rockgrub@disroot.org> - 12.12
- Initial package
