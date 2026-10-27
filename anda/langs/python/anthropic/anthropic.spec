%global pypi_name   anthropic
%global _desc       The Claude SDK for Python provides access to the Claude API from Python applications.

Name:			    python-%{pypi_name}
Version:		    2.3.0
Release:		    1%?dist
Summary:		    The Claude SDK for Python provides access to the Claude API from Python applications.
License:		    Apache-2.0 AND MIT
URL:			    https://github.com/anthropics/anthropic-sdk-python
Source0:		    %{pypi_source anthropic}
BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-hatchling
BuildRequires:      python3-hatch-fancy-pypi-readme
BuildRequires:      python3-pip

Packager:	        Its-J <jonah@fyralabs.com>

%description
%_desc

%package -n         python3-%{pypi_name}
Summary:            %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n     python3-%{pypi_name}
%_desc

%prep
%autosetup -C
%pyproject_patch_dependency hatchling:drop_constraints

%generate_buildrequires
%pyproject_buildrequires -R

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n           python3-%{pypi_name} -f %{pyproject_files}
%doc                README.md
%license            LICENSE LICENSE-MIT

%changelog
* Tue Oct 27 2026 Its-J <jonah@fyralabs.com> - 2.3.0-1
- Initial package
