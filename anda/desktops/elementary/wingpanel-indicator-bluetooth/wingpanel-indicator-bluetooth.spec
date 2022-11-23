%global __provides_exclude_from ^%{_libdir}/wingpanel/.*\\.so$

%global srcname wingpanel-indicator-bluetooth
%global appname io.elementary.wingpanel.bluetooth

Name:           wingpanel-indicator-bluetooth
Summary:        Bluetooth Indicator for wingpanel
Version:        2.1.8
Release:        %autorelease
License:        LGPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  appstream
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(wingpanel) >= 3.0.0

Requires:       bluez
Requires:       wingpanel%{?_isa}

Supplements:    (wingpanel%{?_isa} and bluez)


%description
A bluetooth indicator for wingpanel.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang bluetooth-indicator

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%check
appstreamcli validate --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f bluetooth-indicator.lang
%doc README.md
%license COPYING

%{_libdir}/wingpanel/libbluetooth.so

%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.bluetooth.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
