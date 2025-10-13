%global commit      ac498cd3b228c5218dd91ab6876459a7790b3c8a
%global shortcommit %{sub %commit 1 7}
%global commit_date 20251012

Name:           monita
Version:        0~%{commit_date}git.%shortcommit
Release:        1%?dist
Summary:        A modern, beautiful system monitor
License:        GPL-3.0-only
URL:            https://github.com/tau-OS/monita
Source0:        %url/archive/%commit.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  meson vala
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libhelium-1)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  %_bindir/update-desktop-database

%description
A modern, beautiful system monitor for Linux built with GTK4 and libhelium.

%prep
%autosetup -n %name-%commit

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING
%_bindir/com.fyralabs.Monita
%_datadir/applications/com.fyralabs.Monita.desktop
%_iconsdir/hicolor/*/apps/com.fyralabs.Monita.svg
