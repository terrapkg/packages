project pkg {
    arches = ["x86_64", "aarch64"]
    rpm {
        spec = "terra-caddy.spec"
    }
    labels {
        subrepo = "extras"
    }
}
