%global pypi_name pyfluidsynth
%global _desc Python bindings for FluidSynth.

Name:			python-%{pypi_name}
Version:		1.4.0
Release:		2%{?dist}
Summary:		Python bindings for FluidSynth
License:		LGPL-2.1
URL:			https://github.com/nwhitehead/pyfluidsynth
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-build

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n pyfluidsynth-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fluidsynth

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{python3_sitelib}/fluidsynth.py

%changelog
* Sat Jan 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
