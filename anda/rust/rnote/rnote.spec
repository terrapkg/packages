Name:           rnote
Version:        0.5.9
Release:        %autorelease
Summary:        Sketch and take handwritten notes.
License:        GPLv3
URL:            https://github.com/flxzt/rnote
Source0:        %{url}/releases/download/v%{version}/rnote-%{version}.tar.xz
Requires:       libadwaita poppler-glib glib2 gtk4
BuildRequires:  cargo meson cmake libappstream-glib gcc-c++ pkgconfig(alsa) alsa-lib clang-devel
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4) >= 4.7
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2
BuildRequires:  pkgconfig(poppler-glib) >= 22.07

%description
Rnote is an open-source vector-based drawing app for sketching, handwritten notes and to annotate documents and pictures. Targeted at students, teachers and those who own a drawing tablet, it provides features like PDF and picture import and export, an infinite canvas and an adaptive UI for big and small screens.

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

/usr/bin/rnote
/usr/lib/debug/usr/bin/rnote-*.debug
/usr/share/applications/com.github.flxzt.rnote.desktop
/usr/share/glib-2.0/schemas/com.github.flxzt.rnote.gschema.xml
/usr/share/icons/hicolor/scalable/apps/com.github.flxzt.rnote.svg
/usr/share/icons/hicolor/symbolic/apps/com.github.flxzt.rnote-symbolic.svg
/usr/share/locale/*/LC_MESSAGES/rnote.mo
/usr/share/metainfo/com.github.flxzt.rnote.metainfo.xml
/usr/share/mime/packages/com.github.flxzt.rnote.xml
/usr/share/rnote/*


%changelog
* Wed Nov 2 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Fix requires

* Sun Oct 23 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package
