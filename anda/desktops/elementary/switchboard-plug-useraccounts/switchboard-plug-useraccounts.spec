%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-useraccounts

%global plug_type system
%global plug_name useraccounts
%global plug_rdnn io.elementary.switchboard.useraccounts

Name:           switchboard-plug-useraccounts
Summary:        Switchboard User Accounts Plug
Version:        2.4.3
Release:        2%?dist
License:        LGPL-3.0-or-later

URL:            https://github.com/elementary/%name
Source0:        %url/archive/%version/%srcname-%version.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.46.1
BuildRequires:  vala

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  gobject-introspection-devel
BuildRequires:  gnome-desktop3-devel
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(libhandy-1) >= 0.90.0
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  polkit-devel
BuildRequires:  gtk3-devel
BuildRequires:  switchboard-devel

Requires:       switchboard%?_isa
Supplements:    switchboard%?_isa

%description
%summary.

%prep
%autosetup -n %srcname-%version -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %plug_name-plug


%check
appstream-util validate-relax --nonet \
    %buildroot/%_datadir/metainfo/%plug_rdnn.appdata.xml


%files -f %plug_name-plug.lang
%doc README.md
%license COPYING

%_libdir/switchboard/%plug_type/lib%plug_name.so
%_libdir/switchboard/system/pantheon-useraccounts/guest-session-toggle
%_datadir/metainfo/%plug_rdnn.appdata.xml
%_datadir/polkit-1/actions/%plug_rdnn.policy


%changelog
* Tue Jun 13 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.4.3-1
- Initial package.
