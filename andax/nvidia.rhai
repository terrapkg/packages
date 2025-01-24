// NVIDIA website parser module
// This module is used to parse the NVIDIA website for the latest driver version

fn nvidia_component_list() {
    let series = "12.6.3";
    let url = `https://developer.download.nvidia.com/compute/cuda/redist/redistrib_${series}.json`;
    return get(url).json();
}
fn nvidia_component_version(component) {
    let components = nvidia_component_list();
    return components[component]["version"];
}

fn nvidia_driver_version() {
    let matches = find_all(`(?m)^\s+<span class='dir'><a href='([\d.]+)/'>[\d.]+/</a></span>`, get("https://download.nvidia.com/XFree86/Linux-x86_64/"));
    return(matches[matches.len() - 1][1]);
}
