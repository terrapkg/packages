%global commit 1815ad67432803843058a3cf7eefbf376e9c02c9
%global commit_date 20251029
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rpinters
Version:        0~%commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Raspberry Pi printing utility module
License:        GPL-2+ AND BSD-3-Clause
URL:            https://github.com/raspberrypi-ui/rpinters
Source0:        %url/archive/%commit.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: gcc
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(smbclient)
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(gsettings-desktop-schemas)

%description
%summary.

%prep
%autosetup -n rpinters-%commit

%build
%meson
%meson_build

%install
%meson_install
%find_lang rpcc_%{name}

%files -f rpcc_%{name}.lang
%doc README
%license debian/copyright
%{_datadir}/rpcc/ui/%{name}.ui
%{_libdir}/rpcc/librpcc_rpinters.so

%changelog
* Fri Aug 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Package bookshelf
