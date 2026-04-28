%global pypi_name click_params
%global _desc A bunch of useful click parameter types.

Name:			python-%{pypi_name}
Version:		0.5.0
Release:		1%?dist
Summary:		Bunch of click parameters to use
License:		Apache-2.0
URL:			https://click-params.readthedocs.io/en/stable/
Source0:		https://github.com/click-contrib/click_params/archive/refs/tags/%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       click_params
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%package -n     python3-%{pypi_name}-doc
Summary:        documentation for python3-%{pypi_name}

%description -n python3-%{pypi_name}-doc
documentation for python3-%{pypi_name}.

%prep
%autosetup -n click_params-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files click_params
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a docs/ %{buildroot}%{_pkgdocdir}/

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CONTRIBUTING.md CHANGELOG.md
%license LICENSE

%files -n python3-%{pypi_name}-doc
%license LICENSE
%{_pkgdocdir}/
%license LICENSE

%changelog
* Sat Dec 27 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
