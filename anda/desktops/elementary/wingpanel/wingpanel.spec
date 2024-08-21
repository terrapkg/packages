%global appname io.elementary.wingpanel

%global common_description %{expand:
Stylish top panel that holds indicators and spawns an application
launcher.}

Name:           wingpanel
Summary:        Stylish top panel
Version:        8.0.0
Release:        1%?dist
License:        GPL-2.0-or-later
Epoch:          1

URL:            https://github.com/elementary/wingpanel
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         https://github.com/elementary/wingpanel/compare/3.0.5..5d22d436b45decfb2a50d9a7c27f2c961f1dd39f.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.24.0

BuildRequires:  mesa-libEGL-devel

BuildRequires:  pkgconfig(gala) >= 7.1.3-2
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(mutter-clutter-14)
BuildRequires:  pkgconfig(mutter-cogl-14)
BuildRequires:  pkgconfig(mutter-cogl-pango-14)

Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

# wingpanel ayatana appindicator support was abandoned by upstream
# wingpanel-indicator-ayatana-2.0.3-10.fc32 retired for fedora 33+
Obsoletes:      wingpanel-indicator-ayatana < 2.0.3-11

%description %{common_description}


%package        libs
Summary:        Stylish top panel (shared library)
Enhances:       %{name} = %{epoch}:%{version}-%{release}
Enhances:       %{name}-devel = %{epoch}:%{version}-%{release}

%description    libs %{common_description}

This package contains the shared library.


%package        devel
Summary:        Stylish top panel (development files)
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel %{common_description}

This package contains the files required for developing for wingpanel.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# create plugin directory
mkdir -p %{buildroot}/%{_libdir}/wingpanel

# create settings directory
mkdir -p %{buildroot}/%{_sysconfdir}/wingpanel.d


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_bindir}/%{appname}

%{_libdir}/gala/plugins/libwingpanel-interface.so

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml

%files libs
%license COPYING
%doc README.md

%dir %{_sysconfdir}/wingpanel.d
%dir %{_libdir}/wingpanel

%{_libdir}/libwingpanel.so.3
%{_libdir}/libwingpanel.so.3.*

%files devel
%license COPYING
%doc README.md
%{_includedir}/wingpanel/

%{_libdir}/libwingpanel.so
%{_libdir}/pkgconfig/wingpanel.pc

%{_datadir}/vala/vapi/wingpanel.deps
%{_datadir}/vala/vapi/wingpanel.vapi


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com> - 3.0.2-1
- Repackaged for Terra
