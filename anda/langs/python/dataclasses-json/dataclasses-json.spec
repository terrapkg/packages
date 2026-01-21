%global pypi_name dataclasses-json
%global _desc Easily serialize Data Classes to and from JSON.

%define _python_dist_allow_version_zero %{nil}

Name:			python-%{pypi_name}
Version:		0.6.7
Release:		1%?dist
Summary:		Easily serialize Data Classes to and from JSON
License:		MIT
URL:			https://github.com/lidatong/dataclasses-json
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-dynamic-versioning

Requires:       python3-marshmallow
Requires:       python3-typing-inspect

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
%autosetup -n dataclasses-json-%{version}
sed -i '/\[tool.poetry-dynamic-versioning\]/,+1d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files dataclasses_json

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Wed Jan 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
