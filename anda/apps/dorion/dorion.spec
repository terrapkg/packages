Name:			dorion
Version:		6.11.0
Release:		1%?dist
Summary:		Tiny alternative Discord client with a smaller footprint, snappier startup, themes, plugins and more!
License:		GPL-3.0-only
URL:			https://spikehd.dev/projects/dorion
Source0:		https://github.com/SpikeHD/Dorion/archive/refs/tags/v%version.tar.gz
Packager:		madonuko <mado@fyralabs.com>
BuildRequires:	pnpm rpm_macro(cargo_install) rust-packaging
BuildRequires:	cmake gcc-c++
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	webkit2gtk-web-extension-4.1

%description
Dorion is an alternative Discord client aimed towards lower-spec or storage-sensitive PCs that supports themes, plugins, and more!

%prep
%autosetup -n Dorion-%version
#pnpm i
cd src-tauri
%cargo_prep_online

%build
#pnpm run build:js
cd src-tauri
cd extension_webkit
%cmake
%cmake_build
cd ..
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%install
cd src-tauri
%cargo_install

%files
%doc README.md
%license LICENSE LICENSE.dependencies
%_bindir/dorion
