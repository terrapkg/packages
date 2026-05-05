%global pypi_name bitsandbytes
%global _desc Accessible large language models via k-bit quantization for PyTorch.

Name:			python-%{pypi_name}
Version:		0.49.2
Release:		1%{?dist}
Summary:		Accessible large language models via k-bit quantization for PyTorch
License:		MIT
URL:			https://huggingface.co/docs/bitsandbytes/main/en/index
Source0:		https://github.com/bitsandbytes-foundation/bitsandbytes/archive/refs/tags/%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-scikit-build-core
BuildRequires:  python3-pip
BuildRequires:  python3-hatchling
BuildRequires:  python3-wheel
BuildRequires:  python3-cmake
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
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%license LICENSE

%changelog
* Tue May 05 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
