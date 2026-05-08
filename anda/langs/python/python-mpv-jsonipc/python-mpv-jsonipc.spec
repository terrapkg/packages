%global pypi_name python-mpv-jsonipc
%global _desc Python API to MPV using JSON IPC.

Name:			python-%{pypi_name}
Version:		1.2.1
Release:		1%?dist
Summary:		Python API to MPV using JSON IPC
License:		Apache-2.0
URL:			https://github.com/iwalton3/python-mpv-jsonipc
Source0:		%{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       python-mpv-jsonipc
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files python_mpv_jsonipc

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.md

%changelog
* Sun Dec 07 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
