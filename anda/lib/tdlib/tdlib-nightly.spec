%global commit 91aa6c9e4d0774eabf4f8d7f3aa51239032059a6
%global ver 1.8.36
%global commit_date 20240219
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: tdlib-nightly
Version: %ver^%commit_date.%shortcommit
Release: 1%?dist
License: BSL-1.0
URL: https://github.com/tdlib/td
Summary: Cross-platform library for building Telegram clients
Source0: %url/archive/%commit/tdlib-%commit.tar.gz

BuildRequires: gperftools-devel
BuildRequires: openssl-devel
BuildRequires: ninja-build
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: cmake
BuildRequires: gcc

Provides: bundled(sqlite) = 3.31.0

%description
TDLib (Telegram Database library) is a cross-platform library for
building Telegram clients. It can be easily used from almost any
programming language.

%name tracks the latest version of TDLib on
https://github.com/tdlib/td and determines the latest version via
the CMakeLists.txt file.

%package devel
Summary: Development files for %name
Requires: %name%?_isa = %{?epoch:%epoch:}%version-%release
Provides: pkgconfig(tdjson) = %ver

%package static
Summary: Static libraries for %name
Requires: %name%?_isa = %{?epoch:%epoch:}%version-%release
Requires: %name-devel%?_isa = %{?epoch:%epoch:}%version-%release

%description devel
%summary.

%description static
%summary.

%prep
%autosetup -n td-%commit -p1
sed -e 's/"DEFAULT"/"PROFILE=SYSTEM"/g' -i tdnet/td/net/SslStream.cpp

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
    -DTD_ENABLE_JNI:BOOL=OFF \
    -DTD_ENABLE_DOTNET:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE_1_0.txt
%doc README.md CHANGELOG.md
%_libdir/libtd*.so.%ver

%files devel
%_includedir/td
%_libdir/libtd*.so
%_libdir/cmake/Td
%_libdir/pkgconfig/td*.pc

%files static
%_libdir/libtd*.a

%changelog
* Sun May 28 2023 windowsboy111 <windowsboy111@fyralabs.com> - 1.8.14^54b34e9180dabc017210ebe3995f01d0c2fbaef1-1
- Repackaged for Terra

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 15 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.8.0-1
- Version 1.8.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.7.0-4
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7.0-1
- Updated to version 1.7.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
