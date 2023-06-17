Name:       qofono
Summary:    A library of Qt5 bindings for ofono
Version:    0.120
Release:    %autorelease
License:    LGPLv2
URL:        https://github.com/sailfishos/libqofono
Source0:    %{url}/archive/refs/tags/%{version}.tar.gz
Source1:    https://gitlab.com/ubports/development/core/packaging/libqofono/-/archive/ubports/latest/libqofono-ubports-latest.tar.gz
Patch0:     https://sources.debian.org/data/main/libq/libqofono/0.120-1/debian/patches/1001_context-preferred.patch
Patch1:     https://sources.debian.org/data/main/libq/libqofono/0.120-1/debian/patches/1003_mtk_settings_binding.patch
Patch2:     https://sources.debian.org/data/main/libq/libqofono/0.120-1/debian/patches/2001_path-adjustments.patch
Patch3:     https://sources.debian.org/data/main/libq/libqofono/0.120-1/debian/patches/1004_desktop-file-fields.patch

BuildRequires:  qt5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Test)

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
This package contains Qt5 bindings for ofono cellular service
interfaces.

%package devel
Summary:    Development files for ofono Qt5 bindings
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development header files for the ofono Qt5 bindings.

%package tests
Summary:    Qml tests and examples for the ofono Qt5 bindings
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description tests
This package contains qml tests and examples for ofono Qt5 bindings.

%prep
sed -i 'sX$(dpkg-architecture -qDEB_HOST_MULTIARCH)/XX' '%{PATCH2}'
%autosetup -n libqofono-%{version} -p1

%build
export QT_SELECT=5
%qmake_qt5 "VERSION=$(sed 's/+.*//' <<<"%{version}")"
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README
%license COPYING
%{_libdir}/libqofono-qt5.so.*
%{_qt5_qmldir}/QOfono/

%files devel
%{_libdir}/libqofono-qt5.prl
%{_libdir}/libqofono-qt5.so
%{_libdir}/pkgconfig/qofono-qt5.pc
%dir %{_includedir}/qofono-qt5
%{_includedir}/qofono-qt5/*.h
%dir %{_includedir}/qofono-qt5/dbus
%{_includedir}/qofono-qt5/dbus/ofono*.xml
%{_qt5_datadir}/mkspecs/features/qofono-qt5.prf

%files tests
%dir %{_libexecdir}/libqofono-qt5
%{_libexecdir}/libqofono-qt5/tests/
%{_libexecdir}/libqofono-qt5/ofonotest
%dir %{_datadir}/libqofono-qt5
%dir %{_datadir}/libqofono-qt5/qml
%dir %{_datadir}/libqofono-qt5/qml/ofonotest
%{_datadir}/libqofono-qt5/qml/ofonotest/main.qml

%changelog
%autochangelog
