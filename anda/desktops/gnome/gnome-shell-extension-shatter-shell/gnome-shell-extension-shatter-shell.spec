%global extension   shatter-shell
%global uuid        %{extension}@adilhanney.com
%global appid       org.gnome.shell.extensions.%{extension}

Name:           gnome-shell-extension-%{extension}
Version:        2.2.0
Release:        2%{?dist}
Summary:        Advanced tiling window management extension for GNOME
License:        GPL-3.0-only
URL:            https://github.com/adil192/shatter-shell
Packager:       Adil Hanney <adilhanney@disroot.org>
BuildArch:      noarch

Source0:        %{url}/archive/refs/tags/%{version}/%{extension}-%{version}.tar.gz

Source1:        50_org.gnome.desktop.wm.keybindings.%{extension}.gschema.override
Source2:        50_org.gnome.mutter.%{extension}.gschema.override
Source3:        50_org.gnome.mutter.wayland.%{extension}.gschema.override
Source4:        50_org.gnome.settings-daemon.plugins.media-keys.%{extension}.gschema.override
Source5:        50_%{appid}.gschema.override
# downstream-only
Patch:          0001-Remove-schema-handling-from-transpile.sh.patch

BuildRequires:  anda-srpm-macros
BuildRequires:  nodejs
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-packaging
BuildRequires:  make

Requires:       gnome-shell >= 48
Recommends:     gnome-extensions-app
Recommends:     %{name}-shortcut-overrides = %{version}-%{release}
Provides:       %{extension} = %{version}-%{release}


%description
Shatter Shell is a keyboard-driven layer for GNOME Shell which allows for quick and
sensible navigation and management of windows.  The core feature of Shatter Shell
is the addition of advanced tiling window management - a feature that has been
highly sought within our community.  For many - ourselves included - i3wm has
become the leading competitor to the GNOME desktop.

Shatter Shell is a fork of Pop Shell.


%package shortcut-overrides
Summary:        Shortcut overrides for %{name}
Conflicts:      gnome-shell-extension-pop-shell-shortcut-overrides


%description shortcut-overrides
Shortcut overrides for %{name}.


%prep
%autosetup -p 1 -n %{extension}-%{version}
%__npm ci


%build
/usr/bin/env %{npm_common_envvars} %make_build compile


%install
# install main extension files
/usr/bin/env %{npm_common_envvars} %make_install

# install the schema file
install -D -p -m 0644 \
    schemas/%{appid}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml

# install the gnome-control-center keybindings
install -d -m 0755 %{buildroot}%{_datadir}/gnome-control-center/keybindings
install -p -m 0644 keybindings/*.xml %{buildroot}%{_datadir}/gnome-control-center/keybindings/

# install the schema override files
install -d -m 0755 %{buildroot}%{_datadir}/glib-2.0/schemas
install -p -m 0644 %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{buildroot}%{_datadir}/glib-2.0/schemas/


%files
%license LICENSE
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml


%files shortcut-overrides
%{_datadir}/glib-2.0/schemas/*.%{extension}.gschema.override


%changelog
* Mon Sep 14 2026 Adil Hanney <adilhanney@disroot.org> - 2.2.0-2
- Port to Terra

* Sun Sep 13 2026 Adil Hanney <adilhanney@disroot.org> - 2.2.0-1
- New:
  - Ported the floating exceptions dialog and color chooser dialog to Adwaita/GTK4, and removed all imports of GTK3.
- Developer:
  - Minor cleanups:  this release is 121 lines slimmer

* Sat Sep 12 2026 Adil Hanney <adilhanney@disroot.org> - 2.1.0-1
- New:
  - Added keyboard shortcuts for horizontal workspaces by @laikq in https://github.com/pop-os/shell/pull/1777.
    (Pop!_OS previously only supported vertical workspaces.)
  - Added smarter floating exceptions:
    - Don't tile non-resizeable windows or non-moveable windows, e.g. Steam's sign-in dialog.
    - Don't tile windows with the "skip-taskbar" flag, e.g. XWaylandVideoBridge's invisible window.
    - This nets us wider compatibility and less reliance on an explicit floating exceptions list.
  - Performance improvement in determining which windows to tile by caching compiled RegExp objects.
- Fixed:
  - Ignore no-op stack resize grabs by @philip-sterne in https://github.com/pop-os/shell/pull/1826.
  - Fixed GNOME 48 crash if you click a tab's close button multiple times, based on @siddhpant's fix for https://github.com/pop-os/shell/issues/1794.
  - Replaced pop orange with adwaita blue in another spot that I forgot last release.
- Developer:
  - Suppressed a warning in `make enable` when you don't have the original pop-shell installed.
  - Minor cleanups: this release is 52 lines slimmer

* Fri Sep 11 2026 Adil Hanney <adilhanney@disroot.org> - 2.0.1-1
- New:
  - Improved the smoothness and symmetry of the fade transition between stacked windows.
  - Switched the default active hint color from Pop Orange to Adwaita Blue.
- Fixed:
  - Stack tabs are now clickable even in the 3px gap around each button.
  - Reduced possibility of a window getting stuck as transparent.
- Developer:
  - Formatted code with `@stylistic/eslint-plugin`.
  - Added `checked` attribute to stack tabs, possibly good for accessibility.
  - Improved safety of `window_exec` by passing the `Tab` directly instead of its index.

* Thu Sep 10 2026 Adil Hanney <adilhanney@disroot.org> - 2.0.0-1
- Features:
  - Rebranded from Pop Shell to Shatter Shell.
  - Added GNOME 51 support.
  - Added a setting to stop Shatter Shell from resetting your windows' positions when untiling.
  - Adwaita-themed tab bar for stacked windows: the tabs are bigger and easier to click, and fit in better with GNOME.
  - Added a fade transition when switching between stacked windows.
- Removals:
  - Removed pop-launcher (Super+/) integration in favor of GNOME's overview.
  - Removed system76-scheduler integration, since it's not common outside of Pop!_OS.
  - Removed the "Show Minimize to Tray Windows" setting in favor of stock GNOME Alt+Tab behavior.
  - Removed the "Show Window Titles" setting since it does nothing on Wayland.
- Fixes:
  - Fixed some tiling jank with a fixed `area_right` function.
    This can possibly be upstreamed but needs benchmarking to see if it's actually an improvement or just placebo.
  - Fixed brief flickers in active hints when tiling/untiling/moving windows.
- Floating window exceptions:
  - New: Steam sign-in dialog
  - New: Firefox Picture-in-Picture windows
  - New: Git Credential Manager login popups
  - New: Firefox "About" dialog
  - Fixed: Floating Window Exceptions config window
- Technical:
  - Replaced manual `.d.ts` bindings with `gjsify/gnome-shell`.
  - Updated to Typescript 7 for 10x faster builds and type checking.
  - Enabled eslint for code style and reducing dynamic types.
  - Removed legacy code for X11 and old GNOME versions (47 or older). This is now Wayland only, just like GNOME.
  - Added some basic CI to make sure code at least compiles.
