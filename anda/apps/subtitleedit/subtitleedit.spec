%global pkgdir %_datadir/subtitleedit
%global realname subtitleedit

Name:           %realname.bin
Version:        4.0.12
Release:        1%?dist
Summary:        An advanced subtitle editor and converter
License:        GPL-3.0-only
URL:            https://www.nikse.dk/SubtitleEdit
Source0:        https://github.com/SubtitleEdit/subtitleedit/releases/download/%version/SE%{gsub %version %. %{quote:}}.zip
Source1:        https://github.com/SubtitleEdit/subtitleedit/blob/%version/src/libse/Icon.png?raw=true
Packager:       madonuko <mado@fyralabs.com>
Provides:       %realname = %evr
Conflicts:      %realname
BuildRequires:  unzip anda-srpm-macros
Requires:       mono dejavu-fonts

%description
%summary.


%prep
cat<<EOF > subtitleedit.desktop
[Desktop Entry]
Name=Subtitle Edit
Comment=An advanced subtitle editor and converter
Exec=/usr/bin/subtitleedit %%F
Icon=subtitleedit
Terminal=false
Type=Application
Categories=Video;AudioVideo;AudioVideoEditing;
EOF

cat<<EOF > subtitleedit
#!/usr/bin/sh
exec mono /opt/subtitleedit/SubtitleEdit.exe "$@"
EOF


%install
mkdir -p %buildroot%pkgdir
unzip %{S:0} -d %buildroot%pkgdir
rm -r %buildroot%pkgdir/Tesseract302
rm %buildroot%pkgdir/Hunspell{x86,x64}.dll
touch %buildroot%pkgdir/.PACKAGE-MANAGER

install -Dm755 subtitleedit -t %buildroot%_bindir
install -Dm644 subtitleedit.desktop -t %buildroot%_datadir/applications
install -Dm644 %{S:1} %buildroot%_datadir/pixmaps/subtitleedit.png


%files
%pkgdir
%_bindir/%realname
%_datadir/applications/%realname.desktop
%_datadir/pixmaps/%realname.png
