%global pypi_name datasets
%global _desc The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools.

Name:			python-%{pypi_name}
Version:		5.0.0
Release:		2%{?dist}
Summary:		The largest hub of ready-to-use datasets for AI models with fast, easy-to-use and efficient data manipulation tools
License:		Apache-2.0
URL:			https://github.com/huggingface/datasets
Source0:		%{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-importlib-metadata
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildArch:      noarch

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%pyproject_patch_dependency pyarrow:drop_constraints

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/datasets-cli

%changelog
* Sun May 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
