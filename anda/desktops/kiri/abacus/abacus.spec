%global forgeurl https://gitlab.com/vala-panel-project/vala-panel-appmenu
Name: abacus
Version: 0.1.0
Release: %autorelease
Summary: Calculate Stuff
URL: https://github.com/tau-OS/abacus
Source0: %url/archive/refs/tags/v%{version}.tar.gz
License: GPL-3.0

BuildRequires: meson
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: cmake
BuildRequires: vala
BuildRequires: ninja-build
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libhelium-1)
BuildRequires: pkgconfig(json-glib-1.0)
Requires: libhelium
BuildRequires: desktop-file-utils


%description
%{summary}.

%prep
%forgeautosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang com.fyralabs.Abacus


%files -f com.fyralabs.Abacus.lang
%license LICENSE
%{_bindir}/com.fyralabs.Abacus
%{_datadir}/applications/com.fyralabs.Abacus.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.fyralabs.Abacus*
%{_datadir}/icons/hicolor/symbolic/apps/com.fyralabs.Abacus*


%changelog
%autochangelog