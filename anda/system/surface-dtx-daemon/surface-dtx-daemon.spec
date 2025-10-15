### THIS PACKAGE HAS BEEN DEPRECATED AS THE REASON FOR ITS EXISTANCE HAS BEEN FIXED IN THE UPSTREAM VERSION ###

%global debug_package %{nil}
%global ver v0.3.10-1
%global ver2 %(echo %{ver} | sed 's/^v//')

Name:           terra-surface-dtx-daemon-deprecated
Version:        %(echo %ver | sed 's/-/~/g')
Release:        5%{?dist}
Summary:        Surface Detachment System (DTX) Daemon
License:        MIT
URL:            https://github.com/linux-surface/surface-dtx-daemon
Source:         %url/archive/refs/tags/%ver.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

Obsoletes:      terra-surface-dtx-daemon <= 0.3.10-1
Obsoletes:      terra-surface-dtx-daemon-bash-completion <= 0.3.10-1
Obsoletes:      terra-surface-dtx-daemon-fish-completion <= 0.3.10-1
Obsoletes:      terra-surface-dtx-daemon-zsh-completion <= 0.3.10-1
Requires:       surface-dtx-daemon >= 0.3.10-1

%description
Linux User-Space Detachment System (DTX) Daemon for the Surface ACPI Driver
(and Surface Books). Currently only the Surface Book 2 is supported, due to
lack of driver-support on the Surface Book 1. This may change in the future.

%dnl %pkg_completion -Bfz surface-dtx-daemon surface-dtx-userd

%prep
%dnl %autosetup -n surface-dtx-daemon-%{ver2}
%dnl %cargo_prep_online

%dnl %build
%dnl export CARGO_TARGET_DIR="$PWD/target"
%dnl %cargo_build -- --locked

%install

echo "THIS PACKAGE HAS BEEN DEPRECATED AS THE REASON FOR ITS EXISTANCE HAS BEEN FIXED IN THE UPSTREAM VERSION. PLEASE USE THE `surface-dtx-daemon` PACKAGE INSTEAD!" >> README.md

# binary files
%dnl install -D -m755 "target/rpm/surface-dtx-daemon" "%{buildroot}%{_bindir}/surface-dtx-daemon"
%dnl install -D -m755 "target/rpm/surface-dtx-userd" "%{buildroot}%{_bindir}/surface-dtx-userd"

# application files
%dnl install -D -m644 "target/etc/dtx/surface-dtx-daemon.conf" "%{buildroot}/etc/surface-dtx/surface-dtx-daemon.conf"
%dnl install -D -m644 "target/etc/dtx/surface-dtx-userd.conf" "%{buildroot}/etc/surface-dtx/surface-dtx-userd.conf"
%dnl install -D -m755 "target/etc/dtx/attach.sh" "%{buildroot}/etc/surface-dtx/attach.sh"
%dnl install -D -m755 "target/etc/dtx/detach.sh" "%{buildroot}/etc/surface-dtx/detach.sh"
%dnl install -D -m644 "target/etc/systemd/surface-dtx-daemon.service" "%{buildroot}/usr/lib/systemd/system/surface-dtx-daemon.service"
%dnl install -D -m644 "target/etc/systemd/surface-dtx-userd.service" "%{buildroot}/usr/lib/systemd/user/surface-dtx-userd.service"
%dnl install -D -m644 "target/etc/dbus/org.surface.dtx.conf" "%{buildroot}/etc/dbus-1/system.d/org.surface.dtx.conf"
%dnl install -D -m644 "target/etc/udev/40-surface_dtx.rules" "%{buildroot}/etc/udev/rules.d/40-surface_dtx.rules"

# completion files
%dnl install -D -m644 "target/surface-dtx-daemon.bash" "%{buildroot}/usr/share/bash-completion/completions/surface-dtx-daemon"
%dnl install -D -m644 "target/surface-dtx-userd.bash" "%{buildroot}/usr/share/bash-completion/completions/surface-dtx-userd"
%dnl install -D -m644 "target/_surface-dtx-daemon" "%{buildroot}/usr/share/zsh/site-functions/_surface-dtx-daemon"
%dnl install -D -m644 "target/_surface-dtx-userd" "%{buildroot}/usr/share/zsh/site-functions/_surface-dtx-userd"
%dnl install -D -m644 "target/surface-dtx-daemon.fish" "%{buildroot}/usr/share/fish/vendor_completions.d/surface-dtx-daemon.fish"
%dnl install -D -m644 "target/surface-dtx-userd.fish" "%{buildroot}/usr/share/fish/vendor_completions.d/surface-dtx-userd.fish"

# These systemd services should be included in the preset file for Ultramarine Linux Surface images
%dnl %post
%dnl %systemd_post surface-dtx-daemon.service
%dnl %systemd_user_post surface-dtx-userd.service

%dnl %preun
%dnl %systemd_preun surface-dtx-daemon.service
%dnl %systemd_user_preun surface-dtx-userd.service

%dnl %postun
%dnl %systemd_postun_with_restart surface-dtx-daemon.service
%dnl %systemd_user_postun_with_restart surface-dtx-userd.service

%files
%doc README.md
%dnl %config /etc/dbus-1/system.d/org.surface.dtx.conf
%dnl %config /etc/udev/rules.d/40-surface_dtx.rules
%dnl %config(noreplace) /etc/surface-dtx/*
%dnl /usr/bin/surface-dtx-daemon
%dnl /usr/bin/surface-dtx-userd
%dnl /usr/lib/systemd/system/surface-dtx-daemon.service
%dnl /usr/lib/systemd/user/surface-dtx-userd.service

%changelog
* Tue Oct 14 2025 Owen Zimmerman <owen@fyralabs.com>
- deprecate terra-surface-dtx-daemon in favor of upstream package

* Wed Feb 5 2025 Owen Zimmerman <owen@fyralabs.com>
- rename to terra-surface-dtx-daemon

* Sat Oct 5 2024 Owen Zimmerman <owen@fyralabs.com>
- Package surface-dtx-daemon
