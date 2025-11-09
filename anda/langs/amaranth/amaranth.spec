%global pypi_name amaranth
%global _desc A modern hardware definition language and toolchain based on Python.

%define _python_dist_allow_version_zero 1

Name:			python-%{pypi_name}
Version:		0.5.8
Release:		1%?dist
Summary:		A modern hardware definition language and toolchain based on Python
License:		BSD-2-Clause
URL:			https://github.com/amaranth-lang/amaranth
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-installer
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-packaging
BuildRequires:  python3-pip

Requires:       python3
Requires:       python3-jinja2
Requires:       python3-jschon
Requires:       python3-pyvcd

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       amaranth
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n amaranth-%version

# Swap out pdm.backend to setuptools.build_meta
sed -i 's|pdm.backend|setuptools.build_meta|' pyproject.toml

%build
export PDM_BUILD_SCM_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files amaranth

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CONTRIBUTING.txt
%license LICENSE.txt
%{_bindir}/amaranth-rpc
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc

%changelog
* Sun Sep 28 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
