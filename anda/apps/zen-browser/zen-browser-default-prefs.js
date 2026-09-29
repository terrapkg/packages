// Distribution preferences for the Terra build of Zen Browser.

// Take the locale from the LANG environment variable.
pref("intl.locale.requested", "");

// Use the dictionaries of the system.
pref("spellchecker.dictionary_path", "/usr/share/hunspell");

// The package manager controls the browser, therefore the internal updater
// must stay off.
pref("app.update.auto", false);
pref("app.update.enabled", false);

// Do not show the "make me the default browser" dialog at the first start.
pref("browser.shell.checkDefaultBrowser", false);

// Keep the extensions that the distribution installs.
pref("extensions.autoDisableScopes", 11);
