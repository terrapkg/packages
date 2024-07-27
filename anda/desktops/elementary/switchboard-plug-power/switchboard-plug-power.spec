%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-power

%global plug_type hardware
%global plug_name power
%global plug_rdnn io.elementary.settings.power

Name:           switchboard-plug-power
Summary:        Switchboard Power Plug
Version:        8.0.0
Release:        1%?dist
License:        GPL-2.0-or-later

URL:            https://github.com/elementary/%name
Source0:        %url/archive/%version/%srcname-%version.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
#BuildRequires:  vala
BuildRequires:  fdupes

#BuildRequires:  pkgconfig(dbus-1)
#BuildRequires:  pkgconfig(granite)
#BuildRequires:  pkgconfig(polkit-gobject-1)
#BuildRequires:  polkit-devel
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

# remove the specified stock icon from metainfo (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %buildroot/%_datadir/metainfo/%plug_rdnn.metainfo.xml


%files -f %plug_rdnn.lang
%doc README.md
%license COPYING

%_libdir/switchboard-3/%plug_type/lib%plug_name.so

%_datadir/metainfo/%plug_rdnn.metainfo.xml

%_libexecdir/io.elementary.logind.helper
%_datadir/dbus-1/system-services/io.elementary.logind.helper.service
%_datadir/dbus-1/system.d/io.elementary.logind.helper.conf
%_datadir/polkit-1/actions/%plug_rdnn.policy


%changelog
* Tue Jun 13 2023 windowsboy111 <windowsboy111@fyralabs.com> - 2.7.0-1
- Initial package.
