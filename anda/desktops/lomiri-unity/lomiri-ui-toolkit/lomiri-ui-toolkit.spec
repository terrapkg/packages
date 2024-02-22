%global forgeurl https://gitlab.com/ubports/development/core/lomiri-ui-toolkit
%global commit 454d980c352f3cea725458ff8a3d04ae686d2a96
%forgemeta

Name:           lomiri-ui-toolkit
Version:        1.3.5012
Release:        1%{?dist}
Summary:        QML components to ease the creation of beautiful applications in QML for Lomiri

License:        LGPL-3.0
URL:            https://gitlab.com/ubports/development/core/lomiri-ui-toolkit
Source0:        %{url}/-/archive/%commit/lomiri-ui-toolkit-%commit.tar.gz
Patch0:         https://sources.debian.org/data/main/l/lomiri-ui-toolkit/1.3.5010%2Bdfsg-1/debian/patches/0002-fix-tests-on-qt-5.15.5.patch
Patch1:         https://sources.debian.org/data/main/l/lomiri-ui-toolkit/1.3.5010%2Bdfsg-1/debian/patches/2003_stop-using-Ubuntu-fonts.patch

BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: libXi-devel
BuildRequires: lttng-ust-devel
BuildRequires: qt5-doctools
BuildRequires: qt5-rpm-macros
BuildRequires: qt5-qtdeclarative
BuildRequires: qt5-qtbase-static
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtgraphicaleffects
BuildRequires: qt5-qtfeedback
BuildRequires: qt5-qtsystems-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-pim-devel
BuildRequires: python3-rpm-macros
BuildRequires: qt5-qtsvg-devel
BuildRequires: fdupes
Requires:      qt5-qtgraphicaleffects
Requires:      qt5-qtfeedback

%description
This project consists of a set of QML components to ease the creation of
beautiful applications in QML for Lomiri.
QML alone lacks built-in components for basic widgets like Button, Slider,
Scrollbar, etc, meaning a developer has to build them from scratch. This
toolkit aims to stop this duplication of work, supplying beautiful components
ready-made and with a clear and consistent API.
These components are fully themeable so the look and feel can be easily
customized. Resolution independence technology is built in so UIs are scaled
to best suit the display.

%package devel
Summary:  Lomiri-ui-toolkit development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files needed for lomiri-ui-toolkit.

%package -n python3-lomiriuitoolkit
Summary: Python3 files for Lomiri-ui-toolkit
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildArch: noarch

%description -n python3-lomiriuitoolkit
Python3 files for Lomiri-ui-toolkit.

%package doc
Summary: Documentation for Lomiri-ui-toolkit
BuildArch: noarch

%description doc
Documentation for Lomiri-ui-toolkit.

%package examples
Summary: Examples for Lomiri-ui-toolkit
Requires: %{name}%{?_isa} = %{version}-%{release}

%description examples
Examples for Lomiri-ui-toolkit.

%prep
%autosetup -n lomiri-ui-toolkit-%commit -p1

%build
%{qmake_qt5} 'CONFIG+=ubuntu-uitk-compat' 'CONFIG+=test'

%make_build

%install
%make_install INSTALL_ROOT=%{buildroot} STRIP=/bin/true
# Used by apicheck during tests only
rm -rf %{buildroot}%{_qt5_qmldir}/Extinct
%fdupes %buildroot%_libdir/qt5/qml/Lomiri/Components/
%fdupes %buildroot%_libdir/qt5/examples/%name/examples/

%find_lang %{name}
%find_lang %{name}-gallery

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_libdir}/libLomiriGestures.so.*
%{_libdir}/libLomiriMetrics.so.*
%{_libdir}/libLomiriToolkit.so.*
%dir %{_qt5_plugindir}/lomiri
%dir %{_qt5_plugindir}/lomiri/metrics
%{_qt5_plugindir}/lomiri/metrics/*.so
%dir %{_qt5_qmldir}/Lomiri
%{_qt5_qmldir}/Lomiri/Components/
%{_qt5_qmldir}/Lomiri/Layouts/
%{_qt5_qmldir}/Lomiri/Metrics/
%{_qt5_qmldir}/Lomiri/PerformanceMetrics/
%{_qt5_qmldir}/Lomiri/Test/
%dir %{_qt5_qmldir}/Ubuntu
%{_qt5_qmldir}/Ubuntu/Components/
%{_qt5_qmldir}/Ubuntu/Layouts/
%{_qt5_qmldir}/Ubuntu/Metrics/
%{_qt5_qmldir}/Ubuntu/PerformanceMetrics/
%{_qt5_qmldir}/Ubuntu/Test/

%files devel
%{_bindir}/lomiri-*
%{_libdir}/libLomiriGestures.so
%{_libdir}/libLomiriMetrics.so
%{_libdir}/libLomiriToolkit.so
%{_libdir}/*.prl
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/lomiri-ui-toolkit
%{_libdir}/lomiri-ui-toolkit/apicheck
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_qt5_includedir}/LomiriGestures/
%{_qt5_includedir}/LomiriMetrics/
%{_qt5_includedir}/LomiriToolkit/

%files -n python3-lomiriuitoolkit
%doc README.md
%dir %{python3_sitelib}/lomiriuitoolkit
%{python3_sitelib}/lomiriuitoolkit/*.py
%{python3_sitelib}/lomiriuitoolkit/_custom_proxy_objects/
%{python3_sitelib}/lomiriuitoolkit/__pycache__/
%{python3_sitelib}/lomiriuitoolkit/tests/

%files doc
%license COPYING.CC-BY-SA-3.0
%{_qt5_docdir}/*.qch
%{_datadir}/doc/lomiri-ui-toolkit/

%files examples -f %{name}-gallery.lang
%dir %{_qt5_examplesdir}/lomiri-ui-toolkit
%dir %{_qt5_examplesdir}/lomiri-ui-toolkit/examples
%{_qt5_examplesdir}/lomiri-ui-toolkit/examples/calculator/
%{_qt5_examplesdir}/lomiri-ui-toolkit/examples/customtheme/
%{_qt5_examplesdir}/lomiri-ui-toolkit/examples/jokes/
%{_qt5_examplesdir}/lomiri-ui-toolkit/examples/locale/
%{_qt5_examplesdir}/lomiri-ui-toolkit/examples/lomiri-ui-toolkit-gallery/
%{_qt5_examplesdir}/lomiri-ui-toolkit/examples/unit-converter/

%changelog
%autochangelog
