%global _include_minidebuginfo 0

Name:           falcond
Version:        1.1.5
Release:        1%{?dist}
Summary:        Advanced Linux Gaming Performance Daemon
License:        MIT
URL:            https://git.pika-os.com/general-packages/falcond
Source0:        %{url}/archive/v%{version}.tar.gz
BuildRequires:  anda-srpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  zig >= 0.14.0
BuildRequires:  zig-rpm-macros
Requires:	    %{name}-profiles
Requires:	    (scx-scheds or scx-scheds-nightly)
Conflicts:      gamemode
# We should switch these to explicitly -v3 and up builds once DNF supports this.
ExclusiveArch:  x86_64 aarch64
Packager:       Gilver E. <rockgrub@disroot.org>

%description
falcond is a powerful system daemon designed to automatically optimize your Linux gaming experience. It intelligently manages system resources and performance settings on a per-game basis, eliminating the need to manually configure settings for each game.

%prep
%autosetup -n %{name}/%{name}
ZIG_GLOBAL_CACHE_DIR="%{_zig_cache_dir}" zig build --fetch

%build

%install
install -Dm644 debian/%{name}.service %{buildroot}%{_unitdir}
DESTDIR="%{buildroot}" \
%{zig_build_target -r fast -c x86_64_v3}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
* Thu Jun 19 2025 Gilver E. <rockgrub@disroot.org> - 1.1.5-1
- Initial package
