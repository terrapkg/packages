Name:       ayatana-indicator-notifications
Summary:    Ayatana Indicator Notifications Applet
Version:    23.10.1
Release:    1%?dist
License:    GPL-3.0
URL:        https://github.com/AyatanaIndicators/ayatana-indicator-notifications
Source0:    %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake-extras
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libayatana-common)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(dbustest-1)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(libxml-2.0)
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
%autosetup -n %{name}-%{version}

%build
%cmake -DENABLE_TESTS=ON -DENABLE_COVERAGE=OFF
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%config %{_sysconfdir}/xdg/autostart/ayatana-indicator-notifications.desktop
%{_userunitdir}/ayatana-indicator-notifications.service
%dir %{_libexecdir}/ayatana-indicator-notifications
%{_libexecdir}/ayatana-indicator-notifications/ayatana-indicator-notifications-service
%{_datadir}/ayatana/indicators/org.ayatana.indicator.notifications
%{_datadir}/glib-2.0/schemas/org.ayatana.indicator.notifications.gschema.xml
%{_datadir}/icons/hicolor/scalable/status/*.svg

%changelog
%autochangelog
