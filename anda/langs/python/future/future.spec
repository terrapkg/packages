%global pypi_name future
%global _desc Easy, clean, reliable Python 2/3 compatibility.

Name:			python-%{pypi_name}
Version:		1.0.0
Release:		1%?dist
Summary:		Easy, clean, reliable Python 2/3 compatibility
License:		MIT
URL:			https://github.com/manrajgrover/halo
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n future-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files future

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt
%{_bindir}/futurize
%{_bindir}/pasteurize
%python3_sitelib/libfuturize/
%python3_sitelib/libpasteurize/
%python3_sitelib/past/

%changelog
* Thu Jan 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
