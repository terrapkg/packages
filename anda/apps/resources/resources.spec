Name:           resources
Version:        1.10.2
Release:        1%{?dist}
Summary:        Keep an eye on system resources
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/Incubator/resources
Source0:        %{url}/-/archive/v%{version}/resources-v%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  cargo
BuildRequires:  ninja-build
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

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
%autosetup -n %{name}-v%{version}

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
%{_appsdir}/net.nokyan.Resources.Devel.desktop
%{_datadir}/glib-2.0/schemas/net.nokyan.Resources.Devel.gschema.xml
%{_datadir}/polkit-1/actions/net.nokyan.Resources.Devel.policy
%{_datadir}/resources/resources.gresource
%{_scalableiconsdir}/net.nokyan.Resources.Devel.svg
%{_hicolordir}/symbolic/apps/net.nokyan.Resources.Devel-symbolic.svg
%{_metainfodir}/net.nokyan.Resources.Devel.metainfo.xml

%changelog
* Sat May 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
