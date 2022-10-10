project "pkg" {
    rpm {
        spec = "moby-compose.spec"
        sources = "."
    }
}