%global pypi_name imageio-ffmpeg
%global _desc FFMPEG wrapper for Python.

Name:			python-%{pypi_name}
Version:		0.6.0
Release:		1%?dist
Summary:		FFMPEG wrapper for Python
License:		BSD-2-Clause
URL:			https://github.com/imageio/imageio-ffmpeg
Source0:		%url/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       imageio-ffmpeg
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n imageio-ffmpeg-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files imageio_ffmpeg

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Sun Nov 09 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
