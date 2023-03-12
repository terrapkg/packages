# forgemeta does not work
%global commit e3332ee38d27a134cef6621fdaf36687af1b6f4a

Name:    qt5-qtsystems
Summary: Qt5 Mobility Framework
Version: 5.15
Release: %autorelease

License: GPLv3
URL:     https://invent.kde.org/qt/qt/qtsystems
Source0: %{url}/-/archive/%commit/qt5-mobility-%commit.tar.gz
Source1: https://salsa.debian.org/qt-kde-team/qt/qtsystems/-/archive/master/qtsystems-master.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtDeclarative)
BuildRequires: pkgconfig(QtGui) pkgconfig(QtOpenGL)
BuildRequires: pkgconfig(QtNetwork) >= 4.7
BuildRequires: pkgconfig(xv)
BuildRequires: pkgconfig(QtDBus)
BuildRequires: qt5-doctools
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-rpm-macros
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtbase

Provides: %{name}-bearer = %{version}-%{release}
Provides: %{name}-connectivity = %{version}-%{release}
Provides: %{name}-contacts = %{version}-%{release}
Provides: %{name}-feedback = %{version}-%{release}
Provides: %{name}-gallery = %{version}-%{release}
Provides: %{name}-location = %{version}-%{release}
Provides: %{name}-multimediakit = %{version}-%{release}
Provides: %{name}-organizer = %{version}-%{release}
Provides: %{name}-publishsubscribe = %{version}-%{release}
Provides: %{name}-sensors = %{version}-%{release}
Provides: %{name}-serviceframework = %{version}-%{release}
Provides: %{name}-systeminfo = %{version}-%{release}
Provides: %{name}-versit = %{version}-%{release}

%description
Qt5 Mobility Project delivers a set of new APIs to Qt with features that are well
known from the mobile device world, in particular phones. However, these APIs
allow the developer to use these features with ease from one framework and apply
them to phones, netbooks and non-mobile personal computers. The framework not
only improves many aspects of a mobile experience, because it improves the use
of these technologies, but has applicability beyond the mobile device arena.

%package devel
Summary: Qt5 Mobility Framework development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel
Provides: %{name}-bearer-devel = %{version}-%{release}
Provides: %{name}-connectivity-devel = %{version}-%{release}
Provides: %{name}-contacts-devel = %{version}-%{release}
Provides: %{name}-feedback-devel = %{version}-%{release}
Provides: %{name}-gallery-devel = %{version}-%{release}
Provides: %{name}-location-devel = %{version}-%{release}
Provides: %{name}-multimediakit-devel = %{version}-%{release}
Provides: %{name}-organizer-devel = %{version}-%{release}
Provides: %{name}-publishsubscribe-devel = %{version}-%{release}
Provides: %{name}-sensors-devel = %{version}-%{release}
Provides: %{name}-serviceframework-devel = %{version}-%{release}
Provides: %{name}-systeminfo-devel = %{version}-%{release}
Provides: %{name}-versit-devel = %{version}-%{release}
%description devel
%{summary}.

%package doc
Summary: API documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.

%package examples
Summary: Example files for %{name}
Requires: %{name}-devel
%description examples
%{summary}.

%prep
%autosetup -n qtsystems-%commit
tar -xf '%{SOURCE1}'
for i in qtsystems-master/debian/patches/*.patch; do patch -p1 < $i; done

%build
# Build headers manually
cd src/systeminfo/ && perl /usr/bin/syncqt.pl -copy -module QtSystemInfo -version 5.4.0 -outdir ../../redhat-linux-build -builddir ./ ./
cd ../
cd publishsubscribe/ && perl /usr/bin/syncqt.pl -copy -module QtPublishSubscribe -version 5.4.0 -outdir ../../redhat-linux-build -builddir ./ ./
cd ../
cd serviceframework/ && perl /usr/bin/syncqt.pl -copy -module QtServiceFramework -version 5.4.0 -outdir ../../redhat-linux-build -builddir ./ ./
cd ../../

# For building
cd ./redhat-linux-build/include/QtPublishSubscribe
ln -s 5.4.0/QtPublishSubscribe/private
cd ../QtServiceFramework
ln -s 5.4.0/QtServiceFramework/private
cd ../QtSystemInfo
ln -s 5.4.0/QtSystemInfo/private
cd ../../../

cd ./redhat-linux-build
%qmake_qt5 ..

%make_build
%make_build docs

%install
cd ./redhat-linux-build
%make_install INSTALL_ROOT=%{buildroot}

# manually install docs
mkdir -p %{buildroot}%{_qt5_docdir}/html/ %{buildroot}%{_qt5_docdir}/qch/
mv doc/*.qch %{buildroot}%{_qt5_docdir}/qch/
cp -a doc/* %{buildroot}%{_qt5_docdir}/html/

# Is not needed/out of source
rm -f %{buildroot}%{_qt5_examplesdir}/examples.pro

# manually install headers
cp -a ./include/* %{buildroot}%{_qt5_includedir}

%files
%license LICENSE.GPL2 LICENSE.GPL3 LICENSE.GPL3-EXCEPT
%{_libdir}/libQt5PublishSubscribe.so.*
%{_libdir}/libQt5ServiceFramework.so.*
%{_libdir}/libQt5SystemInfo.so.*
%{_qt5_bindir}/servicefw
%{_qt5_bindir}/sfwlisten
%dir %{_qt5_qmldir}/QtPublishSubscribe
%{_qt5_qmldir}/QtPublishSubscribe/*.so
%{_qt5_qmldir}/QtPublishSubscribe/qmldir
%{_qt5_qmldir}/QtPublishSubscribe/*.qmltypes
%dir %{_qt5_qmldir}/QtServiceFramework
%{_qt5_qmldir}/QtServiceFramework/*.so
%{_qt5_qmldir}/QtServiceFramework/qmldir
%{_qt5_qmldir}/QtServiceFramework/*.qmltypes
%dir %{_qt5_qmldir}/QtSystemInfo
%{_qt5_qmldir}/QtSystemInfo/*.so
%{_qt5_qmldir}/QtSystemInfo/qmldir
%{_qt5_qmldir}/QtSystemInfo/*.qmltypes

%files devel
%license LICENSE.GPL2 LICENSE.GPL3 LICENSE.GPL3-EXCEPT
%{_libdir}/*.prl
%{_libdir}/libQt5PublishSubscribe.so
%{_libdir}/libQt5ServiceFramework.so
%{_libdir}/libQt5SystemInfo.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/cmake/Qt5PublishSubscribe
%{_libdir}/cmake/Qt5PublishSubscribe/*.cmake
%dir %{_libdir}/cmake/Qt5ServiceFramework
%{_libdir}/cmake/Qt5ServiceFramework/*.cmake
%dir %{_libdir}/cmake/Qt5SystemInfo
%{_libdir}/cmake/Qt5SystemInfo/*.cmake
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_qt5_includedir}/QtPublishSubscribe/
%{_qt5_includedir}/QtServiceFramework/
%{_qt5_includedir}/QtSystemInfo/

%files doc
%license LICENSE.FDL
%{_qt5_docdir}/qch/*.qch
%{_qt5_docdir}/html/qtpublishsubscribe/
%{_qt5_docdir}/html/qtserviceframework/
%{_qt5_docdir}/html/qtsysteminfo/

%files examples
%dir %{_qt5_examplesdir}/systeminfo
%{_qt5_examplesdir}/systeminfo/*.pro
%{_qt5_examplesdir}/systeminfo/inputinfo/
%{_qt5_examplesdir}/systeminfo/qml-battery/
%{_qt5_examplesdir}/systeminfo/qml-deviceinfo/
%{_qt5_examplesdir}/systeminfo/qml-inputinfo/

%changelog
%autochangelog
