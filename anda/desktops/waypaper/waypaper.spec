%global pypi_name waypaper
%global _desc GUI wallpaper manager for Wayland and Xorg Linux systems.

%define _python_dist_allow_version_zero 1

Name:			python-%{pypi_name}
Version:		2.7
Release:		1%?dist
Summary:		GUI wallpaper manager for Wayland and Xorg Linux systems
License:		GPL-3.0-only
URL:			https://github.com/anufrievroman/waypaper
Source0:		%url/archive/refs/tags/%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       waypaper
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n waypaper-%version

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files waypaper

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/waypaper
%{_datadir}/applications/waypaper.desktop
%{_datadir}/icons/hicolor/scalable/apps/waypaper.svg
%{_mandir}/man1/waypaper.1.gz
%dnl %python3_sitelib/__pycache__/*.cpython-*.pyc
%dnl %python3_sitelib/waypaper/subcommands/__pycache__/*.cpython-*.pyc

%changelog
* Sun Nov 09 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
