%global toolchain clang
# excluded because syslog-ng claims to provide it.
# we explicitly require cef so we will definitely get it.
%global __requires_exclude ^libcef\\.so\\(\\)\\(64bit\\)$
# determine cef-devel install location from /usr/src/cef-<version>;
%global cef_root %(ls -d /usr/src/cef-*/ 2>/dev/null | sort -V | tail -n 1)
%global appid com.adamcake.Bolt

Name:       bolt-launcher
Version:    0.24.0
Release:    1%{?dist}
Summary:    A third-party, free-software launcher for your favourite MMORPG
License:    AGPL-3.0-or-later
URL:        https://codeberg.org/Adamcake/Bolt
Source0:    %{url}.git

BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: anda-srpm-macros
BuildRequires: clang
BuildRequires: cef
BuildRequires: cef-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(luajit)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: /usr/bin/ld
BuildRequires: mold

Requires:      cef

Packager:      Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.


%prep
%git_clone %{url}.git %{version}

# our version of clang needs this value to be different to compile correctly
sed -i 's/#  define FMT_USE_CONSTEVAL 1/#  define FMT_USE_CONSTEVAL 0/' modules/fmt/include/fmt/base.h

%conf
%cmake \
    -D CEF_ROOT=%{cef_root} \
    -D CMAKE_MODULE_PATH="%{_datadir}/cmake/Modules" \
    -D CEF_LIBRARY="%{_libdir}/cef/libcef.so" \
    -D BUILD_SHARED_LIBS=OFF \
    -D BOLT_META_NAME=%{appid} \
    -D BOLT_CEF_INCLUDEPATH="%{_includedir}/cef" \
    -D BOLT_LIBCEF_DIRECTORY="%{_libdir}/cef" \
    -D BOLT_CEF_RESOURCEDIR_OVERRIDE="%{_libdir}/cef" \
    -D BOLT_CEF_INSTALLDIR="%{_libdir}/%{name}" \
    -D BOLT_LIBDIR="%{_libdir}/%{name}" \
    -D BOLT_BINDIR="%{_bindir}" \
    -D BOLT_SHAREDIR="%{_datadir}" \
    -D CMAKE_CXX_FLAGS="%{build_cxxflags} -Wno-error=undefined-var-template -DFMT_USE_CONSTEVAL=0" \
    -D CMAKE_INSTALL_RPATH='$ORIGIN/../cef;$ORIGIN/../../cef' \
    -D BOLT_SKIP_RPATH=1

%build
export LD_LIBRARY_PATH="%{_libdir}/cef${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENCE
%{_bindir}/bolt
%{_libdir}/%{name}/
%{_appsdir}/%{appid}.desktop
%{_appsdir}/%{appid}.RuneScape.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_scalableiconsdir}/%{appid}.svg

%changelog
* Fri Sep 11 2026 Caleb Jones <owen@fyralabs.com> - 0.24.0-1
- Change CEF root so it works with various cef versons.
- Various improvements

* Fri Sep 04 2026 Caleb Jones <caleb@fyralabs.com> - 0.23.2-2
- Exclude libcef.so to fix unnecessary syslog-ng dependency

* Fri May 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.23.2-1
- Initial commit
