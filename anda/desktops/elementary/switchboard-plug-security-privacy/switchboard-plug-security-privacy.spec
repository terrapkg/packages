%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-security-privacy

%global plug_type personal
%global plug_name security-privacy
%global plug_rdnn io.elementary.switchboard.security-privacy

Name:           switchboard-plug-security-privacy
Summary:        Switchboard Security & Privacy Plug
Version:        8.0.0
Release:        1%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/%name
Source0:        %url/archive/%version/%srcname-%version.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  vala

BuildRequires:  granite-devel
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)
BuildRequires:  meson >= 0.46.1
BuildRequires:  polkit-devel

Requires:       switchboard%{?_isa}

Supplements:    switchboard%{?_isa}

%description
%summary.


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

%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml

%_libdir/switchboard/personal/security-privacy-plug-helper
%_datadir/glib-2.0/schemas/%plug_rdnn.gschema.xml
%_datadir/polkit-1/actions/%plug_rdnn.policy

%changelog
* Tue Jun 13 2023 windowsboy111 <windowsboy111@fyralabs.com> - 7.0.0-1
- Initial package.
