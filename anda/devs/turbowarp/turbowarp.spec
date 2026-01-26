%define appid     org.turbowarp.TurboWarp

Name:             turbowarp-desktop
%electronmeta -D
Version:          1.15.2
Release:          1%?dist
Summary:          A better offline editor for Scratch 3
URL:              https://desktop.turbowarp.org/
License:          GPL-3.0-only AND %{electron_license}

BuildRequires:    anda-srpm-macros
BuildRequires:    terra-appstream-helper

Requires:         glibc
Requires:         glib2
Requires:         nss-util
Requires:         nss
Requires:         atk
Requires:         gtk3
Requires:         cups-libs
Requires:         libX11
Requires:         libXcomposite
Requires:         libXfixes
Requires:         libXrandr
Requires:         mesa-libgbm
Requires:         expat
Requires:         libxcb
Requires:         libxkbcommon
Requires:         systemd-libs
Requires:         alsa-lib
Requires:         at-spi2-core
Requires:         pcre2
Requires:         libffi
Requires:         zlib-ng
Requires:         libmount
Requires:         libselinux
Requires:         nspr
Requires:         avahi-libs
Requires:         gnutls
Requires:         libpng
Requires:         fontconfig
Requires:         freetype
Requires:         libXrender
Requires:         pixman
Requires:         pango
Requires:         harfbuzz
Requires:         fribidi
Requires:         cairo-gobject
Requires:         gdk-pixbuf2
Requires:         libepoxy
Requires:         libXi
Requires:         libcloudproviders
Requires:         libtinysparql
Requires:         libwayland-client
Requires:         libthai
Requires:         libdrm
Requires:         libXau
Requires:         libcap
Requires:         libblkid
Requires:         krb5-libs
Requires:         libcom_err
Requires:         keyutils-libs
Requires:         openssl-libs
Requires:         p11-kit
Requires:         libidn2
Requires:         libunistring
Requires:         libtasn1
Requires:         nettle
Requires:         gmp
Requires:         libxml2
Requires:         bzip2-libs
Requires:         libbrotli
Requires:         libwayland-cursor
Requires:         libwayland-egl
Requires:         libXcursor
Requires:         libXinerama
Requires:         graphite2
Requires:         glycin-libs
Requires:         json-glib
Requires:         sqlite-libs
Requires:         libdatrie
Requires:         xz-libs
Requires:         lcms2
Requires:         libseccomp

Packager:         junefish <june@fyralabs.com>

%description
%summary.

%prep
%git_clone https://github.com/TurboWarp/desktop %version
%__desktop_file_edit linux-files/%appid.desktop --set-key=Exec --set-value=%{_bindir}/turbowarp-desktop

%build
%npm_build -c -B -r fetch,webpack:prod

%install
%electron_install -i %appid -I build/

%terra_appstream -o linux-files/%appid.metainfo.xml

%__desktop_file_install linux-files/%appid.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/turbowarp-desktop
%{_libdir}/turbowarp-desktop/
%{_appsdir}/%appid.desktop
%{_hicolordir}/512x512/apps/%appid.png
%{_metainfodir}/%appid.metainfo.xml

%changelog
* Sat Jan 24 2026 june-fish <git@june.fish> - 1.15.2
- Initial Package
