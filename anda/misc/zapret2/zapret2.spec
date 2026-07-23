%define debug_package %nil

Name:    zapret2
Version: 1.0.3
Release: 1%{?dist}
Summary: A multi-platform Deep Packet Inspection (DPI) bypass tool
License: MIT 
Packager: madonuko <mado@fyralabs.com>

URL:     https://github.com/bol-van/%{name}
Source0: https://github.com/bol-van/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: pkgconfig(luajit)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libnetfilter_queue)

# Build tools.
BuildRequires: gcc
BuildRequires: make
BuildRequires: git
# Headers.
BuildRequires: libmnl-devel
BuildRequires: libcap-devel
BuildRequires: systemd-devel

# Runtime libraries.
Requires: libcap
Requires: systemd
Requires: glibc
# Runtime binaries - scripts.
Suggests: nmap-ncat
Suggests: curl
# Runtime binaries - networking.
Requires: ipset
Requires: nftables
# Subpackage dependencies.
Requires: %{name}-nfqws
Requires: %{name}-tpws

%description
A stand-alone (without 3rd party servers) DPI circumvention tool.
May allow to bypass HTTP(S) website blocking or speed shaping, resist
signature TCP/UDP protocol discovery.

%prep
%autosetup

%build
%make_build CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"

# Credit: https://aur.archlinux.org/packages/zapret2
%install
  for i in ip2net mdig; do
    install -Dm755 binaries/my/$i -t %buildroot/%_datadir/%name/$i/
  done

  install -Dm755 blockcheck2.sh -t %buildroot/%_datadir/%name/
  for i in custom standard; do
    install -Dm644 blockcheck2.d/$i/* -t %buildroot/%_datadir/%name/blockcheck2.d/$i/
  done

  for i in fake; do
    install -Dm644 files/$i/* -t %buildroot/%_datadir/%name/files/$i/
  done

  install -Dm755 ipset/*  -t %buildroot/%_datadir/%name/ipset/
  install -Dm644 common/* -t %buildroot/%_datadir/%name/common/
  install -Dm644 lua/*    -t %buildroot/%_datadir/%name/lua/

  install -dm755 %buildroot/%_datadir/%name/init.d/sysv/custom.d/
  install -Dm755 init.d/sysv/{functions,%name} -t %buildroot/%_datadir/%name/init.d/sysv/
  install -Dm644 init.d/systemd/*                 -t %buildroot/usr/lib/systemd/system/

  install -Dm644 /dev/stdin %buildroot/usr/lib/sysusers.d/%name.conf << END
u %name - "%name %summary"
END

  install -dm755 %buildroot/usr/bin
  for i in init.d/sysv/%name; do
    ln -s /%_datadir/%name/$i %buildroot/usr/bin/${i##*/}
  done

  sed -e '1s/$/\n\nWS_USER=%name/' -i %buildroot/%_datadir/%name/init.d/sysv/functions
  install -Dm644 config.default -T %buildroot/%_datadir/%name/config

  for i in nfq2/nfqws2; do
    install -Dm755 binaries/my/${i##*/} -T %buildroot/%_datadir/%name/$i
    ln -s /%_datadir/%name/$i %buildroot/usr/bin/${i##*/}
  done

  install -Dm644 docs/*.*         -t %buildroot/usr/share/doc/%name/
  install -Dm644 docs/LICENSE.txt -T %buildroot/usr/share/licenses/%name/LICENSE

%files
%doc changes.txt changes_compat.txt LICENSE.txt manual.en.md manual.md readme.md
%license docs/LICENSE.txt LICENSE
%_bindir/zapret2
%_bindir/nfqws2
%_unitdir/nfqws2@.service
%_unitdir/zapret2.service
%_unitdir/zapret2-list-update.service
%_unitdir/zapret2-list-update.timer
%config %_sysusersdir/zapret2.conf
%_datadir/zapret2/

%changelog
* Mon Jul 20 2026 madonuko <mado@fyralabs.com> - 1.0.2-1
- Initial package
