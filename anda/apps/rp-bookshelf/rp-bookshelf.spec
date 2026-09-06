%global commit 8d837571ef02a4c1c4d74e419ebc59d66b47b685
%global commit_date 20260521
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rp-bookshelf
Version:        0~%commit_date.git~%shortcommit
Release:        1%{?dist}
Summary:        Browser for Raspberry Pi Press publications in PDF format
License:        BSD-3-Clause
URL:            https://github.com/raspberrypi-ui/bookshelf
Source0:        %url/archive/%commit.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires: meson
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: intltool
BuildRequires: gcc
BuildRequires: pkgconfig(wayland-protocols)

Requires: libcurl gtk3

%description
%summary.

%prep
%autosetup -n bookshelf-%commit

%conf
%meson

%build
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%doc README
%license debian/copyright
%{_bindir}/rp-bookshelf
%{_hicolordir}/16x16/apps/bookshelf.png
%{_hicolordir}/24x24/apps/bookshelf.png
%{_hicolordir}/32x32/apps/bookshelf.png
%{_hicolordir}/48x48/apps/bookshelf.png
%{_hicolordir}/64x64/apps/bookshelf.png
%{_hicolordir}/96x96/apps/bookshelf.png
%{_scalableiconsdir}/bookshelf.svg
%{_datadir}/applications/rp-bookshelf.desktop
%{_datadir}/rp-bookshelf/*

%changelog
* Fri Aug 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Package bookshelf
