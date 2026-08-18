%define debug_package %nil

# Only the bundled libs — system deps (gtk/cairo/cups/alsa/...) must stay Required.
%global __provides_exclude libffmpeg\\.so.*|libEGL\\.so.*|libGLESv2\\.so.*|libvk_swiftshader\\.so.*|libvulkan\\.so.*
%global __requires_exclude libffmpeg\\.so.*|libEGL\\.so.*|libGLESv2\\.so.*|libvk_swiftshader\\.so.*|libvulkan\\.so.*

Name:           pear-desktop
Version:        3.12.0
Release:        1%{?dist}
Summary:        Pear Desktop, a YouTube Music desktop app with custom plugins
Source1:        com.github.th-ch.youtube-music.desktop
License:        MIT
URL:            https://github.com/pear-devs/pear-desktop
Packager:       Caio Bruno <cbrunofb@gmail.com>

Provides:       youtube-music = %{version}-%{release}
Obsoletes:      youtube-music < 3.11.0-2

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
# pnpm@latest (project needs >=11; Fedora has 10.x) + node-gyp (usocket), into the builddir.
export npm_config_prefix=%{_builddir}/.npm-global
%__npm install -g pnpm@latest node-gyp
export PATH=%{_builddir}/.npm-global/bin:$PATH
export PNPM_HOME=%{_builddir}/.pnpm
pnpm install
pnpm build
pnpm electron-builder --linux --dir

%install
install -D -m 0644 assets/icon.png %{buildroot}%{_hicolordir}/1024x1024/apps/pear-desktop.png
install -D -m 0644 assets/icon.svg %{buildroot}%{_hicolordir}/scalable/apps/pear-desktop.svg

# Inner binary is still "youtube-music" upstream; expose it as pear-desktop.
install -d %{buildroot}%{_libdir}/pear-desktop
cp -r pack/linux*-unpacked/* %{buildroot}%{_libdir}/pear-desktop
# Setuid chrome-sandbox enables the Chromium sandbox (Electron: keep sandbox on in production).
chmod 4755 %{buildroot}%{_libdir}/pear-desktop/chrome-sandbox
install -d %{buildroot}%{_bindir}
ln -sf %{_libdir}/pear-desktop/youtube-music %{buildroot}%{_bindir}/pear-desktop

install -D -m 0644 %{SOURCE1} %{buildroot}%{_appsdir}/com.github.th-ch.youtube-music.desktop

%check
%desktop_file_validate %{buildroot}%{_appsdir}/com.github.th-ch.youtube-music.desktop

%files
%license license
%doc README.md
%{_bindir}/pear-desktop
%{_libdir}/pear-desktop/
%{_hicolordir}/1024x1024/apps/pear-desktop.png
%{_hicolordir}/scalable/apps/pear-desktop.svg
%{_appsdir}/com.github.th-ch.youtube-music.desktop

%changelog
* Fri Jul 31 2026 Caio Bruno <cbrunofb@gmail.com>
- Rename to pear-desktop (upstream rebrand to pear-devs/pear-desktop)
- Build from source (pnpm@latest via %__npm; %git_clone)
- Change maintainer due to complete rewrite

* Thu Dec 25 2025 Owen Zimmerman <owen@fyralabs.com>
- Add %check

* Sat Aug 03 2024 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
