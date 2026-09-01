Name:       bolt-launcher
Version:    0.23.2
Release:    1%{?dist}
Summary:    A third-party, free-software launcher for your favourite MMORPG
License:    AGPL-3.0-or-later
URL:        https://codeberg.org/Adamcake/Bolt
Source0:    %{url}.git

BuildRequires: cmake
BuildRequires: cmake-extras
BuildRequires: gcc-c++
BuildRequires: cef-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
%dnl BuildRequires: pkgconfig(liblomiri-api)
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(gtest)
%dnl BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(luajit)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(x11)
BuildRequires: /usr/bin/ld
BuildRequires: mold

Packager:      Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%package devel
%pkg_devel_files

%prep
%git_clone %{url}.git %{version}

%conf
%cmake \
    -D CEF_ROOT="/usr/src/cef-146.0.11" \
    -D BOLT_CEF_INCLUDEPATH="%{_includedir}" \
    -D BOLT_LIBCEF_DIRECTORY="%{_libdir}" \
    -D BOLT_SKIP_RPATH=1

%build
%cmake_build

%install
%cmake_install

%files
%doc README
%license COPYING

%changelog
* Fri May 22 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
