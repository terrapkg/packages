%global appid com.spacedrive.Spacedrive

Name:			spacedrive
Version:		0.4.3
Release:		1%?dist
Summary:		An open source cross-platform file explorer
License:		AGPL-3.0-or-later
URL:			https://spacedrive.com
Source0:		https://github.com/spacedriveapp/spacedrive/archive/refs/tags/%version.tar.gz
Requires:		ffmpeg libheif gtk3 webkit2gtk4.1 pango gdk-pixbuf2 cairo libsoup glib2 openssl
BuildRequires:	pnpm git-core perl gcc javascriptcoregtk4.1-devel pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(libsoup-2.4) glib2-devel gtk3-devel openssl-devel pkgconfig(zlib)
BuildRequires:  openssl clang-devel
BuildRequires:	bun-bin rustup tauri

%description
Spacedrive is an open source cross-platform file manager,
powered by a virtual distributed filesystem (VDFS) written in Rust. 

%prep
%autosetup
%rustup_nightly
%tauri_prep -n $PWD

%build
%bun_build
%tauri_cargo_license_summary
%{tauri_cargo_license} > LICENSE.dependencies

%install
install -Dm755 -t %buildroot%_bindir apps/desktop/src-tauri/target/rpm/spacedrive

%terra_appstream

%files
%license LICENSE LICENSE.dependencies
%_bindir/spacedrive
%_metainfodir/%appid.metadata.xml
