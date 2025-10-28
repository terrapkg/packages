%global debug_package %{nil}

Name:           supergfxctl
Version:        5.2.7
Release:        1%?dist
Summary:        GPU Utility for ASUS ROG Laptops
URL:            https://gitlab.com/asus-linux/supergfxctl
Source0:        %url/-/archive/%{version}/supergfxctl-%{version}.tar.gz
License:        MPL-2.0
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold rust-udev-devel
Packager:       Its-J

%description
%{summary}.

%prep
%autosetup -n supergfxctl-%{version}
%cargo_prep_online

%build
%make_build

%install
%make_install
install -Dm 0644 data/90-supergfxd-nvidia-pm.rules %{buildroot}/etc/X11/xorg.conf.d/90-supergfxd-nvidia-pm.rules
install -Dm 0644 data/org.supergfxctl.Daemon.conf  %{buildroot}%{_datadir}/dbus-1/system.d/org.supergfxctl.Daemon.conf
install -Dm 0644 data/org.supergfxctl.Daemon.conf  %{buildroot}/etc/dbus-1/system.d/org.supergfxctl.Daemon.conf
install -Dm 0644 data/supergfxd.preset %{buildroot}%{_presetdir}/99-supergfxd.preset
install -Dm 0644 data/90-nvidia-screen-G05.conf %{buildroot}%{_datadir}/X11/xorg.conf.d/90-nvidia-screen-G05.conf

%files
%license LICENSE
%doc README.md
%{_bindir}/supergfxctl
%{_bindir}/supergfxd
%{_sysconfdir}/X11/xorg.conf.d/90-supergfxd-nvidia-pm.rules
%{_udevrulesdir}/90-supergfxd-nvidia-pm.rules
%{_datadir}/X11/xorg.conf.d/90-nvidia-screen-G05.conf
%{_datadir}/dbus-1/system.d/org.supergfxctl.Daemon.conf
%{_unitdir}/supergfxd.service
%{_presetdir}/99-supergfxd.preset
%{_sysconfdir}/dbus-1/system.d/org.supergfxctl.Daemon.conf
# We should not be installing .preset files (errors if not listed)
%ghost /usr/lib/systemd/system-preset/supergfxd.preset

%changelog
* Sun Oct 26 2025 Its-J
- Package SuperGFXctl
