import "andax/bump_extras.rhai" as bump;

rpm.version(bump::bodhi("ghc-hspec-core", bump::as_bodhi_ver(labels.branch)));
