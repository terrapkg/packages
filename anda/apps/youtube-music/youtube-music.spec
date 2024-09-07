%define debug_package %nil


# macro shorthand for calling pnpm
%global pnpm npx pnpm@%{pnpm_version}

Name:           youtube-music
Version:        3.5.2
Release:        1%?dist
Summary:        YouTube Music Desktop App bundled with custom plugins (and built-in ad blocker / downloader)
Source1:        youtube-music.desktop
License:        MIT
URL:            https://github.com/th-ch/youtube-music
Packager:       Cappy Ishihara <cappy@fyralabs.com>

# For some unknown reason, PNPM is not working with Node.js 22 on Aarch64 devices.
# todo: investigate why
#ExclusiveArch: x86_64

BuildRequires:  git-core gcc make
# Required for usocket native module built with node-gyp
BuildRequires:  python3 gcc-c++

%description
YouTube Music Desktop App bundled with custom plugins (and built-in ad blocker / downloader)


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

# Install assets
install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps
install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

# Copy icon files
ls -laR pack
%ifarch aarch64
pushd pack/linux-arm64-unpacked/resources/app.asar.unpacked/assets
%else
pushd pack/linux-unpacked/resources/app.asar.unpacked/assets
%endif
install -m 0644 youtube-music.png %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/youtube-music.png
install -m 0644 youtube-music.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/youtube-music.svg
install -m 0644 youtube-music-tray-paused.png %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/youtube-music-tray-paused.png
install -m 0644 youtube-music-tray.png %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/youtube-music-tray.png
popd

# Actually install the app

install -d -m 0755 %{buildroot}%{_datadir}/youtube-music
# Delete unpacked asar files before copying
rm -rfv pack/linux*-unpacked/resources/app.asar.unpacked
cp -rv pack/linux*-unpacked/* %{buildroot}%{_datadir}/youtube-music
install -d -m 0755 %{buildroot}%{_bindir}
ln -svf %{_datadir}/youtube-music/youtube-music %{buildroot}%{_bindir}/youtube-music

# Install desktop file
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/youtube-music.desktop

%files
%license license
%doc README.md
%doc docs
%{_bindir}/youtube-music
%{_datadir}/youtube-music
%{_datadir}/icons/hicolor/*/apps/youtube-music*
%{_datadir}/applications/youtube-music.desktop



%changelog
* Sat Aug 03 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
