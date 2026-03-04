%global pypi_name standard-chunk
%global _desc Standard library chunk redistribution.

Name:			python-%{pypi_name}
Version:		3.13.0
Release:		1%?dist
Summary:		Standard library chunk redistribution
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
Provides:       standard-chunk
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n python-deadlib-%{version}

%build
pushd chunk
%pyproject_wheel
popd

%install
pushd chunk
%pyproject_install
%pyproject_save_files chunk
popd

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc chunk/Doc/chunk.rst
%doc chunk/README.rst
%license chunk/LICENSE

%changelog
* Fri Dec 26 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
