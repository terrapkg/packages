// Latest release of a Go module, as resolved by the Go module proxy
fn go_latest(path) {
    get_json(`https://proxy.golang.org/${path}/@latest`).Version
}

let modules = #{
    cloudflare_ver: "github.com/caddy-dns/cloudflare",
    porkbun_ver: "github.com/caddy-dns/porkbun",
    desec_ver: "github.com/caddy-dns/desec",
    route53_ver: "github.com/caddy-dns/route53",
    hetzner_ver: "github.com/caddy-dns/hetzner/v2",
    ovh_ver: "github.com/caddy-dns/ovh",
    gandi_ver: "github.com/caddy-dns/gandi",
    linode_ver: "github.com/caddy-dns/linode",
    powerdns_ver: "github.com/caddy-dns/powerdns",
    rfc2136_ver: "github.com/caddy-dns/rfc2136",
    acmedns_ver: "github.com/caddy-dns/acmedns",
};

let release = find(`(?m)^Release:\s*(\d+)`, rpm.f, 1).parse_int();

rpm.global("xcaddy_ver", go_latest("github.com/caddyserver/xcaddy"));
let dist_tags = gh_tags("caddyserver/dist");
rpm.global("dist_ver", dist_tags[dist_tags.len - 1]);
for name in modules.keys() {
    rpm.global(name, go_latest(modules[name]));
}
let deps_changed = rpm.changed();

let old_version = find(`(?m)^Version:\s*(\S+)`, rpm.f, 1);
rpm.version(go_latest("github.com/caddyserver/caddy/v2"));
let new_version = find(`(?m)^Version:\s*(\S+)`, rpm.f, 1);

// A new Caddy release resets Release; a module-only bump needs a new one
if deps_changed && old_version == new_version {
    rpm.release(release + 1);
}
