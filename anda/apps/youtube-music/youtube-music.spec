%global pnpm_version 8
%define debug_package %nil


# macro shorthand for calling pnpm
%global pnpm npx pnpm@%{pnpm_version}

Name:           youtube-music
Version:        3.5.1
Release:        1%{?dist}
Summary:        YouTube Music Desktop App bundled with custom plugins (and built-in ad blocker / downloader)
Source1:        youtube-music.desktop
License:        MIT
URL:            https://github.com/th-ch/youtube-music


BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  git-core gcc make
BuildRequires:  python3 gcc-c++ # Required for usocket native module built with node-gyp

%description
YouTube Music Desktop App bundled with custom plugins (and built-in ad blocker / downloader)


%prep
rm -rf ./*
git clone --recursive %{url} .
git checkout v%{version}



%build
%pnpm install --no-frozen-lockfile
%pnpm build
%pnpm electron-builder --linux --dir



%install

# Install assets
install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps
install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

# Copy icon files
pushd pack/linux-unpacked/resources/app.asar.unpacked/assets
install -m 0644 youtube-music.png %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/youtube-music.png
install -m 0644 youtube-music.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/youtube-music.svg
install -m 0644 youtube-music-tray-paused.png %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/youtube-music-tray-paused.png
install -m 0644 youtube-music-tray.png %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/youtube-music-tray.png
popd

# Actually install the app

install -d -m 0755 %{buildroot}%{_datadir}/youtube-music
# Delete unpacked asar files before copying
rm -rfv pack/linux-unpacked/resources/app.asar.unpacked
cp -rv pack/linux-unpacked/* %{buildroot}%{_datadir}/youtube-music
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



%changelog
* Sat Aug 03 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- 
