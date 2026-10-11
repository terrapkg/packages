%global real_name fjordlauncher
%global nice_name FjordLauncher
%global appid org.unmojang.FjordLauncher

# Change this variables if you want to use custom keys
# Leave blank if you want to build Fjord Launcher without MSA id or curseforge api key
%define msa_id default
%define curseforge_key default

%global qt_version 6
%global min_qt_version 6

%global build_platform terra

Name:             fjordlauncher
Version:          11.1.1.0
Release:          1%{?dist}
Summary:          Minecraft launcher with ability to manage multiple instances and support for alternative auth server
# see COPYING.md for more information
# each file in the source also contains a SPDX-License-Identifier header that declares its license
License:          GPL-3.0-only AND Apache-2.0 AND LGPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND ISC AND OFL-1.1 AND LGPL-2.1-only AND MIT AND BSD-2-Clause-FreeBSD AND BSD-3-Clause AND LGPL-3.0-or-later
Group:            Amusements/Games
URL:              https://github.com/unmojang/FjordLauncher
Source0:          https://github.com/unmojang/FjordLauncher/archive/refs/tags/%{version}.tar.gz

BuildRequires:    cmake >= 3.15
BuildRequires:    extra-cmake-modules
BuildRequires:    gcc-c++
BuildRequires:    clang-tools-extra
# JDKs less than the most recent release & LTS are no longer in the default
# Fedora repositories
# Make sure you have Adoptium's repositories enabled
# https://fedoraproject.org/wiki/Changes/ThirdPartyLegacyJdks
# https://adoptium.net/installation/linux/#_centosrhelfedora_instructions
BuildRequires:    temurin-17-jdk
BuildRequires:    anda-srpm-macros
BuildRequires:    desktop-file-utils
BuildRequires:    libappstream-glib
BuildRequires:    cmake(Qt%{qt_version}Concurrent) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Core) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Gui) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Network) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Test) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Widgets) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Xml) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}NetworkAuth) >= %{min_qt_version}
BuildRequires:    tomlplusplus-devel
BuildRequires:    vulkan-headers
BuildRequires:    pkgconfig(libqrencode)
BuildRequires:    pkgconfig(libarchive)
BuildRequires:    pkgconfig(gamemode)

BuildRequires:    pkgconfig(libcmark)
BuildRequires:    pkgconfig(scdoc)
BuildRequires:    pkgconfig(zlib)

Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

Requires:         qt%{qt_version}-qtimageformats
Requires:         qt%{qt_version}-qtsvg
Requires:         javapackages-filesystem
Recommends:       java-25-openjdk

# xrandr needed for LWJGL [2.9.2, 3) https://github.com/LWJGL/lwjgl/issues/128
Recommends:       xrandr
# libflite needed for using narrator in minecraft
Recommends:       flite

# Prism supports enabling gamemode
Suggests:         gamemode

Obsoletes:        %{real_name}-qt5-nightly <= 9.4

Packager:         PumpkinXD <cucurbita_moschata@yeah.net>

%description
A custom launcher for Minecraft with easy management of multiple instances
and support for alternative authentication servers. (Fork of Prism Launcher)


%prep
%git_clone

# Do not set RPATH
sed -i "s|\$ORIGIN/||" CMakeLists.txt

%conf
%cmake \
  -DLauncher_QT_VERSION_MAJOR="%{qt_version}" \
  -DLauncher_BUILD_PLATFORM="%{build_platform}" \
  %if 0%{?fedora} > 41
  -DLauncher_ENABLE_JAVA_DOWNLOADER=ON \
  %endif
  %if "%{msa_id}" != "default"
  -DLauncher_MSA_CLIENT_ID="%{msa_id}" \
  %endif
  %if "%{curseforge_key}" != "default"
  -DLauncher_CURSEFORGE_API_KEY="%{curseforge_key}" \
  %endif
  -DBUILD_TESTING=OFF \
%if 0%{?fedora} > 43
  -DCMAKE_CXX_FLAGS="$CXXFLAGS -Wno-error=sfinae-incomplete -Wno-error=deprecated-declarations"
%endif

%build
%cmake_build


%install
%cmake_install
%terra_appstream

%check
%ctest


%files
%doc README.md
%license LICENSE COPYING.md
%dir %{_datadir}/%{nice_name}
%{_bindir}/fjordlauncher
%{_datadir}/%{nice_name}/NewLaunch.jar
%{_datadir}/%{nice_name}/JavaCheck.jar
%{_datadir}/%{nice_name}/qtlogging.ini
%{_datadir}/%{nice_name}/NewLaunchLegacy.jar
%{_appsdir}/org.unmojang.FjordLauncher.desktop
%{_scalableiconsdir}/org.unmojang.FjordLauncher.svg
%{_hicolordir}/256x256/apps/org.unmojang.FjordLauncher.png
%{_datadir}/mime/packages/org.unmojang.FjordLauncher.xml
%{_datadir}/qlogging-categories%{qt_version}/fjordlauncher.categories
%{_mandir}/man?/fjordlauncher.*
%{_metainfodir}/org.unmojang.FjordLauncher.metainfo.xml


%changelog
* Fri Oct 02 2026 PumpkinXD <cucurbita_moschata@yeah.net>
- Initial package

