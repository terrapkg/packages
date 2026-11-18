%global ver 0.0.17-beta-release
%bcond test 1
%bcond sqlite 1

Name:          holyc
Version:       0.0.17~beta
Release:       2%{?dist}
Summary:       HolyC compiler and transpiler
License:       BSD-2-Clause
URL:           https://holyc-lang.com
Source0:       https://github.com/Jamesbarford/holyc-lang/archive/refs/tags/v%{ver}.tar.gz
BuildRequires: cmake
BuildRequires: cmake-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
%if %{with test}
BuildRequires: ripgrep
%endif
%if %{with sqlite}
BuildRequires: pkgconfig(sqlite3)
Requires:      pkgconfig(sqlite3)
%endif
Packager:      Gilver E. <roachy@fyralabs.com>

%description
HolyC is a fun recreational programming language designed by Terry A. Davis.
Originally implemented in TempleOS as a general purpose programming language and scripting language for all manner of tasks.

%prep
# Currently needed to fetch the commit hash for hcc --version
%git_clone https://github.com/Jamesbarford/holyc-lang.git v%{ver}
%setup -TDn holyc-lang/src

# Make the binary correctly report its installed location as /usr/bin instead of /usr
sed -i 's|binary: %%s/hcc|binary: %%s/bin/hcc|g' cli.c

# Fix the test ROOT location
sed -i "s|ROOT=.*|ROOT=$(dirname %{rpmbuilddir}%{?buildsubdir:/%{buildsubdir}})|" tests/run.sh

# Fix the tests looking for hcc in a relative path
pushd tests
for file in $(rg '../../hcc' --files-with-matches); do
  sed -i 's|../../hcc|%{buildroot}%{_bindir}/hcc|g' $file
done
popd

%conf
%cmake \
  -DCMAKE_BUILD_TYPE="Release" \
  -DHCC_ENABLE_JIT="ON" \
%if %{with sqlite}
  -DHCC_LINK_SQLITE3="1" \
%endif
  -DCMAKE_INSTALL_PREFIX="%{_prefix}"

%build
%cmake_build

HCC="$PWD/hcc"
LIBTOS_BUILDDIR="$PWD/libtos-build"
SRCDIR="$PWD"

mkdir -pv $LIBTOS_BUILDDIR/include $LIBTOS_BUILDDIR/%{_lib}
cp -v ./holyc-lib/tos.HH -t $LIBTOS_BUILDDIR/include

pushd holyc-lib
$HCC \
  --target=%{_target_cpu}-unknown-linux-gnu \
  --install-dir="$LIBTOS_BUILDDIR" \
  -fPIC -S -o "$SRCDIR/tos.s" ./all.HC
popd

%{__cc} \
  $CFLAGS \
  -c ./tos.s -o ./tos.o

%{__ar} \
  rcs "$LIBTOS_BUILDDIR/%{_lib}/libtos.a" ./tos.o

%{__cc} \
  $CFLAGS \
  -shared \
  $LDFLAGS \
  -Wl,-Bsymbolic -Wl,-soname,libtos.so.0.0.1 \
  ./tos.o -o "$LIBTOS_BUILDDIR/%{_lib}/libtos.so.0.0.1" -lpthread -lc -lm

%install
%cmake_install

%{__install} -Dpm755 ./libtos-build/%{_lib}/* -t %{buildroot}%{_libdir}

%check
HCC="%{buildroot}%{_bindir}/hcc" ; export HCC
BUILD="%{__cmake_builddir}" ; export BUILD

# Fail if the path is wrong
$HCC --version | /usr/bin/grep -C5 'binary: /usr/bin/hcc'

./tests/run.sh '--cflags=-O'
./tests/run.sh '--cflags=-fno-inline -fno-reg-promote'

%files
%license ../COPYING
%doc ../README.md
%{_bindir}/hcc
%{_libdir}/libtos.a
%{_libdir}/libtos.so.0.0.1
%{_includedir}/tos.HH

%changelog
* Sat Jul 4 2026 Gilver E. <roachy@fyralabs.com> - 0.0.14~beta-1
- Update to 0.0.14 beta
* Tue Feb 10 2026 Gilver E. <roachy@fyralabs.com> - 0.0.10~beta-1
- Initial package
