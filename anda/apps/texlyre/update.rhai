rpm.version(gh("TeXlyre/texlyre"));
if rpm.changed() {
    let drawio = gh("TeXlyre/drawio-embed-mirror");
    drawio.crop(1);
    rpm.global("drawio_ver", drawio);
    let busytex = gh("TeXlyre/texlyre-busytex");
    busytex.crop(8);
    rpm.global("busytex_ver", busytex);
}
