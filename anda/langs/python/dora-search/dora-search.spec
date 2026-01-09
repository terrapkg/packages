%global pypi_name dora-search
%global _desc Dora is an experiment management framework. It expresses grid searches as pure python files as part of your repo. It identifies experiments with a unique hash signature. Scale up to hundreds of experiments without losing your sanity.

%define debug_package %{nil}

Name:			python-%{pypi_name}
Version:		0.1.12
Release:		1%?dist
Summary:		Experiment management framework
License:		MIT
URL:			https://github.com/facebookresearch/dora
Source0:		%url/archive/refs/tags/v%version.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%package -n     python3-%{pypi_name}-doc
Summary:        documentation for python3-%{pypi_name}

%description -n python3-%{pypi_name}-doc
documentation for python3-%{pypi_name}.

%prep
%autosetup -n dora-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dora

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/dora

%changelog
* Thu Jan 08 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
