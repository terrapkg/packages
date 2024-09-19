# from Fedora upstream
%global extension   pop-shell
%global uuid        %{extension}@system76.com
%global commit      ced54427487905f42447a07dabff7101b700b5c9
%global shortcommit %{lua:print(macros.commit:sub(1,7))}
%global commit_date 20240919
%global ver         1.2.0

Name:           terra-gnome-shell-extension-%{extension}
Version:        %{ver}^%commit_date.%{shortcommit}
Release:        1%?dist
Summary:        GNOME Shell extension for advanced tiling window management
License:        GPL-3.0-only
URL:            https://github.com/pop-os/shell
BuildArch:      noarch

Source0:        %{url}/archive/%{commit}/%{extension}-%{shortcommit}.tar.gz
Source1:        50_org.gnome.desktop.wm.keybindings.%{extension}.gschema.override
Source2:        50_org.gnome.mutter.%{extension}.gschema.override
Source3:        50_org.gnome.mutter.wayland.%{extension}.gschema.override
Source4:        50_org.gnome.settings-daemon.plugins.media-keys.%{extension}.gschema.override
Source5:        50_org.gnome.shell.%{extension}.gschema.override
# downstream-only
Patch0:         0001-Remove-schema-handling-from-transpile.sh.patch

BuildRequires:  typescript >= 3.8
BuildRequires:  make

Requires:       (gnome-shell >= 45~ with gnome-shell < 46~)
Recommends:     gnome-extensions-app
Recommends:     %{name}-shortcut-overrides = %{version}-%{release}
Provides:       %{extension} = %{version}-%{release}


%description
Pop Shell is a keyboard-driven layer for GNOME Shell which allows for quick and
sensible navigation and management of windows.  The core feature of Pop Shell
is the addition of advanced tiling window management - a feature that has been
highly sought within our community.  For many - ourselves included - i3wm has
become the leading competitor to the GNOME desktop.


%package shortcut-overrides
Summary:        Shortcut overrides for %{name}


%description shortcut-overrides
Shortcut overrides for %{name}.


%prep
%autosetup -p 1 -n shell-%{commit}


%build
%make_build compile


%install
# install main extension files
%make_install

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

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
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml


%files shortcut-overrides
%{_datadir}/glib-2.0/schemas/*.%{extension}.gschema.override


%changelog
%autochangelog
