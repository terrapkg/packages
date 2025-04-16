Name:           readymade
Version:        0.12.0
Release:        2%?dist
Summary:        Install ready-made distribution images!
License:        GPL-3.0-or-later
URL:            https://github.com/FyraLabs/readymade
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	anda-srpm-macros rust-packaging mold
BuildRequires:  pkgconfig(libhelium-1)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  clang-devel
BuildRequires:  cmake

Requires:  efibootmgr

%description
Readymade is a simple Linux Distribution installer.

It is created as a replacement to Red Hat's Anaconda installer.


%package config-ultramarine
Summary:        Readymade Configuration for Ultramarine Linux
Requires:       readymade
Provides:       readymade-config

%description config-ultramarine
This package contains the configuration files for Readymade to install Ultramarine Linux.


%prep
%autosetup
%cargo_prep_online

%build

%install
%cargo_install
./install.sh %buildroot
ln -sf %{_datadir}/applications/com.fyralabs.Readymade.desktop %{buildroot}%{_datadir}/applications/liveinst.desktop


%files config-ultramarine
%_sysconfdir/readymade.toml


%files
%license LICENSE
%_bindir/readymade
%_datadir/polkit-1/actions/com.fyralabs.pkexec.readymade.policy
%_datadir/applications/com.fyralabs.Readymade.desktop
%_datadir/applications/liveinst.desktop
%_datadir/readymade
%_datadir/icons/hicolor/scalable/apps/com.fyralabs.Readymade.svg

