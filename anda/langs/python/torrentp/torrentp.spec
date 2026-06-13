%global pypi_name torrentp
%global _desc Python torrent downloader - Download from torrent with .torrent file or magnet link, with just 3 lines of python code.

Name:			python-%{pypi_name}
Version:		0.2.7
Release:		1%{?dist}
Summary:		Python torrent downloader - Download from torrent with .torrent file or magnet link, with just 3 lines of python code
License:		BSD-2-Clause
URL:			https://github.com/iw4p/torrentp
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
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}
%pyproject_patch_dependency rich:drop_constraints

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/torrentp

%changelog
* Sun Jun 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
