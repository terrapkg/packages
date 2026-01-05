%undefine __brp_mangle_shebangs

Name:			dorion
Version:		6.12.0
Release:		1%?dist
Summary:		Tiny alternative Discord client with a smaller footprint, snappier startup, themes, plugins and more!
SourceLicense:	GPL-3.0-only
License:		((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND 0BSD AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 AND ISC) AND (Apache-2.0 AND MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (BSD-3-Clause AND MIT) AND (BSD-3-Clause OR Apache-2.0) AND (BSD-3-Clause OR MIT) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND CC0-1.0 AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CDLA-Permissive-2.0 AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND Unicode-3.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)
URL:			https://spikehd.dev/projects/dorion
Source0:		https://github.com/SpikeHD/Dorion/archive/refs/tags/v%version.tar.gz
Source1:		https://raw.githubusercontent.com/uwu/shelter-builds/main/shelter.js
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	pnpm rpm_macro(cargo_install) rust-packaging
BuildRequires:	cmake gcc-c++
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(webkit2gtk-web-extension-4.1)
BuildRequires:	pkgconfig(openssl)

%description
Dorion is an alternative Discord client aimed towards lower-spec or storage-sensitive PCs that supports themes, plugins, and more!

%prep
%autosetup -n Dorion-%version
pnpm i

cat<<EOF > Dorion.desktop
[Desktop Entry]
Categories=Network;
Exec=Dorion
Icon=Dorion
Name=Dorion
Terminal=false
Type=Application
MimeType=x-scheme-handler/discord
EOF

cd src-tauri
%cargo_prep_online
cp %{S:1} injection/shelter.js

%build
pnpm run build:js
cd src-tauri
cd extension_webkit
%cmake
%cmake_build
cp %__cmake_builddir/libextension.so .
cd ..
%cargo_license_summary_online
%{cargo_license_online} > ../LICENSE.dependencies

%install
install -Dpm655 Dorion.desktop -t %buildroot%_datadir/applications
cd src-tauri
%cargo_install
install -Dpm644 icons/icon.png %buildroot%_iconsdir/hicolor/512x512/apps/Dorion.png

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%_bindir/Dorion
%_iconsdir/hicolor/512x512/apps/Dorion.png
%_datadir/applications/Dorion.desktop
