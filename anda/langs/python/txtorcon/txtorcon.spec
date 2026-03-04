%global pypi_name txtorcon
%global _desc Twisted-based asynchronous Tor control protocol implementation. Includes unit-tests, examples, state-tracking code and configuration abstraction.

Name:			python-%{pypi_name}
Version:		24.8.0
Release:		1%?dist
Summary:		Twisted-based asynchronous Tor control protocol implementation. Includes unit-tests, examples, state-tracking code and configuration abstraction
License:		MIT
URL:			https://github.com/meejah/txtorcon
Source0:		%{pypi_source}
Patch0:         shebangs.patch
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
Provides:       txtorcon
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -p1 -n txtorcon-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files txtorcon

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst INSTALL
%license LICENSE
%python3_sitelib/twisted/plugins/__pycache__/txtorcon_endpoint_parser.*.pyc
%python3_sitelib/txtorcon-%version.dist-info/*
%python3_sitelib/twisted/plugins/*.py
%{_datadir}/txtorcon/*

%changelog
* Mon Nov 03 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
