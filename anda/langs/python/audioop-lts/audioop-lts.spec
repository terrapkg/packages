%global pypi_name audioop-lts
%global _desc An LTS port of Python's `audioop` module.

Name:			python-%{pypi_name}
Version:		0.2.2
Release:		1%?dist
Summary:		An LTS port of Python's `audioop` module
License:		PSF-2.0
URL:			https://github.com/AbstractUmbra/audioop
Source0:		%url/archive/refs/tags/%version.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  gcc

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       audioop-lts
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n audioop-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files audioop

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%doc docs/audioop.rst
%license LICENSE

%changelog
* Fri Dec 26 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
