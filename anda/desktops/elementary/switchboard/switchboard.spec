%global srcname switchboard
%global appname io.elementary.switchboard

Name:           switchboard
Summary:        Modular Desktop Settings Hub
Version:        8.0.0
Release:        1%?dist
License:        LGPL-2.0-or-later

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1) >= 0.83.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  fdupes sassc

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Requires:       hicolor-icon-theme

%description
Extensible System Settings application.


%package        libs
Summary:        Modular Desktop Settings Hub (shared library)

%description    libs
Extensible System Settings application.

This package contains the shared library.


%package        devel
Summary:        Modular Desktop Settings Hub (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Extensible System Settings application.

This package contains the files required for developing plugs for
switchboard.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%dnl %find_lang %{appname}

# create plug directories
mkdir -p %{buildroot}/%{_libdir}/%{name}

mkdir -p %{buildroot}/%{_libdir}/%{name}/hardware
mkdir -p %{buildroot}/%{_libdir}/%{name}/network
mkdir -p %{buildroot}/%{_libdir}/%{name}/personal
mkdir -p %{buildroot}/%{_libdir}/%{name}/system

%fdupes %buildroot%_datadir/locale/
%fdupes %buildroot%_datadir/icons/hicolor/


%check
%dnl desktop-file-validate \
%dnl     %{buildroot}/%{_datadir}/applications/%{appname}.desktop

%dnl appstream-util validate-relax --nonet \
%dnl     %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml
