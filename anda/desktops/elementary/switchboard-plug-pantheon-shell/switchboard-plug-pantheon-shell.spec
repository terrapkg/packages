%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-pantheon-shell

%global plug_type personal
%global plug_name pantheon-desktop
%global plug_rdnn io.elementary.switchboard.pantheon-shell

Name:           switchboard-plug-pantheon-shell
Summary:        Switchboard Pantheon Shell plug
Version:        6.5.0
Release:        1%{?dist}
License:        GPL-3.0

URL:            https://github.com/elementary/switchboard-plug-pantheon-shell
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         dark-theme-wallpaper.patch

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       contractor
Requires:       gala
Requires:       tumbler
Requires:       wingpanel

Requires:       switchboard%{?_isa}
Supplements:    (switchboard%{?_isa} and gala and wingpanel)

%description
The desktop plug is a section in Switchboard, the elementary System
Settings app, where users can configure the wallpaper, dock, and
hotcorners. In the future the desktop plug might also handle other
desktop settings such as the panel, app launcher, and window manager.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_libexecdir}/io.elementary.contract.set-wallpaper

%{_datadir}/contractor/set-wallpaper.contract
%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%changelog
* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 6.3.1-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
