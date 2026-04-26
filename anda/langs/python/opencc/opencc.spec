%global pypi_name opencc
%global _desc Open Chinese Convert.

Name:			python-%{pypi_name}
Version:		1.3.0
Release:		1%{?dist}
Summary:		Open Chinese Convert
License:		Apache-2.0
URL:			https://github.com/BYVoid/OpenCC
Source0:		%{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  gcc-c++
BuildRequires:  cmake

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
%doc README.md AUTHORS
%license LICENSE

%changelog
* Sun Mar 29 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
