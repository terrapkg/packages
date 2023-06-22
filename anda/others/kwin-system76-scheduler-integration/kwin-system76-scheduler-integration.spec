%global debug_package %nil

Name:			kwin-system76-scheduler-integration
Version:		0.1
Release:		1%?dist
Summary:		Notify the System76 Scheduler which app has focus so it can be prioritized
License:		MIT
URL:			https://github.com/maxiberta/kwin-system76-scheduler-integration
Source0:		%url/archive/refs/tags/%version.tar.gz
Source1:		system76-scheduler-dbus-proxy.sh
Source2:		com.system76.Scheduler.dbusproxy.service
Requires:		bash dbus-tools system76-scheduler kde-cli-tools systemd kf5-kconfig-core qt
BuildRequires:	kf5-kpackage systemd-rpm-macros

%description
System76 Scheduler is a service which optimizes Linux's CPU scheduler and
automatically assigns process priorities for improved desktop responsiveness.

This KWin Script interactively notifies System76 Scheduler which app has focus
via D-Bus, so it is prioritized.

%prep
%autosetup

%build
kpackagetool5 --type=KWin/Script -i .

%install
install -Dm755 %SOURCE1 %buildroot/usr/local/bin/system76-scheduler-dbus-proxy.sh
install -Dm644 %SOURCE2 %buildroot%_unitdir/com.system76.Scheduler.dbusproxy.service
mkdir -p %buildroot%_datadir/kwin-system76-scheduler-integration
cp -r $HOME/.local/share/kwin-system76-scheduler-integration %buildroot%_datadir/kwin-system76-scheduler-integration

%post
if [ $1 -eq 1 ]; then
	# Initial installation
	kwriteconfig5 --file kwinrc --group Plugins --key kwin-system76-scheduler-integrationEnabled true
	qdbus org.kde.KWin /KWin reconfigure
	systemctl enable --now --global com.system76.Scheduler.dbusproxy.service
fi

%preun
if [ $1 -eq 0 ]; then
	# Package removal, not upgrade
	systemctl disable --now --global com.system76.Scheduler.dbusproxy.service
	kwriteconfig5 --file kwinrc --group Plugins --key kwin-system76-scheduler-integrationEnabled false
	qdbus org.kde.KWin /KWin reconfigure
fi

%postun
if [ $1 -ge 1 ] && [ -x "/usr/lib/systemd/systemd-update-helper" ]; then
	# Package upgrade, not uninstall
	systemctl restart --now --global com.system76.Scheduler.dbusproxy.service
fi

%files
%config %_unitdir/com.system76.Scheduler.dbusproxy.service
/usr/local/bin/system76-scheduler-dbus-proxy.sh
%_datadir/kwin-system76-scheduler-integration/


%changelog
%autochangelog
