%global real_name prismlauncher
%bcond_with qt6

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

%global build_platform unknown

%if 0%{?fedora}
%global build_platform Fedora
%endif

%if 0%{?rhel}
%global build_platform RedHat
%endif

%if 0%{?centos}
%global build_platform CentOS
%endif

%if %{with qt6}
Name:             prismlauncher
%else
Name:             prismlauncher-qt5
%endif
Version:          7.1
Release:          1%{?dist}
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

%if %{with qt6}
BuildRequires:    cmake(Qt6Core5Compat)
%endif

BuildRequires:    pkgconfig(libcmark)
BuildRequires:    pkgconfig(scdoc)
BuildRequires:    pkgconfig(zlib)

Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

Requires:         qt%{qt_version}-qtimageformats
Requires:         qt%{qt_version}-qtsvg
Requires:         javapackages-filesystem
Requires:         java-17-openjdk
Requires:         java-1.8.0-openjdk

# xrandr needed for LWJGL [2.9.2, 3) https://github.com/LWJGL/lwjgl/issues/128
Recommends:       xrandr
# libflite needed for using narrator in minecraft
Recommends:       flite

Recommends:       terra-fractureiser-detector
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

appstream-util validate-relax --nonet %buildroot%_metainfodir/org.prismlauncher.PrismLauncher.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop


%post
%if 0%{?rhel} > 8
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :
%endif


%postun
%if 0%{?rhel} > 8
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi
%endif


%posttrans
%if 0%{?rhel} > 8
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
%endif


%files
%doc README.md
%license LICENSE COPYING.md
%dir %{_datadir}/%{real_name}
%{_bindir}/prismlauncher
%{_datadir}/%{real_name}/NewLaunch.jar
%{_datadir}/%{real_name}/JavaCheck.jar
%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.prismlauncher.PrismLauncher.svg
%{_datadir}/mime/packages/modrinth-mrpack-mime.xml
%{_datadir}/qlogging-categories%{qt_version}/prismlauncher.categories
%{_datadir}/PrismLauncher/qtlogging.ini
%{_mandir}/man?/prismlauncher.*
%{_metainfodir}/org.prismlauncher.PrismLauncher.metainfo.xml


%changelog
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
