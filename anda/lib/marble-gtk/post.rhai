let (rc, out, err) = sh(`rpmrebuild -np --change-spec-preamble='sed -e "s/^Provides:\\s*pkgconfig(marble) = 1\\.3\\.0/Provides: pkgconfig(marble) = 42/"' $(ls | sed '/marble-gtk-d/c\\')`);
print(rc);
print(" === out ===");
print(out);
print("\n === err ===");
print(err);
