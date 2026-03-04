Name:           SwayOSD
Version:        0.3.0
Release:        1%?dist
Summary:        A GTK based on screen display for keyboard shortcuts like caps-lock and volume
License:        GPL-3.0-only
URL:            https://github.com/ErikReider/SwayOSD
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gtk3-devel
BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  sassc
BuildRequires:  libevdev-devel
BuildRequires:  gtk4-devel
BuildRequires:  gtk4-layer-shell-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libinput-devel
BuildRequires:  louvre

Requires:       cairo
Requires:       gtk4
Requires:       cairo
Requires:       dbus
Requires:       gdk-pixbuf2
Requires:       glib2
Requires:       glibc
Requires:       gtk4-layer-shell
Requires:       libevdev
Requires:       libinput
Requires:       pulseaudio-libs
Requires:       pango
Requires:       systemd-libs

Provides:       swayosd

%description
%{summary}.

%prep
%autosetup -n SwayOSD-%{version}

%build
%meson
%meson_build

%install
%meson_install

%post
%systemd_post swayosd-libinput-backend.service
%systemd_post org.erikreider.swayosd.service

%preun
%systemd_preun swayosd-libinput-backend.service
%systemd_preun org.erikreider.swayosd.service

%postun
%systemd_postun_with_restart swayosd-libinput-backend.service
%systemd_postun_with_restart org.erikreider.swayosd.service

%files
%doc README.md
%license LICENSE
%{_bindir}/swayosd-client
%{_bindir}/swayosd-server
%{_bindir}/swayosd-libinput-backend
%config(noreplace) %{_sysconfdir}/xdg/swayosd/backend.toml
%config(noreplace) %{_sysconfdir}/xdg/swayosd/config.toml
%config(noreplace) %{_sysconfdir}/xdg/swayosd/style.css
%{_usr}/lib64/systemd/system/swayosd-libinput-backend.service
%{_usr}/lib64/udev/rules.d/99-swayosd.rules
%{_datadir}/dbus-1/system-services/org.erikreider.swayosd.service
%{_datadir}/dbus-1/system.d/org.erikreider.swayosd.conf
%{_datadir}/polkit-1/actions/org.erikreider.swayosd.policy
%{_datadir}/polkit-1/rules.d/org.erikreider.swayosd.rules

%changelog
* Thu Nov 13 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
