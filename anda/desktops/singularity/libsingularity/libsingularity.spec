%global commit 42a84e0ff3d99cb5beb283389c9274a393779900
%global commit_date 20261031
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libsingularity
Summary:        GTK4 application and widget framework for the Singularity Desktop Environment
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://github.com/singularityos-lab/libsingularity
Source0:        %url/archive/%commit/libsingularity-%commit.tar.gz
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  vala-extra-vapis
BuildRequires:  sassc
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(xkbcommon)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A GTK4 application and widget framework for the Singularity Desktop Environment.

%prep
%autosetup -n libsingularity-%{commit}
sed -i 's/Gtk\.DragIcon\.get_for_drag(drag) as Gtk\.DragIcon/new Gtk.DragIcon.get_for_drag(drag)/' src/animation/drag_lift.vala

%package devel
%pkg_devel_files

%conf
%meson

%build
%meson_build

%install
%meson_install
%{__ln_s} -f %{_datadir}/vala/vapi/singularity-1.0.vapi %{buildroot}%{_datadir}/vala/vapi/libsingularity-1.0.vapi

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/girepository-1.0/Singularity-1.0.typelib
%{_libdir}/libsingularity.so.0
%{_libdir}/libsingularity.so.0.1.0
%{_libdir}/libsingularity-system.so.0
%{_libdir}/libsingularity-system.so.0.1.0
%{_datadir}/vala/vapi/singularity-1.0.vapi
%{_datadir}/vala/vapi/libsingularity-1.0.vapi
%{_datadir}/vala/vapi/singularity-1.0.deps
%{_datadir}/vala/vapi/singularity-system-1.0.deps
%{_datadir}/vala/vapi/singularity-system-1.0.vapi
%{_datadir}/vala/vapi/upower-glib.vapi
%{_datadir}/themes/Singularity/
%{_datadir}/singularity
%{_datadir}/dbus-1/interfaces/dev.sinty.UpdateProvider1.xml
%{_datadir}/glib-2.0/schemas/dev.sinty.toolbar.gschema.xml
%{_sysconfdir}/xdg/singularity/text-recognition.conf

%changelog
* Tue Oct 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Update for new deps
- Update for new files
- Patch DragIcon issue for newer vala versions

* Sat May 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
