%define debug_package %nil

# Exclude only the Electron/Chromium libs bundled inside the app (NOT every
# lib*.so — the app still needs system gtk/cairo/cups/alsa/etc. as Requires).
%global __provides_exclude libffmpeg\\.so.*|libEGL\\.so.*|libGLESv2\\.so.*|libvk_swiftshader\\.so.*|libvulkan\\.so.*
%global __requires_exclude libffmpeg\\.so.*|libEGL\\.so.*|libGLESv2\\.so.*|libvk_swiftshader\\.so.*|libvulkan\\.so.*

Name:           pear-desktop
Version:        3.12.0
Release:        1%{?dist}
Summary:        Pear Desktop, a YouTube Music desktop app with custom plugins
Source1:        pear-desktop.desktop
License:        MIT
URL:            https://github.com/pear-devs/pear-desktop
Packager:       Cappy Ishihara <cappy@fyralabs.com>

# Replacement for the former "youtube-music" package (upstream rebranded to
# pear-devs/pear-desktop). Take over upgrades from the old name.
Provides:       youtube-music = %{version}-%{release}
Obsoletes:      youtube-music < %{version}-%{release}

BuildRequires:  git-core gcc make desktop-file-utils
BuildRequires:  nodejs nodejs-npm
BuildRequires:  python3 gcc-c++ python-unversioned-command

Requires:       nss
Requires:       libXext.so.6
Requires:       libXfixes.so.3

%description
Pear Desktop (formerly youtube-music) is a YouTube Music desktop app with
custom plugins, including a built-in ad blocker and downloader.

%prep
%git_clone %{url} v%{version}

%build
# Install a current pnpm (project needs >=11; Fedora ships 10.x) and node-gyp
# (for the usocket native module) into the builddir. Nothing writes to $HOME.
export npm_config_prefix=%{_builddir}/.npm-global
%__npm install -g pnpm@latest node-gyp
export PATH=%{_builddir}/.npm-global/bin:$PATH
export PNPM_HOME=%{_builddir}/.pnpm
pnpm install
pnpm build
pnpm electron-builder --linux --dir

%install
# App icons ship as assets/icon.{png,svg} upstream (the rebrand dropped the
# youtube-music.* names); install them under the pear-desktop identity.
install -d -m 0755 %{buildroot}%{_hicolordir}/1024x1024/apps
install -d -m 0755 %{buildroot}%{_hicolordir}/scalable/apps
install -m 0644 assets/icon.png %{buildroot}%{_hicolordir}/1024x1024/apps/pear-desktop.png
install -m 0644 assets/icon.svg %{buildroot}%{_hicolordir}/scalable/apps/pear-desktop.svg

# Install the bundled Electron app. The inner executable is still named
# "youtube-music" (upstream hasn't renamed the binary yet); expose it as
# pear-desktop via a symlink in %{_bindir}.
install -d -m 0755 %{buildroot}%{_libdir}/pear-desktop
cp -rv pack/linux*-unpacked/* %{buildroot}%{_libdir}/pear-desktop
install -d -m 0755 %{buildroot}%{_bindir}
ln -svf %{_libdir}/pear-desktop/youtube-music %{buildroot}%{_bindir}/pear-desktop

install -D -m 0644 %{SOURCE1} %{buildroot}%{_appsdir}/pear-desktop.desktop

%check
%desktop_file_validate %{buildroot}%{_appsdir}/pear-desktop.desktop

%files
%license license
%doc README.md
%{_bindir}/pear-desktop
%{_libdir}/pear-desktop/
%{_hicolordir}/1024x1024/apps/pear-desktop.png
%{_hicolordir}/scalable/apps/pear-desktop.svg
%{_appsdir}/pear-desktop.desktop

%changelog
* Fri Jul 31 2026 Caio Bruno <cbrunofb@gmail.com>
- Rename package to pear-desktop (upstream rebrand to pear-devs/pear-desktop)
- Install pnpm@latest + node-gyp via npm instead of the curl hack; use %git_clone

* Thu Dec 25 2025 Owen Zimmerman <owen@fyralabs.com>
- Add %check

* Sat Aug 03 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
