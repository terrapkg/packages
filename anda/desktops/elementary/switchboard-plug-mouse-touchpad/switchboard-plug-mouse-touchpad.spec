%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-mouse-touchpad

%global plug_type hardware
%global plug_name mouse-touchpad
%global plug_rdnn io.elementary.settings.mouse-touchpad

Name:           switchboard-plug-mouse-touchpad
Summary:        Switchboard Mouse and Touchpad plug
Version:        8.0.0
Release:        1%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/switchboard-plug-mouse-touchpad
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(switchboard-3)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

%description
A switchboard plug to configure the behavior of mice and touchpads.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_rdnn}


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_rdnn}.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard-3/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%changelog
* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 7.0.0-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
