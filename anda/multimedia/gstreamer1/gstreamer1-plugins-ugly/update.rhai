let release = labels.branch.to_upper();
let ver = get(`https://bodhi.fedoraproject.org/updates/?search=gstreamer1-plugins-ugly-free&status=stable&releases=${release}&rows_per_page=1&page=1`).json().updates[0].title;
rpm.version(find(`gstreamer1-plugins-ugly-free-([\d.]+)`, ver, 1));
rpm.release(find(`gstreamer1-plugins-ugly-free-[\d.]+-([\d.])`, ver, 1));
