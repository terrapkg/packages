%global real_name prismlauncher
%global nice_name PrismLauncher
%bcond_without qt6

# Change this variables if you want to use custom keys
# Leave blank if you want to build Prism Launcher without MSA id or curseforge api key
%define msa_id default
%define curseforge_key default

%if %{with qt6}
%global qt_version 6
%global min_qt_version 6
%else
%global qt_version 5
%global min_qt_version 5.12
%endif

%global build_platform terra

%if %{with qt6}
Name:             prismlauncher
%else
Name:             prismlauncher-qt5
%endif
Version:          8.4
Release:          2%?dist
Summary:          Minecraft launcher with ability to manage multiple instances
# see COPYING.md for more information
# each file in the source also contains a SPDX-License-Identifier header that declares its license
License:          GPL-3.0-only AND Apache-2.0 AND LGPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND ISC AND OFL-1.1 AND LGPL-2.1-only AND MIT AND BSD-2-Clause-FreeBSD AND BSD-3-Clause AND LGPL-3.0-or-later
Group:            Amusements/Games
URL:              https://prismlauncher.org/
Source0:          https://github.com/PrismLauncher/PrismLauncher/releases/download/%{version}/%{real_name}-%{version}.tar.gz

BuildRequires:    cmake >= 3.15
BuildRequires:    extra-cmake-modules
BuildRequires:    gcc-c++
BuildRequires:    java-17-openjdk-devel
BuildRequires:    desktop-file-utils
BuildRequires:    libappstream-glib
BuildRequires:    cmake(ghc_filesystem)
BuildRequires:    cmake(Qt%{qt_version}Concurrent) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Core) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Gui) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Network) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Test) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Widgets) >= %{min_qt_version}
BuildRequires:    cmake(Qt%{qt_version}Xml) >= %{min_qt_version}
BuildRequires:    tomlplusplus-devel

%if %{with qt6}
BuildRequires:    cmake(Qt6Core5Compat)
BuildRequires:    quazip-qt6-devel
%else
BuildRequires:    quazip-qt5-devel
%endif


BuildRequires:    pkgconfig(libcmark)
BuildRequires:    pkgconfig(scdoc)
BuildRequires:    pkgconfig(zlib)

Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

Requires:         qt%{qt_version}-qtimageformats
Requires:         qt%{qt_version}-qtsvg
Requires:         javapackages-filesystem
Recommends:       java-21-openjdk
Recommends:       java-17-openjdk
Suggests:         java-1.8.0-openjdk

# xrandr needed for LWJGL [2.9.2, 3) https://github.com/LWJGL/lwjgl/issues/128
Recommends:       xrandr
# libflite needed for using narrator in minecraft
Recommends:       flite

# Prism supports enabling gamemode
Suggests:         gamemode

%if %{without qt6}
Conflicts:        %{real_name}
%endif

%description
A custom launcher for Minecraft that allows you to easily manage
multiple installations of Minecraft at once (Fork of MultiMC)


%prep
%autosetup -n PrismLauncher-%{version}

rm -rf libraries/{extra-cmake-modules,filesystem,zlib}

# Do not set RPATH
sed -i "s|\$ORIGIN/||" CMakeLists.txt


%build
%cmake \
  -DLauncher_QT_VERSION_MAJOR="%{qt_version}" \
  -DLauncher_BUILD_PLATFORM="%{build_platform}" \
  %if "%{msa_id}" != "default"
  -DLauncher_MSA_CLIENT_ID="%{msa_id}" \
  %endif
  %if "%{curseforge_key}" != "default"
  -DLauncher_CURSEFORGE_API_KEY="%{curseforge_key}" \
  %endif
  -DBUILD_TESTING=OFF

%cmake_build


%install
%cmake_install


%check
%ctest


%files
%doc README.md
%license LICENSE COPYING.md
%dir %{_datadir}/%{nice_name}
%{_bindir}/prismlauncher
%{_datadir}/%{nice_name}/NewLaunch.jar
%{_datadir}/%{nice_name}/JavaCheck.jar
%{_datadir}/%{nice_name}/qtlogging.ini
%{_datadir}/%{nice_name}/NewLaunchLegacy.jar
%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.prismlauncher.PrismLauncher.svg
%{_datadir}/mime/packages/modrinth-mrpack-mime.xml
%{_datadir}/qlogging-categories%{qt_version}/prismlauncher.categories
%{_mandir}/man?/prismlauncher.*
%{_metainfodir}/org.prismlauncher.PrismLauncher.metainfo.xml


%changelog
* Sun Jun 23 2024 Trung Lê <8@tle.id.au> - 8.2-2
- update to 8.4. Add quazip-qt deps

* Wed Apr 03 2024 seth <getchoo at tuta dot io> - 8.2-2
- move JREs to weak deps, add java 21 for snapshots

* Wed Jul 26 2023 seth <getchoo at tuta dot io> - 7.2-2
- remove terra-fractureiser-detector from recommends, use proper build platform

* Thu Jun 08 2023 seth <getchoo@tuta.io> - 6.3-3
- specify jdk 17 + cleanup outdated patches/scriptlets

* Mon Mar 20 2023 seth <getchoo at tuta dot io> - 6.3-2
- recommend flite to support narrator in minecraft

* Sat Feb 04 2023 seth <getchoo at tuta dot io> - 6.3-1
- update to 6.3

* Mon Dec 19 2022 seth <getchoo at tuta dot io> - 6.1-2
- start using non-headless java deps

* Mon Dec 12 2022 seth <getchoo at tuta dot io> - 6.0-1
- update to 6.0

* Mon Dec 05 2022 seth <getchoo at tuta dot io> - 5.2-3
- revise file to better follow fedora packaging guidelines and add java 8 as a
  dependency

* Tue Nov 15 2022 seth <getchoo at tuta dot io> - 5.2-2
- use newer version of toml++ to fix issues on aarch64

* Tue Nov 15 2022 seth <getchoo at tuta dot io> - 5.2-1
- update to 5.2

* Thu Nov 10 2022 seth <getchoo at tuta dot io> - 5.1-2
- add package to Amusements/Games

* Tue Nov 01 2022 seth <getchoo at tuta dot io> - 5.1-1
- update to 5.1

* Wed Oct 19 2022 seth <getchoo at tuta dot io> - 5.0-3
- add missing deps and build with qt6 by default

* Wed Oct 19 2022 seth <getchoo at tuta dot io> - 5.0-2
- add change-jars-path.patch to allow for package-specific jar path

* Wed Oct 19 2022 seth <getchoo at tuta dot io> - 5.0-1
- update to version 5.0

* Tue Oct 18 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 1.4.2.git981e9cf-0.2.20221018.981e9cf
- Update provides and obsoletes

* Tue Oct 18 2022 seth <getchoo at tuta dot io> - 1.4.2.git981e9cf-0.1.20221018.981e9cf
- start using qt6

* Tue Oct 18 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 1.4.2-1
- Repackaged as Prism Launcher
