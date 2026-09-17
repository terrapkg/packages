%global pypi_name rawpy
%global _desc RAW image processing for Python, a wrapper for libraw.

Name:			python-%{pypi_name}
Version:		0.27.1
Release:		1%{?dist}
Summary:		RAW image processing for Python, a wrapper for libraw
License:		MIT AND LGPL-2.1-or-later
URL:			https://pypi.python.org/pypi/rawpy
Source0:		%{pypi_source}

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
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
%license LICENSE LICENSE.LibRaw

%changelog
* Thu Jan 08 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
