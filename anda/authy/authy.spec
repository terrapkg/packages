Name: authy
Version: 2.2.1
Release: 2%{?dist}
Summary: Two factor authentication desktop application
License: Unknown
URL: https://authy.com/
Source0: https://api.snapcraft.io/api/v1/snaps/download/H8ZpNgIoPyvmkgxOWw5MSzsXK1wRZiHn_11.snap
Requires: gtk3
Requires: nss
BuildRequires: squashfs-tools

%description

%prep
unsquashfs -q -f -d snap %{SOURCE0}

%install
install -d "%{buildroot}/opt/authy"
cp -r "snap/." "%{buildroot}/opt/authy"

sed -i 's|${SNAP}/meta/gui/icon.png|authy|g' "%{buildroot}/opt/authy/meta/gui/authy.desktop"
install -Dm644 "%{buildroot}/opt/authy/meta/gui/authy.desktop" -t "%{buildroot}/usr/share/applications"
install -Dm644 "%{buildroot}/opt/authy/meta/gui/icon.png" "%{buildroot}/usr/share/pixmaps/authy.png"

rm -rf "%{buildroot}/opt/authy"/{data-dir,gnome-platform,lib,meta,scripts,usr,*.sh}

install -d "%{buildroot}/usr/bin"
ln -s "/opt/authy/authy" "%{buildroot}/usr/bin"

%files
/opt/authy/
/usr/bin/authy
/usr/share/applications/authy.desktop
/usr/share/pixmaps/authy.png

%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Initial release
