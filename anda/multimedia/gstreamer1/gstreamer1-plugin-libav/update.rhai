let release = labels.branch.to_upper();
let ver = get(`https://bodhi.fedoraproject.org/updates/?search=gstreamer1-plugin-libav&status=stable&releases=${release}&rows_per_page=1&page=1`).json().updates[0].title;
rpm.version(find(`gstreamer1-plugin-libav-([\d.]+)`, ver, 1));
rpm.release(find(`gstreamer1-plugin-libav-[\d.]+-([\d.])`, ver, 1));
