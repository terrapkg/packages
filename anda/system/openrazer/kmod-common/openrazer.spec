Name:           openrazer
Version:        3.12.4
Release:        1%{?dist}
Summary:        Open source driver and user-space daemon for managing Razer devices
License:        GPL-2.0-or-later
URL:            https://openrazer.github.io
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
Source0:        https://github.com/openrazer/openrazer/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        openrazer-sysusers.conf
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  systemd-rpm-macros
Requires:       %{name}-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-kmod-common = %{?epoch:%{epoch}:}%{version}
BuildArch:      noarch

%description
Common files for OpenRazer: the udev rules and the razer_mount helper that
bind Razer devices to the OpenRazer kernel drivers. Install openrazer-meta
for a complete, working setup.

%package        meta
Summary:        Meta package for installing all required OpenRazer packages
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-daemon = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python3-%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    meta
Meta package for installing all required OpenRazer packages.

%package        daemon
Summary:        OpenRazer service package
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-setproctitle
Requires:       python3-pyudev
Requires:       python3-daemonize
Requires:       xautomation
Provides:       razer-daemon = %{version}-%{release}
Obsoletes:      razer-daemon < %{version}-%{release}

%description    daemon
Userspace daemon that abstracts access to the kernel driver. Provides a DBus
service for applications to use.

%package -n     python3-%{name}
Summary:        OpenRazer Python library
Requires:       %{name}-daemon = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-numpy
Provides:       python3-razer = %{version}-%{release}
Obsoletes:      python3-razer < %{version}-%{release}

%description -n python3-%{name}
Python library for accessing the daemon from Python.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
pushd daemon
%pyproject_wheel
popd

pushd pylib
%pyproject_wheel
popd

%install
# udev rules, the razer_mount helper and the AppStream metadata
make udev_install appstream_install DESTDIR=%{buildroot} PREFIX=%{_prefix}

# The openrazer-daemon entrypoint, razer.conf.example, the DBus activation
# file, the systemd user unit and the manpages. Not parallelised because
# install-resources and install-systemd share the "service" target.
make -C daemon install-resources install-systemd manpages \
    DESTDIR=%{buildroot} PREFIX=%{_prefix}

# Installs both wheels built above and fixes up the daemon's shebang
%pyproject_install

install -Dpm644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

%pre
%sysusers_create_compat %{SOURCE1}

%files
%license LICENSES/GPL-2.0-or-later.txt
%doc README.md
%{_udevrulesdir}/99-razer.rules
%{_prefix}/lib/udev/razer_mount
%{_sysusersdir}/%{name}.conf
%{_datadir}/metainfo/io.github.openrazer.openrazer.metainfo.xml

%files          meta

%files          daemon
%{_bindir}/openrazer-daemon
%{python3_sitelib}/openrazer_daemon/
%{python3_sitelib}/openrazer_daemon-%{version}.dist-info/
%{_datadir}/openrazer/
%{_datadir}/dbus-1/services/org.razer.service
%{_prefix}/lib/systemd/user/openrazer-daemon.service
%{_mandir}/man5/razer.conf.5*
%{_mandir}/man8/openrazer-daemon.8*

%files -n       python3-%{name}
%{python3_sitelib}/openrazer/
%{python3_sitelib}/openrazer-%{version}.dist-info/

%changelog
* Mon Aug 31 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 3.12.4-1
- Initial package
