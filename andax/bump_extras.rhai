fn as_bodhi_ver(branch) {
    if branch.starts_with("el") {
        branch.crop(2);
        if branch == "10" {
            return "EPEL-10.0";
        }
        return `EPEL-${release}`;
    } else if branch == "frawhide" {
        return "F43";
    } else if branch.starts_with("f") {
        branch.crop(1);
        return branch;
    } else {
        print(`E: unsupported branch: ${labels.branch}`);
        terminate();
    }
}

fn bodhi(pkg, branch) {
    let url = `https://bodhi.fedoraproject.org/updates/?search=${pkg}&status=stable&releases=${branch}&rows_per_page=1&page=1`;
    return find(`^${pkg}-([\d.]+)-\d+\.[\w\d]+$`, get(url).json().updates[0].title, 1);
}


fn madoguchi_json(pkg, branch) {
    if branch.starts_with("f") {
	    branch.crop(1);
    }
    return get(`https://madoguchi.fyralabs.com/v4/terra${branch}/packages/${pkg}`).json();
}

fn madoguchi(pkg, branch) {
    return madoguchi_json(pkg, branch).ver;
}
