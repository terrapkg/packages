%global source_release 1

Name:          epsonscan2
Version:       6.7.82.0
Release:       1%{?dist}
Summary:       Package for Epson scanner drivers and software
# This was a licensing determination nightmare
License:       LGPL-2.1-or-later AND MIT AND Zlib AND LicenseRef-SHA1
URL:           https://support.epson.net/linux/en/epsonscan2.php
# This software doesn't have versioned download links, absolute nightmare
Source0:       https://download-center.epson.com/f/module/7406d656-d87b-43ae-8efe-16ab16c173c5/%{name}-%{version}-%{source_release}.src.tar.gz
# The non-free-plugin should be redistributable as far as anything I can find in the license but it is NOT provided externally?? Repackage the RPM I guess.
%ifarch x86_64
Source1:       https://download-center.epson.com/f/module/98aba4e9-dc75-4096-9607-be35b5107668/%{name}-bundle-%{version}.x86_64.rpm.tar.gz
%endif
Patch0:        https://aur.archlinux.org/cgit/aur.git/plain/0002-Fix-crash.patch?h=epsonscan2#0002-Fix-crash.patch
Patch1:        https://aur.archlinux.org/cgit/aur.git/plain/0003-Use-XDG-open-to-open-the-directory.patch?h=epsonscan2#0003-Use-XDG-open-to-open-the-directory.patch
Patch2:        https://aur.archlinux.org/cgit/aur.git/tree/0004-Fix-a-crash-on-an-OOB-container-access.patch?h=epsonscan2#0004-Fix-a-crash-on-an-OOB-container-access.patch
Patch3:        https://aur.archlinux.org/cgit/aur.git/plain/0005-Fix-folder-creation-crash.patch?h=epsonscan2#0005-Fix-folder-creation-crash.patch
BuildRequires: boost-filesystem >= 1.36.0
BuildRequires: boost-devel >= 1.36.0
BuildRequires: cmake >= 2.8.12.2
BuildRequires: cpio
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libharu
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: libsane-hpaio
BuildRequires: libtiff-devel
BuildRequires: libusbx-devel
BuildRequires: make
BuildRequires: qt-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qtsinglecoreapplication-qt5
BuildRequires: rapidjson-devel
BuildRequires: sane-backends-devel
BuildRequires: systemd-rpm-macros
Requires:      qt5-qtbase
Packager:      Gilver E. <rockgrub@disroot.org>

%description
This package contains all essential software to use Epson scanners.

%ifarch x86_64
%package      non-free-plugin
License:      Epson End User Software License Agreement
Summary:      Non free plugin for Epson scanners
Requires:     %{name} = %{evr}

%description non-free-plugin
Non-free but redistributable plugin for %{name}.
%endif

%prep
%autosetup -n %{name}-%{version}-%{source_release} -p1
%ifarch x86_64
gzip -dc '%{SOURCE1}' | tar -xof - --strip-components=1
rpm2cpio plugins/*.rpm | cpio -idmv
%endif

sed -i 's|/lib/udev|${CMAKE_INSTALL_PREFIX}/lib/udev|' CMakeLists.txt
sed -i '1 i #include "zlib.h"' src/CommonUtility/DbgLog.cpp
sed -i '/zlib/d' src/Controller/CMakeLists.txt

find . -type f -name CMakeLists.txt -exec sed -i '/BOOST_NO_CXX11_RVALUE_REFERENCES/d' {} \;

for file in Standalone/lastusedsettings.cpp Standalone/defaultsettings.cpp CommonUtility/ESCommonTypedef.h Controller/Src/KeysValues/Key.hpp Controller/Src/KeysValues/KeyMgr.hpp; do
  sed -i '/BOOST_NO_CXX11_RVALUE_REFERENCES/d' src/$file
done

sed -i '/#include/ i #include <cmath>' src/Controller/Src/Filter/GrayToMono.hpp

%build
%cmake  \
   -DBUILD_TYPE=Release \
   -DCMAKE_C_FLAGS="$CFLAGS -Wno-implicit-function-declaration" \
   -DCMAKE_CXX_FLAGS="$CXXFLAGS -Wno-template-body"
%cmake_build

%install
%cmake_install

# The CMakeLists.txt fails to do these steps correctly.
%desktop_file_install desktop/rpm/x86_64/%{name}.desktop

mkdir -p %{buildroot}%{_libdir}/sane
ln -sf ../%{name}/libsane-%{name}.so %{buildroot}%{_libdir}/sane/libsane-%{name}.so.1
ln -sf ../%{name}/libsane-%{name}.so %{buildroot}%{_libdir}/sane/libsane-%{name}.so.1.0.0

# Let RPM handle the doc files. This project's build incorrectly puts licenses in this folder.
rm -rf %{buildroot}%{_defaultdocdir}/%{name}*

%ifarch x86_64
mv usr/share/doc/%{name}*/* -t plugins
rm -rf usr/share/doc/%{name}*
cp -pr usr -t %{buildroot}
%endif

%files
%doc     changelog.Debian
%doc     NEWS
%doc     README
%license AUTHORS
%license COPYING
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/*.so*
%{_libdir}/%{name}/detectalert
%{_libdir}/%{name}/Resources
%{_libdir}/sane/*
%{_udevrulesdir}/60-%{name}.rules
%{_sysconfdir}/sane.d/dll.d/%{name}
%{_appsdir}/%{name}.desktop

%ifarch x86_64
%files   non-free-plugin
%doc     plugins/NEWS
%license plugins/COPYING.EPSON
%license plugins/copyright
%{_libdir}/%{name}/libexec
%{_libdir}/%{name}/non-free-exec
%{_libdir}/%{name}-ocr
%{_libexecdir}/%{name}-ocr
%{_datadir}/%{name}
%{_datadir}/%{name}-ocr
%endif

%changelog
* Thu May 1 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
