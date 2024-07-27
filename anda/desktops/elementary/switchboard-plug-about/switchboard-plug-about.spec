%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global srcname switchboard-plug-about

%global plug_type hardware
%global plug_name system
%global plug_rdnn io.elementary.settings.system

Name:           switchboard-plug-about
Summary:        Switchboard System Information plug
Version:        8.0.0
Release:        1%?dist
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/switchboard-plug-about
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
#BuildRequires:  vala >= 0.22.0
BuildRequires:  fdupes

#BuildRequires:  pkgconfig(appstream) >= 0.12.10
BuildRequires:  pkgconfig(fwupd)
#BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
#BuildRequires:  pkgconfig(gobject-2.0)
#BuildRequires:  pkgconfig(granite)
#BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
#BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(switchboard-3)
#BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(packagekit-glib2)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Requires:       system-logos

%description
This switchboard plug shows system information.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%fdupes %buildroot%_datadir/locale/
%find_lang %{plug_rdnn}

mv %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml{.in,}
# remove the specified stock icon from metainfo (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_rdnn}.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard-3/%{plug_type}/lib%{plug_name}.so

%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com> - 6.1.0-1
- Repackaged for Terra
