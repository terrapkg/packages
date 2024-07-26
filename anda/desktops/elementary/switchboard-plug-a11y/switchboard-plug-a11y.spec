%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-a11y

%global plug_type system
%global plug_name accessibility
%global plug_rdnn io.elementary.switchboard.a11y

Name:           switchboard-plug-a11y
Summary:        Switchboard Accessibility plug
Version:        2.3.0
Release:        1%{?dist}
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/switchboard-plug-a11y
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       gala
Requires:       switchboard%{?_isa}
Requires:       wingpanel

Supplements:    (switchboard%{?_isa} and gala and wingpanel)

%description
The accessibility plug is a section in the Switchboard (System Settings)
that allows the user to manage accessibility settings.


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
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml


%changelog
    * Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
    - Repackaged for Terra
