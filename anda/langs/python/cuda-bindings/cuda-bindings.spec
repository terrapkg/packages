%global pypi_name cuda_bindings
%global _desc standard set of low-level interfaces, providing full coverage of and 1:1 access to the CUDA host APIs from Python.

%undefine _debugsource_packages

Name:			python-%{pypi_name}
Version:		13.4.2
Release:		1%{?dist}
Summary:		standard set of low-level interfaces, providing full coverage of and 1:1 access to the CUDA host APIs from Python
License:		Apache-2.0
URL:			https://nvidia.github.io/cuda-python/latest/
Source0:        https://github.com/NVIDIA/cuda-python/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  cuda-nvrtc-devel
%dnl BuildRequires:  libnvvm-devel
BuildRequires:  libcufile-devel
BuildRequires:  cuda-profiler-devel
BuildRequires:  cuda-cudart-devel
BuildRequires:  cuda-cudart-static
BuildRequires:  cuda-crt
BuildRequires:  gcc-c++

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
pushd cuda_bindings
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
export CUDA_PATH=/usr/bin/
%pyproject_wheel
popd

%install
pushd cuda_bindings
%pyproject_install
%pyproject_save_files cuda
popd

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md cuda_bindings/docs/* cuda_bindings/README.md
%license LICENSE

%changelog
* Fri Sep 18 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
