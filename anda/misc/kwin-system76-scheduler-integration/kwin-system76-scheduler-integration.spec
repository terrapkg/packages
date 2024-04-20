%global debug_package %nil

Name:       kwin-system76-scheduler-integration

%global forgeurl https://github.com/maxiberta/%{name}
%global commit 093a269670275feaa240d02c712f1ec8b812fd80
%global date 20240320
%forgemeta

Version:    0.1
Release:    6%?dist
Summary:    Notify the System76 Scheduler which app has focus so it can be prioritized
License:    MIT
URL:        %forgeurl
Source0:    %forgesource
Source1:    com.system76.Scheduler.dbusproxy.service
Requires:   bash dbus-tools system76-scheduler kde-cli-tools systemd kf6-kconfig
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
install -Dm755 %SOURCE1 %buildroot%_libexecdir/system76-scheduler-dbus-proxy.sh
install -Dm644 %SOURCE2 %buildroot%_userunitdir/com.system76.Scheduler.dbusproxy.service
install -Dm644 metadata.desktop %buildroot%_datadir/kservices5/kwin-system76-scheduler-integration.desktop

%post
%systemd_user_post com.system76.Scheduler.dbusproxy.service


%preun
%systemd_user_preun com.system76.Scheduler.dbusproxy.service

%postun
%systemd_user_postun_with_restart com.system76.Scheduler.dbusproxy.service

%files
%config %_userunitdir/com.system76.Scheduler.dbusproxy.service
%_libexecdir/system76-scheduler-dbus-proxy.sh
%_datadir/kwin/scripts/kwin-system76-scheduler-integration/
%_datadir/kservices5/kwin-system76-scheduler-integration.desktop

%changelog
%autochangelog
