
%global libnbtplusplus_commit       2203af7eeb48c45398139b583615134efd8d407f
%global libnbtplusplus_shortcommit  %(c=%{libnbtplusplus_commit}; echo ${c:0:7})
%global quazip_commit               6117161af08e366c37499895b00ef62f93adc345
%global quazip_shortcommit          %(c=%{quazip_commit}; echo ${c:0:7})
%global tomlplusplus_commit         4b166b69f28e70a416a1a04a98f365d2aeb90de8
%global tomlplusplus_shortcommit    %(c=%{tomlplusplus_commit}; echo ${c:0:7})
%global filesystem_commit           cd6805e94dd5d6346be1b75a54cdc27787319dd2
%global filesystem_shortcommit      %(c=%{filesystem_commit}; echo ${c:0:7})

Name:           prism-launcher
Version:        1.4.2.git0868a5e5
Release:        1%{?dist}
Summary:        Minecraft launcher with ability to manage multiple instances

#
# CC-BY-SA
# ---------------------------------------
# launcher/resources/multimc/
#
# BSD 3-clause "New" or "Revised" License
# ---------------------------------------
# application/
# libraries/LocalPeer/
# libraries/ganalytics/
#
# Boost Software License (v1.0)
# ---------------------------------------
# cmake/
#
# Expat License
# ---------------------------------------
# libraries/systeminfo/
#
# GNU Lesser General Public License (v2 or later)
# ---------------------------------------
# libraries/rainbow
#
# GNU Lesser General Public License (v2.1 or later)
# ---------------------------------------
# libraries/iconfix/
# libraries/quazip/
#
# GNU Lesser General Public License (v3 or later)
# ---------------------------------------
# libraries/libnbtplusplus/
#
# GPL (v2)
# ---------------------------------------
# libraries/pack200/
#
# ISC License
# ---------------------------------------
# libraries/hoedown/
#
# zlib/libpng license
# ---------------------------------------
# libraries/quazip/quazip/unzip.h
# libraries/quazip/quazip/zip.h
#

License:        CC-BY-SA and ASL 2.0 and BSD and Boost and LGPLv2 and LGPLv2+ and LGPLv3+ and GPLv2 and GPLv2+ and GPLv3 and ISC and zlib
URL:            https://polymc.org
Source0:        https://github.com/PlaceholderMC/PrismLauncher/archive/refs/heads/develop.zip

#Source0:        https://github.com/PolyMC/PolyMC/archive/%{version}/polymc-%{version}.tar.gz
Source1:        https://github.com/PolyMC/libnbtplusplus/archive/%{libnbtplusplus_commit}/libnbtplusplus-%{libnbtplusplus_shortcommit}.tar.gz
Source2:        https://github.com/stachenov/quazip/archive/%{quazip_commit}/quazip-%{quazip_shortcommit}.tar.gz
Source3:        https://github.com/marzer/tomlplusplus/archive/%{tomlplusplus_commit}.tar.gz#/tomlplusplus-%{tomlplusplus_shortcommit}.tar.gz
Source4:        https://github.com/gulrak/filesystem/archive/%{filesystem_commit}.tar.gz#/filesystem-%{filesystem_shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules

BuildRequires:  java-devel
BuildRequires:  %{?suse_version:lib}qt5-qtbase-devel
# require zlib to ensure we do not compile against zlib-ng
BuildRequires:  zlib zlib-devel
BuildRequires:  scdoc
BuildRequires:  git-core

# Needed for loading SVG Icons for Themes
%if 0%{?suse_version}
Requires:       libQt5Svg5
%else
Requires:       qt5-qtsvg
%endif

# Needed for a variety of Image formats fetched from the web
Requires:       %{?suse_version:lib}qt5-qtimageformats
# LWJGL uses xrandr for detection
Requires:       xrandr

# Minecraft <  1.17
Recommends:     java-1.8.0-openjdk
# Minecraft >= 1.17
Recommends:     java-17-openjdk
# PolyMC supports enabling gamemode
Recommends:     gamemode

%description
PolyMC is a free, open source launcher for Minecraft. It allows you to have
multiple, separate instances of Minecraft (each with their own mods, texture
packs, saves, etc) and helps you manage them and their associated options with
a simple interface.


%prep
# %%autosetup -p1 -n PolyMC-%{version}
%autosetup -n PrismLauncher-develop -Sgit


git remote add origin https://github.com/PlaceholderMC/PrismLauncher.git

git submodule update --init --recursive

tar -xvf %{SOURCE1} -C libraries
tar -xvf %{SOURCE2} -C libraries
tar -xvf %{SOURCE3} -C libraries
tar -xvf %{SOURCE4} -C libraries
rmdir libraries/libnbtplusplus libraries/quazip
mv -f libraries/quazip-%{quazip_commit} libraries/quazip
mv -f libraries/libnbtplusplus-%{libnbtplusplus_commit} libraries/libnbtplusplus
mv -f libraries/tomlplusplus-%{tomlplusplus_commit}/* libraries/tomlplusplus
mv -f libraries/filesystem-%{filesystem_commit}/* libraries/filesystem


%build
%cmake \
    -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
    -DLauncher_FORCE_BUNDLED_LIBS:BOOL=ON \
    -DLauncher_QT_VERSION_MAJOR=5 \
    -DLauncher_UPDATER_BASE:STRING=""

%cmake_build

%install
%cmake_install


%check
# skip tests on systems that aren't officially supported
%if ! 0%{?suse_version}
# check why broken
#%%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/org.polymc.PolyMC.desktop
%endif


%files
%license COPYING.md
%{_bindir}/polymc
%{_datadir}/icons/hicolor/scalable/apps/org.polymc.PolyMC.svg
%{_datadir}/applications/org.polymc.PolyMC.desktop
%{_datadir}/metainfo/org.polymc.PolyMC.metainfo.xml
%{_datadir}/jars/NewLaunch.jar
%{_datadir}/jars/JavaCheck.jar
%{_mandir}/man6/polymc.6*
#%%config %%{_sysconfdir}/ld.so.conf.d/*


%changelog
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