Name:			sway-audio-idle-inhibit
Version:		0.2.0
Release:		1%?dist
Summary:		Prevents swayidle/hypridle from sleeping while any application is outputting or receiving audio
License:		GPL-3.0-only
URL:			https://github.com/ErikReider/SwayAudioIdleInhibit
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildRequires:	meson gcc-c++
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libsystemd)

%description
%summary.

%prep
%autosetup -n SwayAudioIdleInhibit-%version

%build
%meson -Dlogind-provider=systemd
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%_bindir/sway-audio-idle-inhibit
