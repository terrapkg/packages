let result = sh(`bash prepare-sources.sh`, #{ "cwd": "anda/system/surface-kernel" });

if result.ctx.rc != 0 {
    throw "Failed to generate the terra-surface-kernel spec and sources";
}
