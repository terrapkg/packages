%global appid sh.oven.Bun
# Bun REQUIRES Clang, it uses flags GCC cannot support such as -glldb
%global toolchain clang
%if 0%{?fedora} >= 42
%global llvm_major 20
%global __cc clang-%{llvm_major}
%global __cxx clang++-%{llvm_major}
%global __cpp clang-cpp-%{llvm_major}
%endif
%global zig_version 0.15.2
# We love programs with multiple levels of bootstrapping
%bcond bootstrap 1
%bcond webkit 1
%bcond self_build %{without bootstrap}

Name:			bun
Version:		1.3.5
Release:		2%?dist
Summary:		Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one
License:		MIT
URL:			https://bun.sh
Source0:        https://github.com/oven-sh/bun/archive/refs/tags/%{name}-v%{version}.tar.gz
Source1:        sh.oven.Bun.metainfo.xml
Patch0:         bun-fix-webkit-include-paths.patch
BuildRequires:  anda-srpm-macros
%if %{with self_build}
BuildRequires:  bun
%endif
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  ccache
BuildRequires:  clang%{?llvm_major}
BuildRequires:	cmake
BuildRequires:  cmake-rpm-macros
%if %{with webkit}
BuildRequires:  git-core
%endif
BuildRequires:  golang
BuildRequires:  glibc-common
BuildRequires:  glibc-devel
BuildRequires:  libatomic-static
BuildRequires:  libicu-devel
BuildRequires:  libdeflate-devel
BuildRequires:  libstdc++-static
BuildRequires:  libtool
BuildRequires:  lld%{?llvm_major}
BuildRequires:  llvm%{?llvm_major}
BuildRequires:  mold
BuildRequires:  ninja-build
BuildRequires:  nodejs
BuildRequires:  pkg-config
%if %{with webkit}
BuildRequires:  perl(English)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Math::BigInt::Trace)
%endif
BuildRequires:  perl(Math::BigInt)
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  ruby
BuildRequires:  ruby-bundled-gems
BuildRequires:  sed
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
Obsoletes:      bun-bin <= 1.3.5

%description
%summary.

%package        doc
Summary:        Doc files for Bun.

%description    doc
Documentation for Bun.

%pkg_completion -bfz bun

%prep
%autosetup -p1 -n %{name}-%{name}-v%{version}
%cargo_prep_online

%if %{with webkit}
git clone -c advice.detachedHead=false --recurse-submodules %{?_smp_mflags} https://github.com/oven-sh/WebKit.git vendor/WebKit --depth 1 -b autobuild-$(grep -Eom1 [a-f0-9]{40} cmake/tools/SetupWebKit.cmake)
%endif

%build
#CXXFLAGS="-Wno-unused-result ${CXXFLAGS}"
#export CFLAGS="-Wno-unused-command-line-argument -I%{_includedir}/pthread.h"
#export CXXFLAGS="-Wno-unused-command-line-argument -Wno-unused-result -Wno-missing-braces -Wno-reorder-ctor -Wno-unused-variable -Wno-unused-function -Wno-logical-op-parentheses -Wno-overloaded-virtual -fno-c++-static-destructors -include %{_includedir}/c++/*/cstdint"

%if %{with bootstrap}
%set_node_build_flags
%endif

# Force build Cargo config
export CARGO_HOME="%{_cargo_home}"

%if %{defined llvm_major}
export LLVM_DIR=%{_libdir}/llvm%{?llvm_major}/%{_lib}/cmake
%endif

%if %{with webkit}
pushd vendor/WebKit

%cmake \
  -DCMAKE_BUILD_TYPE="Release" \
  -Wno-dev \
  -DPORT="JSCOnly" \
  -DENABLE_STATIC_JSC="ON" \
  -DALLOW_LINE_AND_COLUMN_NUMBER_IN_BUILTINS="ON" \
  -DUSE_THIN_ARCHIVES="OFF" \
  -DUSE_BUN_JSC_ADDITIONS="ON" \
  -DUSE_BUN_EVENT_LOOP="ON" \
  -DENABLE_FTL_JIT="ON" \
  -DALLOW_LINE_AND_COLUMN_NUMBER_IN_BUILTINS="ON" \
  -DJSEXPORT_PRIVATE="WTF_EXPORT_DECLARATION" \
  -DUSE_VISIBILITY_ATTRIBUTE="1" \
  -DENABLE_REMOTE_INSPECTOR="ON" \
  -DCMAKE_C_FLAGS="$CFLAGS" \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS -fno-c++-static-destructors" \
  -DCMAKE_C_COMPILER="$CC" \
  -DCMAKE_CXX_COMPILER="$CXX" \
  -DCMAKE_LINKER="ld.lld%{?llvm_major:-%{llvm_major}}" \
  -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS -fuse-ld=lld%{?llvm_major:-%{llvm_major}}" \
  -DBUILD_SHARED_LIBS:BOOL="OFF"
%cmake_build --target jsc

rm %{__cmake_builddir}/JavaScriptCore/DerivedSources/inspector/InspectorProtocolObjects.h

# Link system ICU libs
ln -s %{_libdir}/libicudata.so.77.1 %{__cmake_builddir}/lib/libicudata.a
ln -s %{_libdir}/libicui18n.so.77.1 %{__cmake_builddir}/lib/libicui18n.a
ln -s %{_libdir}/libicuuc.so.77.1 %{__cmake_builddir}/lib/libicuuc.a

popd
%endif

# Use system Zig if it is new enough
%if %["%{zig_version}" >= "0.15.2"]
rm -rf vendor/zig
mkdir -p vendor/zig
ln -sf /usr/lib/zig vendor/zig/lib
ln -sf /usr/bin/zig vendor/zig/zig
%else
%cmake \

%endif

%{!?with_bootstrap:%{?with_self_build:%{__bun}}}%{?with_bootstrap:%{__yarn_dlx} bun} ./scripts/glob-sources.mjs

%cmake \
  -DCMAKE_BUILD_TYPE="Release" \
  -DUSE_STATIC_LIBATOMIC="OFF" \
  -DENABLE_CCACHE="ON" \
  -DENABLE_LTO="ON" \
  -DUSE_STATIC_SQLITE="OFF" \
%ifnarch x86_64_v3 x86_64_v4
  -DENABLE_BASELINE="ON" \
%endif
  -DCMAKE_C_FLAGS="$CFLAGS" \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
  -DCMAKE_C_COMPILER="$CC" \
  -DCMAKE_CXX_COMPILER="$CXX" \
  -DCMAKE_LINKER="ld.lld%{?llvm_major:-%{llvm_major}}" \
  -DCMAKE_EXE_LINKER_FLAGS="$LDFLAGS -fuse-ld=lld%{?llvm_major:-%{llvm_major}}" \
  -DCMAKE_AR="/usr/bin/llvm-ar%{?llvm_major:-%{llvm_major}}" \
  -DLLD_PROGRAM="ld.lld%{?llvm_major:-%{llvm_major}}" \
  -DUSE_STATIC_SQLITE="OFF" \
  -DALWAYS_RUN \
%if %["%{zig version}" >= "0.15.2"]
  -DZIG_PATH="/usr/bin/zig" \
%endif
  -DBUILD_SHARED_LIBS:BOOL="OFF" \
%if %{with webkit}
  -DWEBKIT_LOCAL="ON" \
  -DWEBKIT_PATH="$PWD/vendor/WebKit/%{__cmake_builddir}"
%endif

%cmake_build --target %{name}

%install
%cmake_install

%terra_appstream -o %{SOURCE1}

%files
%doc README.md
%license LICENSE
%{_bindir}/bun
%{_bindir}/bunx
%{_datadir}/metainfo/sh.oven.Bun.metainfo.xml

%files doc
%doc docs/*
