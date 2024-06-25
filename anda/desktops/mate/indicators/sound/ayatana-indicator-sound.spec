Name:       ayatana-indicator-sound
Summary:    Ayatana Indicator Sound Applet
Version:    24.5.0
Release:    1%?dist
License:    GPLv3
URL:        https://github.com/AyatanaIndicators/ayatana-indicator-sound
Source0:    %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  lomiri-api-devel
BuildRequires:  lomiri-schemas
BuildRequires:  cmake-extras
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libayatana-common)
BuildRequires:  accountsservice-devel
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(dbustest-1)
BuildRequires:  pkgconfig(libqtdbustest-1)
BuildRequires:  pkgconfig(libqtdbusmock-1)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libgmenuharness)
BuildRequires:  vala
BuildRequires:  vala-devel
BuildRequires:  intltool
Suggests:       accountsservice

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
%cmake -DENABLE_LOMIRI_FEATURES=ON \
       -DENABLE_TESTS=ON \
       -DENABLE_COVERAGE=OFF \
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%config %{_sysconfdir}/xdg/autostart/ayatana-indicator-sound.desktop
%{_userunitdir}/ayatana-indicator-sound.service
%dir %{_libexecdir}/ayatana-indicator-sound
%{_libexecdir}/ayatana-indicator-sound/ayatana-indicator-sound-service
%{_datadir}/accountsservice/interfaces/org.ayatana.indicator.sound.AccountsService.xml
%{_datadir}/ayatana/indicators/org.ayatana.indicator.sound
%{_datadir}/dbus-1/interfaces/org.ayatana.indicator.sound.AccountsService.xml
%{_datadir}/glib-2.0/schemas/org.ayatana.indicator.sound.gschema.xml
%{_datadir}/polkit-1/actions/org.ayatana.indicator.sound.AccountsService.policy
%{_datadir}/polkit-1/rules.d/50-org.ayatana.indicator.sound.AccountsService.rules
%{_sharedstatedir}/polkit-1/localauthority/10-vendor.d/50-org.ayatana.indicator.sound.AccountsService.pkla

%changelog
%autochangelog
