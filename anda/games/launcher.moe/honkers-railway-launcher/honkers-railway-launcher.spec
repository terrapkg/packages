%global cargo_install_lib 0
%global crate honkers-railway-launcher
%global appid moe.launcher.the-honkers-railway-launcher
Name:           %{crate}
Version:        1.14.4
Release:        1%?dist
Summary:        The Honkers Railway launcher for Linux with automatic patching and telemetry disabling 

License:        GPL-3.0-or-later
URL:            https://github.com/an-anime-team/the-honkers-railway-launcher
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Packager:       Cappy Ishihara <cappy@fyralabs.com>


# Allow migrate path from Maroxy's OBS repo
Provides: the-honkers-railway-launcher = %{version}-%{release}

Requires: unzip
Requires: cabextract
Requires: tar
Requires: git
Requires: p7zip
Requires: curl
Requires: xdelta
BuildRequires: gtk4
BuildRequires: git
BuildRequires: rust
BuildRequires: cargo
BuildRequires: gtk4-devel
BuildRequires: openssl-devel
BuildRequires: python3
BuildRequires: python3-gobject
BuildRequires: libadwaita-devel
BuildRequires: cmake
BuildRequires: gcc clang-devel mold
BuildRequires: rust-packaging
BuildRequires: desktop-file-utils
BuildRequires: anda-srpm-macros
BuildRequires: cargo-rpm-macros


%description
%{summary}

%prep
%autosetup -n the-honkers-railway-launcher-%{version}
%cargo_prep_online

%build
%cargo_build

%install
%crate_install_bin

install -Dm644 assets/images/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{appid}.png
desktop-file-install \
    --set-icon="%{appid}" \
    --set-key="Exec" --set-value="%{name}" \
    --dir=%{buildroot}%{_datadir}/applications \
    assets/honkers-railway-launcher.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/honkers-railway-launcher.desktop


%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_datadir}/applications/honkers-railway-launcher.desktop
%{_bindir}/%{crate}
%{_datadir}/icons/hicolor/512x512/apps/%{appid}.png

%changelog
* Sat Sep 20 2025 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial package
