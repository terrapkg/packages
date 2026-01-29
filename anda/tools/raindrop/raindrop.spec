%global commit 2e3859fe3afd65c89eeacb63bdaf7c432f2df30d
%global commit_date 20251202
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           raindrop
Version:        0~%commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Desktop front-end for arandr and wlrandr
License:        BSD-3-Clause
URL:            https://github.com/raspberrypi-ui/raindrop
Packager:       Owen Zimmerman <owen@fyralabs.com>
Source0:        %url/archive/%commit.tar.gz

BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: gtk3-devel
BuildRequires: libxml2-devel
BuildRequires: intltool
BuildRequires: pkgconfig
BuildRequires: gcc
BuildRequires: gtk-layer-shell-devel
BuildRequires: polkit

Requires: libxml2 libinput wlr-randr gtk3 polkit

%description
Screen configuration tool for Raspberry Pi Desktop,
GTK screen configuration tool for labwc and openbox environments.

%prep
%autosetup -n raindrop-%commit

%build
%meson
%meson_build

%install
%meson_install
%find_lang rpcc_%{name}

%files -f rpcc_%{name}.lang
%license debian/copyright
%doc README
%{_libdir}/rpcc/librpcc_raindrop.so
%{_datadir}/rpcc/ui/minus.png
%{_datadir}/rpcc/ui/plus.png
%{_datadir}/rpcc/ui/raindrop.ui

%changelog
* Thu Aug 07 2025 Owen Zimmerman <owen@fyralabs.com>
- Package raindrop
