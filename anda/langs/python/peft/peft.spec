%global pypi_name peft
%global _desc PEFT: State-of-the-art Parameter-Efficient Fine-Tuning.

Name:			python-%{pypi_name}
Version:		0.19.1
Release:		1%{?dist}
Summary:		PEFT: State-of-the-art Parameter-Efficient Fine-Tuning
License:		Apache-2.0
URL:			https://github.com/huggingface/peft
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-devel

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
%doc README.md
%license LICENSE

%changelog
* Mon May 04 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
