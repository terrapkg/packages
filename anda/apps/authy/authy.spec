%define debug_package %nil
%global _build_id_links none

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

Name: authy
Version: 2.5.0
Release: 1%{?dist}
Summary: Two factor authentication desktop application
License: Unlicense
URL: https://authy.com/
Source0: https://api.snapcraft.io/api/v1/snaps/download/H8ZpNgIoPyvmkgxOWw5MSzsXK1wRZiHn_23.snap
Requires: gtk3
Requires: nss
BuildRequires: squashfs-tools desktop-file-utils

%description
%{summary}.

%prep
unsquashfs -q -f -d snap %{SOURCE0}

%build

%install
install -d %buildroot%_datadir/authy
cp -r snap/. %buildroot%_datadir/authy

sed -i 's|${SNAP}/meta/gui/icon.png|authy|g' %buildroot%_datadir/authy/meta/gui/authy.desktop
install -Dm644 %buildroot%_datadir/authy/meta/gui/authy.desktop -t %buildroot%_datadir/applications
install -Dm644 %buildroot%_datadir/authy/meta/gui/icon.png %buildroot%_datadir/pixmaps/authy.png

rm -rf %buildroot%_datadir/authy/{data-dir,gnome-platform,lib,meta,scripts,usr,*.sh}

install -d %buildroot%_bindir
ln -s %_datadir/authy/authy %buildroot%_bindir

%check
desktop-file-validate %buildroot%_datadir/applications/authy.desktop

%files
%_datadir/authy/
%_bindir/authy
%_datadir/applications/authy.desktop
%_datadir/pixmaps/authy.png

%changelog
* Sat Jun 17 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.3.0-2
- Use /usr/share/ instead of /opt/

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com> - 2.2.1-2
- Initial release
