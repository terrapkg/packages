%global appid com.spacedrive.Spacedrive

Name:			spacedrive
Version:		0.4.3
Release:		1%?dist
Summary:		An open source cross-platform file explorer
License:		AGPL-3.0-or-later
URL:			https://spacedrive.com
Source0:		https://github.com/spacedriveapp/spacedrive/archive/refs/tags/%version.tar.gz
Source1:		spacedrive.desktop

Requires:		ffmpeg
Requires:		libheif
Requires:		gtk3
Requires:		webkit2gtk4.1
Requires:		pango
Requires:		gdk-pixbuf2
Requires:		cairo
Requires:		libsoup
Requires:		glib2
Requires:		openssl

BuildRequires:	pnpm
BuildRequires:	rustup
BuildRequires:	%tauri_buildrequires
BuildRequires:	git-core
BuildRequires:	perl
BuildRequires:	gcc
BuildRequires:	clang-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(webkit2gtk-4.1)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	anda-srpm-macros
BuildRequires:	terra-appstream-helper
BuildRequires:	desktop-file-utils

%description
Spacedrive is an open source cross-platform file manager,
powered by a virtual distributed filesystem (VDFS) written in Rust.

%prep
%autosetup
%rustup_nightly
cd apps/desktop
%tauri_prep

%build
%{__pnpm} install --frozen-lockfile
%{__pnpm} tauri build
%tauri_cargo_license_summary
%{tauri_cargo_license} > LICENSE.dependencies

%install
install -Dpm755 apps/desktop/src-tauri/target/rpm/%{name} \
    %{buildroot}%{_bindir}/%{name}
%desktop_file_install %{SOURCE1}
install -Dpm644 apps/desktop/src-tauri/icons/icon.png \
    %{buildroot}%{_hicolordir}/512x512/apps/%{appid}.png

%terra_appstream

%check
desktop-file-validate %{buildroot}%{_appsdir}/spacedrive.desktop

%files
%license LICENSE LICENSE.dependencies
%_bindir/%{name}
%_appsdir/spacedrive.desktop
%_hicolordir/512x512/apps/%{appid}.png
%_metainfodir/%{appid}.metainfo.xml

%changelog
* Wed Aug 26 2026 madonuko <mado@fyralabs.com>
- Initial package
