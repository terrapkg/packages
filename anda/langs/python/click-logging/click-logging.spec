%global pypi_name click-logging
%global _desc Simple and beautiful logging for click applications.

Name:			python-%{pypi_name}
Version:		1.0.1
Release:		1%?dist
Summary:		Simple and beautiful logging for click applications
License:		GPL-3.0
URL:			https://github.com/Toilal/click-logging
# Cannot pull from pypi due to the pypi source not having required install files, causing the build to fail
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       click-logging
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files click_logging

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE

%changelog
* Sun Dec 07 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
