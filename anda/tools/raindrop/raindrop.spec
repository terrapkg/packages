%global commit 9132dbac7cae059943f2b8571edf397ad167aa27
%global commit_date 20251126
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           raindrop
Version:        0~%commit_date.git~%shortcommit
Release:        1%?dist
Summary:        Desktop front-end for arandr and wlrandr
License:        BSD-3-Clause
URL:            https://github.com/raspberrypi-ui/raindrop
Packager:       Owen Zimmerman <owen@fyralabs.com>
Source0:        %url/archive/%commit.tar.gz
Source1:        org.raspberrypi.raindrop.configure-display.policy
Patch0:         desktop-file-call-pkexec.patch

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
%autosetup -n raindrop-%commit -p0

%build
%meson
%meson_build

%install
%meson_install
install -Dm644 %{SOURCE1} %{buildroot}/%{_datadir}/polkit-1/actions/org.raspberrypi.raindrop.configure-display.policy
%find_lang %{name}

%files -f %{name}.lang
%license debian/copyright
%{_bindir}/raindrop
%{_datadir}/polkit-1/actions/org.raspberrypi.raindrop.configure-display.policy
%{_datadir}/applications/raindrop.desktop
%{_datadir}/raindrop/ui/raindrop.ui

%changelog
* Thu Aug 07 2025 Owen Zimmerman <owen@fyralabs.com>
- Package raindrop
