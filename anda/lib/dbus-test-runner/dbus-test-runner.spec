Name:           dbus-test-runner
Version:        19.04.0
Release:        2%?dist
Summary:        A small utility to run executables under a new DBus session for testing
License:        GPL-3.0
URL:            https://launchpad.net/dbus-test-runner
Source0:        %{url}/19.04/%{version}/+download/dbus-test-runner-%{version}.tar.gz
Source1:        https://salsa.debian.org/debian/dbus-test-runner/-/raw/debian/sid/debian/man/dbus-test-runner.1
Source2:        https://salsa.debian.org/debian/dbus-test-runner/-/archive/debian/sid/dbus-test-runner-debian-sid.tar.gz

BuildRequires: automake libtool mate-common
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(dbus-glib-1)

%description
A small little utility to run a couple of executables under a new DBus session
for testing.

%package devel
Summary:  Development files for dbus-test-runner
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and headers for dbus-test-runner.

%prep
%autosetup -n dbus-test-runner-%{version}

# Apply patch fixes from Debian
tar -xf '%{SOURCE2}'
for i in dbus-test-runner-debian-sid/debian/patches/*.patch; do patch -p1 < $i; done

%build
NOCONFIGURE=1 autoreconf -fi

%configure
%make_build

%install
%make_install

# Don't package static files
rm -rf %{buildroot}%{_libdir}/libdbustest.a

# Install manpage
install -dm755 %{buildroot}%{_mandir}/man1/
install -Dm644 %{SOURCE1} %{buildroot}%{_mandir}/man1/

%files
%doc README
%license COPYING
%{_libdir}/libdbustest.so.*
%dir %{_libexecdir}/dbus-test-runner
%{_libexecdir}/dbus-test-runner/dbus-test-watchdog
%{_bindir}/dbus-test-runner
%{_mandir}/man1/dbus-test-runner.1.gz
%dir %{_datadir}/dbus-test-runner
%{_datadir}/dbus-test-runner/*.conf
%{_datadir}/dbus-test-runner/dbus-test-bustle-handler

%files devel
%doc README
%license COPYING
%dir %{_includedir}/libdbustest-1
%dir %{_includedir}/libdbustest-1/libdbustest
%{_includedir}/libdbustest-1/libdbustest/*.h
%{_libdir}/libdbustest.so
%{_libdir}/pkgconfig/dbustest-1.pc

%changelog
%autochangelog
