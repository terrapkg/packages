Name:       ayatana-indicator-datetime
Summary:    A GTK implementation of the StatusNotifierItem Specification
Version:    24.5.0
Release:    1%?dist
License:    GPL-3.0
URL:        https://github.com/AyatanaIndicators/ayatana-indicator-datetime
Source0:    %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake-extras
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(lomiri-url-dispatcher)
BuildRequires:  pkgconfig(lomiri-schemas)
BuildRequires:  pkgconfig(libayatana-common)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(properties-cpp)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(messaging-menu)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(lomiri-sounds)
BuildRequires:  pkgconfig(dbustest-1)
BuildRequires:  pkgconfig(systemd)

%description
The Ayatana Indicators project is the continuation of Application Indicators
and System Indicators, two technologies developed by Canonical Ltd. for the
Unity7 desktop and Lomiri desktop.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DENABLE_LOMIRI_FEATURES=ON \
       -DENABLE_TESTS=OFF\
       -DENABLE_COVERAGE=OFF \
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%config %{_sysconfdir}/xdg/autostart/ayatana-indicator-datetime.desktop
%{_userunitdir}/ayatana-indicator-datetime.service
%dir %{_libexecdir}/ayatana-indicator-datetime
%{_libexecdir}/ayatana-indicator-datetime/ayatana-indicator-datetime-service
%{_datadir}/ayatana/indicators/org.ayatana.indicator.datetime
%{_datadir}/glib-2.0/schemas/org.ayatana.indicator.datetime.gschema.xml

%changelog
%autochangelog
