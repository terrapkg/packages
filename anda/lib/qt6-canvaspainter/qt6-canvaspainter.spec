Name:			    qt6-canvaspainter
Version:		    6.11.1
Release:		    1%{?dist}
Epoch:              1
Summary:		    Accelerated 2D painting solution for Qt Quick and QRhi-based render targets
License:		    GPL-3.0-only AND OFL-1.1 AND (LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0) AND BSD-3-Clause AND (LicenseRef-Qt-Commercial OR GFDL-1.3-no-invariants-only)
URL:			    https://github.com/qt/qtcanvaspainter
Source0:		    %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	    cmake
BuildRequires:      gcc
BuildRequires:      gcc-c++
BuildRequires:      cmake(Qt6Core)
BuildRequires:      cmake(Qt6CorePrivate)
BuildRequires:      cmake(Qt6DBusPrivate)
BuildRequires:      cmake(Qt6Gui)
BuildRequires:      cmake(Qt6GuiPrivate)
BuildRequires:      cmake(Qt6NetworkPrivate)
BuildRequires:      cmake(Qt6Quick)
BuildRequires:      cmake(Qt6QuickPrivate)
BuildRequires:      cmake(Qt6ShaderTools)
BuildRequires:      cmake(Qt6ShaderToolsPrivate)
BuildRequires:      cmake(Qt6Widgets)
BuildRequires:      cmake(Qt6WidgetsPrivate)
BuildRequires:      kf6-rpm-macros
BuildSystem:        cmake

Packager:           Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%package devel
%pkg_devel_files

%prep
%autosetup -C

%conf
%cmake_kf6 -DQT_NO_PACKAGE_VERSION_CHECK=TRUE

%files
%license LICENSES/*
%{_kf6_libdir}/libQt6CanvasPainter.so.6
%{_kf6_libdir}/libQt6CanvasPainter.so.%{version}
%{_kf6_libdir}/libQt6CanvasPainter.prl
%{_kf6_archdatadir}/bin/qcshadergen
%{_kf6_archdatadir}/examples/*
%{_kf6_archdatadir}/metatypes/*.json
%{_kf6_archdatadir}/mkspecs/modules/*.pri
%{_kf6_archdatadir}/modules/*.json
%{_kf6_archdatadir}/sbom/qtcanvaspainter-%{version}.spdx

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com>
- Package stable releases only

* Thu Jul 23 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
