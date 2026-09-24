%global kcgroups_src kcgroups-kcgroups-dmemcg-experimental
%global booster_src kcgroups-booster-dmemcg-experimental

Name:           kcgroups-dmemcg
Version:        0.1
Release:        2%{?dist}
Summary:        KDE library to manipulate cgroups - fork adding dmem cgroup support
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
License:        LGPL-2.1-or-later AND MIT AND CC0-1.0
URL:            https://github.com/pixelcluster/kcgroups

Source0:        %{url}/archive/refs/tags/kcgroups-dmemcg-experimental.tar.gz
Source1:        %{url}/archive/refs/tags/booster-dmemcg-experimental.tar.gz
Source2:        %{url}/tree/dmemcg/LICENSES

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
BuildRequires:  plasma-workspace-devel
BuildRequires:  kf6-kwindowsystem-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-kitemmodels-devel
BuildRequires:  systemd-rpm-macros

Requires:       qt6-qtbase
Requires:       kf6-kwindowsystem
Requires:       kf6-kconfig
Requires:       kf6-kdbusaddons

Conflicts:      kcgroups-git

%description
KDE library to manipulate cgroups (and boost foreground apps).
This is a fork adding dmem cgroup support.

%package -n plasma-foreground-booster-dmemcg
Summary:        Plasma foreground booster with dmemcg support
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n plasma-foreground-booster-dmemcg
Plasma foreground booster utilizing dmem cgroup support.

%package devel
Summary:        Development files for kcgroups-dmemcg
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and CMake files for kcgroups-dmemcg.

%prep
%setup -q -c -n %{name}-%{version} -a 0 -a 1

%build
mkdir kcgroups-build
mkdir kcgroups-install
mkdir booster-build

pushd kcgroups-build
cmake ../%{kcgroups_src} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_WITH_QT6=ON
make %{?_smp_mflags}

make DESTDIR=$(pwd)/../kcgroups-install install
popd

pushd booster-build
export CMAKE_PREFIX_PATH=$(pwd)/../kcgroups-install%{_prefix}
cmake ../%{booster_src} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DBUILD_WITH_QT6=ON
make %{?_smp_mflags}

%install
pushd kcgroups-build
make DESTDIR=%{buildroot} install
popd

pushd booster-build
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}

cp -r %{S:2} %{buildroot}%{_defaultlicensedir}/%{name}/

%post -n plasma-foreground-booster-dmemcg
%systemd_user_post plasma-foreground-booster.service

%preun -n plasma-foreground-booster-dmemcg
%systemd_user_preun plasma-foreground-booster.service

%postun -n plasma-foreground-booster-dmemcg
%systemd_user_postun_with_restart plasma-foreground-booster.service

%files
%license %{_defaultlicensedir}/%{name}/LICENSES
%{_libdir}/libKF5CGroups.so.5*
%{_datadir}/qlogging-categories6/kcgroups.*

%files devel
%{_includedir}/KF6/
%{_libdir}/cmake/KF5CGroups/
%{_libdir}/libKF5CGroups.so
%{_libdir}/qt6/mkspecs/modules/qt_KCGroups.pri

%files -n plasma-foreground-booster-dmemcg
%{_bindir}/foreground_booster
%{_userunitdir}/plasma-foreground-booster.service
%{_datadir}/applications/org.kde.foreground-booster.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/org.kde.foreground-booster.desktop

%changelog
* Thu May 21 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.1-1
- Brought to Terra repo unmodified

* Fri Apr 17 2026 LionHeartP <LionHeartP@proton.me> - 0.1-1
- Initial spec derived from AUR PKGBUILD https://aur.archlinux.org/packages/plasma-foreground-booster-dmemcg
