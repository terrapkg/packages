%global crate neovide
%global raw_forgeurl https://raw.githubusercontent.com/%{crate}/%{crate}

Name:           rust-neovide
Version:        0.15.1
Release:        1%?dist
Summary:        No Nonsense Neovim Client in Rust

License:        MIT
URL:            https://crates.io/crates/neovide
Source0:        %{crates_source}
Source1:        %{raw_forgeurl}/%{version}/assets/%{crate}-16x16.png
Source2:        %{raw_forgeurl}/%{version}/assets/%{crate}-32x32.png
Source3:        %{raw_forgeurl}/%{version}/assets/%{crate}-48x48.png
Source4:        %{raw_forgeurl}/%{version}/assets/%{crate}-256x256.png
Requires:       fontconfig freetype libglvnd
Requires:       neovim >= 0.10.0

BuildRequires:	anda-srpm-macros cargo-rpm-macros >= 24 cmake gtk3 python3 SDL2 mold
BuildRequires:	fontconfig-devel freetype-devel libX11-xcb libX11-devel libstdc++-static libstdc++-devel
ExclusiveArch:	x86_64

%global _description %{expand:
This is a simple graphical user interface for Neovim.
Where possible there are some graphical improvements,
but functionally it should act like the terminal UI.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (BSD-3-Clause OR MIT OR Apache-2.0) AND BSL-1.0 AND CC0-1.0 AND ISC AND LGPL-3.0 AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/%{crate}
%{_datadir}/icons/hicolor/*/apps/%{crate}.png
%{_datadir}/applications/%{crate}.desktop


%prep
%autosetup -n %{crate}-%{version}
%cargo_prep_online

%build
%cargo_build
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
install -Dm755 -t %{buildroot}%{_bindir} target/rpm/%{crate}
install -Dm644 -t %{buildroot}%{_datadir}/applications/ assets/%{crate}.desktop
cp -t assets/ %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} 
for px in 16 32 48 256; do
    install -Dm644 assets/%{crate}-${px}x${px}.png %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps/%{crate}.png
done

%changelog
%autochangelog

