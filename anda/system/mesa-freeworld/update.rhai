if !labels.branch.starts_with("f") {
    print(`mesa-freeworld: unsupported branch: ${labels.branch}`);
    terminate();
}
let b = labels.branch;
if b == "frawhide" {
    b = "rawhide";
}
let spec = get(`https://src.fedoraproject.org/rpms/mesa/raw/${b}/f/mesa.spec`);
let v = find(`(?m)^%global\s+ver\s+([\w\d.-]+)$`, spec, 1);
rpm.global("ver", v);
