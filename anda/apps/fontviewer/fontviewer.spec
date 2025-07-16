Name:           fontviewer
Epoch:          1
Version:        1.2.0
Release:        1%?dist
Summary:        View and install fonts

License:        GPL-2.0
URL:            https://github.com/chocolateimage/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  json-glib-devel

Requires:       gtk3 fontconfig

Packager:       sadlerm <sad_lerm@hotmail.com>

%description
A platform-agnostic GTK+ 3 alternative to GNOME's Font Viewer

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/actions/%{name}-google-symbolic.svg
