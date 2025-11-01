Name:			keyd
Version:		2.5.0
Release:		3%?dist
Summary:		Key remapping daemon for linux
URL:			https://github.com/rvaiya/keyd
License:		MIT
Source0:        %url/archive/refs/tags/v%version.tar.gz
BuildRequires:	gcc mold make kernel-headers systemd-rpm-macros anda-srpm-macros
Packager:   madonuko <mado@fyralabs.com>

%description
keyd provides a flexible system wide daemon which remaps keys using kernel
level input primitives (evdev, uinput).

%prep
%autosetup
cat<<EOF > keyd.conf
g keyd -
EOF

%build
%make_build PREFIX=%_prefix LDFLAGS="$LDFLAGS -fuse-ld=mold"

%install
%make_install PREFIX=%_prefix LDFLAGS="$LDFLAGS -fuse-ld=mold"
install -Dm644 keyd.service %buildroot%_unitdir/keyd.service
install -Dm644 keyd.conf -t %buildroot%_sysusersdir
install -Dm755 scripts/dump-xkb-config -t %buildroot%_datadir/keyd/
install -Dm755 scripts/generate_xcompose -t %buildroot%_datadir/keyd/

%post
%systemd_post keyd.service

%preun
%systemd_preun keyd.service

%postun
%systemd_postun_with_restart keyd.service

%files
%doc README.md
%license LICENSE
%_unitdir/keyd.service
%_bindir/keyd
%_bindir/keyd-application-mapper
%_datadir/keyd
%_datadir/doc/keyd/
%_sysusersdir/keyd.conf
%_mandir/man1/keyd-application-mapper.1.gz
%_mandir/man1/keyd.1.gz
