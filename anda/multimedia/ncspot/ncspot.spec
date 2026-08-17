%global crate ncspot
%global cargo_features cover

Name:           ncspot
Version:        1.3.3
Release:        1%{?dist}
Summary:        Cross-platform ncurses Spotify client written in Rust
Packager:       like-engels <higashikataengels@icloud.com>
License:        BSD-2-Clause AND (MIT OR Apache-2.0)
URL:            https://crates.io/crates/%{crate}
Source0:        https://github.com/hrkfdn/ncspot/archive/refs/tags/v%version.tar.gz

Requires:	dbus
Requires:	glibc
Requires:	libxcb
Requires:	pipewire-pulseaudio
Requires:	pulseaudio-libs
Requires:	openssl

BuildRequires:  anda-srpm-macros
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  gcc
BuildRequires:  binutils
BuildRequires:  mold
BuildRequires:  dbus-devel
BuildRequires:  libxcb-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-libs-devel

%global _description %{expand:
ncurses Spotify client written in Rust using librespot.
It is heavily inspired by ncurses MPD clients, such as ncmpc.
It provides a simple and resource-friendly alternative to the
official Spotify client.}

%description %{_description}

%files -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/%{crate}

%prep
%autosetup -n %{crate}-%{version}
%cargo_prep_online

%build
%cargo_build -f "%{cargo_features}"
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
%crate_install_bin

%changelog
* Wed Mar 18 2026 like-engels <higashikataengels@icloud.com> - 1.3.3-1
- Initial package
