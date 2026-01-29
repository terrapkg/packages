%global commit 3f6bbbb6bfaf28da8e3635a67a7d9502ae7a7b11
%global commit_date 20260104
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           stardust-xr-telescope-nightly
Version:        0~%{commit_date}git.%{shortcommit}
Release:        2%?dist
Summary:        See the stars! Easy stardust setups to run on your computer
License:        MIT
URL:            https://github.com/StardustXR/telescope
Source0:        %url/archive/%commit.tar.gz
Patch0:         libexec.patch

Requires:       bash
Requires:       xwayland-satellite
Requires:       stardust-xr-armillary-nightly
Requires:       stardust-xr-atmosphere-nightly
Requires:       stardust-xr-black-hole-nightly
Requires:       stardust-xr-comet-nightly
Requires:       stardust-xr-flatland-nightly
Requires:       stardust-xr-gravity-nightly
Requires:       stardust-xr-magnetar-nightly
Requires:       stardust-xr-non-spatial-input-nightly
Requires:       stardust-xr-protostar-nightly
Requires:       stardust-xr-server-nightly
Requires:       stardust-xr-solar-sailer-nightly

BuildArch:      noarch
Provides:       telescope-nightly stardust-telescope-nightly
Conflicts:      stardust-xr-telescope

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
See the stars! Easy stardust setups to run on your computer.

%prep
%autosetup -n telescope-%commit -p1

%build

%install
install -Dm755 scripts/telescope                 %buildroot%_bindir/telescope
install -Dm755 scripts/_telescope_startup        %buildroot%_libexecdir/telescope_startup
install -Dm644 org.stardustxr.Telescope.desktop  %buildroot%_appsdir/org.stardustxr.Telescope.desktop
install -Dm644 org.stardustxr.Telescope.png      %buildroot%_hicolordir/512x512/apps/org.stardustxr.Telescope.png

%files
%doc README.md
%license LICENSE
%_bindir/telescope
%_libexecdir/telescope_startup
%_appsdir/org.stardustxr.Telescope.desktop
%_hicolordir/512x512/apps/org.stardustxr.Telescope.png

%changelog
* Sun Jan 11 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit (port from stable)
