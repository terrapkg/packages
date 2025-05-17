project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "exquisite-linux-templates.spec"
    }
    labels {
        weekly = 2
    }
}
