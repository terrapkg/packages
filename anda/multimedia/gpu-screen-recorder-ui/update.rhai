rpm.version(find_all(`/gpu-screen-recorder-ui/tag/\?h=([\d.]+)`, get(`https://git.dec05eba.com/gpu-screen-recorder-ui/refs/`))[0][1]);
