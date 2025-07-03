Name:    zapret
Version: 71.1.1
Release: 2%?dist
Summary: A multi-platform Deep Packet Inspection (DPI) bypass tool
License: MIT 
ExcludeArch: s390x
Packager: libffi <contact@ffi.lol>

URL:     https://github.com/bol-van/%{name}
Source0: https://github.com/bol-van/%{name}/archive/refs/tags/v%{version}.tar.gz
Patch0:  chore-move-to-different-dirs.patch
Patch1:  build-dont-strip.patch

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

# NFQws.
%package nfqws
Summary: NFQUEUE-based worker solution.

BuildRequires: libnetfilter_queue-devel
BuildRequires: zlib-ng-compat-devel

Requires: libnetfilter_queue
Requires: zlib-ng-compat

# TPws.
%package tpws
Summary: Transparent proxy worker solution.

%description
A stand-alone (without 3rd party servers) DPI circumvention tool.
May allow to bypass HTTP(S) website blocking or speed shaping, resist
signature TCP/UDP protocol discovery.

%description nfqws
NFQUEUE-based worker solution.

%description tpws
Transparent proxy worker solution.

%prep
%autosetup -S git
rm -rf files/huawei/ # FIX: Remove a busybox dependency.

%build
%make_build systemd

# Credit: https://aur.archlinux.org/packages/zapret-git
%install
  for n in ip2net mdig; do
    install -Dm755 "binaries/my/$n" "%{buildroot}/%{_bindir}/$n"
  done

  install -Dm755 blockcheck.sh -t "%{buildroot}/%{_datadir}/%{name}/"
  install -dm755 "%{buildroot}" %{buildroot}/%{_datadir}/%{name}/files
  cp --reflink=auto -a files/* "%{buildroot}"/%{_datadir}/%{name}/files

  install -Dm644 init.d/systemd/* -t "%{buildroot}%{_prefix}/lib/systemd/system/"
  install -Dm755 init.d/sysv/{functions,%{name}} -t "%{buildroot}/%{_datadir}/%{name}/init.d/sysv/"
  install -Dm755 ipset/* -t "%{buildroot}/%{_datadir}/%{name}/ipset/"
  install -Dm644 common/* -t "%{buildroot}/%{_datadir}/%{name}/common/"

  install -Dm644 /dev/stdin "%{buildroot}/%{_prefix}/lib/sysusers.d/%{name}.conf" << END
u %{name} - "%{name} dpi bypasser"
END

  install -dm755 "%{buildroot}/{%_bindir}"
  for i in init.d/sysv/zapret; do
    mkdir %{buildroot}/%{_bindir} -p
    ln -s "%{_datadir}/%{name}/$i" "%{buildroot}/%{_bindir}/${i##*/}"
  done

  sed -e '1s/$/\n\nWS_USER=%{name}/' -i "%{buildroot}/%{_datadir}/%{name}/init.d/sysv/functions"

  for i in nfq/nfqws tpws/tpws; do
    install -Dm755 "binaries/my/${i##*/}" "%{buildroot}/%{_bindir}/${i##*/}"
  done

  # docs
  install -Dm644 docs/*.* -t "%{buildroot}/usr/share/doc/%{name}"
  install -Dm644 docs/LICENSE.txt "%{buildroot}/usr/share/licenses/%{name}/LICENSE"

  # config
  install -Dm755 config.default %{buildroot}/etc/zapret/config.default
  ln -s config.default %{buildroot}/etc/zapret/config

%files
# Configuration.
%{_sysconfdir}/%{name}/
%{_prefix}/lib/sysusers.d/zapret.conf

# Units.
%{_unitdir}/%{name}-list-update.service
%{_unitdir}/%{name}-list-update.timer
%{_unitdir}/%{name}.service

# Executables.
%{_bindir}/%{name}
%{_bindir}/ip2net
%{_bindir}/mdig

# Share.
%{_datadir}/%{name}

# Documentation.
%{_docdir}/%{name}
%license LICENSE

%files nfqws
# Binaries.
%{_bindir}/nfqws
%{_unitdir}/nfqws@.service

%files tpws
# Binaries.
%{_bindir}/tpws
%{_unitdir}/tpws@.service

%changelog
* Mon May 26 2025 libffi <contact@ffi.lol> - 71
- Bump upstream.
* Thu May 1 2025 libffi <contact@ffi.lol> - 70.6-6
- Fix init.d breakages.
* Thu May 1 2025 libffi <contact@ffi.lol> - 70.6-5
- Depend on subpackages.
* Thu May 1 2025 libffi <contact@ffi.lol> - 70.6-4
- Use subpackages.
* Wed Apr 30 2025 libffi <contact@ffi.lol> - 70.6-3
- Use more macros in the .spec file
* Wed Apr 23 2025 libffi <contact@ffi.lol> - 70.6-2
- Change from /opt/ to /usr/
