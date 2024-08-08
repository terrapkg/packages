%define debug_package %nil
%global _build_id_links none

# do not strip binaries
%define __strip /bin/true

# do not perform compression in cpio
%define _source_payload w0.ufdio
%define _binary_payload w0.ufdio

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

Name:			voicevox
Version:		0.20.0
Release:		1%?dist
Summary:		Free Japanese text-to-speech editor
License:		LGPL-3.0
URL:			https://voicevox.hiroshiba.jp
Source0:        https://github.com/VOICEVOX/voicevox/releases/download/%version/VOICEVOX.AppImage.7z.001
Source1:        https://github.com/VOICEVOX/voicevox/releases/download/%version/VOICEVOX.AppImage.7z.002
Source2:        https://github.com/VOICEVOX/voicevox/releases/download/%version/VOICEVOX.AppImage.7z.003
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  p7zip-plugins
ExclusiveArch:  x86_64

%description
VOICEVOX is a free Japanese text-to-speech software with medium output quality.

%package doc
Summary: Documentation files for voicevox (Japanese)

%description doc
%summary.

%prep
cat<<EOF > voicevox.sh
#!/usr/bin/sh
/usr/share/voicevox/VOICEVOX.AppImage
EOF
7z x %SOURCE0
chmod a+x VOICEVOX.AppImage

./VOICEVOX.AppImage --appimage-extract '*.desktop'
./VOICEVOX.AppImage --appimage-extract 'usr/share/icons/**'

sed -i "s|Exec=.*|Exec=/usr/share/voicevox/VOICEVOX.AppImage|" squashfs-root/voicevox.desktop

%build

%install
install -Dm755 VOICEVOX.AppImage %buildroot%_datadir/voicevox/VOICEVOX.AppImage
install -Dm755 voicevox.sh %buildroot%_bindir/voicevox
install -Dm644 squashfs-root%_iconsdir/hicolor/0x0/apps/voicevox.png %buildroot%_iconsdir/hicolor/256x256/apps/voicevox.png
install -Dm644 squashfs-root/voicevox.desktop %buildroot%_datadir/applications/voicevox.desktop

%files
%_bindir/voicevox
%_datadir/applications/voicevox.desktop
%_datadir/voicevox/VOICEVOX.AppImage
%_iconsdir/hicolor/256x256/apps/voicevox.png
