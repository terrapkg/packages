%global pypi_name fx2
%global _desc Chip support package for Cypress EZ-USB FX2 series microcontrollers.

Name:			python-%{pypi_name}
Version:		0.13
Release:		1%?dist
Summary:		Chip support package for Cypress EZ-USB FX2 series microcontrollers
License:		0BSD
URL:			https://github.com/whitequark/libfx2
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-pdm-backend
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

Requires:       python3dist(libusb1)

Provides:       fx2
Provides:       python3-fx2
Provides:       libfx2
Provides:       python3-libfx2

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n libfx2-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
pushd software
%pyproject_wheel
popd

%install
%pyproject_install
%pyproject_save_files fx2

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE-0BSD.txt
%{_bindir}/fx2tool
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc

%changelog
* Sun Sep 28 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
