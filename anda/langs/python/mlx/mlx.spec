%global pypi_name mlx
%global _desc MLX: An array framework for Apple silicon.

Name:			python-%{pypi_name}
Version:		0.32.2
Release:		1%?dist
Summary:		MLX: An array framework for Apple silicon
License:		MIT
URL:			https://ml-explore.github.io/mlx/build/html/index.html
Source0:		https://github.com/ml-explore/mlx/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-accelerate
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  openblas-devel

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
export PYPI_RELEASE=1
export CMAKE_ARGS="-DBLAS_INCLUDE_DIRS=/usr/include/openblas -DLAPACK_INCLUDE_DIRS=/usr/include/openblas -DCMAKE_INSTALL_LIBDIR=lib"
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/mlx.distributed_config
%{_bindir}/mlx.launch

%changelog
* Sun Mar 29 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
