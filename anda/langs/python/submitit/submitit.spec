%global pypi_name submitit
%global _desc Python 3.8+ toolbox for submitting jobs to Slurm.

Name:			python-%{pypi_name}
Version:		1.2.0
Release:		1%?dist
Summary:		Python 3.8+ toolbox for submitting jobs to Slurm
License:		MIT
URL:			https://github.com/facebookincubator/submitit
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
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

%package        doc
Summary:        Documentation for %{name}
Requires:       python3-%{pypi_name} = %{evr}

%description    doc
Documentation for %{name}.

%prep
%autosetup -n submitit-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files submitit

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%files doc
%doc docs/

%changelog
* Fri Jan 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
