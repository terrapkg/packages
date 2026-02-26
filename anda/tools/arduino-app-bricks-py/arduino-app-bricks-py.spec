%global pypi_name app-bricks-py
%global _desc The code of the Arduino App Lab Bricks

%global ver release/0.7.3
%global sanitized_ver %(echo %{ver} | sed 's|release/||')

Name:			%{pypi_name}
Version:		%sanitized_ver
Release:		1%?dist
Summary:		The code of the Arduino App Lab Bricks
License:		MPL-2.0
URL:			https://github.com/arduino/app-bricks-py
Source0:		%url/archive/refs/tags/release/%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-build
BuildRequires:  python3-pip
BuildRequires:  python3-docstring-parser
BuildRequires:  python3-watchdog
BuildRequires:  python3-pillow
BuildRequires:  python3-requests
BuildRequires:  python3-numpy

Provides:       arduino-app-bricks-py
Provides:       arduino-app-bricks

Requires:       python3-watchdog
Requires:       python3-%{pypi_name} = %evr

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python libaries for Arduino App Lab Bricks

%prep
%autosetup -n %{pypi_name}-release-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files arduino

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/arduino-bricks-list-modules
%{_bindir}/arduino-bricks-release
%{_bindir}/arduino-bricks-update-ai-container-ref

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
* Mon Dec 08 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
