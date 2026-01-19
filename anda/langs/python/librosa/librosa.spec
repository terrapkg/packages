%global pypi_name librosa
%global _desc Python library for audio and music analysis.

Name:			python-%{pypi_name}
Version:		0.11.0
Release:		1%?dist
Summary:		Python library for audio and music analysis
License:		MIT
URL:			https://librosa.org
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
Provides:       librosa
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n librosa-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files librosa

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md AUTHORS.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%license LICENSE.md
%python3_sitelib/librosa-%version.dist-info/*

%changelog
* Sat Dec 27 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
