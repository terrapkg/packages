%global pypi_name nemo_toolkit
%global real_name nemo-toolkit
%global _desc A scalable generative AI framework built for researchers and developers working on Large Language Models, Multimodal, and Speech AI (Automatic Speech Recognition and Text-to-Speech).

Name:			python-%{real_name}
Version:		2.7.3
Release:		1%{?dist}
Summary:		Scalable generative AI framework built for researchers and developers
License:		Apache-2.0
URL:			https://docs.nvidia.com/nemo/speech/nightly/index.html
Source0:		%{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-hatchling
BuildRequires:  python3-importlib-metainfo
BuildRequires:  python3-setuptools
BuildArch:      noarch

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{real_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{real_name}}

%description -n python3-%{real_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%pyproject_patch_dependency protobuf:drop_constraints
%pyproject_patch_dependency fsspec:drop_constraints

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nemo
%pyproject_save_files scripts
%pyproject_save_files tests

%files -n python3-%{real_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{python3_sitelib}/nemo/
%{python3_sitelib}/scripts/
%{python3_sitelib}/examples/

%changelog
* Sun May 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
