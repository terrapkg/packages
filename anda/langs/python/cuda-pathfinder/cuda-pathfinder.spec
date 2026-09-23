%global pypi_name cuda-pathfinder
%global _desc Pathfinder for CUDA components.

%define _python_dist_allow_version_zero 1

Name:			python-%{pypi_name}
Version:		13.4.3
Release:		1%{?dist}
Summary:		Pathfinder for CUDA components
License:		Apache-2.0
URL:			https://nvidia.github.io/cuda-python/latest/
Source0:        https://github.com/NVIDIA/cuda-python/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildArch:      noarch

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
pushd cuda_pathfinder
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
popd

%install
pushd cuda_pathfinder
%pyproject_install
%pyproject_save_files cuda
popd

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md cuda_pathfinder/docs/* cuda_pathfinder/README.md
%license LICENSE

%changelog
* Fri Sep 18 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
