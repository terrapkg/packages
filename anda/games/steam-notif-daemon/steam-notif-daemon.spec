Name:			steam-notif-daemon
Version:		1.0.1
Release:		1%?dist
Summary:		Steam notification daemon
License:		MIT
URL:			https://github.com/Jovian-Experiments/steam_notif_daemon
Source0:        %url/archive/refs/tags/v%version.tar.gz
Packager:		madonuko <mado@fyralabs.com>
Provides:		steam_notif_daemon = %version-%release
BuildRequires:	meson gcc
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libcurl)

%description
%summary.

%prep
%autosetup -n steam_notif_daemon-%version

%build
%meson -Dsd-bus-provider=libsystemd
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%_bindir/steam_notif_daemon
