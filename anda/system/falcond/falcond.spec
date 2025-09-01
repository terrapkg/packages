%global _include_minidebuginfo 0

Name:           falcond
Version:        1.1.7
Release:        1%?dist
Summary:        Advanced Linux Gaming Performance Daemon
License:        MIT
URL:            https://git.pika-os.com/general-packages/falcond
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        %{name}.preset
BuildRequires:  anda-srpm-macros >= 0.2.18
BuildRequires:  systemd-rpm-macros
BuildRequires:  zig >= 0.14.0
BuildRequires:  zig-rpm-macros
Requires:       %{name}-profiles
Requires:       (scx-scheds or scx-scheds-nightly)
Conflicts:      gamemode
Packager:       Gilver E. <rockgrub@disroot.org>

%description
falcond is a powerful system daemon designed to automatically optimize your Linux gaming experience.
It intelligently manages system resources and performance settings on a per-game basis.
This eliminates the need to manually configure settings for each game.

%prep
%autosetup -n %{name}/%{name}

%build

%install
install -Dm644 debian/%{name}.service -t %{buildroot}%{_unitdir}
install -Dm644 %{SOURCE1} %{buildroot}%{_presetdir}/60-%{name}.preset
# When DNF supports microarchitectures the fallback option for -c can be used here instead
DESTDIR="%{buildroot}" \
%ifarch x86_64
%{zig_build_target -r fast -c x86_64_v2 -s} \
%elifarch aarch64
%{zig_build_target -r fast -s} \
%endif

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
%{_presetdir}/60-%{name}.preset

%changelog
* Fri Jun 20 2025 Gilver E. <rockgrub@disroot.org> - 1.1.5-2
- Enable service by default
- Enable aarch64 CPU features
* Thu Jun 19 2025 Gilver E. <rockgrub@disroot.org> - 1.1.5-1
- Initial package
