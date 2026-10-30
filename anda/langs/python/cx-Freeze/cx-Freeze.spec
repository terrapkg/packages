%global pypi_name cx-Freeze
%global _desc Create standalone executables from Python scripts.

Name:			python-%{pypi_name}
Version:		8.7.4
Release:		1%{?dist}
Summary:		Create standalone executables from Python scripts
License:		PSF-2.0
URL:			https://marcelotduarte.github.io/cx_Freeze
Source0:		%{pypi_source cx_freeze}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
Requires:       patchelf

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
%pyproject_patch_dependency filelock:drop_constraints
# We are pulling in the proper patchelf package instead of a python wrapper.
%pyproject_patch_dependency patchelf:ignore

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cx_Freeze

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.md
%{_bindir}/cxfreeze
%{_bindir}/cxfreeze-quickstart

%changelog
* Wed Jan 07 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
