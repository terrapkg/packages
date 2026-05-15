Name:           falcond
Version:        2.0.6
Release:        1%{?dist}
Summary:        Advanced Linux Gaming Performance Daemon
License:        MIT
URL:            https://git.pika-os.com/general-packages/falcond
Source0:        %{url}/archive/v%{version}.tar.gz
BuildRequires:  anda-srpm-macros >= 0.3.9
BuildRequires:  systemd-rpm-macros
BuildRequires:  zig >= 0.16.0
BuildRequires:  zig-rpm-macros
Requires:       %{name}-profiles
Requires:       (scx-scheds or scx-scheds-nightly)
Suggests:       %{name}-gui
Conflicts:      gamemode
Provides:       group(falcond)
Packager:       Gilver E. <roachy@fyralabs.com>

%description
falcond is a powerful system daemon designed to automatically optimize your Linux gaming experience.
It intelligently manages system resources and performance settings on a per-game basis.
This eliminates the need to manually configure settings for each game.

%prep
%autosetup -n %{name}/%{name}
%zig_prep

%build

%install
# When DNF supports microarchitectures the fallback option for -c can be used here instead
%ifarch x86_64
%{zig_install_target -r fast -Cx86_64_v2 -s}
%elifarch aarch64
%{zig_install_target -r fast -s}
%endif
install -Dm644 debian/%{name}.service -t %{buildroot}%{_unitdir}

%pre
# Create falcond group if it doesn't exist
getent group 'falcond' >/dev/null || groupadd -f -r 'falcond' || :

# Root must be a member of the group
usermod -aG 'falcond' root || :

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc ../README.md
%license ../LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
* Thu May  14 2026 Gilver E. <roachy@fyralabs.com> - 2.0.6-2
- Updated for Zig and zig-rpm-macros 0.16.0
- Updated for anda-srpm-macros 0.3.9
* Thu Jan 1 2026 Gilver E. <roachy@fyralabs.com> - 1.2.1-2
- Disabled service by default in favor of user enablement via falcond-gui
- Added weak dep on falcond-gui
* Fri Jun 20 2025 Gilver E. <rockgrub@disroot.org> - 1.1.5-2
- Enable service by default
- Enable aarch64 CPU features
* Thu Jun 19 2025 Gilver E. <rockgrub@disroot.org> - 1.1.5-1
- Initial package
