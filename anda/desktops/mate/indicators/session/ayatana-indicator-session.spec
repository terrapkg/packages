Name:       ayatana-indicator-session
Summary:    Ayatana Indicator Session Applet
Version:    24.5.0
Release:    1%?dist
License:    GPL-3.0
URL:        https://github.com/AyatanaIndicators/ayatana-indicator-session
Source0:    %{url}/archive/refs/tags/%{version}.tar.gz
Patch0:     0001-fix-tests-import-cstdint.patch

BuildRequires:  cmake
BuildRequires:  cmake-extras
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libayatana-common)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(dbustest-1)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(rda)
BuildRequires:  intltool

%description
The Ayatana Indicators project is the continuation of Application Indicators
and System Indicators, two technologies developed by Canonical Ltd. for the
Unity7 desktop and Lomiri desktop.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development header files for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake -DENABLE_TESTS=ON \
       -DENABLE_COVERAGE=OFF
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%config %{_sysconfdir}/xdg/autostart/ayatana-indicator-session.desktop
%{_userunitdir}/ayatana-indicator-session.service
%dir %{_libexecdir}/ayatana-indicator-session
%{_libexecdir}/ayatana-indicator-session/ayatana-indicator-session-service
%{_datadir}/ayatana/indicators/org.ayatana.indicator.session
%{_datadir}/glib-2.0/schemas/org.ayatana.indicator.session.gschema.xml
%{_datadir}/icons/hicolor/scalable/status/*.svg
%{_datadir}/icons/hicolor/scalable/actions/*.svg
%{_datadir}/icons/hicolor/16x16/actions/*.png
%{_datadir}/icons/hicolor/16x16/status/*.png
%{_datadir}/icons/hicolor/22x22/actions/*.png
%{_datadir}/icons/hicolor/22x22/status/*.png
%{_datadir}/icons/hicolor/24x24/status/*.png
%{_datadir}/icons/hicolor/24x24/actions/*.png
%{_datadir}/icons/hicolor/32x32/actions/*.png
%{_datadir}/icons/hicolor/32x32/status/*.png

%changelog
%autochangelog
