# Original credits to Patrick Laimbock for the original spec,
# this one is cleaned up because the the COPR version is messy as hell

##trace

# force single job compilation
%dnl %define _smp_mflags -j1
%global cargo_install_lib 0

%undefine _hardened_build
%undefine _include_frame_pointers

# target wine version
%global wineversion      9.21
%global debug_package    %{nil}
%global _lto_cflags      %{nil}

%global with_32bit       1
%global vst3sdkversion   3.7.7_build_19-patched
%global vst3ver          %(b=%{vst3sdkversion}; echo ${b:1:6})

%global gitdate          20250601
%global commit           918d24a16e8eda9ac2eac692704770dfed96f6ee
%global shortcommit      %(c=%{commit}; echo ${c:0:7})

%global version          5.1.1
%global release 1

# set this to "1" if building a git/beta/rc release
%global beta_or_rc       0


#=============================================================================
# general
#-----------------------------------------------------------------------------
Name:           yabridge
Version:        %{version}
%if %{beta_or_rc}
Release:        0.%{release}.%{gitdate}.git%{shortcommit}%{?dist}
%else
Release:        %{release}%{?dist}
%endif
Summary:        Yet Another VST bridge, run Windows VST2 plugins under Linux
License:        GPLv3
Packager:       Cappy Ishihara <cappy@fyralabs.com>
URL:            https://github.com/robbert-vdh/yabridge
%if %{beta_or_rc}
Source0:        https://github.com/robbert-vdh/yabridge/archive/{commit}/%{name}-%{version}-git%{shortcommit}.tar.gz
#Source0:        https://github.com/robbert-vdh/yabridge/archive/yabridge-master.zip
%else
Source0:        https://github.com/robbert-vdh/yabridge/archive/%{version}/%{name}-%{version}.tar.gz
%endif
# https://github.com/robbert-vdh/vst3sdk

Source4:        https://github.com/robbert-vdh/vst3sdk/archive/refs/tags/v%{vst3sdkversion}.tar.gz
#Source5:        vst3sdk-meson.build
#

BuildRequires:  vim
BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  uuid-devel
BuildRequires:  cmake
BuildRequires:  cargo
BuildRequires:  mold
BuildRequires:  clang-devel
BuildRequires:  git-core
BuildRequires:  meson >= 0.56
BuildRequires:  gcc
BuildRequires:  gcc-c++
#BuildRequires:  asio-devel
BuildRequires:  boost
BuildRequires:  boost-devel
BuildRequires:  boost-filesystem
BuildRequires:  boost-system
BuildRequires:  dbus-devel
BuildRequires:  git-core
BuildRequires:  glibc-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libxcb-devel
BuildRequires:  rust
BuildRequires:  /usr/bin/winegcc
BuildRequires: (wine-devel or wine-staging-devel or wine-stable-devel or wine-dev-devel)
BuildRequires:  xcb-util-wm-devel
%if %{with_32bit}
#BuildRequires:  asio-devel(x86-32)
BuildRequires:  boost(x86-32)
BuildRequires:  boost-devel(x86-32)
BuildRequires:  boost-filesystem(x86-32)
BuildRequires:  boost-iostreams(x86-32)
BuildRequires:  boost-system(x86-32)
BuildRequires:  dbus-devel(x86-32)
BuildRequires:  glibc-devel(x86-32)
BuildRequires:  libstdc++-devel(x86-32)
BuildRequires:  libxcb-devel(x86-32)
# We need shell32 and ole32, for some reason terra wine just doens't have it
%dnl BuildRequires:  (wine-devel(x86-32) or wine-staging-devel(x86-32) or wine-stable-devel(x86-32) or wine-dev-devel(x86-32))
BuildRequires:  wine-devel(x86-32)
BuildRequires:  /usr/bin/winegcc
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-wm-devel(x86-32)
%endif

ExclusiveArch:      x86_64

Requires:       boost
Requires:       boost-filesystem
Requires:       boost-system
Requires:       libxcb
Requires:       libXau
Requires:       python3

%if %{with_32bit}
Requires:       glibc(x86-32)
Requires:       libgcc(x86-32)
Requires:       libstdc++(x86-32)
Requires:       libxcb(x86-32)
Requires:       libXau(x86-32)
%endif

%description
Yet Another way to use Windows VST plugins on Linux. Yabridge seamlessly
supports running both 64-bit Windows VST2 plugins as well as 32-bit Windows
VST2 plugins in a 64-bit Linux VST host. This project aims to be as
transparent as possible to achieve the best possible plugin compatibility
while also staying easy to debug and maintain.


#=============================================================================
# prep
#-----------------------------------------------------------------------------
%prep
%if %{beta_or_rc}
%autosetup -p1 -n %{name}
%else
%autosetup -p1 -n %{name}-%{version}
%endif

pushd subprojects/
tar -xvf %{SOURCE4}
#mv vst3sdk-%{vst3sdkversion} vst3
# vst3sdk
#rm -rf vst3/.git vst3/.gitmodules
#cp -av %%{SOURCE5} vst3/meson.build
popd


# rename migration README.md for easier inclusion in the package
mv -v tools/migration/README.md tools/migration/README-migration.md


%if %{beta_or_rc}
# sync yabridgectl version with yabridge version
sed -i -e's|^version.*$|version = "%{version}"|' tools/yabridgectl/Cargo.toml
%endif

## change deprecated dialect option 'c++2a' to c++20 in meson.build
## see https://gcc.gnu.org/onlinedocs/gcc/C-Dialect-Options.html#Options-Controlling-C-Dialect
#sed -i -e's|c++2a|c++20|g' meson.build

# hack: fix problem with detecting the wine version
#sed -i -e"s|wine_version = wine_version.stdout()|wine_version = '9.21'|" meson.build


#=============================================================================
# build
#-----------------------------------------------------------------------------
%build
export LDFLAGS="%{build_ldflags}"

%ifarch x86_64
%define bitbridge true
%else
%define bitbridge false
%endif

export CC_LD=mold
export LD=mold

%if %{with_32bit}
%meson --cross-file cross-wine.conf \
  -Dbitbridge=true --wrap-mode=default --unity=on --unity-size=1000
%else
%meson --cross-file cross-wine.conf \
  -Dbitbridge=false --wrap-mode=default --unity=on --unity-size=1000
%endif

%meson_build

pushd tools/yabridgectl
%cargo_prep_online
%cargo_build
popd


#=============================================================================
# check
#-----------------------------------------------------------------------------
%check
# there are no tests
# ninja test -v -j1 -C build test


#=============================================================================
# install
#-----------------------------------------------------------------------------
%install
ls -R
# create directories
install -d -m0755 %{buildroot}%{_bindir}
install -d -m0755 %{buildroot}%{_libdir}

# install apps and libs
install -D -m 0755 %{_vpath_builddir}/yabridge-host*.exe* %{buildroot}%{_bindir}/
install -D -m 0755 %{_vpath_builddir}/libyabridge-chainloader-vst*.so %{buildroot}%{_libdir}/
install -D -m 0755 %{_vpath_builddir}/libyabridge-chainloader-clap*.so %{buildroot}%{_libdir}/
install -D -m 0755 %{_vpath_builddir}/libyabridge-vst*.so %{buildroot}%{_libdir}/
install -D -m 0755 %{_vpath_builddir}/libyabridge-clap*.so %{buildroot}%{_libdir}/

# install tool
pushd tools/yabridgectl
%cargo_install
#install -D -m 0755 tools/yabridgectl/target/release/yabridgectl %{buildroot}%{_bindir}/
popd

# install migration scripts
install -D -m 0755 tools/migration/*.py %{buildroot}%{_bindir}/



#=============================================================================
# files
#-----------------------------------------------------------------------------
%files
%defattr(-,root,root)
%license COPYING
%doc CHANGELOG.md README.md ROADMAP.md tools/migration/README-migration.md
%attr(0755,root,root)        %{_bindir}/yabridgectl
%attr(0755,root,root)        %{_bindir}/yabridge-host.exe
%attr(0755,root,root)        %{_bindir}/yabridge-host.exe.so
# migration scripts
%attr(0755,root,root)        %{_bindir}/migrate-ardour.py
%attr(0755,root,root)        %{_bindir}/migrate-bitwig.py
%attr(0755,root,root)        %{_bindir}/migrate-reaper.py
%attr(0755,root,root)        %{_bindir}/migrate-renoise.py
%if %{with_32bit}
%attr(0755,root,root)        %{_bindir}/yabridge-host-32.exe
%attr(0755,root,root)        %{_bindir}/yabridge-host-32.exe.so
%endif
%attr(0755,root,root)        %{_libdir}/libyabridge-chainloader-clap.so
%attr(0755,root,root)        %{_libdir}/libyabridge-chainloader-vst2.so
%attr(0755,root,root)        %{_libdir}/libyabridge-chainloader-vst3.so
%attr(0755,root,root)        %{_libdir}/libyabridge-clap.so
%attr(0755,root,root)        %{_libdir}/libyabridge-vst2.so
%attr(0755,root,root)        %{_libdir}/libyabridge-vst3.so


#=============================================================================
# post
#-----------------------------------------------------------------------------
%post
/sbin/ldconfig


#=============================================================================
# postun
#-----------------------------------------------------------------------------
%postun
/sbin/ldconfig


#=============================================================================
# changelog
#-----------------------------------------------------------------------------
%changelog
%autochangelog
