Name:           kde-material-you-colors
Version:        2.0.0
Release:        1%?dist
Summary:        Automatic Material You Colors Generator from your wallpaper for the Plasma Desktop
License:        GPL-3.0-only
URL:            https://github.com/luisbocanegra/%{name}
# The PyPi source is a more generic install and lacks the Plasmoid config
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 6.0.0
BuildRequires:  fdupes
BuildRequires:  generic-logos
BuildRequires:  libplasma-devel
BuildRequires:  plasma5support-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools) >= 61.0
BuildRequires:  python3dist(wheel) >= 0.37.1
BuildRequires:  qt5-qtbase-devel
Requires:       qt5-qtbase
Requires:       kf6-filesystem >= 6.0.0
Requires:       python3-%{name} = %{version}-%{release}
Packager:       Gilver E. <rockgrub@disroot.org>

%description
Automatic Material You Colors Generator from your wallpaper for the Plasma Desktop

%package -n     python3-%{name}
Summary:        Python files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       python3-dbus
Requires:       python3dist(numpy) >= 1.20
Requires:       python3dist(materialyoucolor) >= 2.0.9
Requires:       python3dist(pywal16)
Requires:       python3dist(pillow)
BuildArch:      noarch

%description -n python3-%{name}
Python files for KDE Material You Colors.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%pyproject_wheel
%cmake \
   -DCMAKE_INSTALL_PREFIX=%{_prefix} \
   -DINSTALL_PLASMOID=ON
%cmake_build

%install
%pyproject_install
DESTDIR="%{buildroot}" %cmake_install

sed -i "1{/^#!\/usr\/bin\/env python3/d}" %{buildroot}%{python3_sitelib}/kde_material_you_colors/main.py
%fdupes %{buildroot}%{python3_sitelib}/%{name}/


%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE
%{_bindir}/%{name}-screenshot-helper
%{_datadir}/applications/%{name}-screenshot-helper.desktop
%{_datadir}/metainfo/luisbocanegra.kdematerialyou.colors.appdata.xml
%{_datadir}/plasma/plasmoids/luisbocanegra.kdematerialyou.colors/

%files -n python3-%{name}
%{_bindir}/%{name}
%{python3_sitelib}/kde_material_you_colors/
%{python3_sitelib}/kde_material_you_colors-%{version}.dist-info/

%changelog
* Wed May 28 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
