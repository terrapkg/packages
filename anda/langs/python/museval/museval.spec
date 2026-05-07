%global pypi_name museval
%global _desc Source separation evaluation tools for python.

Name:			python-%{pypi_name}
Version:		0.4.1
Release:		1%?dist
Summary:		Source separation evaluation tools for python
License:		MIT
URL:			https://github.com/sigsep/sigsep-mus-eval
Source0:		%{pypi_source}
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
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n museval-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files museval

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/bsseval
%{_bindir}/museval

%changelog
* Thu Jan 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
