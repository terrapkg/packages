%global ver build/0.1.529

Name:			openutau.bin
Version:		%(echo %ver | sed -E 's@^build/@@')
Release:		3%?dist
Summary:		Open singing synthesis platform / Open source UTAU successor
License:		MIT
URL:			http://www.openutau.com
Source0:		https://github.com/stakira/OpenUtau/releases/download/%ver/OpenUtau-linux-x64.tar.gz
Source1:		https://github.com/stakira/OpenUtau/raw/refs/tags/%ver/LICENSE.txt
Source2:		https://github.com/stakira/OpenUtau/raw/refs/tags/%ver/OpenUtau/Assets/open-utau.ico
Packager:		madonuko <mado@fyralabs.com>
Provides:		openutau = %evr
Provides:		OpenUtau = %evr
AutoReqProv:	0

%description
OpenUtau is a free, open-source editor made for the UTAU community.

%prep
cp %{S:1} %{S:2} .
cat<<EOF > OpenUtau.desktop
[Desktop Entry]
Version=1.0
Terminal=false
Type=Application
Name=OpenUtau
Categories=Audio;AudioVideoEditing;
Comment=%summary
Keywords=utau;synthesis;
Exec=%_bindir/OpenUtau
Icon=%_iconsdir/hicolor/apps/open-utau.ico
EOF

%install
mkdir -p %buildroot%_bindir
ln -s %_datadir/openutau/OpenUtau %buildroot%_bindir/OpenUtau
install -Dm644 OpenUtau.desktop -t %buildroot%_datadir/applications
install -Dpm644 open-utau.ico -t %buildroot%_iconsdir/hicolor/apps

mkdir -p %buildroot%_datadir/openutau
cd %buildroot%_datadir/openutau
tar xf %{S:0}

%files
%license LICENSE.txt
%_bindir/OpenUtau
%_datadir/openutau
%_datadir/applications/OpenUtau.desktop
%_iconsdir/hicolor/apps/open-utau.ico
