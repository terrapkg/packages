%global srcname onboarding
%global appname io.elementary.onboarding

Name:           elementary-onboarding
Summary:        Onboarding app for new users
Version:        8.0.0
Release:        1%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/onboarding
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Patch to fix "NotShowIn" in group "Desktop Entry" contains an unregistered value "Installer"
# https://github.com/elementary/onboarding/issues/154
# Patch0:         %%{url}/pull/155.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)     >= 2.64.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7)    >= 7.0.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

Requires:       hicolor-icon-theme

%description
Onboarding application for new users to the Pantheon DE.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

# Remove @2 scaled icons that's not supported by hicolor-icon-theme
# - https://bugzilla.redhat.com/show_bug.cgi?id=1537318
# - https://gitlab.freedesktop.org/xdg/default-icon-theme/-/issues/2
# - https://src.fedoraproject.org/rpms/hicolor-icon-theme/pull-request/2
rm -r %{buildroot}/%{_datadir}/icons/hicolor/*@2/

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%config %_sysconfdir/guest-session/prefs.sh


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com> - 6.1.0-1
- Repackaged for Terra
