// Take the locale from the LANG environment variable.
pref("intl.locale.requested", "");

// Use the dictionaries of the system.
pref("spellchecker.dictionary_path", "/usr/share/hunspell");

// The package manager controls the browser, therefore the internal updater
// must stay off.
pref("app.update.auto", false);
pref("app.update.enabled", false);

// Do not show the default-browser prompt at first start.
pref("browser.shell.checkDefaultBrowser", false);

// Avoid Wayland session-management issues seen on Fedora 45+.
pref("widget.wayland.session-management.enabled", false);

// Keep extensions installed by the distribution enabled.
pref("extensions.autoDisableScopes", 11);
