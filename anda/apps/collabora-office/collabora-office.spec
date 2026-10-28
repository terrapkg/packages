%global appid com.collaboraoffice.Office
# Desktop releases are tagged coda-<version>-<tagrel> upstream. This is the
# same tag the Flathub manifest pins.
%global tagrel 1
%global srctag coda-%{version}-%{tagrel}
%global lodir %{_libdir}/collaboraoffice

# The engine is a full LibreOffice-based build. Its debuginfo is several GB and
# debugedit takes hours on the merged library, so skip it.
%global debug_package %{nil}
%global _lto_cflags %{nil}
%global __brp_mangle_shebangs %{nil}

%global _pkg_extra_ldflags -fuse-ld=lld

# The engine bundles its own private libraries under %%{lodir}/program. Keep
# them out of the public provides, and drop the requires they satisfy. The
# list of names is written in %%install, so this macro stays lazy (%%define,
# not %%global) and is only read when the dependency generators run.
%global __provides_exclude_from ^%{lodir}/.*$
%define __requires_exclude %(cat %{_builddir}/%{name}-requires-exclude 2>/dev/null)

Name:           collabora-office
Version:        26.04.4.3
Release:        1%{?dist}
Summary:        Office suite based on Collabora Online and LibreOffice technology
# Collabora Online and the Qt app are MPL-2.0. The engine is LibreOffice-based
# (MPL-2.0, with older code under LGPL-3.0-or-later). The bundled third-party
# libraries are listed in CODA-THIRDPARTYLICENSES.html and LICENSE.html.
License:        MPL-2.0 AND LGPL-3.0-or-later AND Apache-2.0 AND BSD-3-Clause AND MIT
URL:            https://www.collaboraoffice.com
Source0:        https://github.com/CollaboraOnline/online.mirror/archive/refs/tags/%{srctag}.tar.gz
# Online UI theme and branding assets, as shipped by the Flathub build.
Source1:        https://www.collaboraoffice.com/downloads/collabora-office-brand/collabora-office-brand-%{version}.tar.gz
# OpenSSL 4 returns const X509_NAME pointers from X509_get_subject_name and
# X509_get_issuer_name.
Patch0:         openssl4-const-x509-name.patch
Packager:       Cypress Reed <cypress@fyralabs.com>
ExclusiveArch:  x86_64 aarch64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gperf
# genbrk, genccode and gencmn
BuildRequires:  icu
BuildRequires:  terra-appstream-helper
BuildRequires:  libtool
BuildRequires:  lld
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  nodejs-npm
BuildRequires:  patch
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::PP)
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-polib
BuildRequires:  python3-setuptools
BuildRequires:  rsync
BuildRequires:  unzip
BuildRequires:  wget
BuildRequires:  zip

# Engine, matching the --with-system-* switches in CPLinuxQtFlatpak.conf
BuildRequires:  cppunit-devel
BuildRequires:  hunspell-devel
BuildRequires:  hyphen-devel
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  libxslt-devel
BuildRequires:  mythes-devel
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(graphite2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(harfbuzz-icu)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

# Qt app
BuildRequires:  libcap-devel
BuildRequires:  pam-devel
BuildRequires:  qt6-linguist
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6WebChannel)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(Qt6WebEngineWidgets)
BuildRequires:  pkgconfig(Qt6WebSockets)
BuildRequires:  pkgconfig(Qt6Widgets)

Requires:       hicolor-icon-theme
# The app shells out to the openssl CLI to mint its loopback certificate.
Requires:       openssl
Recommends:     hunspell-en-US
Recommends:     hyphen-en
Recommends:     mythes-en
Recommends:     google-carlito-fonts
Recommends:     google-crosextra-caladea-fonts
Recommends:     liberation-fonts

%description
Collabora Office is a desktop office suite built on Collabora Online and
LibreOffice technology. It edits text documents, spreadsheets, presentations,
and drawings in OpenDocument and Microsoft Office formats, with the Collabora
Online interface running in a Qt WebEngine window.

%prep
%autosetup -p1 -n online.mirror-%{srctag}
mkdir -p brand
tar -xzf %{SOURCE1} -C brand --strip-components=1

# Translations live in their own repo, tagged alongside the app. There is no
# tarball for them.
git clone --depth=1 --branch=%{srctag} \
    https://gerrit.collaboraoffice.com/translations engine/translations

%conf
pushd engine
# Like Fedora's libreoffice.spec, drop the flags the engine sets itself.
# configure probes the compiler without CFLAGS, so the hardened-ld spec
# would force PIE onto non-PIE objects; --enable-hardening-flags covers it.
for i in $CFLAGS; do
    case "$i" in
        -pipe|-Wall|-Werror*|-fexceptions) continue;;
    esac
    ARCH_FLAGS="$ARCH_FLAGS $i"
done
CFLAGS="$ARCH_FLAGS" CXXFLAGS="$ARCH_FLAGS" \
LDFLAGS="$(echo "$LDFLAGS" | sed 's/-specs=[^ ]*redhat-hardened-ld[^ ]*//g')" \
./autogen.sh \
    --with-distro=CPLinuxQtFlatpak \
    --prefix=$(pwd)/inst \
    --with-parallelism=%{_smp_build_ncpus} \
    --enable-symbols=no \
    --without-package-format
# The engine's gbuild runs its own jobs (--with-parallelism), so plain make.
make
make distro-pack-install
popd

autoreconf -vfi
%configure \
    --enable-qtapp \
    --disable-server \
    --disable-werror \
    --enable-ld \
    --with-lo-builddir=$(pwd)/engine \
    --with-lokit-path=$(pwd)/engine/include \
    --with-lo-path=%{lodir} \
    --with-vendor="Collabora Productivity Limited" \
    --with-app-name="Collabora Office" \
    --with-info-url=https://collaboraoffice.com/

# npm 12 dropped npm-shrinkwrap.json support for "npm ci". configure
# generates the shrinkwrap, so give npm the lockfile name it wants.
cp browser/npm-shrinkwrap.json browser/package-lock.json

%build
%make_build

%install
mkdir -p %{buildroot}%{lodir}
cp -a engine/inst/lib/collaboraoffice/. %{buildroot}%{lodir}/

%make_install
%terra_appstream -o qt/%{appid}.metainfo.xml

python3 scripts/insert-coda-license.py \
    %{buildroot}%{lodir}/LICENSE.html CODA-THIRDPARTYLICENSES.html

cp -a brand/online-theme %{buildroot}%{lodir}/share/theme_definitions/online/
cp -a brand/branding* brand/images brand/welcome \
    %{buildroot}%{_datadir}/coolwsd/browser/dist/

# Every library the engine ships for itself, as a requires filter.
find %{buildroot}%{lodir} \( -name '*.so' -o -name '*.so.*' \) -printf '%%f\n' | sort -u \
    | sed 's/\./\\./g; s/$/.*/' | paste -sd'|' \
    | sed 's/^/^(/; s/$/)$/' > %{_builddir}/%{name}-requires-exclude

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%license COPYING CODA-THIRDPARTYLICENSES.html
%doc README.md
%{_bindir}/coda-qt
%{lodir}/
%{_datadir}/coolwsd/
%{_datadir}/coda-qt/
%{_appsdir}/%{appid}.desktop
%{_metainfodir}/%{appid}.metainfo.xml
%{_iconsdir}/hicolor/*/apps/%{appid}.startcenter.*

%changelog
* Wed Oct 28 2026 Cypress Reed <cypress@fyralabs.com> - 26.04.4.3-1
- Initial package
