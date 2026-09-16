rpm.version(gh("TeXlyre/texlyre"));
if rpm.changed() {
    rpm.global("drawio_ver", gh("TeXlyre/drawio-embed-mirror").crop(1));
    rpm.global("busytex_ver", gh("TeXlyre/texlyre-busytex").crop(8));
}
