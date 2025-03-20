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
        return `F${branch}`;
    } else {
        print(`E: unsupported branch: ${labels.branch}`);
        terminate();
    }
}

fn bodhi(pkg, branch) {
    let url = `https://bodhi.fedoraproject.org/updates/?search=${pkg}&status=stable&releases=${branch}&rows_per_page=1&page=1`;
    for entry in get(url).json().updates[0].title.split(' ') {
        let matches = find_all(`${pkg}-([\d.]+)-(\d+)\.[\w\d]+$`, entry);
        //                             ──────── ───── .fc??
        //                             version  release
        if matches.len() != 0 {
            return matches[0][1];
        }
    }
}

fn bodhi_vr(pkg, branch) {
    let url = `https://bodhi.fedoraproject.org/updates/?search=${pkg}&status=stable&releases=${branch}&rows_per_page=1&page=1`;

    for entry in get(url).json().updates[0].title.split(' ') {
        let matches = find_all(`${pkg}-([\d.]+)-(\d+)\.[\w\d]+$`, entry);
        if matches.len() != 0 {
            return matches[0];
        }
    }
}

fn follow_bodhi_vr(rpm, pkg, branch) {
    let vr = bodhi_vr(pkg, branch);
    rpm.version(vr[1]);
    rpm.release(vr[2]);
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
