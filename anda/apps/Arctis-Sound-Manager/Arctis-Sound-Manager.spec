%global pypi_name arctis-sound-manager
%global _desc Linux GUI for SteelSeries Arctis headsets — Nova Pro Wireless & Wired, Nova Pro Omni, Nova Elite, Nova 7/7P/5/3, Arctis 7/7+/9/Pro Wireless. Device settings, Sonar EQ, 4-channel Game/Chat/Media mixer, PipeWire routing.

%global arctis_sound_manager_services arctis-manager.service arctis-video-router.service arctis-stream-guard.service app-ArctisManager.service

Name:			python-%{pypi_name}
Version:		1.4.6
Release:		1%{?dist}
Summary:		GUI for SteelSeries Arctis headsets
License:		GPL-3.0-or-later
# GitHub pages URL 404s
URL:			https://github.com/loteran/Arctis-Sound-Manager
Source0:		%{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-importlib-metadata
BuildRequires:  python3-uv-build
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3-ruamel-yaml
BuildRequires:  desktop-file-utils

# ── Runtime dependencies ─────────────────────────────────────────────────────
# Kept in sync with the upstream spec at
# https://github.com/loteran/Arctis-Sound-Manager/blob/main/arctis-sound-manager.spec
# The Python bindings are omitted on purpose: they are declared in
# pyproject.toml, so RPM generates them automatically. Everything below is
# reached through the filesystem or dlopen, where nothing can infer it.
#
# Audio stack the daemon drives directly.
Requires:       pipewire
Requires:       pipewire-pulseaudio
Requires:       wireplumber
Requires:       libusb1
Requires:       pulseaudio-libs
# The `pactl` CLI (used at GUI startup and for EQ/Sonar routing) ships in
# pulseaudio-utils, NOT in pipewire-pulseaudio or pulseaudio-libs. Without it
# a clean install crashes on launch with FileNotFoundError: 'pactl'.
# https://github.com/loteran/Arctis-Sound-Manager/issues/117
Requires:       pulseaudio-utils
# Fedora ships the Steve Harris SWH LADSPA pack as `ladspa-swh-plugins`.
# Required by the HeSuVi 7.1 virtual surround graph (`plate_1423` reverb);
# Spatial Audio loads nothing and stays silent without it.
# https://github.com/loteran/Arctis-Sound-Manager/issues/23
Requires:       ladspa-swh-plugins
# Used by asm-setup to fetch the HRIR file on first run; without it Spatial
# Audio has no impulse response to convolve with.
Requires:       curl

Packager:	    Owen Zimmerman <owen@fyralabs.com>

BuildArch:      noarch

Provides:       Arctis-Sound-Manager

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       arctis-sound-manager = %{evr}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n Arctis-Sound-Manager-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files arctis_sound_manager

install -Dm644 /dev/null %{buildroot}%{_udevrulesdir}/91-steelseries-arctis.rules
python3 scripts/generate_udev_rules.py src/arctis_sound_manager/devices/ \
    > %{buildroot}%{_udevrulesdir}/91-steelseries-arctis.rules

# Systemd user services (single source of truth in systemd/, not heredocs)
install -Dm644 systemd/*.service -t %{buildroot}%{_userunitdir}

# dinit service templates
install -Dm644 dinit/arctis-manager %{buildroot}%{_datadir}/%{name}/dinit/arctis-manager
install -Dm644 dinit/arctis-video-router %{buildroot}%{_datadir}/%{name}/dinit/arctis-video-router
install -Dm644 dinit/arctis-gui %{buildroot}%{_datadir}/%{name}/dinit/arctis-gui
install -Dm644 dinit/pipewire-filter-chain %{buildroot}%{_datadir}/%{name}/dinit/pipewire-filter-chain
install -Dm755 scripts/asm-diag-dinit.py %{buildroot}%{_bindir}/asm-diag-dinit

# Desktop entry
install -Dm644 src/arctis_sound_manager/desktop/ArctisManager.desktop \
    %{buildroot}%{_datadir}/applications/ArctisManager.desktop

# Icon
install -Dm644 src/arctis_sound_manager/gui/images/steelseries_logo.svg \
    %{buildroot}%{_scalableiconsdir}/arctis-manager.svg

# PipeWire configs
install -Dm644 scripts/pipewire/10-arctis-virtual-sinks.conf \
    %{buildroot}%{_datadir}/%{name}/pipewire/10-arctis-virtual-sinks.conf
install -Dm644 scripts/pipewire/sink-virtual-surround-7.1-hesuvi.conf \
    %{buildroot}%{_datadir}/%{name}/pipewire/sink-virtual-surround-7.1-hesuvi.conf

# filter-chain.service (bundled for distros that don't ship one)
install -Dm644 scripts/filter-chain.service \
    %{buildroot}%{_datadir}/%{name}/filter-chain.service

# First-run autostart (triggers asm-setup on first graphical login)
install -Dm644 debian/asm-first-run.desktop \
    %{buildroot}%{_sysconfdir}/xdg/autostart/asm-first-run.desktop

%check
%desktop_file_validate %{buildroot}%{_appsdir}/ArctisManager.desktop

%post
%systemd_user_post %{arctis_sound_manager_services}

%preun
%systemd_user_preun %{arctis_sound_manager_services}

%postun
%systemd_postun_with_restart %{arctis_sound_manager_services}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CONTRIBUTING.md CHANGELOG.md
%license LICENSE
%{_bindir}/asm-cli
%{_bindir}/asm-clipd
%{_bindir}/asm-daemon
%{_bindir}/asm-diag-dinit
%{_bindir}/asm-gui
%{_bindir}/asm-router
%{_bindir}/asm-setup
%{_bindir}/asm-stream-guard
%{_udevrulesdir}/91-steelseries-arctis.rules
%{_userunitdir}/arctis-manager.service
%{_userunitdir}/arctis-video-router.service
%{_userunitdir}/arctis-stream-guard.service
%{_userunitdir}/app-ArctisManager.service
%{_datadir}/%{name}/dinit/arctis-manager
%{_datadir}/%{name}/dinit/arctis-video-router
%{_datadir}/%{name}/dinit/pipewire-filter-chain
%{_bindir}/asm-diag-dinit
%{_appsdir}/ArctisManager.desktop
%{_scalableiconsdir}/arctis-manager.svg
%{_datadir}/%{name}/pipewire/10-arctis-virtual-sinks.conf
%{_datadir}/%{name}/pipewire/sink-virtual-surround-7.1-hesuvi.conf
%{_datadir}/%{name}/filter-chain.service
%{_sysconfdir}/xdg/autostart/asm-first-run.desktop
%{_datadir}/python-arctis-sound-manager/dinit/arctis-gui

%changelog
* Fri Jul 31 2026 loteran <https://github.com/loteran> - 1.2.19-2
- Declare the runtime dependencies RPM cannot infer: the audio stack the daemon
  drives, pulseaudio-utils for pactl (issue #117), ladspa-swh-plugins for the
  virtual surround graph (issue #23), and curl for the first-run HRIR download

* Mon Jun 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
