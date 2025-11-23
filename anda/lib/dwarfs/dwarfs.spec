%global _description %{expand:
The Deduplicating Warp-speed Advanced Read-only File System.

A fast high compression read-only file system for Linux and Windows.}

Name:          dwarfs
Version:       0.14.1
Release:       4%?dist
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

%package        bash-completion
Summary:        dwarfs Bash completion
Requires:       %{name}
Requires:       bash
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description    bash-completion
Bash shell completion for dwarfs.

%package        zsh-completion
Summary:        dwarfs Zsh completion
Requires:       %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description    zsh-completion
Zsh shell completion for dwarfs.

%prep
%autosetup

%build
%cmake -DWITH_TESTS=ON \
-DWITH_LIBDWARFS=ON \
-DWITH_TOOLS=ON \
-DWITH_FUSE_DRIVER=ON \
-DBUILD_SHARED_LIBS=ON \
-DWITH_MAN_OPTION=OFF \
-DCMAKE_INSTALL_SBINDIR=%(echo %{_sbindir} | sed 's|^/usr||') \
%ifarch aarch64
-DCMAKE_C_FLAGS="-fno-lto -fno-use-linker-plugin" \
-DCMAKE_CXX_FLAGS="-fno-lto -fno-use-linker-plugin" \
-DCMAKE_SHARED_LINKER_FLAGS="-fno-lto -fno-use-linker-plugin" \
%endif
%cmake_build

%install
%cmake_install

%files
%doc README.md
%doc CHANGES.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}ck
%{_bindir}/%{name}extract
%{_bindir}/mk%{name}
%{_sbindir}/mount.%{name}
%{_libdir}/lib%{name}_*.so.*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}ck.1*
%{_mandir}/man1/%{name}extract.1*
%{_mandir}/man1/mk%{name}.1*
%{_mandir}/man5/%{name}-format.5*
%{_mandir}/man7/%{name}-env.7*
%{_datadir}/applications/%{name}-mount-handler.desktop
%{_datadir}/mime/packages/%{name}.xml

%files devel
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/lib%{name}_*.so
%{_includedir}/%{name}/*.h
%{_includedir}/%{name}/*/*.h
%{_includedir}/%{name}/*/*/*.h

%files bash-completion
%{bash_completions_dir}/%{name}
%{bash_completions_dir}/%{name}ck
%{bash_completions_dir}/%{name}extract
%{bash_completions_dir}/mk%{name}

%files zsh-completion
%{zsh_completions_dir}/_%{name}
%{zsh_completions_dir}/_%{name}ck
%{zsh_completions_dir}/_%{name}extract
%{zsh_completions_dir}/_mk%{name}

%changelog
* Sat Nov 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Create shell completion subpackages

* Fri Nov 07 2025 A. Garcia <alberto@garcialnk.com>
- Fix up INSTALL_SBINDIR path with duplicated /usr
- Add missing installed files to the package

* Thu Mar 20 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
