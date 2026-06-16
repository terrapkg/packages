project pkg {
    rpm {
        spec = "enteauth.spec"
    }
    labels {
        mock = 1 # flutter requires root
    }
}
