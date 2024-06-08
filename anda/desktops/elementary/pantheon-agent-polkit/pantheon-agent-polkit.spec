%global srcname pantheon-agent-polkit
%global appname io.elementary.desktop.agent-polkit

Name:           pantheon-agent-polkit
Summary:        Pantheon Polkit Agent
Version:        8.0.0
Release:        1%?dist
License:        LGPL-2.0-or-later

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.34.1
BuildRequires:  fdupes

BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk4)

%description
An agent for Polkit authorization designed for Pantheon.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%fdupes %buildroot/%_datadir/locale/
%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_libexecdir}/policykit-1-pantheon/

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
