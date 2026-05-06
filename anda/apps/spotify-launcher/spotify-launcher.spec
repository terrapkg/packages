Name:           spotify-launcher
Version:        0.6.5
Release:        3%?dist
Summary:        Client for spotify's apt repository in Rust
License:        Apache-2.0 AND MIT AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND CDLA-Permissive-2.0 AND ISC AND (ISC AND (Apache-2.0 OR ISC)) AND (ISC AND (Apache-2.0 OR ISC) AND OpenSSL) AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib
Packager:       veuxit <erroor234@gmail.com>
ExclusiveArch:  x86_64
URL:            https://github.com/kpcyrd/spotify-launcher

Source0:        https://github.com/kpcyrd/spotify-launcher/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo cargo-rpm-macros anda-srpm-macros pkgconfig(liblzma) desktop-file-utils
Requires:       sequoia-sqv zenity alsa-lib gtk3 desktop-file-utils openssl nss at-spi2-atk libcurl libSM libayatana-appindicator-gtk3


%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%{cargo_build} --locked

%install

install -Dm755 target/release/spotify-launcher %{buildroot}%{_bindir}/spotify-launcher

install -Dm644 data/pubkey_5384CE82BA52C83A.gpg %{buildroot}/%{_datadir}/spotify-launcher/keyring.pgp

install -Dm644 contrib/spotify-launcher.desktop %{buildroot}%{_appsdir}/spotify-launcher.desktop

install -Dm644 contrib/icons/spotify-linux-256.png "%{buildroot}/%{_datadir}/pixmaps/spotify-launcher.png"

install -Dm644 contrib/spotify-launcher.conf %{buildroot}%{_sysconfdir}/spotify-launcher.conf

for size in 22 24 32 48 64 128 256 512; do
  install -Dm644 contrib/icons/spotify-linux-${size}.png %{buildroot}%{_hicolordir}/${size}x${size}/apps/spotify-launcher.png
done
%{cargo_license_online} > LICENSE.dependencies

%check
%desktop_file_validate %{buildroot}%{_appsdir}/spotify-launcher.desktop

%files
%{_appsdir}/%{name}.desktop
%{_sysconfdir}/spotify-launcher.conf
%{_datadir}/pixmaps/spotify-launcher.png
%{_hicolordir}/22x22/apps/spotify-launcher.png
%{_hicolordir}/24x24/apps/spotify-launcher.png
%{_hicolordir}/32x32/apps/spotify-launcher.png
%{_hicolordir}/48x48/apps/spotify-launcher.png
%{_hicolordir}/64x64/apps/spotify-launcher.png
%{_hicolordir}/128x128/apps/spotify-launcher.png
%{_hicolordir}/256x256/apps/spotify-launcher.png
%{_hicolordir}/512x512/apps/spotify-launcher.png
%{_bindir}/spotify-launcher
%{_datadir}/spotify-launcher/keyring.pgp
%license LICENSE-MIT LICENSE-APACHE LICENSE.dependencies
%doc README.md

%changelog
* Tue Mar 17 2026 veux <erroor234@gmail.com> - 0.6.5-2
- Fix big package size and enable debug subpackages

* Fri Feb 27 2026 veux <erroor234@gmail.com> - 0.6.5-1
- Initial package release
