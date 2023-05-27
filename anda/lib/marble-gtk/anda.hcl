project pkg {
	rpm {
		spec = "marble-gtk.spec"
		post_script = "rpmrebuild --change-spec-preamble='sed -e \"s/^Provides:.*/Provides: pkgconfig(marble) = 42/\"' anda-build/rpm/rpms/marble-gtk*.rpm"
	}
}
