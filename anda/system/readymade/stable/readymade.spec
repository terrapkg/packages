Name:           readymade
Version:        0.12.2
Release:        1%?dist
Summary:        Install ready-made distribution images!
License:        GPL-3.0-or-later
URL:            https://github.com/FyraLabs/readymade
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/FyraLabs/rdms_proc_macros/archive/HEAD.tar.gz
BuildRequires:	anda-srpm-macros rust-packaging mold
BuildRequires:  pkgconfig(libhelium-1)
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
tar xf %{S:1}
rmdir taidan_proc_macros && mv rdms_proc_macros* taidan_proc_macros
%cargo_prep_online

%build
%{cargo_build} --locked

%install
%crate_install_bin
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

