%global pypi_name sisou
%global _desc A powerful tool to conveniently update all of your ISOs!

Name:			python-%{pypi_name}
Version:		2.4.1
Release:		1%{?dist}
Summary:		%{_desc}
License:		GPL-3.0-or-later
URL:			https://github.com/JoshuaVandaele/SuperISOUpdater
Source0:		%url/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%{_desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       sisou
Provides:       SuperISOUpdater
Provides:       superisoupdater
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{_desc}

%prep
%autosetup -n SuperISOUpdater-%{version}

%pyproject_patch_dependency requests-cache:drop_constraints

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sisou

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/sisou
%{python3_sitelib}/sisou-%{version}.dist-info/*
%{python3_sitelib}/config/*.py
%{python3_sitelib}/config/__pycache__/*.cpython-*.pyc
%{python3_sitelib}/config/__pycache__/*.cpython-*.*-*.pyc
%{python3_sitelib}/modules/*.py
%{python3_sitelib}/config/sisou.toml.default
%{python3_sitelib}/modules/mirrors/
%{python3_sitelib}/modules/__pycache__/*.pyc
%{python3_sitelib}/modules/updaters/*.py
%{python3_sitelib}/modules/updaters/__pycache__/*.pyc
%{_prefix}/sisou/config/sisou.toml.default

%changelog
* Wed Oct 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
