%global rustflags_debuginfo 1

Name:           rnote
Version:        0.12.0
Release:        2%?dist
Summary:        Sketch and take handwritten notes
License:        GPL-3.0
URL:            https://github.com/flxzt/rnote
Packager:       madonuko <mado@fyralabs.com>
Source0:        %{url}/archive/refs/tags/v%version.tar.gz
Recommends:     rnote-cli = %evr
BuildRequires:  rust-packaging
BuildRequires:  cargo meson cmake libappstream-glib gcc-c++ alsa-lib clang-devel python desktop-file-utils mold
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4) >= 4.7
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2
BuildRequires:  pkgconfig(poppler-glib) >= 22.07

%description
Rnote is an open-source vector-based drawing app for sketching, handwritten
notes and to annotate documents and pictures. Targeted at students, teachers
and those who own a drawing tablet, it provides features like PDF and picture
import/export, an infinite canvas and an adaptive UI for big and small screens.

%package cli
Summary: The cli version of rnote (`rnote-cli`)
License: GPL-3.0

%description cli
This provides the `rnote-cli` binary. For more information, see the `rnote` package.


%prep
%autosetup -n rnote-%{version}
%cargo_prep_online

%build
%meson
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies
%meson_build


%install
%meson_install


%files
%doc README.md
%license LICENSE LICENSE.dependencies
%_bindir/rnote
%_datadir/thumbnailers/rnote.thumbnailer
%_datadir/applications/com.github.flxzt.rnote.desktop
%_datadir/glib-2.0/schemas/com.github.flxzt.rnote.gschema.xml
%_datadir/icons/hicolor/scalable/apps/com.github.flxzt.rnote.svg
%_datadir/icons/hicolor/scalable/mimetypes/application-rnote.svg
%_datadir/icons/hicolor/symbolic/apps/com.github.flxzt.rnote-symbolic.svg
%_datadir/locale/*/LC_MESSAGES/rnote.mo
%_datadir/metainfo/com.github.flxzt.rnote.metainfo.xml
%_datadir/mime/packages/com.github.flxzt.rnote.xml
%_datadir/rnote/
%_datadir/fonts/rnote-fonts/

%files cli
%doc README.md
%license LICENSE LICENSE.dependencies
%_bindir/rnote-cli
