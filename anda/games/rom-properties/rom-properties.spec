Name:           rom-properties
Version:        2.7.1
Release:        1%{?dist}
Summary:        File browser extension for managing video game ROM and disc images
License:        GPL-2.0-only
URL:            https://github.com/GerbilSoft/%{name}
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>

Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconf
BuildRequires:  gettext-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libcurl-devel
BuildRequires:  nettle-devel
BuildRequires:  zlib-devel
BuildRequires:  lz4-devel
BuildRequires:  lzo-devel
BuildRequires:  libzstd-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  pugixml-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  kf6-kfilemetadata-devel
BuildRequires:  kf6-kcrash-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk4-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  nautilus-devel
BuildRequires:  cairo-devel
BuildRequires:  gsound-devel
BuildRequires:  gtk3-devel

Requires:       %{name}-common = %{version}-%{release}
Recommends:     %{name}-utils = %{version}-%{release}
Recommends:     lz4
Recommends:     lzo

%description
This shell extension adds a few nice features to file browsers for managing
video game ROM and disc images.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake \
  -DBUILD_GTK3=ON \
  -DBUILD_GTK4=ON \
  -DBUILD_KDE4=OFF \
  -DBUILD_KF5=OFF \
  -DBUILD_KF6=ON \
  -DBUILD_XFCE=OFF \
  -DSPLIT_DEBUG=OFF \
  -DUSE_INTERNAL_XML=OFF
%cmake_build

%install
%cmake_install

%files
%{_defaultdocdir}/%{name}/
%{_libdir}/libromdata.*

%package cli
Summary:        CLI tools for rom-properties
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description cli
Command-line interface tools for rom-properties.

%files cli
%{_bindir}/rpcli

%package common
Summary:        Common files for rom-properties
BuildArch:      noarch

%description common
Common files for rom-properties.

%files common
%{_datadir}/%{name}/amiibo-data.bin
%{_datadir}/applications/com.gerbilsoft.rom-properties.rp-config.desktop
%{_datadir}/metainfo/com.gerbilsoft.rom-properties.metainfo.xml
%{_datadir}/mime/packages/rom-properties.xml
%{_datadir}/locale/*/LC_MESSAGES/rom-properties.mo

%package gtk4
Summary:        GTK4 integration for rom-properties
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     %{name}-localsearch3 = %{version}-%{release}

%description gtk4
GNOME/Nautilus file manager integration for rom-properties.

%files gtk4
%{_libdir}/nautilus/extensions-4/rom-properties-gtk4.so

%package gtk3
Summary:        GTK3 integration for rom-properties
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gtk3
GTK3 file manager integration for rom-properties. Provides extensions
for Nautilus, Caja, Nemo, and Thunar.

%files gtk3
%{_libdir}/nautilus/extensions-3.0/rom-properties-gtk3.so
%{_libdir}/caja/extensions-2.0/rom-properties-gtk3.so
%{_datadir}/caja/extensions/rom-properties-gtk3.caja-extension
%{_libdir}/nemo/extensions-3.0/rom-properties-gtk3.so
%{_libdir}/thunarx-3/rom-properties-gtk3.so

%package kf6
Summary:        KDE6 integration for rom-properties
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description kf6
KDE Plasma 6 file manager integration for rom-properties.

%files kf6
%{_datadir}/kio/servicemenus/rp-convert-to-png.desktop
%{_libdir}/qt6/plugins/kf6/propertiesdialog/xattrview-kf6.so
%{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_rom-properties-kf6.so
%{_libdir}/qt6/plugins/kf6/overlayicon/overlayiconplugin_rom-properties-kf6.so
%{_libdir}/qt6/plugins/kf6/propertiesdialog/rom-properties-kf6.so
%{_libdir}/qt6/plugins/kf6/thumbcreator/RomThumbnailCreator-kf6.so

%package utils
Summary:        Utilities for rom-properties
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
Utility programs for rom-properties including the thumbnail generator
and configuration tool.

%files utils
%{_libexecdir}/rp-download
%{_libexecdir}/rp-thumbnail
%{_datadir}/thumbnailers/rom-properties.thumbnailer
%{_bindir}/rp-stub
%{_bindir}/rp-config

%package localsearch3
Summary:        GNOME localsearch3 integration for rom-properties
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description localsearch3
GNOME localsearch 3.0 extract modules for rom-properties, providing
full-text search integration for ROM and disc image metadata.

%files localsearch3
%{_libdir}/localsearch-3.0/extract-modules/libextract-rom-properties.so
%{_datadir}/localsearch3/extract-rules/14-rp-application-packages.rule
%{_datadir}/localsearch3/extract-rules/14-rp-audio.rule
%{_datadir}/localsearch3/extract-rules/14-rp-banners.rule
%{_datadir}/localsearch3/extract-rules/14-rp-cd-images.rule
%{_datadir}/localsearch3/extract-rules/14-rp-disk-images.rule
%{_datadir}/localsearch3/extract-rules/14-rp-executables.rule
%{_datadir}/localsearch3/extract-rules/14-rp-rom-images.rule
%{_datadir}/localsearch3/extract-rules/14-rp-save-files.rule
%{_datadir}/localsearch3/extract-rules/14-rp-textures.rule

%package thumbnailer-dbus
Summary:        D-Bus thumbnailer service for rom-properties
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description thumbnailer-dbus
D-Bus specialized thumbnailer service for rom-properties.

%files thumbnailer-dbus
%{_bindir}/rp-thumbnailer-dbus
%{_datadir}/dbus-1/services/com.gerbilsoft.rom-properties.SpecializedThumbnailer1.service
%{_datadir}/thumbnailers/com.gerbilsoft.rom-properties.SpecializedThumbnailer1.service

%package apparmor
Summary:        AppArmor profiles for rom-properties
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildArch:      noarch

%description apparmor
AppArmor profiles for rom-properties utilities.

%files apparmor
%{_sysconfdir}/apparmor.d/

%changelog
* Fri Apr 03 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
