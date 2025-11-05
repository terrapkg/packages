%global pypi_name pywebview
%global _desc Build GUI for your Python program with JavaScript, HTML, and CSS.

Name:			python-%{pypi_name}
Version:		6.1
Release:		1%?dist
Summary:		Build GUI for your Python program with JavaScript, HTML, and CSS
License:		BSD-3-Clause
URL:			https://github.com/r0x0r/pywebview
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       pywebview
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n pywebview-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files webview

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE SECURITY.md

%changelog
* Tue Nov 04 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
