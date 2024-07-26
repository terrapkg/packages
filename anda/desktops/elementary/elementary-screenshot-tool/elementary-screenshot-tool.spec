%global srcname screenshot
%global appname io.elementary.screenshot

Name:           elementary-screenshot-tool
Summary:        Screenshot tool designed for elementary
Version:        8.0.0
Release:        1%?dist
License:        LGPL-3.0

URL:            https://github.com/elementary/screenshot
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

# meson: remove deprecated positional arguments from i18n.merge_file calls
#Patch1:         0001-meson-remove-deprecated-positional-arguments-from-i1.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.46
BuildRequires:  vala >= 0.24

BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:  pkgconfig(libhandy-1) >= 0.83.0

Requires:       hicolor-icon-theme

%description
Screenshot tool designed for elementary.


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

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml


%changelog
* Fri Dec 02 2022 root - 6.0.3-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com> - 6.0.2-1
- Repackaged for Terra
