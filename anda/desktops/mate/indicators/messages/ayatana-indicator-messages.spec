Name:       ayatana-indicator-messages
Summary:    Ayatana Indicator Messages Applet
Version:    24.5.0
Release:    1%?dist
License:    GPLv3
URL:        https://github.com/AyatanaIndicators/ayatana-indicator-messages
Source0:    %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(lomiri-url-dispatcher)
BuildRequires:  cmake-extras
BuildRequires:  systemd-rpm-macros
BuildRequires:  accountsservice-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(dbustest-1)
BuildRequires:  vala
BuildRequires:  gtk-doc
BuildRequires:  vala-devel
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

%package doc
Summary:   Documentation for %{name}
BuildArch: noarch

%description doc
This package contains documentation files for %{name}.

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
%config %{_sysconfdir}/xdg/autostart/ayatana-indicator-messages.desktop
%{_userunitdir}/ayatana-indicator-messages.service
%{_libdir}/libmessaging-menu.so.*
%{_libdir}/girepository-1.0/MessagingMenu-1.0.typelib
%dir %{_libexecdir}/ayatana-indicator-messages
%{_libexecdir}/ayatana-indicator-messages/ayatana-indicator-messages-service
%{_datadir}/ayatana/indicators/org.ayatana.indicator.messages
%{_datadir}/glib-2.0/schemas/org.ayatana.indicator.messages.gschema.xml
%{_datadir}/icons/hicolor/scalable/status/*.svg
%{_datadir}/icons/hicolor/scalable/categories/*.svg
%{_datadir}/icons/hicolor/16x16/categories/*.png
%{_datadir}/icons/hicolor/16x16/status/*.png
%{_datadir}/icons/hicolor/22x22/categories/*.png
%{_datadir}/icons/hicolor/22x22/status/*.png
%{_datadir}/icons/hicolor/24x24/status/*.png
%{_datadir}/icons/hicolor/32x32/categories/*.png
%{_datadir}/icons/hicolor/32x32/status/*.png
%{_datadir}/icons/hicolor/48x48/status/*.png

%files devel
%dir %{_includedir}/messaging-menu
%{_includedir}/messaging-menu/*.h
%{_libdir}/libmessaging-menu.so
%{_libdir}/pkgconfig/messaging-menu.pc
%{_datadir}/vala/vapi/MessagingMenu-1.0.vapi
%{_datadir}/gir-1.0/MessagingMenu-1.0.gir

%files doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%dir %{_datadir}/gtk-doc/html/messaging-menu
%{_datadir}/gtk-doc/html/messaging-menu/*.html
%{_datadir}/gtk-doc/html/messaging-menu/*.png
%{_datadir}/gtk-doc/html/messaging-menu/messaging-menu.devhelp2
%{_datadir}/gtk-doc/html/messaging-menu/style.css

%changelog
%autochangelog
