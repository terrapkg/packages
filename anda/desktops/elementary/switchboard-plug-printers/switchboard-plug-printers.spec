%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-printers

%global plug_type hardware
%global plug_name printers
%global plug_rdnn io.elementary.settings.printers

Name:           switchboard-plug-printers
Summary:        Switchboard Printers Plug
Version:        8.0.0
Release:        1%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/switchboard-plug-printers
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
#BuildRequires:  vala >= 0.22.0
BuildRequires:  fdupes

BuildRequires:  cups-devel

BuildRequires:  pkgconfig(glib-2.0)
#BuildRequires:  pkgconfig(granite) >= 6.0.0
#BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-3)

Requires:       cups%{?_isa}
Requires:       switchboard%{?_isa}

Supplements:    (switchboard%{?_isa} and cups%{?_isa})

%description
A printers plug for Switchboard.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%fdupes %buildroot%_datadir/locale/
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
* Thu Nov 17 2022 windowsboy111 <wboy111@outlook.com> - 2.2.1-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
