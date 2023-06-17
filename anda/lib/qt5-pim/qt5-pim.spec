Name:    qt5-pim
Summary: Qt5 PIM Framework
Version: 5.15
Release: %autorelease

License: GPL-3.0
URL:     https://invent.kde.org/qt/qt/qtpim
Source0: %{url}/-/archive/kde/5.15/qtpim-kde-%{version}.tar.gz
Source1: https://salsa.debian.org/qt-kde-team/qt/qtpim/-/archive/5.15/qtpim-master.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: pkgconfig(QtCore)
BuildRequires: perl
BuildRequires: qt5-doctools
BuildRequires: qt5-rpm-macros

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
Qt Mobility Project delivers a set of new APIs to Qt with features that are well
known from the mobile device world, in particular phones. However, these APIs
allow the developer to use these features with ease from one framework and apply
them to phones, netbooks and non-mobile personal computers. The framework not
only improves many aspects of a mobile experience, because it improves the use
of these technologies, but has applicability beyond the mobile device arena.

%package devel
Summary: Qt Mobility Framework development files
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
%autosetup -n qtpim-kde-%{version}
tar -xf '%{SOURCE1}'
for i in qtpim-master/debian/patches/*.patch; do patch -p1 < $i; done

%build
PATH=%{_qt5_bindir}:$PATH; export PATH
# Build headers manually
cd src/contacts/ && perl /usr/bin/syncqt.pl -copy -module QtContacts -version 5.4.0 -outdir ../../redhat-linux-build -builddir ./ ./
cd ../
cd organizer/ && perl /usr/bin/syncqt.pl -copy -module QtOrganizer -version 5.4.0 -outdir ../../redhat-linux-build -builddir ./ ./
cd ../
cd versit/ && perl /usr/bin/syncqt.pl -copy -module QtVersit -version 5.4.0 -outdir ../../redhat-linux-build -builddir ./ ./
cd ../
cd versitorganizer/ && perl /usr/bin/syncqt.pl -copy -module QtVersitOrganizer -version 5.4.0 -outdir ../../redhat-linux-build -builddir ./ ./
cd ../../

# For building
cd ./redhat-linux-build/include/QtContacts
ln -s 5.4.0/QtContacts/private
cd ../QtOrganizer
ln -s 5.4.0/QtOrganizer/private
cd ../QtVersit
ln -s 5.4.0/QtVersit/private
cd ../QtVersitOrganizer
ln -s 5.4.0/QtVersitOrganizer/private
cd ../../../

cd ./redhat-linux-build
qmake-qt5 ..

%make_build
%make_build docs

%install
cd ./redhat-linux-build
%make_install INSTALL_ROOT=%{buildroot}

# manually install docs
mkdir -p %{buildroot}%{_qt5_docdir}/html/ %{buildroot}%{_qt5_docdir}/qch/
mv doc/*.qch %{buildroot}%{_qt5_docdir}/qch/
cp -a doc/* %{buildroot}%{_qt5_docdir}/html/

cp -a ./include/* %{buildroot}%{_qt5_includedir}

%files
%license LICENSE.GPL2 LICENSE.GPL3 LICENSE.GPL3-EXCEPT
%{_libdir}/libQt5Contacts.so.*
%{_libdir}/libQt5Organizer.so.*
%{_libdir}/libQt5Versit.so.*
%{_libdir}/libQt5VersitOrganizer.so.*
%dir %{_qt5_qmldir}/QtContacts
%{_qt5_qmldir}/QtContacts/*.so
%{_qt5_qmldir}/QtContacts/qmldir
%{_qt5_qmldir}/QtContacts/*.qmltypes
%dir %{_qt5_qmldir}/QtOrganizer
%{_qt5_qmldir}/QtOrganizer/*.so
%{_qt5_qmldir}/QtOrganizer/qmldir
%{_qt5_qmldir}/QtOrganizer/*.qmltypes
%dir %{_qt5_plugindir}/contacts
%{_qt5_plugindir}/contacts/*.so
%dir %{_qt5_plugindir}/organizer
%{_qt5_plugindir}/organizer/*.so
%dir %{_qt5_plugindir}/versit
%{_qt5_plugindir}/versit/*.so

%files devel
%license LICENSE.GPL2 LICENSE.GPL3 LICENSE.GPL3-EXCEPT
%{_libdir}/*.prl
%{_libdir}/libQt5Contacts.so
%{_libdir}/libQt5Organizer.so
%{_libdir}/libQt5Versit.so
%{_libdir}/libQt5VersitOrganizer.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/cmake/Qt5Contacts
%{_libdir}/cmake/Qt5Contacts/*.cmake
%dir %{_libdir}/cmake/Qt5Organizer
%{_libdir}/cmake/Qt5Organizer/*.cmake
%dir %{_libdir}/cmake/Qt5Versit
%{_libdir}/cmake/Qt5Versit/*.cmake
%dir %{_libdir}/cmake/Qt5VersitOrganizer
%{_libdir}/cmake/Qt5VersitOrganizer/*.cmake
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_qt5_includedir}/QtContacts/
%{_qt5_includedir}/QtOrganizer/
%{_qt5_includedir}/QtVersit/
%{_qt5_includedir}/QtVersitOrganizer/

%files doc
%license LICENSE.FDL
%{_qt5_docdir}/qch/*.qch
%{_qt5_docdir}/html/qtcontacts/
%{_qt5_docdir}/html/qtorganizer/
%{_qt5_docdir}/html/qtversit/

%files examples
%dir %{_qt5_examplesdir}/contacts
%{_qt5_examplesdir}/contacts/*.pro
%{_qt5_examplesdir}/organizer/

%changelog
%autochangelog
