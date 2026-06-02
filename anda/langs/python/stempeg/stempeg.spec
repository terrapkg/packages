%global pypi_name stempeg
%global _desc Python I/O for STEM audio files.

Name:			python-%{pypi_name}
Version:		0.2.6
Release:		1%?dist
Summary:		Python I/O for STEM audio files
License:		MIT
URL:			https://faroit.com/stempeg/
Source0:		%{pypi_source}
BuildArch:      noarch

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
%autosetup -n stempeg-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files stempeg

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/stem2files

%changelog
* Thu Jan 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
