#? https://github.com/openrazer/OBS-packaging/blob/80f039ee374bc2254a22aca19af572d4993e9893/openrazer.spec

Name:           openrazer
Version:        3.10.0
Release:        1%?dist
Summary:        Open source driver and user-space daemon for managing Razer devices
License:        GPL-2.0-or-later
URL:            https://openrazer.github.io
Source0:        https://github.com/openrazer/openrazer/releases/download/v%{version}/openrazer-%{version}.tar.gz
Requires:       %name-dkms
Requires:       %name-daemon
Requires:       python3-%name
Packager:       madonuko <mado@fyralabs.com>

%description
%summary.


%package common
Summary: Common files for OpenRazer packages
BuildArch: noarch

%description common
%summary.

This package provides all common files for the openrazer-* packages.

%files common
%doc README.md
%license LICENSES/GPL-2.0-or-later.txt


%package dkms
Summary: OpenRazer Driver DKMS package
Requires: dkms
BuildArch: noarch

%description dkms
%summary.

Linux kernel driver for OpenRazer.

#? https://github.com/openrazer/OBS-packaging/blob/80f039ee374bc2254a22aca19af572d4993e9893/openrazer.spec#L181C1-L185C41
# I officially have no idea what I'm doing -- mado
%files dkms
%defattr(-,root,root,-)
%{_udevrulesdir}/../razer_mount
%{_udevrulesdir}/99-razer.rules
%{_usrsrc}/%{dkms_name}-%{dkms_version}/


%package daemon
Summary: OpenRazer Service package
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: (%name-dkms or akmod-%name)
Requires: python3
Requires: python3-dbus
Requires: python3-gobject
Requires: python3-setproctitle
Requires: python3-pyudev
Requires: python3-daemonize
Requires: xautomation

%description daemon
%summary.

Userspace daemon that abstracts access to the kernel driver. Provides a DBus service for applications to use.

%files daemon
%{_bindir}/openrazer-daemon
%{python3_sitelib}/openrazer_daemon/
%{python3_sitelib}/openrazer_daemon-*.egg-info/
%{_datadir}/openrazer/
%{_datadir}/dbus-1/services/org.razer.service
%{_prefix}/lib/systemd/user/openrazer-daemon.service
%{_mandir}/man5/razer.conf.5*
%{_mandir}/man8/openrazer-daemon.8*


%package -n python3-%name
Summary: OpenRazer Python library
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: %name-daemon
Requires: python3
Requires: python3-dbus
Requires: python3-gobject
Requires: python3-numpy

%description -n python3-openrazer
%summary.

Python library for accessing the daemon from Python.

%files -n python3-openrazer
%{python3_sitelib}/openrazer/
%{python3_sitelib}/openrazer-*.egg-info/



%prep
%autosetup -n openrazer-%{version}

%build

%install
# FIXME: follow PG?
%make_build setup_dkms udev_install daemon_install python_library_install


%pre dkms
getent group plugdev >/dev/null || groupadd -r plugdev

%posttrans dkms
dkms install %{dkms_name}/%{dkms_version}

echo -e "\e[31m********************************************"
echo -e "\e[31m* To complete installation, please run:    *"
echo -e "\e[31m* # sudo gpasswd -a <yourUsername> plugdev *"
echo -e "\e[31m********************************************"
echo -e -n "\e[39m"

%preun dkms
if [ "$(dkms status -m %{dkms_name} -v %{dkms_version})" ]; then
  dkms remove -m %{dkms_name} -v %{dkms_version} --all
fi
