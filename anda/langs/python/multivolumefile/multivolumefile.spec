%global pypi_name multivolumefile
%global _desc Multi-volume file wrapper library.

Name:			python-%{pypi_name}
Version:		0.2.3
Release:		1%?dist
Summary:		Multi-volume file wrapper library
License:		LGPL-2.1-or-later
URL:			https://github.com/miurahr/multivolume
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
%dnl BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Its-J <jonah@fyralabs.com>

%description
%{_desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{_desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Wed Sep 16 2026 Its-J <jonah@fyralabs.com> - 0.2.3-1
- Initial commit
