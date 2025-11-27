project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "mullvad-vpn.spec"
    }
    labels {
        mock =1
    }
}
