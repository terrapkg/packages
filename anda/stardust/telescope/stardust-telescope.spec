%global commit cf5f3bc5a4b97aeacfe072725433a66da5bca68d
%global commit_date 20260102
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           stardust-xr-telescope
Version:        %commit_date.git~%shortcommit
Release:        1%?dist
Summary:        See the stars! Easy stardust setups to run on your computer
License:        MIT
URL:            https://github.com/StardustXR/telescope
Source0:        %url/archive/%commit.tar.gz

Requires:       bash
Requires:       xwayland-satellite
Requires:       stardust-xr-armillary
Requires:       stardust-xr-atmosphere
Requires:       stardust-xr-black-hole
Requires:       stardust-xr-comet
Requires:       stardust-xr-flatland
Requires:       stardust-xr-gravity
Requires:       stardust-xr-magnetar
Requires:       stardust-xr-non-spatial-input
Requires:       stardust-xr-protostar
Requires:       stardust-xr-server

BuildArch:      noarch
Provides:       telescope stardust-telescope

%description
See the stars! Easy stardust setups to run on your computer.

%prep
%autosetup -n telescope-%commit

%build

%install
install -Dm755 scripts/telescope                 %buildroot%_bindir/telescope
install -Dm755 scripts/_telescope_startup        %buildroot%_bindir/_telescope_startup
install -Dm644 org.stardustxr.Telescope.desktop  %buildroot%_appsdir/org.stardustxr.Telescope.desktop
install -Dm644 org.stardustxr.Telescope.png      %buildroot%_hicolordir/512x512/apps/org.stardustxr.Telescope.png

%files
%doc README.md
%license LICENSE
%_bindir/telescope
%_bindir/_telescope_startup
%_appsdir/org.stardustxr.Telescope.desktop
%_hicolordir/512x512/apps/org.stardustxr.Telescope.png
