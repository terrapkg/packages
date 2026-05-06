%global appid luisbocanegra.kdematerialyou.colors
%global developer "Luis Bocanegra"
%global org "com.github.luisbocanegra"
%global pypi_name kde_material_you_colors

Name:           kde-material-you-colors
Version:        2.2.0
Release:        3%{?dist}
Summary:        Automatic Material You Colors Generator from your wallpaper for the Plasma Desktop
License:        GPL-3.0-only
URL:            https://github.com/luisbocanegra/%{name}
# The PyPi source is a more generic install and lacks the Plasmoid config
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 6.0.0
BuildRequires:  generic-logos
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools) >= 61.0
BuildRequires:  python3dist(wheel) >= 0.37.1
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  pkgconfig(ocl-icd)
Requires:       qt5-qtbase
Requires:       kf6-filesystem >= 6.0.0
Requires:       python3-%{name} = %{evr}
Packager:       Gilver E. <roachy@fyralabs.com>

%description
Automatic Material You Colors Generator from your wallpaper for the Plasma Desktop

%package -n     python3-%{name}
Summary:        Python files for %{name}
Requires:       %{name} = %{evr}
Requires:       python%{python3_version}dist(file-magic)
Requires:       python%{python3_version}dist(pywal16)
BuildArch:      noarch

%description -n python3-%{name}
Python files for KDE Material You Colors.

%prep
%autosetup -n %{name}-%{version}
%pyproject_patch_dependency python-magic:ignore

%conf
%cmake \
   -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
   -DINSTALL_PLASMOID="ON"

%build
%pyproject_wheel
%cmake_build

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
%cmake_install

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE
%{_bindir}/%{name}-screenshot-helper
%{_appsdir}/%{name}-screenshot-helper.desktop
%{_datadir}/plasma/plasmoids/%{appid}/

%files -n python3-%{name} -f %{pyproject_files}
%{_bindir}/%{name}

%changelog
* Tue May 5 2026 Gilver E. <roachy@fyralabs.com> - 2.2.0-4
- Refactor build around new RPM macros
* Wed May 28 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
