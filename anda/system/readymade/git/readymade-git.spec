%global commit cb4a987d9e92423f645056532b5e19e34de36a4d
%global commit_date 20250611
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           readymade-git
Version:        %commit_date.%shortcommit
Release:        1%?dist
Summary:        Install ready-made distribution images!
License:        GPL-3.0-or-later
URL:            https://github.com/FyraLabs/readymade
Source0:        %url/archive/%commit.tar.gz
Source1:        https://github.com/FyraLabs/rdms_proc_macros/archive/HEAD.tar.gz
BuildRequires:	anda-srpm-macros rust-packaging mold
BuildRequires:  pkgconfig(libhelium-1)
BuildRequires:  clang-devel
BuildRequires:  cmake
Conflicts:      readymade
Obsoletes:      readymade-nightly < 20250502.4dc78ec-3

Requires:  efibootmgr

%description
Readymade is a simple Linux Distribution installer.

It is created as a replacement to Red Hat's Anaconda installer.


%package config-ultramarine
Summary:        Readymade Configuration for Ultramarine Linux
Requires:       readymade-git
Provides:       readymade-git-config
Conflicts:      readymade-config-ultramarine
Obsoletes:      readymade-nightly-config-ultramarine < 20250502.4dc78ec-3

%description config-ultramarine
This package contains the configuration files for Readymade to install Ultramarine Linux.


%prep
%autosetup -n readymade-%commit
tar xf %{S:1}
rmdir taidan_proc_macros && mv rdms_proc_macros* taidan_proc_macros
%cargo_prep_online

%build
%{cargo_build} --locked

%install
install -Dm755 target/rpm/readymade -t %buildroot%_bindir
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
%ghost %_datadir/readymade
%_datadir/icons/hicolor/scalable/apps/com.fyralabs.Readymade.svg
