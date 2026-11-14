%global commit 4e7356a43481ff41b287556906aac0c7e5111535
%global commit_date 20261015
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           singularity-atelier
Summary:        Atelier for the Singularity Desktop Environment
Version:        0~%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
License:        GPL-3.0-or-later
URL:            https://github.com/singularityos-lab/singularity-atelier
Source0:        %url/archive/%commit/singularity-atelier-%commit.tar.gz
Patch0:         libsoup-dep.patch
Patch1:         fix-fedora-rpath.patch
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(singularity-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Atelier for the Singularity Desktop Environment:
sketch, make patterns, grade sizes and prepare tech packs.

%package devel
%pkg_devel_files
%{_libdir}/singularity-atelier/plugins/cut-list/cut-list.plugin
%{_libdir}/singularity-atelier/plugins/cut-list/libatelier-cut-list.so
%{_datadir}/vala/vapi/atelier-plugin.vapi

%prep
%autosetup -C -p1

%conf
%meson

%build
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/singularity-atelier
%{_appsdir}/dev.sinty.atelier.desktop
%{_datadir}/glib-2.0/schemas/dev.sinty.atelier.gschema.xml
%{_scalableiconsdir}/dev.sinty.atelier.svg
%{_metainfodir}/dev.sinty.atelier.metainfo.xml
%{_datadir}/mime/packages/dev.sinty.atelier.xml
%{_datadir}/singularity/app-settings/dev.sinty.atelier.json
%{_datadir}/singularity/files-actions/dev.sinty.atelier.open.ini

%changelog
* Fri Oct 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
