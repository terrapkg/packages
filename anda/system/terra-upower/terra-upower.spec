%global pkgname upower

Summary:        Power Management Service
Name:           terra-upower
Version:        1.91.3
Release:        1%{?dist}
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
License:        GPL-2.0-or-later
URL:            https://upower.freedesktop.org/
Source0:        https://gitlab.freedesktop.org/upower/%{pkgname}/-/archive/v%{version}/%{pkgname}-v%{version}.tar.bz2

# Valve patches
Patch0:         valve.patch

Provides:       upower = %{evr}
Conflicts:      upower

BuildRequires:  meson
BuildRequires:  git
BuildRequires:  gettext
BuildRequires:  libgudev1-devel
%define idevice disabled
%ifnarch s390 s390x
%if ! 0%{?rhel}
%define idevice enabled
BuildRequires:  libimobiledevice-devel
%endif
%endif
BuildRequires:  glib2-devel >= 2.6.0
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  polkit-devel
BuildRequires:  systemd

Requires:       %{name}-libs%{?_isa} = %{evr}
Requires:       udev

%description
UPower (formerly DeviceKit-power) provides a daemon, API and command
line tools for managing power devices attached to the system.

%package libs
Summary:        Client libraries for UPower
Provides:       upower-libs = %{evr}
Conflicts:      upower-libs
Requires:       gobject-introspection
Recommends:     %{name}%{?_isa} = %{evr}

%description libs
Client libraries for UPower.

%package devel
Summary:        Headers and libraries for UPower
Provides:       upower-devel = %{evr}
Conflicts:      upower-devel
Requires:       %{name}-libs%{?_isa} = %{evr}

%description devel
Headers and libraries for UPower.

%package devel-docs
Summary:        Developer documentation for for libupower-glib
Provides:       upower-devel-docs = %{evr}
Conflicts:      upower-devel-docs
Requires:       %{name}-libs = %{evr}
BuildArch:      noarch

%description devel-docs
Developer documentation for for libupower-glib.

%package tests
Summary:        Test files for Upower
Provides:       upower-tests = %{evr}
Conflicts:      upower-tests
Requires:       %{name}%{?_isa} = %{evr}

%description tests
Test files for Upower

%prep
%autosetup -n %{pkgname}-v%{version} -p1 -S git

%build
%meson \
  -Didevice=%{idevice} \
  -Dman=true \
  -Dgtk-doc=true \
  -Dintrospection=enabled

%meson_build

%install
%meson_install

mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/installed-tests
mv $RPM_BUILD_ROOT%{_libexecdir}/upower $RPM_BUILD_ROOT%{_libexecdir}/installed-tests

%find_lang upower

%ldconfig_scriptlets

%post
%systemd_post upower.service

%preun
%systemd_preun upower.service

%postun
%systemd_postun_with_restart upower.service

%files -f upower.lang
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc NEWS AUTHORS HACKING.md README.md
%{_datadir}/dbus-1/system.d/*.conf
%{_udevrulesdir}/*.rules
%{_udevhwdbdir}/*.hwdb
%ghost %dir %{_localstatedir}/lib/upower
%dir %{_sysconfdir}/UPower
%config %{_sysconfdir}/UPower/UPower.conf
%{_sysconfdir}/UPower/UPower.conf.d/README.md
%{_bindir}/upower
%{_libexecdir}/upowerd
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_mandir}/man8/*
%{_datadir}/dbus-1/system-services/*.service
%{_unitdir}/*.service
%{_datadir}/polkit-1/actions/org.freedesktop.upower.policy
%{_datadir}/polkit-1/rules.d/org.freedesktop.upower.rules
%{_datadir}/zsh/*

%files libs
%license COPYING
%{_libdir}/libupower-glib.so.3{,.*}
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_datadir}/dbus-1/interfaces/*.xml
%{_libdir}/libupower-glib.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_includedir}/libupower-glib
%{_includedir}/libupower-glib/up-*.h
%{_includedir}/libupower-glib/upower.h

%files devel-docs
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html/UPower
%{_datadir}/gtk-doc/html/UPower/*

%files tests
%{_libexecdir}/installed-tests/upower
%dir %{_datadir}/installed-tests/
%dir %{_datadir}/installed-tests/upower/
%{_datadir}/installed-tests/upower/upower-integration.test

%changelog
* Wed Oct 07 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 1.91.5-1
- Initial terra-upower package
