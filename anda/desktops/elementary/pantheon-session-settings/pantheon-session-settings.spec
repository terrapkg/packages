%global srcname session-settings

Name:           pantheon-session-settings
Summary:        Pantheon session configuration files
Version:        35.0
Release:        %autorelease
License:        GPLv3

URL:            https://pagure.io/pantheon-fedora/session-settings
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

Requires:       elementary-settings-daemon
Requires:       gala
Requires:       gnome-disk-utility
Requires:       gnome-keyring
Requires:       gnome-session
Requires:       gnome-session-xsession
Requires:       gnome-settings-daemon
Requires:       orca
Requires:       pantheon-agent-geoclue2
Requires:       pantheon-agent-polkit
Requires:       plank
Requires:       xdg-user-dirs-gtk
Requires:       wingpanel

# experimental wayland session is not provided anymore
Obsoletes:      %{name}-wayland < 0.9.90-3

# cerbere is obsolete and retired on fedora 32+
Obsoletes:      cerbere < 2.5.0-5

# merged overrides into main package on fedora 34
Obsoletes:      %{name}-overrides < 33.91-1
Provides:       %{name}-overrides = %{version}-%{release}

# default fonts, icons, sounds, and GTK theme
Requires:       elementary-icon-theme
Requires:       elementary-sound-theme
Requires:       elementary-theme
Requires:       open-sans-fonts

%description
Configuration files and settings overrides for the Pantheon desktop session.


%prep
%autosetup -n %{srcname}-%{version} -p1


%install
# copy / create autostart entries for the Pantheon session
mkdir -p %{buildroot}/%{_sysconfdir}/xdg/autostart
cp -p autostart/* %{buildroot}/%{_sysconfdir}/xdg/autostart/

# copy Pantheon gnome-session configuration files
mkdir -p %{buildroot}/%{_datadir}/gnome-session/sessions
cp -p gnome-session/* %{buildroot}/%{_datadir}/gnome-session/sessions/

# copy list of default application overrides for Pantheon
mkdir -p %{buildroot}/%{_datadir}/applications
cp -p applications/pantheon-mimeapps.list %{buildroot}/%{_datadir}/applications

# copy Pantheon xsession configuration file
mkdir -p %{buildroot}/%{_datadir}/xsessions
cp -p xsessions/pantheon.desktop %{buildroot}/%{_datadir}/xsessions/

# copy Overrides schema to appropriate location
mkdir -p %{buildroot}/%{_datadir}/glib-2.0/schemas
cp -p overrides/io.elementary.desktop.gschema.override %{buildroot}/%{_datadir}/glib-2.0/schemas/

#iInstall accountsservice extension files
mkdir -p %{buildroot}/%{_datadir}/dbus-1/interfaces
cp -p accountsservice/io.elementary.pantheon.AccountsService.xml \
    %{buildroot}/%{_datadir}/dbus-1/interfaces/

mkdir -p %{buildroot}/%{_datadir}/polkit-1/actions
cp -p accountsservice/io.elementary.pantheon.AccountsService.policy \
    %{buildroot}/%{_datadir}/polkit-1/actions/

mkdir -p %{buildroot}/%{_datadir}/accountsservice/interfaces
ln -s ../../dbus-1/interfaces/io.elementary.pantheon.AccountsService.xml \
    %{buildroot}/%{_datadir}/accountsservice/interfaces/io.elementary.pantheon.AccountsService.xml


# these scriptlets are apparently still necessary, because
# .override files don't seem to trigger schema recompilation
%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%license COPYING
%doc README.md NEWS.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/*.desktop

%{_datadir}/applications/pantheon-mimeapps.list
%{_datadir}/accountsservice/interfaces/io.elementary.pantheon.AccountsService.xml
%{_datadir}/dbus-1/interfaces/io.elementary.pantheon.AccountsService.xml
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.gschema.override
%{_datadir}/gnome-session/sessions/pantheon.session
%{_datadir}/polkit-1/actions/io.elementary.pantheon.AccountsService.policy
%{_datadir}/xsessions/pantheon.desktop


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
