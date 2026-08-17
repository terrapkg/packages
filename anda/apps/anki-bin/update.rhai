let aarch64_regex = `<a href="https://files\.pythonhosted\.org/packages/(..)/(..)/(.{60})/anki-([\d.]+)-cp(\d+)-abi3-manylinux_.+?_aarch64.whl">`;
let html = get("https://pypi.org/project/anki/");
let relevant = find(aarch64_regex, html, 0);
let ver = find(aarch64_regex, relevant, 4);
rpm.version(ver);
if rpm.changed() {
    rpm.release();
    rpm.global("aurl", find(`"(.+)"`, relevant, 1));
    let cp = find(aarch64_regex, relevant, 5);
    let x86_64_regex = `<a href="https://files\.pythonhosted\.org/packages/(..)/(..)/(.{60})/anki-${ver}-cp${cp}-abi3-manylinux_.+?_x86_64.whl">`;
    let relevant1 = find(x86_64_regex, html, 0);
    rpm.global("xurl", find(`"(.+)"`, relevant1, 1));
    let qhtml = get("https://pypi.org/project/aqt/");
    rpm.global("qurl", find(`<a href="(https://files\.pythonhosted\.org/packages/../../.{60}/aqt-${ver}-py3-none.any.whl)">`, qhtml, 1));
}
