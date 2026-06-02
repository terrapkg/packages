%global pypi_name standard-asynchat
%global _desc Standard library asynchat redistribution.

Name:			python-%{pypi_name}
Version:		3.13.0
Release:		1%?dist
Summary:		Standard library asynchat redistribution
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
Provides:       standard-asynchat
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n python-deadlib-%{version}

%build
pushd asynchat
%pyproject_wheel
popd

%install
pushd asynchat
%pyproject_install
%pyproject_save_files asynchat
popd

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc asynchat/Doc/asynchat.rst
%doc asynchat/README.rst
%license asynchat/LICENSE

%changelog
* Mon Jan 12 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
