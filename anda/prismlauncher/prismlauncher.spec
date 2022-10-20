%global fancy_name PrismLauncher
%global repo https://github.com/%{fancy_name}/%{fancy_name}
%bcond_without qt6 1

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

%if 0%{?suse_version}
%global build_platform openSUSE
%endif

%if 0%{?fedora}
%global build_platform Fedora
%endif

Name:           prismlauncher
Version:        5.0
Release:        3%{?dist}
Summary:        Minecraft launcher with ability to manage multiple instances
License:        GPL-3.0-only
URL:            https://prismlauncher.org/
Source0:        %{repo}/releases/download/%{version}/%{fancy_name}-%{version}.tar.gz
Patch0:         change-jars-path.patch
BuildRequires:  cmake >= 3.15
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  java-devel
%if 0%{?suse_version}
BuildRequires:  appstream-glib
%else
BuildRequires:	libappstream-glib
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(Qt%{qt_version}Concurrent) >= %{min_qt_version}
BuildRequires:  cmake(Qt%{qt_version}Core) >= %{min_qt_version}
BuildRequires:  cmake(Qt%{qt_version}Gui) >= %{min_qt_version}
BuildRequires:  cmake(Qt%{qt_version}Network) >= %{min_qt_version}
BuildRequires:  cmake(Qt%{qt_version}Test) >= %{min_qt_version}
BuildRequires:  cmake(Qt%{qt_version}Widgets) >= %{min_qt_version}
BuildRequires:  cmake(Qt%{qt_version}Xml) >= %{min_qt_version}
%if %{with qt6}
BuildRequires:  cmake(Qt6Core5Compat)
%endif
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  zlib-devel
# Prism Launcher requires QuaZip >= 1.3
%if 0%{?suse_version} >= 1550
BuildRequires:  cmake(QuaZip-Qt%{qt_version})
%endif
%if 0%{?suse_version}
Requires:       qt%{qt_version}-imageformats
Requires:       qt%{qt_version}-svg
%else
Requires:       qt%{qt_version}-qtimageformats
Requires:       qt%{qt_version}-qtsvg
%endif
Recommends:     java-openjdk-headless
# xrandr needed for LWJGL [2.9.2, 3) https://github.com/LWJGL/lwjgl/issues/128
Recommends:     xrandr
# Prism supports enabling gamemode
Recommends:     gamemode

%description
A custom launcher for Minecraft that allows you to easily manage
multiple installations of Minecraft at once (Fork of MultiMC)


%prep
%autosetup -p1 -n %{fancy_name}-%{version}

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

appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/org.prismlauncher.PrismLauncher.metainfo.xml

%check
%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop

%files
%doc README.md
%license LICENSE COPYING.md
%dir %{_datadir}/%{name}
%{_bindir}/prismlauncher
%{_datadir}/%{name}/NewLaunch.jar
%{_datadir}/%{name}/JavaCheck.jar
%{_datadir}/applications/org.prismlauncher.PrismLauncher.desktop
%{_datadir}/metainfo/org.prismlauncher.PrismLauncher.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/org.prismlauncher.PrismLauncher.svg
%{_mandir}/man?/prismlauncher.*


%changelog
* Wed Oct 19 2022 seth <getchoo at tuta dot io> - 5.0-3
- add missing deps and build with qt6 by default

* Wed Oct 19 2022 seth <getchoo at tuta dot io> - 5.0-2
- add change-jars-path.patch and allow for building on opensuse

* Wed Oct 19 2022 seth <getchoo at tuta dot io> - 5.0-1
- update to version 5.0

* Tue Oct 18 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 1.4.2.git981e9cf-0.2.20221018.981e9cf
- Update provides and obsoletes

* Tue Oct 18 2022 seth <getchoo at tuta dot io> - 1.4.2.git981e9cf-0.1.20221018.981e9cf
- start using qt6

* Tue Oct 18 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 1.4.2-1
- Repackaged as Prism Launcher

* Thu Sep 08 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Fri Jul 29 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Sat Jul 23 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.4.0-2
- Recommend gamemode

* Sat Jul 23 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Wed Jun 15 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.3.2-2
- Fixing OpenSuse Tumbleweed compilation

* Sun Jun 12 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.3.2-1
- Update to 1.3.2

* Mon May 30 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Mon May 23 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Sat May 14 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Mon Apr 25 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.2.1-2
- Correct dependencies for openSUSE

* Wed Apr 20 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Tue Apr 19 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Tue Apr 19 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.1.1-3
- Correct dependencies for openSuse

* Wed Apr 06 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.1.1-2
- Add missing dependencies

* Mon Mar 28 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Wed Mar 16 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Mon Jan 24 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.0.5-2
- remove explicit dependencies, correct dependencies to work on OpenSuse

* Sun Jan 09 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.0.5-1
- Update to 1.0.5

* Sun Jan 09 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 1.0.4-2
- rework spec

* Fri Jan 7 2022 getchoo <getchoo at tuta dot io> - 1.0.4-1
- Initial polymc spec
