%global pypi_name lhotse
%global _desc Tools for handling multimodal data in machine learning projects.

Name:			python-%{pypi_name}
Version:		1.33.0
Release:		2%{?dist}
Summary:		Tools for handling multimodal data in machine learning projects
License:        Apache-2.0
URL:			https://lhotse.readthedocs.io/en/latest/
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%git_clone https://github.com/lhotse-speech/lhotse.git %{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/lhotse

%changelog
* Sun May 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
