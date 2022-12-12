%define real_name prismlauncher
%global tomlplusplus_commit 0a90913abf9390b9e08ab6d3b40ac11634553f38
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

Name:             prismlauncher-qt5
Version:          6.0
Release:          3%{?dist}
Summary:          Minecraft launcher with ability to manage multiple instances
License:          GPL-3.0-only
Group:            Amusements/Games
URL:              https://prismlauncher.org/
Source0:          https://github.com/PrismLauncher/PrismLauncher/releases/download/%{version}/%{real_name}-%{version}.tar.gz
Source1:          https://github.com/marzer/tomlplusplus/archive/%{tomlplusplus_commit}/tomlplusplus-%{tomlplusplus_commit}.tar.gz
Patch0:           fix-disable-FLOAT16-in-toml.patch

BuildRequires:    cmake >= 3.15
BuildRequires:    extra-cmake-modules
BuildRequires:    gcc-c++
BuildRequires:    java-devel >= 17
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

BuildRequires:    pkgconfig(scdoc)
BuildRequires:    pkgconfig(zlib)

Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils

Requires:         qt%{qt_version}-qtimageformats
Requires:         qt%{qt_version}-qtsvg
Requires:         javapackages-filesystem
Requires:         java-headless >= 17
Requires:         java-1.8.0-openjdk-headless

# xrandr needed for LWJGL [2.9.2, 3) https://github.com/LWJGL/lwjgl/issues/128
Recommends:       xrandr
# Prism supports enabling gamemode
Suggests:         gamemode

Conflicts:        prismlauncher


%description
A custom launcher for Minecraft that allows you to easily manage
multiple installations of Minecraft at once (Fork of MultiMC)


%prep
%autosetup -n PrismLauncher-%{version}

tar -xzf %{SOURCE1} -C libraries
rm -rf libraries/tomlplusplus/*
mv -f libraries/tomlplusplus-%{tomlplusplus_commit}/* libraries/tomlplusplus

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

%cmake_build


%install
%cmake_install


%check
%ctest

%if 0%{?fedora} > 35
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/org.prismlauncher.PrismLauncher.metainfo.xml
%endif

desktop-file-validate %{buildroot}%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop


%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%doc README.md
%license LICENSE COPYING.md
%dir %{_datadir}/%{real_name}
%{_bindir}/prismlauncher
%{_datadir}/%{real_name}/NewLaunch.jar
%{_datadir}/%{real_name}/JavaCheck.jar
%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop
%{_metainfodir}/org.prismlauncher.PrismLauncher.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/org.prismlauncher.PrismLauncher.svg
%{_mandir}/man?/prismlauncher.*


%changelog
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
