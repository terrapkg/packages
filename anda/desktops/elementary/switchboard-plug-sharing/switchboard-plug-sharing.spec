%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-sharing

%global plug_type network
%global plug_name sharing
%global plug_rdnn io.elementary.settings.sharing

Name:           switchboard-plug-sharing
Summary:        Switchboard Sharing Plug
Version:        2.1.6
Release:        1%{?dist}
License:        GPL-3.0

URL:            https://github.com/elementary/switchboard-plug-sharing
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(switchboard-3)

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

%find_lang %{plug_rdnn}


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_rdnn}.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard-3/%{plug_type}/lib%{plug_rdnn}.so

%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%changelog
* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 2.1.6-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
