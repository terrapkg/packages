%global pypi_name sisou
%global _desc A powerful tool to conveniently update all of your ISOs!

Name:			python-%{pypi_name}
Version:		1.5.0
Release:		1%?dist
Summary:		%{_desc}
License:		GPLv3
URL:			https://github.com/JoshuaVandaele/SuperISOUpdater
Source0:		%url/archive/refs/tags/%{version}.tar.gz
Patch0:         remove-version-reqs.patch
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
%autosetup -p1 -n SuperISOUpdater-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sisou

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/sisou
%ghost %{python3_sitelib}/__pycache__/*.cpython-*.pyc
%ghost %{python3_sitelib}/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%{python3_sitelib}/sisou-%{version}.dist-info/*
%{python3_sitelib}/config/*.py
%{python3_sitelib}/config/__pycache__/*.cpython-*.pyc
%{python3_sitelib}/config/__pycache__/*.cpython-*.*-*.pyc
%{python3_sitelib}/config/config.toml.default
%{python3_sitelib}/modules/*.py
%{python3_sitelib}/modules/__pycache__/*.pyc
%{python3_sitelib}/modules/updaters/*.py
%{python3_sitelib}/modules/updaters/__pycache__/*.pyc

%changelog
* Wed Oct 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
