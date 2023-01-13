project "pkg" {
    rpm {
        spec = "openasar-canary.spec"
    }
    labels {
        nightly = "1"
    }
}
