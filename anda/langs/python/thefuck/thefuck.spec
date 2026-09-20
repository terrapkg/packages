%global pypi_name thefuck
%global _desc Magnificent app which corrects your previous console command.

Name:			python-%{pypi_name}
Version:		3.34
Release:		1%{?dist}
Summary:		Magnificent app which corrects your previous console command
License:		MIT
URL:			https://github.com/C14147/thefuck
# This is a fork, as the main repo has not been updated in years. Because of this we will not use {pypi_source}
Source0:		https://github.com/C14147/thefuck/archive/refs/tags/3.34.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Requires:       python3-pyte

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
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.md
%{_bindir}/fuck
%{_bindir}/thefuck

%changelog
* Thu Aug 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
