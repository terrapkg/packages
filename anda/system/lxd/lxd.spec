%global goipath github.com/canonical/lxd
%global archcommit e71f11c92c87d03862c2a32c80f9aac717238dda
%global altcommit  5f5a41d87f8d9e9d4f65be93b4d352b5c94396b4

Name:           lxd
Version:        6.9
Release:        1%{?dist}
Summary:        System container and virtual machine manager

SourceLicense:  AGPL-3.0-only AND Apache-2.0
License:        AGPL-3.0-only AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND LGPL-2.1-only AND MIT AND MPL-2.0 AND Unlicense

URL:            https://canonical.com/lxd

Source0:        https://github.com/canonical/lxd/releases/download/lxd-%{version}/lxd-%{version}.tar.gz
Source2:        https://gitlab.archlinux.org/archlinux/packaging/packages/lxd/-/raw/%{archcommit}/lxd.service
Source3:        https://git.altlinux.org/gears/l/lxd.git?p=lxd.git;a=blob_plain;f=.gear/lxd-startup.service;hb=%{altcommit}#/lxd-startup.service
Source4:        https://gitlab.archlinux.org/archlinux/packaging/packages/lxd/-/raw/%{archcommit}/lxd.sysusers

Packager:       Jaiden Riordan <jade@fyralabs.com>

BuildRequires:  anda-srpm-macros go-rpm-macros gcc systemd-rpm-macros libacl-devel
BuildRequires:  golang >= 1.26.4
BuildRequires:  pkgconfig(lxc) >= 5.0.0
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(dqlite) >= 1.18.2
%{?sysusers_requires_compat}

Requires(post): shadow-utils
Requires:       attr dnsmasq iproute lxcfs nftables rsync squashfs-tools tar xz
Requires:       %{name}-client = %{version}-%{release}

%if 0%{?fedora} <= 44
Requires:       terra-dqlite%{?_isa} >= 1.18.2
%else
Requires:       dqlite%{?_isa} >= 1.18.2
%endif


Recommends:     %{name}-agent = %{version}-%{release}
Recommends:     lxc-templates
Suggests:       btrfs-progs lvm2

%description
LXD is an open source solution for managing virtual machines and system containers.
It provides a security-maintained and scalable environment with minimal overhead.

%package client
Summary:        Command line client for LXD
License:        AGPL-3.0-only AND Apache-2.0

%description client
Command line client for LXD.

%package agent
Summary:        LXD guest agent for virtual machines
License:        AGPL-3.0-only AND Apache-2.0
Recommends:     edk2-ovmf qemu-img qemu-kvm-core swtpm virtiofsd xorriso

%description agent
The agent that runs inside LXD virtual machines. It has to be installed on
the LXD host so it can be injected into VM guests.

%package tools
Summary:        Extra tools for LXD
License:        AGPL-3.0-only AND Apache-2.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      incus-tools

%description tools
Extra tools for LXD.

%prep
%autosetup -p1
rm -rf vendor/dqlite vendor/liblxc
cp -p client/COPYING COPYING.Apache-2.0

%build
export GOTOOLCHAIN=local
export CGO_LDFLAGS_ALLOW="(-Wl,-wrap,pthread_create)|(-Wl,-z,now)"
%global gomodulesmode GO111MODULE=on
mkdir -p _bin _man _completions

# fucking nvidia shit
%define __golang_extldflags -Wl,-z,lazy
BUILDTAGS="libsqlite3" %gobuild -o _bin/lxd ./lxd
%undefine __golang_extldflags
%gobuild -o _bin/lxc ./lxc
%gobuild -o _bin/fuidshift ./fuidshift

gobuild_static() {
    CGO_ENABLED=0 go build -compiler gc -v -tags "rpm_crashtraceback $1" \
        -ldflags "-B 0x$(echo "%{name}-%{version}-%{release}-$2" | sha1sum | cut -d' ' -f1) -compressdwarf=false" \
        -o "_bin/$2" "./$2"
}
gobuild_static "agent netgo" lxd-agent
gobuild_static netgo lxd-benchmark
gobuild_static netgo lxd-convert

for sh in bash zsh fish; do
    _bin/lxc completion $sh > _completions/lxc.$sh
done
_bin/lxc manpage _man/
_bin/lxd manpage _man/

%install
install -Dm755 -t %{buildroot}%{_bindir} _bin/*

install -Dm644 %{SOURCE2} %{buildroot}%{_unitdir}/lxd.service
install -Dm644 %{SOURCE3} %{buildroot}%{_unitdir}/lxd-startup.service
# selinux bullshit
sed -i 's/ lxd\.socket//' %{buildroot}%{_unitdir}/lxd.service
sed -i 's/lxd\.socket/lxd.service/g' %{buildroot}%{_unitdir}/lxd-startup.service
install -Dm644 %{SOURCE4} %{buildroot}%{_sysusersdir}/lxd.conf

install -Dm644 -t %{buildroot}%{_mandir}/man1 _man/*.1
install -Dm644 _completions/lxc.bash %{buildroot}%{bash_completions_dir}/lxc
install -Dm644 _completions/lxc.zsh  %{buildroot}%{zsh_completions_dir}/_lxc
install -Dm644 _completions/lxc.fish %{buildroot}%{fish_completions_dir}/lxc.fish

install -dm711 %{buildroot}%{_localstatedir}/lib/lxd
install -dm700 %{buildroot}%{_localstatedir}/cache/lxd
install -dm700 %{buildroot}%{_localstatedir}/log/lxd

%pre
%sysusers_create_compat %{SOURCE4}

%post
%systemd_post lxd.service lxd-startup.service
if [ $1 -eq 1 ] && ! grep -qs '^root:' %{_sysconfdir}/subuid && ! grep -qs '^root:' %{_sysconfdir}/subgid; then
    usermod --add-subuids 1000000-1000999999 --add-subgids 1000000-1000999999 root || :
fi

%preun
%systemd_preun lxd.service lxd-startup.service

%postun
%systemd_postun lxd.service

%files
%license COPYING
%doc README.md SECURITY.md
%{_bindir}/lxd
%{_unitdir}/lxd.service
%{_unitdir}/lxd-startup.service
%{_sysusersdir}/lxd.conf
%{_mandir}/man1/lxd.*
%dir %attr(0711,root,root) %{_localstatedir}/lib/lxd
%dir %attr(0700,root,root) %{_localstatedir}/cache/lxd
%dir %attr(0700,root,root) %{_localstatedir}/log/lxd

%files client
%license COPYING COPYING.Apache-2.0
%{_bindir}/lxc
%{_mandir}/man1/lxc.*

%files agent
%license COPYING
%{_bindir}/lxd-agent

%files tools
%license COPYING
%{_bindir}/fuidshift
%{_bindir}/lxd-benchmark
%{_bindir}/lxd-convert

%pkg_completion -Bzf -n lxd-client lxc

%changelog
* Tue Oct 13 2026 Jaiden Riordan <jade@fyralabs.com> - 6.9-1
- Initial package
