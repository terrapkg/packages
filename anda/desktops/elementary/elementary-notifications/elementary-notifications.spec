%global srcname notifications
%global appname io.elementary.notifications


Name:           elementary-notifications
Version:        6.0.3
Release:        1%{?dist}
Summary:        GTK Notification server for Pantheon

License:        GPLv3
URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz


BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libcanberra-devel
BuildRequires:  libcanberra-gtk3
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(libhandy-1) >= 0.91.0
BuildRequires:  meson
BuildRequires:  vala

Provides:      %{name} = %{version}-%{release}


%description


%prep
%autosetup -n %{srcname}-%{version}


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md

%{_bindir}/%{appname}
%{_bindir}/%{appname}.demo
%{_datadir}/applications/%{appname}.demo.desktop

%{_sysconfdir}/xdg/autostart/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_metainfodir}/%{appname}.appdata.xml


%changelog
* Wed Nov 09 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Packaged
