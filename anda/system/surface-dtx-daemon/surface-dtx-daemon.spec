%global debug_package %{nil}
%global ver 0.3.8-1

Name:           surface-dtx-daemon
Version:        %(echo %ver | sed 's/-/~/g')
Release:        1%{?dist}
Summary:        Surface Detachment System (DTX) Daemon
License:        MIT
URL:            https://github.com/linux-surface/surface-dtx-daemon
Source:         %url/archive/refs/tags/v%ver.tar.gz
BuildRequires:  rust cargo dbus-devel anda-srpm-macros

%description
Linux User-Space Detachment System (DTX) Daemon for the Surface ACPI Driver
(and Surface Books). Currently only the Surface Book 2 is supported, due to
lack of driver-support on the Surface Book 1. This may change in the future.

%prep
%autosetup -n %name-%ver

%build
export CARGO_TARGET_DIR="$PWD/target"
%cargo_build -- --locked

%install

# binary files
install -D -m755 "target/release/surface-dtx-daemon" "%{buildroot}/usr/bin/surface-dtx-daemon"
install -D -m755 "target/release/surface-dtx-userd" "%{buildroot}/usr/bin/surface-dtx-userd"

# application files
install -D -m644 "target/etc/dtx/surface-dtx-daemon.conf" "%{buildroot}/etc/surface-dtx/surface-dtx-daemon.conf"
install -D -m644 "target/etc/dtx/surface-dtx-userd.conf" "%{buildroot}/etc/surface-dtx/surface-dtx-userd.conf"
install -D -m755 "target/etc/dtx/attach.sh" "%{buildroot}/etc/surface-dtx/attach.sh"
install -D -m755 "target/etc/dtx/detach.sh" "%{buildroot}/etc/surface-dtx/detach.sh"
install -D -m644 "target/etc/systemd/surface-dtx-daemon.service" "%{buildroot}/usr/lib/systemd/system/surface-dtx-daemon.service"
install -D -m644 "target/etc/systemd/surface-dtx-userd.service" "%{buildroot}/usr/lib/systemd/user/surface-dtx-userd.service"
install -D -m644 "target/etc/dbus/org.surface.dtx.conf" "%{buildroot}/etc/dbus-1/system.d/org.surface.dtx.conf"
install -D -m644 "target/etc/udev/40-surface_dtx.rules" "%{buildroot}/etc/udev/rules.d/40-surface_dtx.rules"

# completion files
install -D -m644 "target/surface-dtx-daemon.bash" "%{buildroot}/usr/share/bash-completion/completions/surface-dtx-daemon"
install -D -m644 "target/surface-dtx-userd.bash" "%{buildroot}/usr/share/bash-completion/completions/surface-dtx-userd"
install -D -m644 "target/_surface-dtx-daemon" "%{buildroot}/usr/share/zsh/site-functions/_surface-dtx-daemon"
install -D -m644 "target/_surface-dtx-userd" "%{buildroot}/usr/share/zsh/site-functions/_surface-dtx-userd"
install -D -m644 "target/surface-dtx-daemon.fish" "%{buildroot}/usr/share/fish/vendor_completions.d/surface-dtx-daemon.fish"
install -D -m644 "target/surface-dtx-userd.fish" "%{buildroot}/usr/share/fish/vendor_completions.d/surface-dtx-userd.fish"

%files
%config /etc/dbus-1/system.d/org.surface.dtx.conf
%config /etc/udev/rules.d/40-surface_dtx.rules
%config(noreplace) /etc/surface-dtx/*
/usr/bin/surface-dtx-daemon
/usr/bin/surface-dtx-userd
/usr/lib/systemd/system/surface-dtx-daemon.service
/usr/lib/systemd/user/surface-dtx-userd.service
/usr/share/bash-completion/completions/surface-dtx-daemon
/usr/share/bash-completion/completions/surface-dtx-userd
/usr/share/zsh/site-functions/_surface-dtx-daemon
/usr/share/zsh/site-functions/_surface-dtx-userd
/usr/share/fish/vendor_completions.d/surface-dtx-daemon.fish
/usr/share/fish/vendor_completions.d/surface-dtx-userd.fish

%changelog
* Sat Oct 5 2024 Owen Zimmerman <owen@fyralabs.com>
- Package surface-dtx-daemon