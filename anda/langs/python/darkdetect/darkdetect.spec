%global pypi_name darkdetect
%global _desc Detect OS Dark Mode from Python.

Name:			python-%{pypi_name}
Version:		0.8.0
Release:		1%?dist
Summary:		Detect OS Dark Mode from Python
License:		BSD-3-Clause
URL:			https://github.com/albertosottile/darkdetect
Source0:		%{pypi_source}
BuildArch:      noarch

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

%package -n     python3-%{pypi_name}-doc
Summary:        documentation for python3-%{pypi_name}

%description -n python3-%{pypi_name}-doc
documentation for python3-%{pypi_name}.

%prep
%autosetup -n darkdetect-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files darkdetect

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Wed Jan 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
