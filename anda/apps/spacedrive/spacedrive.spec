Name:			spacedrive
Version:		0.3.1
Release:		1%?dist
Summary:		An open source cross-platform file explorer
License:		AGPL-3.0
URL:			https://spacedrive.com
Source0:		https://github.com/spacedriveapp/spacedrive/archive/refs/tags/%version.tar.gz
Requires:		ffmpeg libheif gtk3 webkit2gtk4.1 pango gdk-pixbuf2 cairo libsoup glib2 openssl
BuildRequires:	pnpm git-core perl gcc javascriptcoregtk4.0-devel pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(libsoup-2.4) glib2-devel gtk3-devel openssl-devel pkgconfig(zlib)
BuildRequires:  openssl clang-devel

%description
Spacedrive is an open source cross-platform file manager, powered by a virtual distributed filesystem (VDFS) written in Rust. 

%prep
%autosetup

# we need nightly cargo
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -o rustup.sh
chmod +x ./rustup.sh
./rustup.sh -y -t nightly --profile minimal
source "$HOME/.cargo/env"
rm rustup.sh %SOURCE0

pnpm setup
pnpm i -g pnpm
pnpm install
pnpm store prune # GH workers running out of disk space… oh well

%build
source $HOME/.cargo/env
export CARGO_TARGET_DIR=target
#export RUSTUP_TOOLCHAIN=1.73

pnpm prep
pnpm tauri build --bundles app -- --no-default-features

%install
install -Dm755 -t %buildroot%_bindir apps/desktop/src-tauri/target/release/spacedrive

%files
%license LICENSE
%_bindir/spacedrive

%changelog
%autochangelog
