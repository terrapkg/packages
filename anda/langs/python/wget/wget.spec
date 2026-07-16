%global pypi_name wget
%global _desc Pure Python download utility.

%global commit fdd3a0f8404ccab90f939f9952af139e6c55142a
%global commit_date 20141004
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:			python-%{pypi_name}
Version:		3.2
Release:		2%{?dist}
Summary:		Pure Python download utility
License:	    LicenseRef-Fedora-Public-Domain
URL:			https://pypi.org/project/wget/
Source0:		https://github.com/steveej/python-wget/archive/%commit/python-wget-%commit.zip
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-importlib-metadata
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools

Packager:	    Its-J <jonah@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{name}-%{commit}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files wget

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt

%changelog
* Sun May 24 2026 Its-J <jonah@fyralabs.com>
- Initial commit
