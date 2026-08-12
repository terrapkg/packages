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
BuildRequires:  policycoreutils
BuildRequires:  checkpolicy
BuildRequires:  bzip2
Requires:       policycoreutils
Requires:       innoextract
Requires:       open-fprintd

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

pushd selinux
checkmodule -M -m -o python3-validity.mod python3-validity.te
semodule_package -o python3-validity.pp -m python3-validity.mod
bzip2 python3-validity.pp
popd

%install
%pyproject_install
%pyproject_save_files %{pkg_name}sensor
install -Dm 0600 etc/python-validity/dbus-service.yaml %{buildroot}%{_sysconfdir}/python-validity/dbus-service.yaml
install -Dm 0644 debian/python3-validity.service       %{buildroot}%{_prefix}/lib/systemd/system/python3-validity.service
install -Dm 0644 debian/python3-validity.udev          %{buildroot}%{_prefix}/lib/udev/rules.d/40-python3-validity.udev
install -Dm 0644 selinux/python3-validity.pp.bz2       %{buildroot}%{_datadir}/selinux/packages/python3-validity.pp.bz2

%post -n python3-%{pkg_name}
%selinux_modules_install %{_datadir}/selinux/packages/python3-validity.pp.bz2
/usr/bin/validity-sensors-firmware || true
udevadm control --reload-rules || true
udevadm trigger || true
%systemd_post python3-validity.service

%preun -n python3-%{pkg_name}
%systemd_preun python3-validity.service

%postun -n python3-%{pkg_name}
%systemd_postun_with_restart python3-validity.service
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall %{_datadir}/selinux/packages/python3-validity.pp.bz2
fi

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/validity-led-dance
%{_bindir}/validity-sensors-firmware
%{_libdir}/python-validity/dbus-service
%config %{_datadir}/dbus-1/system.d/io.github.uunicorn.Fprint.conf
%{_datadir}/python-validity/playground/__pycache__/*.pyc
%{_datadir}/python-validity/playground/*.py
%config(noreplace) %{_sysconfdir}/python-validity/dbus-service.yaml
%{_prefix}/lib/systemd/system/python3-validity.service
%{_udevrulesdir}/40-python3-validity.udev
%{_datadir}/selinux/packages/python3-validity.pp.bz2

%changelog
* Tue Aug 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
