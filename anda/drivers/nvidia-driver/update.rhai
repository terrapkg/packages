let html = get("https://www.nvidia.com/en-us/drivers/unix/");
let v = find("Linux x86_64/AMD64/EM64T[^\n]+Latest Production Branch Version:\\s*<a[^>]+>\\s*([\\d.]+)\\s*</a>", html, 1);
rpm.version(v);

sh("sed -i -E 's@^VERSION=.+?$@VERSION=${VERSION:-" + v + "}@' anda/drivers/nvidia-driver/nvidia-generate-tarballs.sh");
