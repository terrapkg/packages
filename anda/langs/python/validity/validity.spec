# Doesn't exist on pypi
%global pkg_name validity
%global _desc Validity fingerprint sensor prototype.

Name:			python-%{pkg_name}
Version:		0.15
Release:		1%{?dist}
Summary:		Validity fingerprint sensor prototype
License:		MIT
URL:			https://github.com/uunicorn/python-validity
Source0:		%{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-hatchling

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
%_desc

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pkg_name}sensor

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/validity-led-dance
%{_bindir}/validity-sensors-firmware
%{_libdir}/python-validity/dbus-service
%config %{_datadir}/dbus-1/system.d/io.github.uunicorn.Fprint.conf
%{_datadir}/python-validity/playground/__pycache__/*.pyc
%{_datadir}/python-validity/playground/*.py

%changelog
* Tue Aug 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
