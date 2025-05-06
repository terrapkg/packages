Name:           pwvucontrol
Version:        0.4.9
Release:        1%?dist
Summary:        Pipewire Volume Control
License:        GPL-3.0-only
URL:            https://github.com/saivert/pwvucontrol
Source0:        %url/archive/refs/tags/%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  rust-packaging anda-srpm-macros cargo-rpm-macros meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libpipewire-0.3)
# pkgconfig(wireplumber-0.4)
BuildRequires:  pkgconfig(wireplumber-0.5)
# glib-compile-resources
BuildRequires:  glib2-devel
BuildRequires:  desktop-file-utils
BuildRequires:	libappstream-glib

%description
%summary.

%prep
%autosetup
%cargo_prep_online

%build
%meson
%{cargo_license_summary_online}
%{cargo_license_online} > LICENSE.dependencies

%install
%cargo_install

%files
%doc README.md
%license COPYING
%_bindir/pwvucontrol
