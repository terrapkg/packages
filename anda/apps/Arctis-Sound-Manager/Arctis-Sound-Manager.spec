%global pypi_name arctis-sound-manager
%global _desc Linux GUI for SteelSeries Arctis headsets — Nova Pro Wireless & Wired, Nova Pro Omni, Nova Elite, Nova 7/7P/5/3, Arctis 7/7+/9/Pro Wireless. Device settings, Sonar EQ, 4-channel Game/Chat/Media mixer, PipeWire routing.

%global arctis_sound_manager_services arctis-manager.service arctis-video-router.service arctis-gui.service

Name:			python-%{pypi_name}
Version:		1.1.84
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

Packager:	    Owen Zimmerman <owen@fyralabs.com>

BuildArch:      noarch

Provides:       Arctis-Sound-Manager

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
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
install -Dm644 systemd/arctis-manager.service       %{buildroot}%{_userunitdir}/arctis-manager.service
install -Dm644 systemd/arctis-video-router.service  %{buildroot}%{_userunitdir}/arctis-video-router.service
install -Dm644 systemd/arctis-gui.service           %{buildroot}%{_userunitdir}/arctis-gui.service

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
%{_bindir}/asm-daemon
%{_bindir}/asm-diag-dinit
%{_bindir}/asm-gui
%{_bindir}/asm-router
%{_bindir}/asm-setup
%{_udevrulesdir}/91-steelseries-arctis.rules
%{_userunitdir}/arctis-manager.service
%{_userunitdir}/arctis-video-router.service
%{_userunitdir}/arctis-gui.service
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
* Mon Jun 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
