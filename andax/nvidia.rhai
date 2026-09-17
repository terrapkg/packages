// NVIDIA website parser module
// This module is used to parse the NVIDIA website for the latest driver version

fn nvidia_component_list() {
    let url = "https://developer.download.nvidia.com/compute/cuda/redist/";
    let matches = find_all("redistrib_[\\d.]+.json", get(url));
    let series = `${url}${matches[matches.len - 1][0]}`;
    return get(series).json();
}
fn nvidia_component_version(component) {
    let components = nvidia_component_list();
    return components[component]["version"];
}

fn nvidia_driver_version() {
    let driver = get("https://gfwsl.geforce.com/services_toolkit/services/com/nvidia/services/AjaxDriverService.php?func=DriverManualLookup&osID=12&languageCode=1033&numberOfResults=1&beta=0").json().IDS[0].downloadInfo.DisplayVersion;
    return(driver);
}

fn nvidia_legacy_version() {
    let driver = get("https://gfwsl.geforce.com/services_toolkit/services/com/nvidia/services/AjaxDriverService.php?func=DriverManualLookup&osID=12&languageCode=1033&numberOfResults=1&beta=0&release=580").json().IDS[0].downloadInfo.DisplayVersion;
    return(driver);
}
