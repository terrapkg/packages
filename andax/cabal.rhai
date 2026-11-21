fn freeze(spec, script_path) {
    let pkg_dir = sub(`/[^/]+$`, "", script_path);
    let topdir = sh("mktemp -d", #{ "stdout": "piped" }).ctx.stdout;
    topdir.trim();

    let prep = `set -euo pipefail
mkdir -p "$1/SOURCES"
cp -a "$2/." "$1/SOURCES/"
spectool -g -C "$1/SOURCES" "$1/freeze.spec" >&2
rpmbuild -bp --nodeps \
    --define "_topdir $1" \
    --define "_sourcedir $1/SOURCES" \
    --define "cabal_regenerate_freeze HEAD" \
    "$1/freeze.spec" >&2
cat "$(find "$1/BUILD" -mindepth 2 -maxdepth 3 -name cabal.project.freeze -print -quit)"`;
    prep.write(`${topdir}/prep.sh`);
    spec.write(`${topdir}/freeze.spec`);

    let result = sh(`bash '${topdir}/prep.sh' '${topdir}' '${pkg_dir}'`, #{ "stdout": "piped" });
    sh(`rm -rf '${topdir}'`, #{});

    if result.outcome != "success" || result.ctx.rc != 0 || result.ctx.stdout == "" {
        throw `cabal freeze regeneration failed for ${pkg_dir}`;
    }
    result.ctx.stdout.write(`${pkg_dir}/cabal.project.freeze`);
}
