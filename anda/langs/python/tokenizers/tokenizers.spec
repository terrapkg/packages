%global pypi_name tokenizers
%global _desc Fast State-of-the-Art Tokenizers optimized for Research and Production.

Name:			python-%{pypi_name}
Version:		0.22.2
Release:		1%?dist
Summary:		Fast State-of-the-Art Tokenizers optimized for Research and Production
License:		Apache-2.0
URL:			https://github.com/huggingface/tokenizers
Source0:		%{pypi_source}
Source1:        https://github.com/huggingface/tokenizers/blob/main/LICENSE
Source2:        https://github.com/huggingface/tokenizers/blob/main/README.md

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  maturin
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
%autosetup -n tokenizers-%{version}
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tokenizers

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Sat Jan 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
