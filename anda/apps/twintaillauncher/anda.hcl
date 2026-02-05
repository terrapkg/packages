project "pkg" {
    arches = ["x86_64"]
    rpm {
        spec = "twintaillauncher.spec"
    }
    labels {
         mock = 1
     }
}
