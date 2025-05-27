# can't figure out how to apply usual build flags to lazbuild
%define debug_package %nil

Name:           peazip
Version:        10.4.0
Release:        1%?dist
Summary:        Free Zip / Unzip software and Rar file extractor. Cross-platform file and archive manager
License:        LGPL-3.0-only
URL:            https://peazip.github.io
Source0:        https://github.com/peazip/PeaZip/archive/refs/tags/%version.tar.gz
# holy smoke this is written in pascal?
BuildRequires:  lazarus-tools
BuildRequires:  lazarus-lcl-gtk2
BuildRequires:  lazarus-lcl-gtk3
BuildRequires:  lazarus-lcl-qt5
BuildRequires:  lazarus-lcl-qt6
Requires:       (peazip-gtk2 or peazip-gtk3 or peazip-gtk4 or peazip-qt5 or peazip-qt6)
Requires:       p7zip brotli zstd
Suggests:       (peazip-gtk4 if gtk4)
Suggests:       (peazip-qt5 if qt5-qtbase)
Suggests:       (peazip-qt6 if qt6-qtbase)

%description
PeaZip is a free file archiver utility and rar extractor for Linux, macOS, and
Windows, which works with 200+ archive types and variants (7z, ace, arc, bz2,
cab, gz, iso, paq, pea, rar, tar, wim, zip, zipx...), handles spanned archives
(001, r01, z01...), supports multiple archive encryption standards, file
hashing, exports tasks as console scripts.

%package gtk2
Summary: GTK2 version of peazip
Requires: peazip
RemovePathPostFixes: .gtk2
%description gtk2
GTK2 version of peazip.
%package gtk3
Summary: GTK3 version of peazip
Requires: peazip
RemovePathPostFixes: .gtk3
%description gtk3
GTK3 version of peazip.
%package qt5
Summary: Qt5 version of peazip
Requires: peazip
RemovePathPostFixes: .qt5
%description qt5
Qt5 version of peazip.
%package qt6
Summary: Qt6 version of peazip
Requires: peazip
RemovePathPostFixes: .qt6
%description qt6
Qt6 version of peazip.


%package -n pea
Summary: Engine for PEA file format support
%description -n pea
Engine for PEA file format support.

%package -n pea-gtk2
Summary: GTK2 version of pea
Requires: pea
RemovePathPostFixes: .gtk2
%description -n pea-gtk2
GTK2 version of pea.
%package -n pea-gtk3
Summary: GTK3 version of pea
Requires: pea
RemovePathPostFixes: .gtk3
%description -n pea-gtk3
GTK3 version of pea.
%package -n pea-qt5
Summary: Qt5 version of pea
Requires: pea
RemovePathPostFixes: .qt5
%description -n pea-qt5
Qt5 version of pea.
%package -n pea-qt6
Summary: Qt6 version of pea
Requires: pea
RemovePathPostFixes: .qt6
%description -n pea-qt6
Qt6 version of pea.

%prep
%autosetup -n PeaZip-%version

%build
cd peazip-sources
lazbuild --add-package dev/metadarkstyle/metadarkstyle.lpk
lazbuild --ws=gtk2 dev/project_peach.lpi && cp dev/peazip ../peazip.gtk2
lazbuild --ws=gtk3 dev/project_peach.lpi && cp dev/peazip ../peazip.gtk3
lazbuild --ws=qt5 dev/project_peach.lpi && cp dev/peazip ../peazip.qt5
lazbuild --ws=qt6 dev/project_peach.lpi && cp dev/peazip ../peazip.qt6
lazbuild --ws=gtk2 dev/project_pea.lpi && cp dev/pea ../pea.gtk2
lazbuild --ws=gtk3 dev/project_pea.lpi && cp dev/pea ../pea.gtk3
lazbuild --ws=qt5 dev/project_pea.lpi && cp dev/pea ../pea.qt5
lazbuild --ws=qt6 dev/project_pea.lpi && cp dev/pea ../pea.qt6

%install
install -Dm755 peazip.* -t %buildroot%_bindir
install -Dm755 pea.* -t %buildroot%_bindir
install -Dm644 peazip-sources/res/share/batch/freedesktop_integration/peazip.desktop -t %{buildroot}%{_datadir}/applications
install -Dm644 peazip-sources/res/share/batch/freedesktop_integration/*.png -t %{buildroot}%{_datadir}/pixmaps
install -Dm644 peazip-sources/res/share/batch/freedesktop_integration/KDE-servicemenus/KDE6-dolphin/peazip-kde6.desktop -t %{buildroot}%{_datadir}/kio/servicemenus
install -Dm644 peazip-sources/res/share/batch/freedesktop_integration/Nautilus-scripts/PeaZip/* -t %{buildroot}%{_datadir}/nautilus/scripts/PeaZip

%files
%doc README.md
%license LICENSE SECURITY.md
%{_datadir}/applications/peazip.desktop
%{_datadir}/pixmaps/peazip*.png
%{_datadir}/kio/servicemenus/peazip-kde6.desktop
%dir %{_datadir}/nautilus/scripts/PeaZip
%{_datadir}/nautilus/scripts/PeaZip/*

%files -n pea
%doc README.md
%license LICENSE SECURITY.md

%files gtk2
%_bindir/peazip.gtk2
%files gtk3
%_bindir/peazip.gtk3
%files qt5
%_bindir/peazip.qt5
%files qt6
%_bindir/peazip.qt6

%files -n pea-gtk2
%_bindir/pea.gtk2
%files -n pea-gtk3
%_bindir/pea.gtk3
%files -n pea-qt5
%_bindir/pea.qt5
%files -n pea-qt6
%_bindir/pea.qt6
