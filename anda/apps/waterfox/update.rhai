rpm.version(gh("BrowserWorks/waterfox"));
if rpm.changed() {
    rpm.global("commit", get(`https://api.github.com/repos/BrowserWorks/waterfox/commits/${v}`).json().sha);
    let locales = get(`https://api.github.com/repos/BrowserWorks/waterfox/contents/waterfox/browser/locales?ref=${v}`).json();
    rpm.global("l10n_commit", locales.sha);
}
