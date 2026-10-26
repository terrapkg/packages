%global pypi_name libusb-package
%global _desc installation vehicle for libusb shared libraries.

Name:			python-%{pypi_name}
Version:		1.0.30.0
Release:		1%{?dist}
Summary:		installation vehicle for libusb shared libraries
License:		Apache-2.0
URL:			https://github.com/pyocd/libusb-package
Source0:		%{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
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
%pyproject_save_files libusb_package

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Sat Oct 24 2026 Owen Zimmerman <owen@fyralabs.com> - 1.0.30.0-1
- Initial commit
