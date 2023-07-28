%define debug_package %nil

Name:		neovide
Version:	0.10.4
Release:	1%?dist
Summary:	No Nonsense Neovim Client in Rust
License:	MIT
URL:		https://neovide.dev/
Source0:	https://github.com/neovide/neovide/archive/refs/tags/%version.tar.gz
Requires:	neovim fontconfig freetype libglvnd
BuildRequires:	anda-srpm-macros cargo-rpm-macros >= 24 cmake gtk3 python3 SDL2 ninja-build
BuildRequires:	fontconfig-devel freetype-devel libX11-xcb libX11-devel libstdc++-static libstdc++-devel

%description
This is a simple graphical user interface for Neovim.
Where possible there are some graphical improvements,
but functionally it should act like the terminal UI.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install

install -Dm755 -t %buildroot%_bindir target/release/%name
install -Dm644 -t %buildroot%_datadir/applications/ assets/%name.desktop
for px in 16 32 48 256; do
	install -Dm644 assets/%name-${px}x${px}.png %buildroot%_datadir/icons/hicolor/${px}x${px}/apps/%name.png
done

%files
%doc README.md
%license LICENSE
%_bindir/%name
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/applications/%name.desktop


%changelog
%autochangelog
