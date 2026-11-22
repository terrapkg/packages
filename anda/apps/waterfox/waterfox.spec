%global giturl          https://github.com/BrowserWorks/waterfox
%global commit          4416ccc3421edf75265e987fa8e693a2639322c4
%global l10n_commit     022908fe5b6236c6746d5e2810c9f4f346dd518f
%global appid           net.waterfox.waterfox
%global name_pretty     Waterfox
%global appstream_component desktop-application
%global wfdir           %{_libdir}/%{name}
%global brandingdir     waterfox/browser/branding
%global l10ndir         waterfox/browser/locales

%global rust_triple     %{_arch}-unknown-linux-gnu

%global debug_package   %{nil}
%global _lto_cflags     %{nil}
%undefine _package_note_flags
%global _package_note_status 0

%global __provides_exclude_from ^%{wfdir}
%global __requires_exclude ^(%%(find %{buildroot}%{wfdir} -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))

%global toolchain clang

Name:           waterfox
Version:        6.7.9
Release:        1%{?dist}
Summary:        Privacy-focused web browser built for power users

License:        MPL-2.0
URL:            https://www.waterfox.com

Source0:        %{giturl}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/BrowserWorks/l10n/archive/%{l10n_commit}.tar.gz#/%{name}-l10n-%{l10n_commit}.tar.gz
Source2:        waterfox.sh.in
Source3:        %{appid}.desktop
Source4:        waterfox-default-prefs.js
Source5:        distribution.ini
Source6:        %{appid}.metainfo.xml

ExclusiveArch:  x86_64 aarch64

BuildRequires:  anda-srpm-macros
BuildRequires:  terra-appstream-helper
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  lld
BuildRequires:  compiler-rt
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  cbindgen
BuildRequires:  nasm >= 2.14
BuildRequires:  yasm
BuildRequires:  sccache
BuildRequires:  make
BuildRequires:  m4
BuildRequires:  perl-interpreter
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  nodejs
BuildRequires:  zip
BuildRequires:  unzip
BuildRequires:  xz

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  nss-static
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libvpx-devel
BuildRequires:  pixman-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  bzip2-devel
BuildRequires:  libproxy-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  pciutils-libs

Requires:       hicolor-icon-theme
Requires:       xdg-utils

Recommends:     ffmpeg-free
Recommends:     libva
Recommends:     libnotify
Recommends:     xdg-desktop-portal
Recommends:     speech-dispatcher
Suggests:       hunspell

Provides:       webclient

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Waterfox is a privacy-focused browser built on Firefox ESR for power users who
value customization and control. Telemetry, experiments, analytics and ad
feeds are removed, and layout options that usually need userChrome.css are
available in the settings.

%prep
%autosetup -n %{name}-%{version}
%{__rm} -rf %{l10ndir}
%{__mkdir_p} %{l10ndir}
%{__tar} -xf %{S:1} -C %{l10ndir} --strip-components=1

echo '%{version}' > browser/config/version_display.txt

%build
export MOZBUILD_STATE_PATH="%{_builddir}/mozbuild"
export MOZ_NOSPAM=1
export MOZILLA_OFFICIAL=1
export MOZ_BUILD_DATE=$(date -u +%%Y%%m%%d%%H%%M%%S)

moz_filter_flags() {
    %{__sed} -e 's/-Wall//' \
             -e 's/-fexceptions//' \
             -e 's/-Werror=format-security//' \
             -e 's/-fcf-protection//' \
             -e 's/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2/'
}
MOZ_CFLAGS=$(echo "%{build_cflags}" | moz_filter_flags)
MOZ_CXXFLAGS=$(echo "%{build_cxxflags}" | moz_filter_flags)

cat > .mozconfig <<EOF
ac_add_options --enable-application=browser
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/objdir

ac_add_options --host=%{rust_triple}
ac_add_options --target=%{rust_triple}
ac_add_options --prefix="%{_prefix}"
ac_add_options --libdir="%{_libdir}"

ac_add_options --with-app-name=%{name}
ac_add_options --with-app-basename=Waterfox
ac_add_options --with-branding=%{brandingdir}
ac_add_options --with-distribution-id=net.waterfox
ac_add_options --with-l10n-base=\$topsrcdir/%{l10ndir}
ac_add_options --enable-update-channel=release
ac_add_options --without-onnx-runtime
export MOZ_SOURCE_REPO=%{giturl}
export MOZ_SOURCE_CHANGESET=%{commit}

ac_add_options --enable-release
ac_add_options --enable-optimize
ac_add_options --enable-hardening
ac_add_options --enable-rust-simd
ac_add_options --enable-jxl
ac_add_options --disable-debug
ac_add_options --disable-debug-symbols
ac_add_options --disable-debug-js-modules
ac_add_options --disable-dmd
ac_add_options --disable-profiling
ac_add_options --disable-tests
ac_add_options --disable-rust-tests
ac_add_options --disable-geckodriver
ac_add_options --disable-updater
ac_add_options --disable-crashreporter
ac_add_options --disable-bootstrap

ac_add_options MOZ_TELEMETRY_REPORTING=
ac_add_options --with-unsigned-addon-scopes=app,system
ac_add_options --allow-addon-sideload
export MOZ_REQUIRE_SIGNING=

ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-zlib
ac_add_options --with-system-jpeg
ac_add_options --with-system-libvpx
ac_add_options --with-system-webp
ac_add_options --with-system-libevent
ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman
ac_add_options --without-system-icu

ac_add_options --enable-alsa
ac_add_options --enable-pulseaudio
ac_add_options --enable-necko-wifi

ac_add_options --without-wasm-sandboxed-libraries
ac_add_options --without-sysroot

ac_add_options --enable-linker=lld
ac_add_options --enable-lto=cross,thin
ac_add_options --disable-elf-hack
ac_add_options --enable-strip
ac_add_options --enable-install-strip
ac_add_options --with-libclang-path=$(llvm-config --libdir)

ac_add_options --with-ccache=%{__sccache}
mk_add_options 'export RUSTC_WRAPPER=%{__sccache}'

export CC="%{__cc}"
export CXX="%{__cxx}"
export AR="llvm-ar"
export NM="llvm-nm"
export RANLIB="llvm-ranlib"
export CFLAGS="$MOZ_CFLAGS"
export CXXFLAGS="$MOZ_CXXFLAGS"
export LDFLAGS="%{build_ldflags}"
EOF

%ifarch x86_64
echo 'ac_add_options --enable-eme=widevine' >> .mozconfig
%endif

%constrain_build -m 4096
echo "mk_add_options MOZ_MAKE_FLAGS=\"-j%{_smp_build_ncpus}\"" >> .mozconfig

./mach build

complete_locales=$(
    cd %{l10ndir}
    for locale in */; do
        locale=${locale%/}
        [ "$locale" = ja-JP-mac ] && continue
        count=$(find "$locale"/browser "$locale"/toolkit "$locale"/waterfox -type f -size +0 2>/dev/null | wc -l)
        [ "$count" -ge 10 ] && echo "$locale"
    done | LC_ALL=C sort -u | paste -sd ' ' -
)
test -n "$complete_locales"
./mach package-multi-locale --locales $complete_locales

%install
packages=(objdir/dist/%{name}-*.linux-*.tar.*)
test ${#packages[@]} -eq 1
%{__mkdir_p} %{buildroot}%{_libdir}
%{__tar} -xf "${packages[0]}" -C %{buildroot}%{_libdir}
test -x %{buildroot}%{wfdir}/%{name}

%{__rm} -f %{buildroot}%{wfdir}/updater \
           %{buildroot}%{wfdir}/updater.ini \
           %{buildroot}%{wfdir}/update-settings.ini

%{__sed} -e 's,__PREFIX__,%{_prefix},g' \
         -e 's,__APP_DIR__,%{wfdir},g' \
         -e 's,__APP_NAME__,%{name},g' \
         %{S:2} | %{__install} -Dm755 /dev/stdin %{buildroot}%{_bindir}/%{name}

%desktop_file_install %{S:3}

for size in 16 22 24 32 48 64 128 256; do
    %{__install} -Dpm644 %{brandingdir}/default${size}.png \
        %{buildroot}%{_hicolordir}/${size}x${size}/apps/%{appid}.png
done

%{__install} -Dpm644 %{S:4} %{buildroot}%{wfdir}/browser/defaults/preferences/vendor.js
%{__install} -Dpm644 %{S:5} %{buildroot}%{wfdir}/distribution/distribution.ini

%{__rm} -rf %{buildroot}%{wfdir}/dictionaries
%{__ln_s} -f %{_datadir}/hunspell %{buildroot}%{wfdir}/dictionaries

%terra_appstream -o %{S:6}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%license LICENSE
%doc README.md
%{wfdir}/
%{_bindir}/%{name}
%{_appsdir}/%{appid}.desktop
%{_hicolordir}/*/apps/%{appid}.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sun Nov 22 2026 Cypress Reed <cypress@fyralabs.com> - 6.7.9-1
- Initial package
