fn alma_vr(pkg, repo, branch) {
    if branch.starts_with("el") {
        branch.crop(2);
    } else if branch.starts_with("f") {
        print(`E: alma functions can only be used on el branches`);
        terminate();
    } else {
        print(`E: unsupported branch: ${labels.branch}`);
        terminate();
    }
    let majorminor = [];
    for matches in find_all(`(${branch}\.[\d]+)/`, get("https://repo.almalinux.org/almalinux/")) {
        majorminor += matches[1].parse_float();
    }
    majorminor.dedup();
    majorminor.sort();
    let url = get(`https://repo.almalinux.org/almalinux/${majorminor[majorminor.len()-1]}/${repo}/x86_64/os/Packages/`);
    let matches = find_all(`${pkg}-([\d.]+)-([\d.]+)\.el${branch}.*?\.rpm`, url);
    //                             ──────── ───── .el??
    //                             version  release
    matches.dedup();
    if matches.len() != 0 {
        return matches[0];
    }
}

fn alma(pkg, repo, branch) {
  let vr = alma_vr(pkg, repo, branch);
  return(vr[1]);
}

fn codeberg_commit(repo) {
    return get(`https://codeberg.org/api/v1/repos/${repo}/commits?stat=false&verification=false&files=false&limit=1`).json_arr()[0].sha;
}

fn codeberg(repo) {
    return get(`https://codeberg.org/api/v1/repos/${repo}/releases/latest`).json().tag_name;
}

fn as_bodhi_ver(branch) {
    if branch.starts_with("el") {
        branch.crop(2);
        if branch == "10" {
            return "EPEL-10.1";
        }
        return `EPEL-${release}`;
    } else if branch == "frawhide" {
        return "F45";
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
