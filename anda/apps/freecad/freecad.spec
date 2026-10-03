%global appid org.freecad.FreeCAD
%global appstream_component desktop-application
%global name_pretty FreeCAD
%global developer The FreeCAD Team
%global org org.freecad
%global appstream_description An open source parametric 3D CAD modeler

# Fedora has no salomesmesh package. FreeCAD's FEM meshers are built from
# the sources in src/3rdParty/salomesmesh.
%global bundled_smesh_version 7.7.1.0

# Private modules and libraries under %%{_libdir}/%%{name}/lib.
# Names are the installed SONAME stems, without ".so" and without a trailing "Gui".
# The name filters drop those SONAMEs from the public dependency set. System
# libraries that only a workbench links, such as PCL, stay as Requires.
%global plugins AssemblyApp AssemblyGui CAMSimulator DraftUtils Fem FreeCAD Import Inspection MatGui Materials Measure Mesh MeshPart Part PartDesignGui PathApp PathGui PathSimulator Points QtUnitGui ReverseEngineering Robot Sketcher Spreadsheet Start Surface TechDraw Web _PartDesign area flatmesh libDriver libDriverDAT libDriverSTL libDriverUNV libMEFISTO2 libSMDS libSMESH libSMESHDS libStdMeshers libarea-native
%global plugin_exclude %(for i in %{plugins}; do echo -n "\\|${i}\\(Gui\\)\\?"; done)
%global __provides_exclude_from ^%{_libdir}/%{name}/Mod/.*
%global __provides_exclude ^(libFreeCAD.*%{plugin_exclude})\\.so.*
%global __requires_exclude ^(libFreeCAD.*%{plugin_exclude})\\.so.*

Name:           freecad
Epoch:          1
Version:        1.1.4
Release:        1%{?dist}
Summary:        A general purpose 3D CAD modeler
# FreeCAD sources are LGPL-2.0-or-later (GNU Library GPL v2 or later) or
# LGPL-2.1-or-later. AddonManager is LGPL-2.1-or-later.
# Vendored zipios++ is the Lesser GPL, version 2 or later.
# salomesmesh contains both LGPL-2.1-only and LGPL-2.1-or-later files.
# clipper and WildMagic4 are BSL-1.0. The DXF reader is BSD-3-Clause.
# GSL, nlohmann-json, lru-cache, and the Khronos OpenGL headers are MIT.
# lazy_loader is Apache-2.0. Base64 is Zlib.
# libkdtree ships in the source tree and is not compiled.
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-only AND BSL-1.0 AND BSD-3-Clause AND MIT AND Apache-2.0 AND Zlib
URL:            https://www.freecad.org/
Packager:       Utkarsh Verma <hi@utkarshverma.com>
ExclusiveArch:  x86_64 aarch64

# The external switch skips the bundled copy, but nothing calls
# find_package. The imported target is local to src/3rdParty unless it is
# promoted, so Points never gets /usr/include/E57Format.
Patch0:         use-system-e57format.patch

BuildRequires:  anda-srpm-macros
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  swig
BuildRequires:  terra-appstream-helper

BuildRequires:  boost-devel
BuildRequires:  Coin4-devel
BuildRequires:  eigen3-devel
BuildRequires:  fmt-devel
BuildRequires:  freeimage-devel
BuildRequires:  hdf5-static
BuildRequires:  libE57Format-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libicu-devel
BuildRequires:  libspnav-devel
BuildRequires:  libXmu-devel
BuildRequires:  med-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ondselsolver-devel
BuildRequires:  opencascade-devel
BuildRequires:  openmpi-devel
BuildRequires:  pcl-devel
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-pivy
BuildRequires:  python3-pybind11
BuildRequires:  python3-pycxx-devel
BuildRequires:  python3-pyside6-devel
BuildRequires:  python3-shiboken6-devel
BuildRequires:  pyside6-tools
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qttools-static
BuildRequires:  tbb-devel
BuildRequires:  vtk-devel
BuildRequires:  xerces-c-devel
BuildRequires:  yaml-cpp-devel

Requires:       hicolor-icon-theme
Requires:       shared-mime-info

# Runtime tools and Python modules the 1.1.4 sources import.
# CalculiX, the Netgen mesher, IfcOpenShell, OpenCAMLib, pythonOCC,
# debugpy, and xlutils are not in Fedora 44.
Requires:       gmsh
Requires:       graphviz
Requires:       python3-collada
Requires:       python3-defusedxml
Requires:       python3-matplotlib
Requires:       python3-numpy
Requires:       python3-pip
Requires:       python3-pivy
Requires:       python3-ply
Requires:       python3-pyside6
Requires:       python3-pyyaml
Requires:       python3-requests
Requires:       python3-typing-extensions
Requires:       qt6-assistant
Requires:       qt6-qtwayland

Obsoletes:      %{name}-doc < 0.22-1

Provides:       bundled(smesh) = %{bundled_smesh_version}

%description
FreeCAD is an open source parametric 3D CAD modeler for product design,
mechanical engineering, and architecture. Sketches, parts, assemblies,
drawings, and meshes are built from the model history, and the workbenches
cover FEM, BIM, and CAM.

%prep
# Git is required so the GSL and AddonManager submodules are present.
# GitHub release archives omit them. OndselSolver and libE57Format come from
# the system packages.
%git_clone https://github.com/FreeCAD/FreeCAD %{version}
%autopatch -p1

%conf
# PCL 1.15 asks for Eigen3 3.3. Eigen 5 treats that as "3.3.x only" and
# rejects itself. Fedora built this PCL against Eigen 5, so accept 5.
mkdir -p eigen-prefix/share/cmake
cp -a %{_datadir}/cmake/eigen3 eigen-prefix/share/cmake/
ln -sfn %{_includedir} eigen-prefix/include
sed -i 's/set(PACKAGE_VERSION_COMPATIBLE FALSE)/set(PACKAGE_VERSION_COMPATIBLE TRUE)/g' \
    eigen-prefix/share/cmake/eigen3/Eigen3ConfigVersion.cmake

# The program tree lives under %%{_libdir}/freecad. Docs, headers, and
# resources stay on the normal system paths.
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_libdir}/%{name} \
    -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
    -DCMAKE_INSTALL_DATADIR=%{_datadir}/%{name} \
    -DRESOURCEDIR=%{_datadir}/%{name} \
    -DFREECAD_QT_VERSION=6 \
    -DFREECAD_USE_EXTERNAL_FMT=ON \
    -DFREECAD_USE_EXTERNAL_PIVY=ON \
    -DFREECAD_USE_EXTERNAL_PYCXX=ON \
    -DFREECAD_USE_PCL=ON \
    -DEigen3_DIR:PATH=${PWD}/eigen-prefix/share/cmake/eigen3 \
    -DFREECAD_USE_PYBIND11=ON \
    -DBUILD_FEM_NETGEN=OFF \
    -DBUILD_GUI=ON \
    -DOpenGL_GL_PREFERENCE=GLVND \
    -DFREECAD_USE_EXTERNAL_E57FORMAT=ON \
    -DFREECAD_USE_EXTERNAL_ONDSELSOLVER=ON \
    -DENABLE_DEVELOPER_TESTS=OFF

%build
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_bindir}
ln -s ../%{_lib}/%{name}/bin/FreeCAD %{buildroot}%{_bindir}/FreeCAD
ln -s ../%{_lib}/%{name}/bin/FreeCADCmd %{buildroot}%{_bindir}/FreeCADCmd

# Headers from bundled third-party libraries that are not part of the public API.
rm -rf %{buildroot}%{_libdir}/%{name}/include/E57Format
rm -rf %{buildroot}%{_libdir}/%{name}/%{_lib}/cmake
rm -rf %{buildroot}%{_libdir}/%{name}/%{_lib}/pkgconfig

# CMake installs desktop integration under the FreeCAD prefix. Move it onto
# the system data dirs so menus, icons, and MIME types are picked up.
mkdir -p %{buildroot}%{_datadir}
mv %{buildroot}%{_libdir}/%{name}/share/applications %{buildroot}%{_appsdir}
mkdir -p %{buildroot}%{_metainfodir}
mv %{buildroot}%{_libdir}/%{name}/share/metainfo/* %{buildroot}%{_metainfodir}/
mv %{buildroot}%{_libdir}/%{name}/share/icons %{buildroot}%{_datadir}/
mv %{buildroot}%{_libdir}/%{name}/share/pixmaps %{buildroot}%{_datadir}/
mv %{buildroot}%{_libdir}/%{name}/share/mime %{buildroot}%{_datadir}/
mv %{buildroot}%{_libdir}/%{name}/share/thumbnailers %{buildroot}%{_datadir}/
if [ -d %{buildroot}%{_libdir}/%{name}/share/pkgconfig ]; then
    mv %{buildroot}%{_libdir}/%{name}/share/pkgconfig %{buildroot}%{_datadir}/
fi

# Keep the upstream metainfo, including its categories, and fill any gaps
# from the installed desktop file and icons.
%terra_appstream

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

# Fail the build when the private-library filters above no longer match
# what actually got installed.
new_plugins=$(find %{buildroot}%{_libdir}/%{name}/%{_lib} -maxdepth 1 -name '*.so*' -printf '%f\n' | sed \
    -e '/^\(libFreeCAD.*%{plugin_exclude}\)\(\|Gui\)\.so\(\.[0-9.]*\)\?$/d')
if [ -n "$new_plugins" ]; then
    echo "Plugins missing from %%plugins:" >&2
    echo "$new_plugins" >&2
    exit 1
fi
for p in %{plugins}; do
    if [ -z "$(ls %{buildroot}%{_libdir}/%{name}/%{_lib}/$p.so* 2>/dev/null)" ]; then
        echo "%%plugins entry has no matching library: $p" >&2
        exit 1
    fi
done

%files
%license LICENSE
%license src/3rdParty/salomesmesh/LICENCE.lgpl.txt
%license src/3rdParty/lru-cache/LICENSE
%license src/3rdParty/GSL/LICENSE
%license src/Base/Base64.h
%doc README.md
%{_bindir}/FreeCAD
%{_bindir}/FreeCADCmd
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_hicolordir}/*/apps/%{appid}.*
%{_hicolordir}/scalable/mimetypes/application-x-extension-fcstd.svg
%{_datadir}/pixmaps/freecad.svg
%{_datadir}/mime/packages/%{appid}.xml
%{_datadir}/thumbnailers/FreeCAD.thumbnailer
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/bin/
%{_libdir}/%{name}/%{_lib}/
%{_libdir}/%{name}/Ext/
%{_libdir}/%{name}/Mod/
%{_libdir}/%{name}/share/
%{python3_sitelib}/freecad/
%{_datadir}/%{name}/
%{_docdir}/%{name}/LICENSE.html
%{_docdir}/%{name}/ThirdPartyLibraries.html

%changelog
* Sat Oct 03 2026 Utkarsh Verma <hi@utkarshverma.com> - 1.1.4-1
- Initial package, built from source against the system libraries
