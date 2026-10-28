%global pypi_name   mirascope
%global _desc       Use any frontier LLM with one unified interface.

Name:			    python-%{pypi_name}
Version:		    2.8.2
Release:		    1%{?dist}
Summary:		    Use any frontier LLM with one unified interface
License:		    MIT
URL:			    https://mirascope.com/
Source0:		    %{pypi_source}
BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-pip
BuildRequires:      python3-hatchling

Packager:	        Its-J <jonah@fyralabs.com>

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
* Tue Oct 27 2026 Its-J <jonah@fyralabs.com> - 2.8.2-1
- Initial commit
