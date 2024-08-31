Name:           modrinth
Version:        1.2.3
Release:        1%?dist
Summary:        Desktop app for managing mods and modpacks from Modrinth
URL:            https://github.com/modrinth/code
License:        GPL-3.0-or-later
BuildRequires:  git-core rust tauri
Packager:       Willow Reed <willow@willowidk.dev>
 
%description
Desktop app for managing mods and modpacks from Modrinth
 
%prep
rm -rf ./*
git clone --recursive %{url} .
git checkout v%{version}
 
%build
# Vendor PNPM directly instead of installing from packages, because we need to somehow force PNPM to use Node.js 20
# We are not using Fedora's PNPM because we need to use `pnpm env`, which PNPM does not support when not vendored directly from upstream
curl -fsSL https://get.pnpm.io/install.sh | sh -
source /builddir/.bashrc
pnpm env use --global 20
pnpm install
pnpm build
pnpm electron-builder --linux --dir
 
%install
echo "this will also run when building pkg but for installing it into %{buildroot} so that anda (mock) can package it"
 
%files
/usr/bin/pkgname-binary
/path/to/more/files/*/package
 
%changelog
* Wed Jan 11 2006 your-username-here <your_email@idk.xyz>
- Description on what you've done