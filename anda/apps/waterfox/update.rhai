let v = gh("BrowserWorks/waterfox");
rpm.version(v);
if rpm.changed()) {
    let locales = get(`https://api.github.com/repos/BrowserWorks/waterfox/contents/waterfox/browser/locales?ref=${v}`).json();
    rpm.global("l10n_commit", locales.sha);
}
