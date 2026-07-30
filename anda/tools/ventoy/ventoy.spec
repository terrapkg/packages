%define debug_package %{nil}
%global __strip /bin/true

Name:           ventoy
Version:        1.1.17
Release:        1%{?dist}
Summary:        A new bootable USB solution for ISO/WIM/IMG/VHD(x)/EFI files

License:        GPL-3.0-or-later
URL:            https://www.ventoy.net
Source0:        https://github.com/ventoy/Ventoy/releases/download/v%{version}/%{name}-%{version}-linux.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}
Source3:        %{name}gui
Source4:        %{name}web
Source5:        %{name}plugson
Source6:        %{name}-persistent
Source7:        %{name}-extend-persistent
Source8:        https://raw.githubusercontent.com/ventoy/Ventoy/v%{version}/COPYING
Patch0:         sanitize.patch
Packager:       Caio Bruno <cbrunofb@gmail.com>

ExclusiveArch:  x86_64 aarch64

BuildRequires:  xz
Requires:       bash dosfstools util-linux which xz
Recommends:     e2fsprogs gtk3 polkit
Recommends:     ntfs-3g parted xfsprogs

%description
Ventoy is an open source tool to create bootable USB drive for ISO/WIM/IMG/VHD(x)/EFI files. With Ventoy you don't need to format the disk over and over, just copy the image files to the USB drive and boot them.

%prep
%autosetup -n ventoy-%{version} -p1
cp %{SOURCE8} COPYING

# Decompress bundled tool binaries
pushd tool/%{_arch}
for f in *.xz; do
  xzcat "$f" > "${f%.xz}"
  chmod +x "${f%.xz}"
done
rm -f *.xz
popd

# Log location
sed -i 's|log\.txt|/var/log/ventoy.log|g' WebUI/static/js/languages.js tool/languages.json
sed -i 's|\./log\.txt|/var/log/ventoy.log|g' Ventoy2Disk.sh tool/ventoy_lib.sh tool/VentoyWorker.sh

# Use bash for non-POSIX scripts
sed -i 's|bin/sh|usr/bin/env bash|g' Ventoy2Disk.sh VentoyVlnk.sh tool/create_ventoy_iso_part_dm.sh tool/ventoy_lib.sh tool/VentoyWorker.sh

# Drop bundled tools we replace with system ones
rm -f tool/%{_arch}/{xzcat,hexdump}

%build
# Prebuilt binaries, nothing to compile.

%install
DEST=%{buildroot}/opt/ventoy
install -d -m0755 "$DEST"/{boot,ventoy,tool/%{_arch}}

install -Dm0644 -t "$DEST"/boot/          boot/*
install -Dm0644 -t "$DEST"/ventoy/         ventoy/*
install -Dm0644 -t "$DEST"/tool/           tool/*.{cer,glade,json,sh,xz}
install -Dm0755 -t "$DEST"/tool/%{_arch}/  tool/%{_arch}/*
install -Dm0755 -t "$DEST"/                *.sh
cp -a plugin WebUI "$DEST"/

install -Dm0755 VentoyGUI.%{_arch} "$DEST"/
install -Dm0644 WebUI/static/img/VentoyLogo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm0644 %{SOURCE1} %{buildroot}%{_appsdir}/%{name}.desktop

install -Dm0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}
install -Dm0755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}gui
install -Dm0755 %{SOURCE4} %{buildroot}%{_bindir}/%{name}web
install -Dm0755 %{SOURCE5} %{buildroot}%{_bindir}/%{name}plugson
install -Dm0755 %{SOURCE6} %{buildroot}%{_bindir}/%{name}-persistent
install -Dm0755 %{SOURCE7} %{buildroot}%{_bindir}/%{name}-extend-persistent

# Use system xzcat/hexdump instead of the bundled ones
ln -s %{_bindir}/xzcat   "$DEST"/tool/%{_arch}/xzcat
ln -s %{_bindir}/hexdump "$DEST"/tool/%{_arch}/hexdump

# Drop the gtk2 variant on x86_64 (we ship gtk3/qt5)
%ifarch x86_64
rm -f "$DEST"/tool/%{_arch}/Ventoy2Disk.gtk2
%endif

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_bindir}/%{name}gui
%{_bindir}/%{name}web
%{_bindir}/%{name}plugson
%{_bindir}/%{name}-persistent
%{_bindir}/%{name}-extend-persistent
/opt/ventoy/
%{_appsdir}/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jul 30 2026 Caio Bruno <cbrunofb@gmail.com>
- Initial package
