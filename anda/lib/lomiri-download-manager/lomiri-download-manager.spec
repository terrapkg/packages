%global forgeurl https://gitlab.com/ubports/development/core/lomiri-download-manager
%global commit 86d086292db613df0b0cbc5fc2cfcdc33c3315bb
%forgemeta

Name:       lomiri-download-manager
Version:    0.1.2
Release:    %autorelease
Summary:    Upload Download Manager for Lomiri
License:    LGPLv3
URL:        https://gitlab.com/ubports/development/core/lomiri-download-manager
Source0:    %{url}/-/archive/%commit/lomiri-download-manager-%commit.tar.gz

BuildRequires: systemd-rpm-macros
BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: qt5-doctools
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libglog)
BuildRequires: pkgconfig(liblomiri-api)

%description
Upload Download Manager performs uploads and downloads from a centralized
location.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation files for %{name}
BuildArch: noarch

%description doc
%{name}-doc contains documentation for %{name}-devel.

%prep
%autosetup -n lomiri-download-manager-%commit
sed -e "s/-Werror//g" -i CMakeLists.txt
sed -i 's/ -qt=qt5//' docs/qml/CMakeLists.txt

%build
%cmake -DCMAKE_INSTALL_LIBEXECDIR=%{_libdir} -DENABLE_UBUNTU_COMPAT=ON
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%{_sysconfdir}/dbus-1/system.d/*.conf
%{_bindir}/lomiri-*
%{_userunitdir}/*.service
%{_libdir}/liblomiri-download-manager-client.so.*
%{_libdir}/liblomiri-download-manager-common.so.*
%{_libdir}/liblomiri-upload-manager-common.so.*
%{_libdir}/libldm-common.so.*
%{_libdir}/libldm-priv-common.so.*
%dir %{_libdir}/lomiri-download-manager
%{_libdir}/lomiri-download-manager/ldm-extractor
%{_qt5_qmldir}/Lomiri/
%{_qt5_qmldir}/Ubuntu/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service

%files devel
%dir %{_includedir}/lomiri/download_manager
%{_includedir}/lomiri/download_manager/*.h
%dir %{_includedir}/lomiri/transfers
%{_includedir}/lomiri/transfers/*.h
%dir %{_includedir}/lomiri/transfers/errors
%{_includedir}/lomiri/transfers/errors/*.h
%dir %{_includedir}/lomiri/upload_manager
%{_includedir}/lomiri/upload_manager/*.h
%{_libdir}/liblomiri-download-manager-client.so
%{_libdir}/liblomiri-download-manager-common.so
%{_libdir}/liblomiri-upload-manager-common.so
%{_libdir}/libldm-common.so
%{_libdir}/libldm-priv-common.so
%{_libdir}/pkgconfig/*.pc

%files doc
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/cpp
%{_docdir}/%{name}/cpp/html/
%dir %{_docdir}/%{name}/qml
%{_docdir}/%{name}/qml/html/

%changelog
%autochangelog
