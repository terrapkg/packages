%global srcname calculator
%global appname io.elementary.calculator

Name:           elementary-calculator
Summary:        Calculator app designed for elementary
Version:        2.0.0
Release:        %autorelease
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  appstream
BuildRequires:  meson >= 0.49
BuildRequires:  vala

BuildRequires:  pkgconfig(granite-7) >= 7.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires:  pkgconfig(libhandy-1) >= 0.91.0
BuildRequires:  pkgconfig(gtk4)

Requires:       hicolor-icon-theme

Provides:       pantheon-calculator = %{version}-%{release}
Obsoletes:      pantheon-calculator < 0.1.3-5

%description
A simple calculator for everyday use.

It supports basic and some scientific calculations, including trigonometry
functions (sin, cos, and tan).


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstreamcli validate --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%license COPYING
%doc README.md

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra
