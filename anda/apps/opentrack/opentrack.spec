%global debug_package %{nil}
%global openvr_ver 2.12.14
%global appid com.github.opentrack
%global ver opentrack-2026.1.0
%global sanitized_ver %(echo %{ver} | sed 's/opentrack\-//')

Name:           opentrack
Version:        %{sanitized_ver}
Release:        2%{?dist}
Summary:        Head tracking software for MS Windows, Linux, and Apple OSX

License:        ISC AND BSD-3-Clause AND BSD-2-Clause AND LGPL-2.1-only AND GPL-3.0-only AND LGPL-2.1-or-later AND MIT AND LGPL-3.0-or-later
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        https://github.com/ValveSoftware/openvr/archive/refs/tags/v%{openvr_ver}.tar.gz
Source2:        %{appid}.desktop
Source3:        %{appid}.metainfo.xml

Patch0:         fix-qt6-resolve.patch

ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  faust
BuildRequires:  faust-osclib-devel
BuildRequires:  libevdev-devel
BuildRequires:  librealsense-devel
BuildRequires:  libX11-devel
BuildRequires:  libXtst-devel
BuildRequires:  ninja-build
BuildRequires:  onnxruntime-devel
BuildRequires:  opencv-devel
BuildRequires:  procps-ng-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtserialport-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  terra-wine-staging
BuildRequires:  wine-staging-devel

Requires:       qt6-qtbase
Requires:       qt6-qt5compat
Requires:       qt6-qtserialport
Requires:       opencv
Requires:       faust-osclib
Requires:       onnxruntime

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
opentrack is a program for tracking user's head rotation and transmitting it to flight simulation software and military-themed video games.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1
tar -xf %{SOURCE1}

# Rename the OpenVR license so we can include it in the RPM
cp openvr-%{openvr_ver}/LICENSE LICENSE-OpenVR

mkdir -p external-include/include/oscpack/osc
mkdir -p external-include/lib
ln -s /usr/include/faust/osc/*.h external-include/include/oscpack/osc/
ln -s /usr/share/faust/osclib/oscpack/osc/*.h external-include/include/oscpack/osc/
ln -s /usr/lib/libOSCFaust.so external-include/lib/liboscpack.so

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DSDK_HIERARCHY=ON \
    -DSDK_WINE=ON \
    -DSDK_LIBDIR=%{_lib}/%{name} \
    -DSDK_PLUGINDIR=%{_lib}/%{name} \
    -DSDK_OSCPACK=$PWD/external-include \
    -DSDK_ONNX=ON \
    -DONNXRuntime_DIR=%{_libdir} \
    -DONNXRuntime_INCLUDE_DIRS=%{_includedir}/onnxruntime \
    -DSDK_OPENCV=ON \
    -DSDK_VALVE_STEAMVR=$PWD/openvr-%{openvr_ver} \
    -DOPENCV_PREFIX=%{_prefix}

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_libdir}/%{name}
install -Dm755 openvr-%{openvr_ver}/bin/linux64/libopenvr_api.so %{buildroot}%{_libdir}/%{name}/

install -Dm644 gui/images/opentrack.png %{buildroot}%{_hicolordir}/256x256/apps/opentrack.png

%desktop_file_install %{S:2}

%terra_appstream -o %{S:3}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%doc %{_datadir}/doc/%{name}/
%license OPENTRACK-LICENSING.txt WARRANTY.txt LICENSE-OpenVR 3rdparty-notices/
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_libdir}/%{name}/libopenvr_api.so
%{_datadir}/%{name}/
%{_datadir}/applications/%{appid}.desktop
%{_hicolordir}/256x256/apps/opentrack.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sun Mar 15 2026 Owen Zimmerman <owen@fyralabs.com> - 2026.1.0-1
- Port to Terra

* Wed Mar 11 2026 LionHeartP <LionHeartP@proton.me> - 2026.1.0-1
- Initial Nobara package
