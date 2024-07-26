%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-sharing

%global plug_type network
%global plug_name sharing
%global plug_rdnn io.elementary.switchboard.sharing

Name:           switchboard-plug-sharing
Summary:        Switchboard Sharing Plug
Version:        8.0.0
Release:        1%?dist
License:        GPL-3.0

URL:            https://github.com/elementary/switchboard-plug-sharing
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       rygel
Requires:       switchboard%{?_isa}

Supplements:    (switchboard%{?_isa} and rygel)

%description
Configure the sharing of system services.


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
* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 2.1.6-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
