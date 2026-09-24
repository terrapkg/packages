let result = sh(`bash prepare-sources.sh`, #{ "cwd": "anda/system/linux-surface/kernel-surface" });

if result.ctx.rc != 0 {
    throw "Failed to generate the kernel-surface spec and sources";
}
