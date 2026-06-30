%global pypi_name magika
%global _desc A tool to determine the content type of a file with deep learning.

%undefine __brp_mangle_shebangs %{python3_sitelib}/magika/cli/

Name:			python-%{pypi_name}
Version:		1.1.0
Release:		1%{?dist}
Summary:		A tool to determine the content type of a file with deep learning
License:		Apache-2.0
URL:			https://securityresearch.google/magika/introduction/overview
Source0:		https://github.com/google/magika/archive/refs/tags/cli/v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-hatchling
BuildRequires:  maturin
BuildRequires:  pkgconfig(openssl)
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-cli-v%{version}

%pyproject_patch_dependency onnxruntime:drop_constraints

%build
pushd python
%pyproject_wheel
popd

%install
pushd python
%pyproject_install
%pyproject_save_files %{pypi_name}
popd

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%doc python/README.md
%license LICENSE
%{_bindir}/magika

%changelog
* Mon Jun 29 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
