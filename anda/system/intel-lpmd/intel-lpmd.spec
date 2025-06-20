%global _distro_extra_cflags -Wno-unused-variable -Wno-unused-function -Wno-switch -I/usr/lib/gcc/**/include/

Name:			intel-lpmd
Version:		0.0.9
Release:		1%?dist
Summary:		Linux daemon designed to optimize active idle power
License:		GPL-2.0-only
URL:			https://github.com/intel/intel-lpmd
Packager:		madonuko <mado@fyralabs.com>
Source0:		%url/archive/refs/tags/v%version.tar.gz
ExclusiveArch:	x86_64
BuildRequires:	automake autoconf-archive glib2-devel dbus-glib-devel libxml2-devel libnl3-devel systemd-devel gtk-doc upower-devel
BuildRequires:	gcc

%description
Intel Low Power Mode Daemon (lpmd) is a Linux daemon designed to optimize active idle power. It selects the most power-efficient CPUs based on a configuration file or CPU topology. Depending on system utilization and other hints, it puts the system into Low Power Mode by activating the power-efficient CPUs and disabling the rest, and restores the system from Low Power Mode by activating all CPUs.

%prep
%autosetup
sed -i 's@mandb || true@@' Makefile.am

%conf
./autogen.sh --prefix=%_usr

%build
%make_build

%install
%make_install

%if "%_sbindir" == "%_bindir"
mv %buildroot{%_usr/sbin/*,%_bindir}
%endif

%files
%doc README.md ChangeLog AUTHORS NEWS security.md
%license COPYING
%_bindir/intel_lpmd_control
%_sbindir/intel_lpmd
%_datadir/dbus-1/system-services/org.freedesktop.intel_lpmd.service
%_mandir/man5/intel_lpmd_config.xml.5.gz
%_mandir/man8/intel_lpmd.8.*
%_mandir/man8/intel_lpmd_control.8.*
%_usr%_sysconfdir/intel_lpmd/
%_sysconfdir/dbus-1/system.d/org.freedesktop.intel_lpmd.conf
%_unitdir/intel_lpmd.service
