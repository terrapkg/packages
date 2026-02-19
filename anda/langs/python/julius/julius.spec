%global pypi_name julius
%global _desc Fast PyTorch based DSP for audio and 1D signals.

Name:			python-%{pypi_name}
Version:		0.2.7
Release:		1%?dist
Summary:		Fast PyTorch based DSP for audio and 1D signals
License:		MIT
URL:			https://github.com/adefossez/julius
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-build
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

%prep
%autosetup -n julius-%version

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files julius

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Fri Jan 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
