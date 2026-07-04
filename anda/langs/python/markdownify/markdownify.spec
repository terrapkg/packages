%global pypi_name markdownify
%global _desc Convert HTML to Markdown.

Name:			python-%{pypi_name}
Version:		1.2.3
Release:		1%{?dist}
Summary:		Convert HTML to Markdown
License:		MIT
URL:			https://github.com/matthewwithanm/python-markdownify
Source0:		%{url}/archive/refs/tags/%{version}.tar.gz
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
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/markdownify

%changelog
* Sat Jul 04 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
