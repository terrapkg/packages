Name:           DOtherSide
Version:        0.9.0
Release:        1%?dist
Summary:        C language library for creating bindings for the Qt QML language
License:        LGPL-3.0-only
URL:            https://github.com/filcuc/DOtherSide
Source0:        %url/archive/refs/tags/v%{version}.tar.gz
Provides:       dotherside = %version-%release
BuildRequires:  cmake make 
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6XcbQpaPrivate)

%description
%summary.

%prep
%autosetup -n dotherside-%version

%build
%cmake
%cmake_build

%install
%cmake_install

mv %buildroot/usr/lib/ %buildroot%_libdir

%files
%doc README.md
%license LICENSE
%_includedir/DOtherSide/DOtherSide.h
%_includedir/DOtherSide/DOtherSideTypes.h
%_libdir/libDOtherSide.so
%_libdir/libDOtherSide.so.%(echo "%version" | sed -E 's@\.[0-9]+$@@')
%_libdir/libDOtherSide.so.%version
