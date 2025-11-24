%global appid sh.oven.bun
# Currently unused but here in case it is needed in the future
%if 0%{?fedora} >= 45
%global llvm_major 21
%endif
%global zig_version 0.14.1
%bcond bootstrap 1

Name:			bun
Version:		1.3.3
Release:		2%?dist
Summary:		Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one
License:		MIT
URL:			https://bun.sh
Source0:        https://github.com/oven-sh/bun/archive/refs/tags/%{name}-v%{version}.tar.gz
Patch0:         BuildBrotli.patch
BuildRequires:  anda-srpm-macros
%if %{without bootstrap}
BuildRequires:  bun
%endif
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  ccache
BuildRequires:  clang%{?llvm_major}
BuildRequires:	cmake
BuildRequires:  cmake-rpm-macros
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glibc-common
BuildRequires:  libicu-devel
BuildRequires:  libdeflate-devel
BuildRequires:  libtool
BuildRequires:  lld%{?llvm_major}
BuildRequires:  llvm%{?llvm_major}
BuildRequires:  mold
BuildRequires:  ninja-build
BuildRequires:  nodejs
BuildRequires:  pkg-config
BuildRequires:  perl(Math::BigInt)
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  ruby
BuildRequires:  ruby-bundled-gems
BuildRequires:  unzip
%if %{with bootstrap}
BuildRequires:  yarnpkg-berry
%endif
BuildRequires:  zig
Requires:       c-ares
Requires:       libarchive
Requires:       libuv
Requires:       mimalloc
Requires:       (zlib-ng-compat or zlib)
Requires:       zstd
Obsoletes:      bun-bin < 1.3.3

%description
%summary.

%package        doc
Summary:        Doc files for Bun.

%description    doc
Documentation for Bun.

%pkg_completion -bfz bun

%prep
%autosetup -p1 -n %{name}-%{name}-v%{version}

#for dir in packages/bun-build-mdx-rs packages/bun-native-plugin-rs bench/ffi/src packages/bun-native-plugin-rs/bun-macro; do
#pushd $dir
%dnl %cargo_prep_online
#popd
#done

%build
CXXFLAGS="-Wno-unused-result ${CXXFLAGS}"
%set_build_flags

mkdir -p %{__cmake_builddir}
# Bun build must be bootstrapped by another build system or itself
# Bun also REQUIRES Clang, it uses flags GCC cannot support such as -glldb
BUN_HOME=%{rpmbuilddir}/.bun %{!?with_bootstrap:%{__bun}}%{?with_bootstrap:BUN_RUNTIME_TRANSPILER_CACHE_PATH=0 %{__yarn} dlx bun} \
 ./scripts/build.mjs -GNinja -B %{__cmake_builddir} \
  -DCMAKE_BUILD_TYPE=Release \
  -DUSE_STATIC_LIBATOMIC=OFF \
  -DENABLE_CCACHE=ON \
  -DENABLE_LTO=ON \
  -DUSE_STATIC_SQLITE=OFF \
%ifnarch x86_64_v3 x86_64_v4
  -DENABLE_BASELINE=ON \
%endif
  -DCMAKE_C_FLAGS="$CFLAGS" \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
  -DCMAKE_C_COMPILER=clang%{?llvm_major:-%{llvm-major}} \
  -DCMAKE_CXX_COMPILER=clang++%{?llvm_major:-%{llvm-major}} \
  -DLLD_PROGRAM="ld.lld%{?llvm_major:-%{llvm-major}}" \
%if %{zig_version} >= 0.15.2
  -DZIG_PATH="/usr/bin/zig" \
%endif
  -DBUILD_SHARED_LIBS:BOOL=OFF

%install
%cmake_install

%terra_appstream -o %{SOURCE1}

%files
%doc README.md
%license LICENSE
%{_bindir}/bun
%{_bindir}/bunx
%{_datadir}/metainfo/sh.oven.bun.metainfo.xml

%files doc
%doc docs/*
