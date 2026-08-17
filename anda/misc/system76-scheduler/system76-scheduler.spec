%define debug_package %nil

Name:			system76-scheduler
Version:		2.0.2
Release:		1%?dist
Summary:		Auto-configure CFS, process priorities for improved DE responsiveness
License:		MPL-2.0
URL:			https://github.com/pop-os/system76-scheduler
Source0:		%url/archive/refs/tags/%version.tar.gz
BuildRequires:	cargo clang clang-devel pipewire-devel pkg-config systemd-rpm-macros rust-packaging just
BuildRequires:  bcc-tools
Requires:       bcc-tools

%description
Scheduling service which optimizes Linux's CPU scheduler and automatically
assigns process priorities for improved desktop responsiveness. Low latency CPU
scheduling will be activated automatically when on AC, and the default
scheduling latencies set on battery. Processes are regularly sweeped and
assigned process priorities based on configuration files. When combined with
pop-shell, foreground processes and their sub-processes will be given higher
process priority.

%prep
%autosetup

%build
export EXECSNOOP_PATH=/usr/share/bcc/tools/execsnoop
# We don't use our macro since one of the dependencies fails to build with our profile :/
%(echo "%{cargo_build}" | sed "s@--profile rpm@--profile release@g" | sed "s@-j @@")

%install
just rootdir=%buildroot sysconfdir=%_datadir install


%post
%systemd_post com.system76.Scheduler.service


%preun
%systemd_preun com.system76.Scheduler.service


%postun
%systemd_postun_with_restart com.system76.Scheduler.service


%files
%doc README.md
%license LICENSE
%_bindir/system76-scheduler
%config %ghost %_sysconfdir/dbus-1/system.d/com.system76.Scheduler.conf
%config %ghost %_sysconfdir/system76-scheduler/config.kdl
%config %ghost %_sysconfdir/system76-scheduler/process-scheduler/pop_os.kdl
%_datadir/dbus-1/system.d/com.system76.Scheduler.conf
%_datadir/system76-scheduler/config.kdl
%_datadir/system76-scheduler/process-scheduler/pop_os.kdl
%_unitdir/com.system76.Scheduler.service

%changelog
* Tue Sep 26 2023 Cappy Ishihara <cappy@cappuchino.xyz> - 2.0.1-2
- Move default configurations to /usr/share/system76-scheduler
- Add Requires: bcc-tools so execsnoop is available

* Tue May 23 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.0.1-1
- Initial package.
