%global pypi_name standard-sunau
%global _desc Standard library sunau redistribution.

Name:			python-%{pypi_name}
Version:		3.13.0
Release:		1%?dist
Summary:		Standard library sunau redistribution
License:		PSF-2.0
URL:			https://github.com/youknowone/python-deadlib
Source0:		%url/archive/refs/tags/v%version.tar.gz
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
Provides:       standard-sunau
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n python-deadlib-%{version}

%build
pushd sunau
%pyproject_wheel
popd

%install
pushd sunau
%pyproject_install
%pyproject_save_files sunau
popd

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc sunau/Doc/sunau.rst
%doc sunau/README.rst
%license sunau/LICENSE

%changelog
* Sat Dec 27 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
