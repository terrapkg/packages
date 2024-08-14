%global forgeurl https://gitlab.com/ubports/development/core/lomiri-download-manager
%global commit 682c4928a91da598767e0be2496d9c35af7db035
%forgemeta

Name:       lomiri-download-manager
Version:    0.1.3
Release:    1%?dist
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
BuildRequires: pkgconfig(systemd)
BuildRequires: fdupes

%description
Upload Download Manager performs uploads and downloads from a centralized
location.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %name-devel package contains libraries and header files
for developing applications that use %{name}.

%package doc
Summary: Documentation files for %{name}
BuildArch: noarch

%description doc
The %name-doc package contains documentation for
%{name}-devel.

%prep
%autosetup -n lomiri-download-manager-%commit
sed -e "s/-Werror//g" -i CMakeLists.txt

%build
%cmake -DCMAKE_INSTALL_LIBEXECDIR=%{_libdir} -DENABLE_UBUNTU_COMPAT=ON
%cmake_build

%install
%cmake_install
%fdupes %buildroot%_docdir/%name/cpp/html/
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%config /usr/etc/dbus-1/system.d/*.conf
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
%{_mandir}/man1/*.gz

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
