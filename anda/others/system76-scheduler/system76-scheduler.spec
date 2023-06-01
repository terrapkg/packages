%define debug_package %nil

Name:			system76-scheduler
Version:		2.0.1
Release:		2%?dist
Summary:		Auto-configure CFS, process priorities for improved DE responsiveness
License:		MPL-2.0
URL:			https://github.com/pop-os/system76-scheduler
Source0:		%url/archive/refs/tags/%version.tar.gz
BuildRequires:	cargo clang just clang-devel pipewire-devel pkg-config

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
just execsnoop=$(which execsnoop-bpfcc) build-release

%install
just rootdir=%buildroot unitdir=%_unitdir sysconfdir=%_sysconfdir install

%files
%doc README.md
%license LICENSE
%_bindir/system76-scheduler
/usr/share/dbus-1/system.d/com.system76.Scheduler.conf
/usr/share/system76-scheduler/config.kdl
/usr/share/system76-scheduler/process-scheduler/pop_os.kdl
%{_unitdir}/com.system76.Scheduler.service

%changelog
* Tue May 23 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.0.1-1
- Initial package.
