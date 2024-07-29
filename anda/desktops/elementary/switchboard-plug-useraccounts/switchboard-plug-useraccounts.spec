%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-useraccounts

%global plug_type system
%global plug_name useraccounts
%global plug_rdnn io.elementary.settings.useraccounts

Name:           switchboard-plug-useraccounts
Summary:        Switchboard User Accounts Plug
Version:        8.0.0
Release:        1%?dist
License:        LGPL-3.0-or-later

URL:            https://github.com/elementary/%name
Source0:        %url/archive/%version/%srcname-%version.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.46.1
BuildRequires:  fdupes

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(pwquality)
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
%fdupes %buildroot%_datadir/locale/
%find_lang %plug_rdnn


%check
appstream-util validate-relax --nonet \
    %buildroot/%_datadir/metainfo/%plug_rdnn.metainfo.xml


%files -f %plug_rdnn.lang
%doc README.md
%license COPYING

%_libdir/switchboard-3/%plug_type/lib%plug_name.so
%_libdir/switchboard-3/system/useraccounts/guest-session-toggle
%_datadir/metainfo/%plug_rdnn.metainfo.xml
%_datadir/polkit-1/actions/%plug_rdnn.policy


%changelog
* Tue Jun 13 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.4.3-1
- Initial package.
