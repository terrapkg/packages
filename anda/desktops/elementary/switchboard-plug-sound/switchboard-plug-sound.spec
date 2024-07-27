%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-sound

%global plug_type system
%global plug_name sound
%global plug_rdnn io.elementary.switchboard.sound

Name:           switchboard-plug-sound
Summary:        Switchboard Sound Plug
Version:        8.0.0
Release:        1%?dist
License:        LGPL-2.0-or-later

URL:            https://github.com/elementary/switchboard-plug-sound
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.34.1

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
A sound plug for Switchboard.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{plug_name}-plug

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
