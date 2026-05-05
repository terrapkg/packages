%global pypi_name transformers
%global _desc The model-definition framework for state-of-the-art machine learning models.

Name:			python-%{pypi_name}
Version:		5.7.0
Release:		1%?dist
Summary:		The model-definition framework for state-of-the-art machine learning models
License:		Apache-2.0
URL:			https://huggingface.co/docs/transformers/index
Source0:		%{pypi_source}
Patch0:			versions.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       synapse-s3-storage-provider
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files transformers

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/transformers

%changelog
* Mon May 04 2026 Owen Zimmerman <owen@fyralabs.com>
- Update spec for version 5.7.0

* Sat Jan 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
