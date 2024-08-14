%global srcname stylesheet
%global appname io.elementary.stylesheet

Name:           elementary-theme
Summary:        Elementary GTK+ Stylesheet
Version:        8.1.0
Release:        1%?dist
License:        GPL-3.0

URL:            https://github.com/elementary/stylesheet
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  sassc
BuildRequires:  fdupes

# gtk-version-specific subpackages were dropped in Fedora 34
Obsoletes:      %{name}-gtk2 < 5.4.2-4.20210216.gitf0c3b7f
Obsoletes:      %{name}-gtk3 < 5.4.2-4.20210216.gitf0c3b7f
Provides:       %{name}-gtk3 = %{version}-%{release}

%description
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.


%package        plank
Summary:        Elementary GTK+ Stylesheet for plank

Requires:       %{name} = %{version}-%{release}
Requires:       plank

Supplements:    (%{name} and plank)

%description    plank
An original Gtk.CSS stylesheet designed specifically for elementary OS
and its desktop environment: Pantheon.

This package contains the plank theme.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

%fdupes %buildroot%_datadir/themes/


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files
%doc README.md
%license COPYING

%dir %{_datadir}/themes/%{appname}.*/
%{_datadir}/themes/%{appname}.*/gtk-3.0/
%{_datadir}/themes/%{appname}.*/gtk-4.0/

%{_datadir}/metainfo/%{appname}.appdata.xml

%files plank
%doc README.md
%license COPYING
%{_datadir}/themes/%{appname}.*/plank/
%{_datadir}/themes/%{appname}.*/plank-dark/


%changelog
%autochangelog
