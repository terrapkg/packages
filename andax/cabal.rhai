fn freeze(spec, script_path) {
    let pkg_dir = sub(`/[^/]+$`, "", script_path);
    let workdir = sh("mktemp -d", #{ "stdout": "piped" }).ctx.stdout;
    workdir.trim();

    sh(`cp -a '${pkg_dir}/.' '${workdir}/'`, #{});
    spec.write(`${workdir}/freeze.spec`);

    let result = sh(`cabalfreeze '${workdir}/freeze.spec' && cp '${workdir}/cabal.project.freeze' '${pkg_dir}/cabal.project.freeze'`, #{});
    sh(`rm -rf '${workdir}'`, #{});

    if result.outcome != "success" || result.ctx.rc != 0 {
        throw `cabal freeze regeneration failed for ${pkg_dir}`;
    }
}
