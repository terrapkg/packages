# Doesn't exist on pypi
%global pkg_name open-fprintd
%global _desc Fprintd replacement which allows you to have your own backend as a standalone service.

Name:			python-%{pkg_name}
Version:		0.7
Release:		1%{?dist}
Summary:		Fprintd replacement which allows you to have your own backend as a standalone service
License:		GPL-2.0-or-later
URL:			https://github.com/uunicorn/open-fprintd
Source0:		%{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-hatchling
Conflicts:      fprintd

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pkg_name}
Provides:       open-fprintd
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
%_desc

%prep
%autosetup -C

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files openfprintd

%post -n python3-%{pkg_name}
%systemd_post net.reactivated.Fprint.service

%preun -n python3-%{pkg_name}
%systemd_preun net.reactivated.Fprint.service

%postun -n python3-%{pkg_name}
%systemd_postun_with_restart net.reactivated.Fprint.service

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md
%license COPYING
%{_libdir}/open-fprintd/open-fprintd
%{_libdir}/open-fprintd/resume.py
%{_libdir}/open-fprintd/suspend.py
%{_datadir}/dbus-1/system-services/net.reactivated.Fprint.service
%{_datadir}/dbus-1/system.d/net.reactivated.Fprint.conf
%{_libdir}/open-fprintd/__pycache__/*.cpython-314.pyc

%changelog
* Thu Aug 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
