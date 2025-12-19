Name:           supergfxctl
Version:        5.2.7
Release:        1%?dist
Summary:        GPU Utility for ASUS ROG Laptops
URL:            https://gitlab.com/asus-linux/supergfxctl
Source0:        %url/-/archive/%{version}/supergfxctl-%{version}.tar.gz
SourceLicense:  MPL-2.0
License:        ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT)
BuildRequires:  cargo anda-srpm-macros cargo-rpm-macros mold rust-udev-devel
BuildRequires:  rpm_macro(systemd_post)
Packager:       Its-J

%description
%{summary}.

%prep
%autosetup -n supergfxctl-%{version}
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies
%cargo_build -f "cli daemon"

%install
install -Dm 0755 target/rpm/supergfxd target/rpm/supergfxctl -t %buildroot%_bindir
install -Dm 0644 data/90-supergfxd-nvidia-pm.rules %{buildroot}%{_udevrulesdir}/90-supergfxd-nvidia-pm.rules
install -Dm 0644 data/org.supergfxctl.Daemon.conf  %{buildroot}%{_datadir}/dbus-1/system.d/org.supergfxctl.Daemon.conf
install -Dm 0644 data/supergfxd.preset %{buildroot}%{_presetdir}/99-supergfxd.preset
install -Dm 0644 data/90-nvidia-screen-G05.conf %{buildroot}%{_datadir}/X11/xorg.conf.d/90-nvidia-screen-G05.conf
install -Dm 0644 data/supergfxd.service -t %buildroot%_unitdir

%post
%systemd_post supergfxd.service

%preun
%systemd_preun supergfxd.service

%postun
%systemd_postun_with_restart supergfxd.service

%files
%license LICENSE
%doc README.md
%{_bindir}/supergfxctl
%{_bindir}/supergfxd
%{_udevrulesdir}/90-supergfxd-nvidia-pm.rules
%{_datadir}/X11/xorg.conf.d/90-nvidia-screen-G05.conf
%{_datadir}/dbus-1/system.d/org.supergfxctl.Daemon.conf
%{_unitdir}/supergfxd.service
# We should not be installing .preset files (errors if not listed)
%ghost %{_presetdir}/99-supergfxd.preset

%changelog
* Sun Oct 26 2025 Its-J
- Package SuperGFXctl
