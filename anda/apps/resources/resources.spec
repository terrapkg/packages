Name:           resources
Version:        51.0
Release:        1%{?dist}
Summary:        Keep an eye on system resources
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/Incubator/resources
Source0:        %{url}/-/archive/%{version}/resources-%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  cargo
BuildRequires:  ninja-build
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsoup-3.0)

Requires:         cairo
Requires:         graphene
Requires:         gtk4
Requires:         hicolor-icon-theme
Requires:         libadwaita
Requires:         libgcc
Requires:         polkit


%description
Resources is a simple yet powerful monitor for your system resources
and processes, written in Rust and using GTK 4 and libadwaita for its GUI.
It’s capable of displaying usage and details of your CPU, memory, GPUs, NPUs,
network interfaces and block devices. It’s also capable of listing and
terminating running graphical applications as well as processes.

Resources is not a program that will try to display every single possible
piece of information about each tiny part of your device. Instead, it aims
to strike a balance between information richness, user-friendliness and a
balanced user interface — showing you most of the information most
of you need most of the time.

%prep
%autosetup -n %{name}-%{version}

%conf
%meson

%build
%meson_build

%install
%meson_install
%find_lang resources

%files -f resources.lang
%doc README.md
%license LICENSE
%{_bindir}/resources
%{_libexecdir}/resources/resources-adjust
%{_libexecdir}/resources/resources-kill
%{_libexecdir}/resources/resources-processes
%{_appsdir}/org.gnome.Resources.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Resources.gschema.xml
%{_datadir}/polkit-1/actions/org.gnome.Resources.policy
%{_datadir}/resources/resources.gresource
%{_scalableiconsdir}/org.gnome.Resources.svg
%{_hicolordir}/symbolic/apps/org.gnome.Resources-symbolic.svg
%{_metainfodir}/org.gnome.Resources.metainfo.xml

%changelog
* Mon Nov 13 2026 Dave Vasilevsky <dave@vasilevsky.ca>
- Update for version 51.0

* Sat May 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
