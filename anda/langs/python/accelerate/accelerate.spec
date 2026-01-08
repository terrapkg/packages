%define debug_package %{nil}

%global pypi_name accelerate
%global _desc A simple way to launch, train, and use PyTorch models on almost any device and distributed configuration, automatic mixed precision (including fp8), and easy-to-configure FSDP and DeepSpeed support.

Name:			python-%{pypi_name}
Version:		1.12.0
Release:		1%?dist
Summary:		A simple way to launch, train, and use PyTorch models on almost any device and distributed configuration
License:		Apache-2.0
URL:			https://github.com/huggingface/accelerate
# pypi_source does not include all doc files
Source0:		%url/archive/refs/tags/v%version.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n accelerate-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files accelerate

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/%{pypi_name}
%{_bindir}/%{pypi_name}-config
%{_bindir}/%{pypi_name}-estimate-memory
%{_bindir}/%{pypi_name}-launch
%{_bindir}/%{pypi_name}-merge-weights

%changelog
* Wed Jan 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
