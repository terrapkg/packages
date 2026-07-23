%global ver v6.12.0-beta2
%global sanitized_ver %(echo %{ver} | sed 's/^v//; s/-beta2//')

Name:			    qtcanvaspainter6
Version:		    %{sanitized_ver}
Release:		    1%?dist
Summary:		    Accelerated 2D painting solution for Qt Quick and QRhi-based render targets
License:		    GPL-3.0-only AND OFL-1.1 AND (LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0) AND BSD-3-Clause AND (LicenseRef-Qt-Commercial OR GFDL-1.3-no-invariants-only)
URL:			    https://github.com/qt/qtcanvaspainter
Source0:		    %{url}/archive/refs/tags/%{ver}.tar.gz
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
BuildSystem:        cmake
BuildOption(conf):  -DQT_NO_PACKAGE_VERSION_CHECK=TRUE

%description
%{summary}.

%package devel
%pkg_devel_files
%{_libdir}/qt6/qml/QtCanvas2D/libcanvas2dplugin.so

%prep
%autosetup -C
find . -name "CMakeLists.txt" -exec sed -i 's/qt_standard_project_setup(REQUIRES 6\.12)/qt_standard_project_setup(REQUIRES 6.11)/g' {} +

%files
%doc CONTRIBUTING.md
# No license file upstream, so this will have to do
%license REUSE.toml
%{_libdir}/libQt6Canvas2D.prl
%{_libdir}/libQt6Canvas2D.so.6
%{_libdir}/libQt6Canvas2D.so.%{sanitized_ver}
%{_libdir}/libQt6CanvasPainter.so.6
%{_libdir}/libQt6CanvasPainter.so.%{sanitized_ver}
%{_libdir}/libQt6CanvasPainter.prl
%{_libdir}/qt6/bin/qcshadergen
%{_libdir}/qt6/examples/*
%{_libdir}/qt6/metatypes/*.json
%{_libdir}/qt6/mkspecs/modules/*.pri
%{_libdir}/qt6/modules/*.json
%{_libdir}/qt6/qml/QtCanvas2D/plugins.qmltypes
%{_libdir}/qt6/qml/QtCanvas2D/qmldir
%{_libdir}/qt6/sbom/qtcanvaspainter-%{sanitized_ver}.spdx

%changelog
* Thu Jul 23 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
