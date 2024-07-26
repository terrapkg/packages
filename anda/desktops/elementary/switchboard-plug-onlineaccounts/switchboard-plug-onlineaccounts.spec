%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type network
%global plug_name online-accounts
%global plug_rdnn io.elementary.switchboard.onlineaccounts

Name:           switchboard-plug-onlineaccounts
Summary:        Switchboard Online Accounts plug
Version:        6.5.3
Release:        1%{?dist}
License:        GPL-3.0-or-later

URL:            https://github.com/elementary/switchboard-plug-onlineaccounts
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(camel-1.2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  evolution-data-server-devel 
BuildRequires:  pkgconfig(libhandy-1) >= 1.0.0
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Requires:       hicolor-icon-theme


%description
Manage online accounts and connected applications.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{plug_name}-plug

# remove the specified stock icon from appdata (invalid in libappstream-glib)
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml


%files -f %{plug_name}-plug.lang
%license LICENSE
%doc README.md

%{_datadir}/metainfo/%{plug_rdnn}.metainfo.xml
%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so


%changelog
* Thu Nov 17 2022 windowsboy111 <windowsboy111@fyralabs.com> - 6.5.1-1
- New version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
