# Despite supposedly being a purely C++ project it will not build without this flag. Don't ask me.
%global build_cflags %{__build_flags_lang_c} %{?_distro_extra_cflags} -Wno-implicit-function-declaration
%global build_cxxflags %(%{__build_flags_lang_cxx}) %{?_distro_extra_cxxflags} -Wno-template-body

Name:          epsonscan2
Version:       6.7.70.0
Release:       1
Summary:       Package for Epson scanner drivers and software
# This was a licensing determination nightmare
License:       LGPL-2.1-or-later AND MIT AND Zlib AND LicenseRef-SHA1
URL:           https://support.epson.net/linux/en/epsonscan2.php
# This software doesn't have versioned download links, absolute nightmare
Source0:       https://download3.ebz.epson.net/dsc/f/03/00/16/60/70/c7fc14e41ec84255008c6125b63bcac40f55e11c/epsonscan2-%{version}-%{release}.src.tar.gz
# The non-free-plugin should be redistributable as far as anything I can find in the license but it is NOT provided externally?? Repackage the RPM I guess.
%ifarch x86_64
Source1:       https://download3.ebz.epson.net/dsc/f/03/00/16/14/40/9cb99579f9fa7facf54f77f0ce6fe5600677f30a/epsonscan2-bundle-%{version}.x86_64.rpm.tar.gz
%endif
BuildRequires: boost-filesystem >= 1.36.0
BuildRequires: boost-devel >= 1.36.0
BuildRequires: cmake >= 2.8.12.2
BuildRequires: cpio
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
Requires:     %{name} = %{version}-%{release}

%description non-free-plugin
Non-free but redistributable plugin for %{name}.
%endif

%prep
%autosetup -n %{name}-%{version}-%{release}
%ifarch x86_64
gzip -dc '%{SOURCE1}' | tar -xof - --strip-components=1
rpm2cpio plugins/*.rpm | cpio -idmv
%endif

%build
# CMake macro fails to generate the build files somehow? This works however. I don't really understand.
cmake . \
   -DBUILD_TYPE=Release

%make_build

%install
%make_install

# The Makefile fails to do these steps correctly but just using CMake was even more problematic.
# The file is also very annoying to patch. Thank God this doesn't seem to update anymore.
mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}/lib/udev/rules.d/60-%{name}.rules -t %{buildroot}%{_udevrulesdir}
install -Dpm644 desktop/rpm/x86_64/%{name}.desktop -t %{buildroot}%{_datadir}/applications/

mkdir -p %{buildroot}%{_libdir}/sane
ln -sf ../%{name}/libsane-%{name}.so %{buildroot}%{_libdir}/sane/libsane-%{name}.so.1
ln -sf ../%{name}/libsane-%{name}.so %{buildroot}%{_libdir}/sane/libsane-%{name}.so.1.0.0

# Let RPM handle the doc files. This project's build incorrectly puts licenses in this folder.
rm -rf %{buildroot}%{_defaultdocdir}/%{name}*

%ifarch x86_64
mv usr/share/doc/%{name}*/* -t plugins
rm -rf usr/share/doc/%{name}*
cp -pr usr %{buildroot}
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
%{_datadir}/applications/%{name}.desktop

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
