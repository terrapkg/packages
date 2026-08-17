%global forgeurl https://gitlab.com/ubports/development/core/click
%global commit 6e4342ae0ef3710343e2dbf0b8da586853625e2e
%forgemeta

Name:           click
Version:        0.5.2
Release:        1%?dist
Summary:        An app building method
License:        LGPL-3.0
URL:            https://gitlab.com/ubports/development/core/click
Source0:        %{url}/-/archive/%commit/click-%commit.tar.gz

BuildRequires: automake libtool
BuildRequires: make
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(properties-cpp)
BuildRequires: dbus-test-runner
BuildRequires: vala
BuildRequires: python3-devel
BuildRequires: python3-sphinx
BuildRequires: systemd-rpm-macros
BuildRequires: systemd

%description
Click is a simplified packaging format that installs in a separate part of
the file system, suitable for third-party applications.

%package devel
Summary:  Click development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and headers for Click.

%package -n python3-lomiri-click
Summary:  Python3 files for Click
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: ubuntu-sdk
Requires: python3-debian
Requires: python3-gobject
BuildArch: noarch

%description -n python3-lomiri-click
Python3 files and the main interface for Click.

%package doc
Summary:   Documentation files for Click
BuildArch: noarch

%description doc
Provides HTML and Manpage (documentation) for Click.

%prep
%autosetup -n click-%commit

%build
NOCONFIGURE=1 \
./autogen.sh

export CFLAGS="$CFLAGS -Wno-implicit-function-declaration"
%configure
%make_build

%install
%make_install -- PYTHON_INSTALL_FLAGS="--root=%{buildroot}"

# Create documentation
pushd doc
make man
mv _build/man/click.1 %{buildroot}%{_mandir}/man1/click.1
make html
mkdir -p %{buildroot}%_pkgdocdir
mv _build/html %{buildroot}%_pkgdocdir
popd
mv README %{buildroot}%_pkgdocdir

%files
%doc doc/index.rst
%license LICENSE
%config %{_sysconfdir}/dbus-1/system.d/com.lomiri.click.conf
%{_libdir}/libclick-0.4.so.*
%dir %{_libdir}/click
%{_libdir}/click/libclickpreload.so
%dir %{_libexecdir}/click
%{_libexecdir}/click/click-service
%{_datadir}/dbus-1/system-services/com.lomiri.click.service
%{_libdir}/girepository-1.0/Click-0.4.typelib

%files devel
%dir %{_includedir}/click-0.4
%{_includedir}/click-0.4/click.h
%{_libdir}/libclick-0.4.so
%{_libdir}/pkgconfig/click-0.4.pc
%{_datarootdir}/gir-1.0/Click-0.4.gir

%files -n python3-lomiri-click
%dir %{_sysconfdir}/click
%dir %{_sysconfdir}/click/databases
%config %{_sysconfdir}/click/databases/*.conf
%dir %{_sysconfdir}/schroot
%dir %{_sysconfdir}/schroot/click
%{_sysconfdir}/schroot/click/fstab
%{_bindir}/dh_click
%{_bindir}/click
%{_mandir}/man1/dh_click.1.gz
%{_datarootdir}/debhelper/
%{_datarootdir}/perl5/*
%{_unitdir}/click-system-hooks.service
%{_userunitdir}/click-user-hooks.service
%dir %{python3_sitelib}/click_package
%{python3_sitelib}/click_package/*.py
%dir %{python3_sitelib}/click_package/tests
%{python3_sitelib}/click_package/tests/*.py
%dir %{python3_sitelib}/click_package/tests/integration
%{python3_sitelib}/click_package/tests/integration/*.py
%dir %{python3_sitelib}/click_package/tests/integration/__pycache__
%{python3_sitelib}/click_package/tests/integration/__pycache__/*.pyc
%dir %{python3_sitelib}/click_package/tests/__pycache__
%{python3_sitelib}/click_package/tests/__pycache__/*.pyc
%dir %{python3_sitelib}/click_package/commands
%{python3_sitelib}/click_package/commands/*.py
%dir %{python3_sitelib}/click_package/commands/__pycache__
%{python3_sitelib}/click_package/commands/__pycache__/*.pyc
%dir %{python3_sitelib}/click_package/__pycache__
%{python3_sitelib}/click_package/__pycache__/*.pyc
%dir %{python3_sitelib}/click-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/click-%{version}-py%{python3_version}.egg-info/*.txt
%{python3_sitelib}/click-%{version}-py%{python3_version}.egg-info/PKG-INFO

%files doc
%{_mandir}/man1/click.1.gz
%dir %_pkgdocdir
%_pkgdocdir/README
%dir %_pkgdocdir/html
%_pkgdocdir/html/*.html
%_pkgdocdir/html/.buildinfo
%_pkgdocdir/html/*inv
%_pkgdocdir/html/*.js
%dir %_pkgdocdir/html/_sources
%_pkgdocdir/html/_sources/*.txt
%dir %_pkgdocdir/html/_static
%_pkgdocdir/html/_static/*.png
%_pkgdocdir/html/_static/*.css
%_pkgdocdir/html/_static/*.js

%changelog
%autochangelog
