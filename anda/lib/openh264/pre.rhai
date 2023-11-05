let cwd = "anda/lib/openh264";
let html = get("https://gstreamer.freedesktop.org/src/gst-plugins-bad/?C=N;O=D");
let gst = find("gst-plugins-bad-([\\d.]+).tar.xz", html, 1);
print(`:: found gst version ${gst}`);
sh(`wget https://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-${gst}.tar.xz`, cwd);
sh(`sh gst-p-bad-cleanup.sh gst-plugins-bad-${gst}.tar.xz`, cwd);
