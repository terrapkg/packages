# Caddy built with xcaddy, bundling DNS provider modules for the ACME DNS-01
# challenge. Every version below is bumped by update.rhai.
#
# Included modules (caddy list-modules ID -> Go module):
#   dns.providers.cloudflare  github.com/caddy-dns/cloudflare
#   dns.providers.porkbun     github.com/caddy-dns/porkbun
#   dns.providers.desec       github.com/caddy-dns/desec
#   dns.providers.route53     github.com/caddy-dns/route53
#   dns.providers.hetzner     github.com/caddy-dns/hetzner/v2
#   dns.providers.ovh         github.com/caddy-dns/ovh
#   dns.providers.gandi       github.com/caddy-dns/gandi
#   dns.providers.linode      github.com/caddy-dns/linode
#   dns.providers.powerdns    github.com/caddy-dns/powerdns
#   dns.providers.rfc2136     github.com/caddy-dns/rfc2136
#   dns.providers.acmedns     github.com/caddy-dns/acmedns
#
# caddy-dns/duckdns and caddy-dns/namecheap are left out on purpose: they have
# no license, so they can't be redistributed.
%global xcaddy_ver          v0.4.7
%global dist_ver            v2.11.7
%global cloudflare_ver      v0.2.4
%global porkbun_ver         v0.3.1
%global desec_ver           v1.1.0
%global route53_ver         v1.6.2
%global hetzner_ver         v2.0.1
%global ovh_ver             v1.1.0
%global gandi_ver           v1.2.1
%global linode_ver          v0.8.0
%global powerdns_ver        v1.0.2
%global rfc2136_ver         v1.0.0
%global acmedns_ver         v0.7.0

%global dns_providers cloudflare porkbun desec route53 hetzner ovh gandi linode powerdns rfc2136 acmedns

%global gomodulesmode GO111MODULE=on

Name:           terra-caddy
Version:        2.11.7
Release:        1%{?dist}
Summary:        Web server with automatic HTTPS and DNS provider modules
# Caddy and the caddy-dns modules are Apache-2.0 and MIT; the rest covers
# their vendored Go dependencies (vendor-modules.txt lists them).
License:        Apache-2.0 AND MIT AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND CC0-1.0 AND MPL-2.0 AND OFL-1.1
URL:            https://caddyserver.com
Source0:        https://github.com/caddyserver/dist/archive/refs/tags/%{dist_ver}.tar.gz
# Config, units and sysusers match Fedora's caddy package so this is a
# drop-in replacement for it
Source1:        Caddyfile
Source2:        caddy.service
Source3:        caddy-api.service
Source4:        caddy.sysusers
# From Fedora: the binary is managed by RPM, so drop the commands that
# download and replace it. Applied to the vendored caddy module.
Source10:       0001-Disable-commands-that-can-alter-the-binary.patch
Packager:       Cypress Reed <cypress@fyralabs.com>

BuildRequires:  golang
BuildRequires:  go-rpm-macros
BuildRequires:  git-core
BuildRequires:  patch
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}

Provides:       caddy = %{evr}
Provides:       caddy%{?_isa} = %{evr}
Conflicts:      caddy
Provides:       webserver

%description
Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS.

This build is made with xcaddy and includes DNS provider modules so
certificates can be issued with the ACME DNS-01 challenge: Cloudflare,
Porkbun, deSEC, Amazon Route 53, Hetzner, OVH, Gandi, Linode, PowerDNS,
RFC 2136 and ACME-DNS.

It ships the same caddy.service, caddy-api.service and /etc/caddy layout as
Fedora's caddy package and replaces it.

%pkg_completion -Bfz caddy

%prep
%autosetup -n dist-%(echo %{dist_ver} | sed 's/^v//')

%build
export GOPROXY=https://proxy.golang.org,direct
export GOPATH=$PWD/_gopath
export GOBIN=$PWD/_bin
# keep the module cache deletable when the build tree is cleaned up
export GOFLAGS=-modcacherw
go install github.com/caddyserver/xcaddy/cmd/xcaddy@%{xcaddy_ver}

# Let xcaddy resolve Caddy and the plugins into a module, then build it
# ourselves so the binary gets Fedora's Go build flags.
rm -rf _xcaddy && mkdir _xcaddy
TMPDIR=$PWD/_xcaddy XCADDY_SKIP_BUILD=1 $GOBIN/xcaddy build v%{version} \
    --with github.com/caddy-dns/cloudflare@%{cloudflare_ver} \
    --with github.com/caddy-dns/porkbun@%{porkbun_ver} \
    --with github.com/caddy-dns/desec@%{desec_ver} \
    --with github.com/caddy-dns/route53@%{route53_ver} \
    --with github.com/caddy-dns/hetzner/v2@%{hetzner_ver} \
    --with github.com/caddy-dns/ovh@%{ovh_ver} \
    --with github.com/caddy-dns/gandi@%{gandi_ver} \
    --with github.com/caddy-dns/linode@%{linode_ver} \
    --with github.com/caddy-dns/powerdns@%{powerdns_ver} \
    --with github.com/caddy-dns/rfc2136@%{rfc2136_ver} \
    --with github.com/caddy-dns/acmedns@%{acmedns_ver}

pushd _xcaddy/buildenv_*
go mod tidy -e
go mod vendor
patch -d vendor/github.com/caddyserver/caddy/v2 -p1 < %{S:10}
# xcaddy's default tags, which leave out unused smallstep database drivers
export GO_BUILDTAGS="nobadger nomysql nopgx"
%gobuild -o ../../bin/caddy .
cp -p vendor/modules.txt ../../vendor-modules.txt
find vendor -type f \( -iname 'LICENSE*' -o -iname 'LICENCE*' -o -iname 'COPYING*' \
    -o -iname 'COPYRIGHT*' -o -iname 'NOTICE*' -o -iname 'PATENTS*' \) \
    -exec cp -p --parents -t ../../ {} +
popd

%install
install -D -p -m 0755 -t %{buildroot}%{_bindir} bin/caddy

# man pages
./bin/caddy manpage --directory %{buildroot}%{_mandir}/man8

# config
install -D -p -m 0644 -t %{buildroot}%{_sysconfdir}/caddy %{S:1}
install -d -m 0755 %{buildroot}%{_sysconfdir}/caddy/Caddyfile.d

# systemd units and service user
install -D -p -m 0644 -t %{buildroot}%{_unitdir} %{S:2} %{S:3}
install -D -p -m 0644 %{S:4} %{buildroot}%{_sysusersdir}/caddy.conf

# data directory
install -d -m 0750 %{buildroot}%{_sharedstatedir}/caddy

# welcome page served by the default Caddyfile
install -D -p -m 0644 welcome/index.html %{buildroot}%{_datadir}/caddy/index.html

# shell completions
install -d -m 0755 %{buildroot}%{bash_completions_dir} %{buildroot}%{zsh_completions_dir} %{buildroot}%{fish_completions_dir}
./bin/caddy completion bash > %{buildroot}%{bash_completions_dir}/caddy
./bin/caddy completion zsh > %{buildroot}%{zsh_completions_dir}/_caddy
./bin/caddy completion fish > %{buildroot}%{fish_completions_dir}/caddy.fish

%check
# the version must be embedded correctly (taken from the caddy module)
[[ "$(./bin/caddy version | cut -d' ' -f1)" == "v%{version}" ]]
# every bundled DNS provider must be registered
modules="$(./bin/caddy list-modules --skip-standard)"
for provider in %{dns_providers}; do
    grep -qx "dns.providers.$provider" <<< "$modules"
done
# the binary-replacing commands must be gone
! ./bin/caddy upgrade --help >/dev/null 2>&1

%post
%systemd_post caddy.service caddy-api.service

if [ -x /usr/sbin/getsebool ]; then
    # connect to ACME endpoint to request certificates
    setsebool -P httpd_can_network_connect on
fi
if [ -x /usr/sbin/semanage -a -x /usr/sbin/restorecon ]; then
    # file contexts
    semanage fcontext --add --type httpd_exec_t        '%{_bindir}/caddy'               2> /dev/null || :
    semanage fcontext --add --type httpd_sys_content_t '%{_datadir}/caddy(/.*)?'        2> /dev/null || :
    semanage fcontext --add --type httpd_config_t      '%{_sysconfdir}/caddy(/.*)?'     2> /dev/null || :
    semanage fcontext --add --type httpd_var_lib_t     '%{_sharedstatedir}/caddy(/.*)?' 2> /dev/null || :
    semanage fcontext --add --type httpd_log_t         '%{_localstatedir}/log/caddy(/.*)?' 2> /dev/null || :
    restorecon -r %{_bindir}/caddy %{_datadir}/caddy %{_sysconfdir}/caddy %{_sharedstatedir}/caddy %{_localstatedir}/log/caddy || :
fi
if [ -x /usr/sbin/semanage ]; then
    # QUIC
    semanage port --add --type http_port_t --proto udp 80   2> /dev/null || :
    semanage port --add --type http_port_t --proto udp 443  2> /dev/null || :
    # admin endpoint
    semanage port --add --type http_port_t --proto tcp 2019 2> /dev/null || :
fi

%preun
%systemd_preun caddy.service caddy-api.service

%postun
%systemd_postun_with_restart caddy.service caddy-api.service

if [ $1 -eq 0 ]; then
    if [ -x /usr/sbin/getsebool ]; then
        # connect to ACME endpoint to request certificates
        setsebool -P httpd_can_network_connect off
    fi
    if [ -x /usr/sbin/semanage ]; then
        # file contexts
        semanage fcontext --delete --type httpd_exec_t        '%{_bindir}/caddy'               2> /dev/null || :
        semanage fcontext --delete --type httpd_sys_content_t '%{_datadir}/caddy(/.*)?'        2> /dev/null || :
        semanage fcontext --delete --type httpd_config_t      '%{_sysconfdir}/caddy(/.*)?'     2> /dev/null || :
        semanage fcontext --delete --type httpd_var_lib_t     '%{_sharedstatedir}/caddy(/.*)?' 2> /dev/null || :
        semanage fcontext --delete --type httpd_log_t         '%{_localstatedir}/log/caddy(/.*)?' 2> /dev/null || :
        # QUIC
        semanage port     --delete --type http_port_t --proto udp 80   2> /dev/null || :
        semanage port     --delete --type http_port_t --proto udp 443  2> /dev/null || :
        # admin endpoint
        semanage port     --delete --type http_port_t --proto tcp 2019 2> /dev/null || :
    fi
fi

%files
%license vendor
%doc vendor-modules.txt
%{_bindir}/caddy
%{_mandir}/man8/caddy*.8*
%{_datadir}/caddy
%{_unitdir}/caddy.service
%{_unitdir}/caddy-api.service
%{_sysusersdir}/caddy.conf
%dir %{_sysconfdir}/caddy
%config(noreplace) %{_sysconfdir}/caddy/Caddyfile
%dir %{_sysconfdir}/caddy/Caddyfile.d
%attr(0750,caddy,caddy) %dir %{_sharedstatedir}/caddy

%changelog
* Sat Oct 17 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
