%global commit af18bcf210659b8b5a40624ffab791d49e831017
%global commit_date 20241015
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global pypi_name gay
%global _desc Colour your text / terminal to be more gay.

Name:			python-%{pypi_name}
Version:		%commit_date.%shortcommit
Release:		3%?dist
Summary:		Colour your text / terminal to be more gay
License:		MIT
URL:			https://github.com/ms-jpq/gay
Source0:		%url/archive/%commit/gay-%commit.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
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
%autosetup -n %{pypi_name}-%{commit}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gay

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/gay

%changelog
* Tue Sep 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
