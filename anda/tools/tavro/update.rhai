import "andax/cabal.rhai" as cabal;

rpm.version(hackage("tavro"));
if rpm.changed() {
    cabal::freeze(rpm.f, __script_path);
}
