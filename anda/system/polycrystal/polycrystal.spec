Name:           polycrystal
Version:        0.2.0
Release:        2%?dist
Summary:        Barebones "automatic" Flatpak installer for distribution-default Flatpak packages.
URL:            https://github.com/Ultramarine-Linux/polycrystal
Source0:        %url/archive/refs/tags/v%version.tar.gz
License:        GPL-3.0-only
BuildRequires:  cargo cmake anda-srpm-macros cargo-rpm-macros systemd-rpm-macros mold glib2-devel flatpak-devel
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%summary.

%prep
%autosetup -n polycrystal-%version
%cargo_prep_online

%build
%cargo_build

%install
mkdir -p %{buildroot}%{_datadir}/polycrystal %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/polycrystal/entries %{buildroot}%{_sharedstatedir}/polycrystal
%cargo_install
install -Dm644 polycrystal.service %{buildroot}%{_unitdir}/polycrystal.service

%post
%systemd_post polycrystal.service

%preun
%systemd_preun polycrystal.service

%postun
%systemd_postun_with_restart polycrystal.service

%files
%{_bindir}/polycrystal
%{_datadir}/polycrystal/
%{_unitdir}/polycrystal.service
%dir %{_sysconfdir}/polycrystal
%dir %{_sysconfdir}/polycrystal/entries
%dir %{_sharedstatedir}/polycrystal
%license LICENSE
%doc README.md

%changelog
* Tue Nov 19 2024 Owen-sz <owen@fyralabs.com>
- Switch from commit based to release based, and add systemd services
* Fri Nov 15 2024 Owen-sz <owen@fyralabs.com>
- Package Polycrystal