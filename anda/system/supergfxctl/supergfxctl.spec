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
%{Summary}.

%prep
%autosetup -n supergfxctl-%{version}
%cargo_prep_online

%build
%make_build

%install
%make_install
%dnl install -Dm 755 target/rpm/supergfxctl %{buildroot}%{_bindir}/supergfxctl
%dnl install -Dm 0755 target/release/supergfxd %{buildroot}%{_bindir}/supergfxd
%dnl install -Dm 0644 data/90-supergfxd-nvidia-pm.rules %{buildroot}%{_udevrulesdir}/90-supergfxd-nvidia-pm.rules
%dnl install -Dm 0644 data/org.supergfxctl.Daemon.conf  %{buildroot}%{_sysconfdir}/dbus-1/system.d/org.supergfxctl.Daemon.conf
%dnl install -Dm 0644 data/supergfxd.service %{buildroot}%{_unitdir}/supergfxd.service
%dnl install -Dm 0644 data/supergfxd.preset %{buildroot}%{_presetdir}/99-supergfxd.preset

%files
%{_bindir}/supergfxctl
%{_bindir}/supergfxd
%{_udevrulesdir}/90-supergfxd-nvidia-pm.rules
%{_sysconfdir}/X11/xorg.conf.d/90-nvidia-screen-G05.conf
%{_sysconfdir}/dbus-1/system.d/org.supergfxctl.Daemon.conf
%{_unitdir}/supergfxd.service
%{_presetdir}/99-supergfxd.preset
%license LICENSE
%doc README.md

%changelog
* Sun Oct 26 2025 Its-J
- Package SuperGFXctl
