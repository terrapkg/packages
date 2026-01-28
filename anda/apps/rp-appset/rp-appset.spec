<<<<<<< HEAD
%global commit b3f3f1da2fa59a2cbdea73c75b7d67bc312ce2bc
%global commit_date 20251115
=======
%global commit 605d9dd8c825b650deeaa614e1b83e8dbb41e87d
%global commit_date 20260128
>>>>>>> 93ea6f333 (chore: Bump out of sync packages (#9513))
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           appset
Version:        0~%commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Application for customisation of appearance of Raspberry Pi Desktop
License:        BSD-3-Clause
URL:            https://github.com/raspberrypi-ui/appset
Source0:        %url/archive/%commit.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gtk3-devel
BuildRequires:  libxml2-devel
BuildRequires:  intltool
BuildRequires:  gcc

Requires:       libxml2

Provides:       pipanel
Provides:       rp-appset

%description
%summary.

%prep
%autosetup -n appset-%commit

%build
%meson
%meson_build

%install
%meson_install

%find_lang rpcc_pipanel

%files -f rpcc_pipanel.lang
%doc README
%license debian/copyright
%{_datadir}/rpcc/ui/pipanel.ui
%{_libdir}/rpcc/librpcc_pipanel.so
%{_iconsdir}/hicolor/24x24/apps/appset-desktop.png
%{_iconsdir}/hicolor/24x24/apps/appset-taskbar.png
%{_iconsdir}/hicolor/32x32/apps/appset-desktop.png
%{_iconsdir}/hicolor/32x32/apps/appset-taskbar.png

%changelog
* Sat Oct 25 2025 Owen Zimmerman <owen@fyralabs.com>
- Follow upstream by changing to build plugin instead of application
* Fri Aug 15 2025 Owen Zimmerman <owen@fyralabs.com>
- Package appset
