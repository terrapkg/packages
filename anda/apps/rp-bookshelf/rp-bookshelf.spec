%global commit a720bf5041fd832a278378fd6f5cf9a0b3f8cc6f
%global commit_date 20251217
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rp-bookshelf
Version:        0~%commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Browser for Raspberry Pi Press publications in PDF format
License:        BSD-3-Clause
URL:            https://github.com/raspberrypi-ui/bookshelf
Source0:        %url/archive/%commit.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: gtk3-devel
BuildRequires: libcurl-devel
BuildRequires: intltool
BuildRequires: gcc

Requires: libcurl gtk3

%description
%summary.

%prep
%autosetup -n bookshelf-%commit

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%doc README
%license debian/copyright
%{_bindir}/rp-bookshelf
%{_datadir}/icons/hicolor/16x16/apps/bookshelf.png
%{_datadir}/icons/hicolor/24x24/apps/bookshelf.png
%{_datadir}/icons/hicolor/32x32/apps/bookshelf.png
%{_datadir}/icons/hicolor/48x48/apps/bookshelf.png
%{_datadir}/applications/rp-bookshelf.desktop
%{_datadir}/rp-bookshelf/*

%changelog
* Fri Aug 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Package bookshelf
