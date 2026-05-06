%global pypi_name openunmix
%global _desc Open-Unmix - Music Source Separation for PyTorch.

Name:			python-%{pypi_name}
Version:		1.3.0
Release:		1%{?dist}
Summary:		Open-Unmix - Music Source Separation for PyTorch
License:		MIT
URL:			https://github.com/sigsep/open-unmix-pytorch
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

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

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/umx

%changelog
* Mon May 04 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
