%global appid   app.winboat.WinBoat

Name:           winboat
%electronmeta -D
Version:        0.9.2
Release:        1%{?dist}
Summary:        Run Windows apps on Linux with seamless integration
License:        MIT AND %{electron_license}
URL:            https://github.com/winboat-org/winboat
Source0:        %{url}/archive/v%{version}.tar.gz
Source1:        %{appid}.metainfo.xml
ExclusiveArch:  %{electron_arches}

BuildRequires:  git-core
BuildRequires:  libxcrypt-compat
BuildRequires:  golang
BuildRequires:  /usr/bin/zip
BuildRequires:  nodejs24-bin
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(alsa)

Requires:       freerdp
Requires:       gtk3
Requires:       nss
Requires:       ((moby-engine and docker-compose) or (podman and podman-compose))

Packager:       Its-J <jonah@fyralabs.com>, Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -S git
%{__npm} i

%build
%npm_build -r build:linux-gs

%install
%electron_install -D -I icons/winboat_logo.svg

find dist -type f -exec file {} + | grep 'ELF' | grep -v 'ARM aarch64' | cut -d: -f1
find dist -type f -exec file {} + | grep -E 'FreeBSD|OpenBSD|Android|ld-musl' | cut -d: -f1
find "%{buildroot}%{_libdir}/winboat" -type f -name '*musl*' -print -delete
find "%{buildroot}%{_libdir}/winboat" -type d \( -path '*/prebuilds/freebsd-*' -o -path '*/prebuilds/android-*' \) -prune -print -exec rm -rf {} +

%ifarch aarch64
keep='ARM aarch64'
%elifarch x86_64
keep='x86-64'
%endif
find "%{buildroot}%{_libdir}/winboat" -type f -exec file {} + \
 | grep 'ELF' \
 | grep -Ev "ELF 64-bit LSB.*${keep}" \
 | cut -d: -f1 | xargs -r rm -v

%terra_appstream -o %{S:1}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_scalableiconsdir}/winboat.svg
%{_appsdir}/winboat.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_libdir}/winboat/*

%changelog
* Thu Oct 01 2026 Owen Zimmerman <owen@fyralabs.com> - 0.9.2-1
- Fix build steps
- Remove bad libraries
- Fix metainfo

* Wed Sep 30 2026 Its-J <jonah@fyralabs.com> - 0.9.2-1
- Initial commit
