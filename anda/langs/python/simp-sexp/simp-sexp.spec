%global pypi_name simp-sexp
%global _desc A simple S-expression parser.

Name:			python-%{pypi_name}
Version:		0.3.1
Release:		1%{?dist}
Summary:		A simple S-expression parser
License:		MIT
URL:			https://github.com/devbisme/simp_sexp
Source0:		%{pypi_source simp_sexp}
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
%autosetup -C

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files simp_sexp

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Sun Sep 27 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
