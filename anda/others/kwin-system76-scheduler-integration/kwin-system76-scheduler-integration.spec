%global debug_package %nil

Name:			kwin-system76-scheduler-integration
Version:		0.1
Release:		2%?dist
Summary:		Notify the System76 Scheduler which app has focus so it can be prioritized
License:		MIT
URL:			https://github.com/maxiberta/kwin-system76-scheduler-integration
Source0:		%url/archive/refs/tags/%version.tar.gz
Source1:		system76-scheduler-dbus-proxy.sh
Source2:		com.system76.Scheduler.dbusproxy.service
Requires:		bash dbus-tools system76-scheduler kde-cli-tools systemd kf5-kconfig-core qt
BuildRequires: systemd-rpm-macros

%description
System76 Scheduler is a service which optimizes Linux's CPU scheduler and
automatically assigns process priorities for improved desktop responsiveness.

This KWin Script interactively notifies System76 Scheduler which app has focus
via D-Bus, so it is prioritized.

%prep
%autosetup

%build

%install
mkdir -p %buildroot%_datadir/kwin/scripts/kwin-system76-scheduler-integration/
cp -r * %buildroot%_datadir/kwin/scripts/kwin-system76-scheduler-integration/
install -Dm755 %SOURCE1 %buildroot/usr/local/bin/system76-scheduler-dbus-proxy.sh
install -Dm644 %SOURCE2 %buildroot%_userunitdir/com.system76.Scheduler.dbusproxy.service
install -Dm644 metadata.desktop %buildroot%_datadir/kservices5/kwin-system76-scheduler-integration.desktop

%post
%systemd_user_post com.system76.Scheduler.dbusproxy.service


%preun
%systemd_user_preun com.system76.Scheduler.dbusproxy.service


%files
%config %_userunitdir/com.system76.Scheduler.dbusproxy.service
/usr/local/bin/system76-scheduler-dbus-proxy.sh
%_datadir/kwin/scripts/kwin-system76-scheduler-integration/
%_datadir/kservices5/kwin-system76-scheduler-integration.desktop

%changelog
%autochangelog
