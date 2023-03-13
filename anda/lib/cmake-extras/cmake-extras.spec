%global forgeurl https://gitlab.com/ubports/development/core/lomiri-api
%global commit 99aab4514ee182cb7a94821b4b51e4d8cb9a82ef
%forgemeta

Name:       cmake-extras
Version:    1.6
Release:    1%{?dist}
Summary:    A collection of add-ons for the CMake build tool
License:    GPLv3
URL:        https://gitlab.com/ubports/development/core/cmake-extras
Source0:    %{url}/-/archive/%commit/cmake-extras-%commit.tar.gz
BuildArch:  noarch

BuildRequires: cmake
BuildRequires: gcc-c++
Requires:      gcovr
Requires:      gmock-devel
Requires:      intltool
Requires:      gettext
Requires:      lcov
Requires:      qt5-qtdeclarative-devel

%description
A collection of add-ons for the CMake build tool used to build lomiri and other applications. 

%prep
%autosetup -n cmake-extras-%commit
sed -i 's/#!\/bin\/sh/#!\/usr\/bin\/sh/' src/FormatCode/formatcode.in
sed -i 's/#!\/bin\/sh/#!\/usr\/bin\/sh/' src/CopyrightTest/check_copyright.sh
sed -i 's/python/python3/' src/IncludeChecker/include_checker.py
sed -i 'sX/usr/lib/qt5X${CMAKE_LIBDIR}/qt5X' src/QmlPlugins/QmlPluginsConfig.cmake

%build
%cmake
%cmake_build

%install
%cmake_install
# Correct this as we actually don't have a gmock source dir
#rm {buildroot}/usr/share/cmake/GMock/GMockConfig.cmake
#cp {SOURCE1} {buildroot}/usr/share/cmake/GMock/

%files
%license LICENSE
%{_datadir}/cmake/CopyrightTest/CopyrightTestConfig.cmake
%{_datadir}/cmake/CopyrightTest/check_copyright.sh
%{_datadir}/cmake/CoverageReport/CoverageReportConfig.cmake
%{_datadir}/cmake/CoverageReport/EnableCoverageReport.cmake
%{_datadir}/cmake/DoxygenBuilder/Doxyfile.in
%{_datadir}/cmake/DoxygenBuilder/DoxygenBuilderConfig.cmake
%{_datadir}/cmake/GDbus/GDbusConfig.cmake
%{_datadir}/cmake/GMock/GMockConfig.cmake
%{_datadir}/cmake/GSettings/GSettingsConfig.cmake
%{_datadir}/cmake/Intltool/IntltoolConfig.cmake
%{_datadir}/cmake/Lcov/LcovConfig.cmake
%{_datadir}/cmake/QmlPlugins/QmlPluginsConfig.cmake
%{_datadir}/cmake/FormatCode/unity-api.clang-format
%{_datadir}/cmake/FormatCode/formatcode.in
%{_datadir}/cmake/FormatCode/formatcode_format.cmake.in
%{_datadir}/cmake/FormatCode/unity-api.astyle
%{_datadir}/cmake/FormatCode/formatcode_test.cmake.in
%{_datadir}/cmake/FormatCode/FormatCodeConfig.cmake
%{_datadir}/cmake/FormatCode/formatcode_common.cmake
%{_datadir}/cmake/gcovr/gcovrConfig.cmake
%{_datadir}/cmake/IncludeChecker/IncludeCheckerConfig.cmake
%{_datadir}/cmake/IncludeChecker/deps
%{_datadir}/cmake/IncludeChecker/include_checker.py
%{_datadir}/cmake/GObjectIntrospection/GObjectIntrospectionConfig.cmake
%{_datadir}/cmake/GdbusCodegen/GdbusCodegenConfig.cmake
%{_datadir}/cmake/Vala/ValaConfig.cmake

%changelog
%autochangelog
