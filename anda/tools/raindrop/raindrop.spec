%global commit 66271d1eea4740131bae3aaec499a7ce06441ace
%global commit_date 20250530
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           raindrop
Version:        %commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Desktop front-end for arandr and wlrandr
License:        BSD-3-Clause
URL:            https://github.com/raspberrypi-ui/raindrop
Source0:        %url/archive/%commit.tar.gz

BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: gtk3-devel
BuildRequires: libxml2-devel
BuildRequires: intltool
BuildRequires: pkgconfig
BuildRequires: gcc
BuildRequires: gtk-layer-shell-devel

Requires: libxml2 libinput wlr-randr gtk3

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

%files
%license debian/copyright
%{_bindir}/raindrop
%dnl /usr/lib/debug/usr/bin/raindrop-20250530.git~66271d1-1.fcrawhide.x86_64.debug
%{_datadir}/applications/raindrop.desktop
%{_datadir}/locale/ar/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/br/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/bs/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/ca/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/ckb/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/cs/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/da/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/de/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/el/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/es/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/et/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/fa/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/fi/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/fr/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/gl/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/he/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/hu/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/hy/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/id/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/it/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/ja/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/kn/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/ko_KR/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/lt/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/nb_NO/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/nl/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/pl/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/ro/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/ru/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/sc/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/sk/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/sq/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/sr/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/sv/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/tr/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/uk/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/raindrop.mo
%{_datadir}/locale/zh_Hant/LC_MESSAGES/raindrop.mo
%{_datadir}/raindrop/ui/raindrop.ui

%changelog
* Thu Aug 07 2025 Owen Zimmerman <owen@fyralabs.com>
- Package raindrop
