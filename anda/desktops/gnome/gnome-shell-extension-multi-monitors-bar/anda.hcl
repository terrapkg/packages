project pkg {
  arches = ["x86_64"]
    rpm {
        spec = "gnome-shell-extension-multi-monitors-bar.spec"
    }
    labels {
        nightly = 1
    }
}
