Name:           rnote
Version:        0.11.0
Release:        1%?dist
Summary:        Sketch and take handwritten notes.
License:        GPL-3.0
URL:            https://github.com/flxzt/rnote
Source0:        %{url}/archive/refs/tags/v%version.tar.gz
Requires:       gtk4
BuildRequires:  cargo meson cmake libappstream-glib gcc-c++ pkgconfig(alsa) alsa-lib clang-devel python desktop-file-utils
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4) >= 4.7
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2
BuildRequires:  pkgconfig(poppler-glib) >= 22.07

%description
Rnote is an open-source vector-based drawing app for sketching, handwritten
notes and to annotate documents and pictures. Targeted at students, teachers
and those who own a drawing tablet, it provides features like PDF and picture
import/export, an infinite canvas and an adaptive UI for big and small screens.

%prep
%autosetup -n rnote-%{version}


%build
%meson
%meson_build


%install
%meson_install


%files
%doc README.md
%license LICENSE

%_bindir/rnote
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


%changelog
* Wed Nov 2 2022 windowsboy111 <windowsboy111@fyralabs.com> - 0.5.7-1
- Fix requires

* Sun Oct 23 2022 windowsboy111 <windowsboy111@fyralabs.com> - 0.5.7-1
- Initial package
