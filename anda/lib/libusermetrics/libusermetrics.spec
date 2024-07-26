Name:       libusermetrics
Version:    1.3.2
Release:    1%?dist
Summary:    library for retrieving anonymous metrics about users
License:    GPLv3 AND LGPLv3 AND LGPLv2
URL:        https://gitlab.com/ubports/development/core/libusermetrics
Source0:    %url/-/archive/%version/libusermetrics-%version.tar.gz

BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtxmlpatterns-devel
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(click-0.4)
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libapparmor)
BuildRequires: qdjango-devel


%description
library for retrieving anonymous metrics about users
This package contains shared libraries to be used by applications.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documenation for %{name}
BuildArch: noarch

%description doc
The %{name}-doc contains documentation for %{name}.

%prep
%autosetup -n libusermetrics-%version

%build
%cmake -DENABLE_TESTS=ON
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog
%license LGPL_EXCEPTION.txt LICENSE.GPL LICENSE.LGPL LICENSE.LGPL-3
/usr/etc/dbus-1/system.d/com.lomiri.UserMetrics.conf
%{_bindir}/usermetricsinput
%{_bindir}/usermetricsinput-increment
%{_libdir}/libusermetricsinput.so.*
%{_libdir}/libusermetricsoutput.so.*
%dir %{_qt5_qmldir}/UserMetrics
%{_qt5_qmldir}/UserMetrics/libusermetrics-qml.so
%{_qt5_qmldir}/UserMetrics/qmldir
%dir %{_libexecdir}/libusermetrics
%{_libexecdir}/libusermetrics/usermetricsservice
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system-services/com.lomiri.UserMetrics.service
%{_datadir}/glib-2.0/schemas/com.lomiri.UserMetrics.gschema.xml
%dir %{_datadir}/libusermetrics
%dir %{_datadir}/libusermetrics/themes
%{_datadir}/libusermetrics/themes/color-theme.xsd
%{_datadir}/libusermetrics/themes/default.xml

%files devel
%dir %{_includedir}/libusermetrics-1
%dir %{_includedir}/libusermetrics-1/libusermetricsinput
%{_includedir}/libusermetrics-1/libusermetricsinput/*.h
%dir %{_includedir}/libusermetrics-1/libusermetricsoutput
%{_includedir}/libusermetrics-1/libusermetricsoutput/*.h
%{_libdir}/libusermetricsinput.so
%{_libdir}/libusermetricsoutput.so
%{_libdir}/pkgconfig/libusermetricsinput-1.pc
%{_libdir}/pkgconfig/libusermetricsoutput-1.pc

%files doc
%dir %{_docdir}/libusermetrics-doc
%{_docdir}/libusermetrics-doc/html/
%{_docdir}/libusermetrics-doc/xml/

%changelog
%autochangelog
