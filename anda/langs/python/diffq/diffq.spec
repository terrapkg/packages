%global pypi_name diffq
%global _desc DiffQ performs differentiable quantization using pseudo quantization noise.

Name:			python-%{pypi_name}
Version:		0.2.4
Release:		1%?dist
Summary:		DiffQ performs differentiable quantization using pseudo quantization noise
License:		CC-BY-NC-4.0
URL:			https://github.com/facebookresearch/diffq
Source0:		%{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  cython
BuildRequires:  gcc

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
%autosetup -n diffq-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files diffq

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Thu Jan 08 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
