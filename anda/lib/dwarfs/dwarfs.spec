%global _description %{expand:
The Deduplicating Warp-speed Advanced Read-only File System.

A fast high compression read-only file system for Linux and Windows.}

Name:          dwarfs
Version:       0.12.2
Release:       1%?dist
Summary:       A fast high compression read-only file system for Linux, Windows and macOS
License:       GPL-3.0-or-later
URL:           https://github.com/mhx/%{name}
Source0:       https://github.com/mhx/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires: binutils-devel
BuildRequires: bison
BuildRequires: boost-chrono
BuildRequires: boost-context
BuildRequires: boost-devel
BuildRequires: boost-filesystem
BuildRequires: boost-iostreams
BuildRequires: boost-program-options
BuildRequires: boost-regex
BuildRequires: boost-system
BuildRequires: boost-thread
BuildRequires: brotli-devel
BuildRequires: ccache
BuildRequires: clang
BuildRequires: cmake
BuildRequires: date-devel
BuildRequires: double-conversion-devel
BuildRequires: elfutils-devel
BuildRequires: file-devel
BuildRequires: flac-devel
BuildRequires: flex
BuildRequires: fmt-devel
BuildRequires: fuse3
BuildRequires: fuse3-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: glog-devel
BuildRequires: gmock-devel
BuildRequires: google-benchmark-devel
BuildRequires: gtest-devel 
BuildRequires: jemalloc-devel
BuildRequires: json-devel
BuildRequires: libacl-devel
BuildRequires: libarchive-devel
BuildRequires: libdwarf-devel
BuildRequires: libevent-devel
BuildRequires: libunwind-devel
BuildRequires: lz4-devel
BuildRequires: make
BuildRequires: ninja-build
BuildRequires: openssl-devel
BuildRequires: pkgconf
BuildRequires: range-v3-devel
BuildRequires: rubygem-ronn-ng
BuildRequires: utf8cpp-devel
BuildRequires: xxhash-devel
BuildRequires: xz-devel
Requires:      bzip2-libs
Requires:      gflags
Requires:      libattr
Requires:      libxml2
Requires:      libzstd
Requires:      zlib-ng-compat
Packager:      Gilver E. <rockgrub@disroot.org>

%description %_description

%package       devel
Summary:       Development files for DWARFS.
Requires:      %{name}

%description devel
This package contains the development files for DWARFS.

%prep
%autosetup

%build
%cmake -DWITH_TESTS=ON \
-DWITH_LIBDWARFS=ON \
-DWITH_TOOLS=ON \
-DWITH_FUSE_DRIVER=ON \
-DBUILD_SHARED_LIBS=ON \
-DWITH_MAN_OPTION=OFF \
-DCMAKE_INSTALL_SBINDIR=%{_sbindir} \
%cmake_build 
%ctest -j

%install
%cmake_install

%files
%doc README.md
%doc CHANGES.md
%license LICENSE
%{_bindir}/dwarfsck
%{_bindir}/dwarfsextract
%{_bindir}/mkdwarfs
%{_sbindir}/dwarfs
%{_sbindir}/mount.dwarfs
%{_libdir}/libdwarfs_*.so.*
%{_mandir}/man1/dwarfs.1*
%{_mandir}/man1/dwarfsck.1*
%{_mandir}/man1/dwarfsextract.1*
%{_mandir}/man1/mkdwarfs.1*
%{_mandir}/man5/dwarfs-format.5*

%files devel
%dir %{_libdir}/cmake/dwarfs
%{_libdir}/cmake/dwarfs/*.cmake
%{_libdir}/libdwarfs_*.so
%{_includedir}/dwarfs/*.h
%{_includedir}/dwarfs/*/*.h

%changelog
* Thu Mar 20 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
