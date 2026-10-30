%global pkgdir %_datadir/subtitleedit
%global realname subtitleedit
%ifarch x86_64
%global a x64
%elifarch aarch64
%global a ARM64
%endif

%global debug_package %nil
%global __strip /bin/true

Name:           %realname.bin
Version:        5.3.0
Release:        1%{?dist}
Summary:        An advanced subtitle editor and converter
License:        GPL-3.0-only
URL:            https://www.nikse.dk/SubtitleEdit
Source0:        https://github.com/SubtitleEdit/subtitleedit/releases/download/v%version/SubtitleEdit-Linux-%a.tar.gz
Source1:        https://raw.githubusercontent.com/SubtitleEdit/subtitleedit/v%{version}/src/libse/Icon.png
Packager:       madonuko <mado@fyralabs.com>
Provides:       %realname = %evr
Conflicts:      %realname
Requires:       dejavu-sans-mono-fonts mono-core

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

%install
mkdir -p %buildroot%pkgdir
tar xf %{S:0} -C %buildroot%pkgdir

mkdir -p %buildroot%_bindir
%{__ln_s} %pkgdir/SubtitleEdit %buildroot%_bindir/%realname

install -Dm644 subtitleedit.desktop -t %buildroot%_datadir/applications
install -Dm644 %{S:1} %buildroot%_datadir/pixmaps/subtitleedit.png

mv %buildroot%pkgdir/LICENSE .

%files
%pkgdir
%license LICENSE
%_bindir/%realname
%_datadir/applications/%realname.desktop
%_datadir/pixmaps/%realname.png

%changelog
* Thu Oct 29 2026 Owen Zimmerman <owen@fyralabs.com>, Madonuko <mado@fyralabs.com> - 5.3.0-1
- Update build for 5.3.0
