%global pypi_name inspice
%global _desc Python interface to Ngspice and Xyce circuit simulators (forked from InSpice).

Name:			python-%{pypi_name}
Version:		1.7.0.7
Release:		1%{?dist}
Summary:		Python interface to Ngspice and Xyce circuit simulators (forked from InSpice)
License:		GPL-3.0-or-later OR AGPL-3.0-or-later
URL:			https://github.com/insim-ai/InSpice
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
%autosetup -C

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files InSpice

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/inspice-post-installation

%changelog
* Sun Sep 27 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
