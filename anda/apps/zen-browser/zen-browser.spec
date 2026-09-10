%global giturl          https://github.com/zen-browser/desktop
%global appid           app.zen_browser.zen
%global name_pretty     Zen Browser
%global appstream_component desktop-application
%global zen_app_name    zen
%global zendir          %{_libdir}/%{zen_app_name}
%global brandingdir     browser/branding/release
%global download_ver

# Fedora rustc gives more than one valid target triple.
# `x86_64-oe-linux-gnu` and `x86_64-unknown-linux-gnu` both agree with
# `x86_64-pc-linux-gnu` and so the mozilla build system just stops.
# Just Fedora Things:tm:
%global rust_triple     %{_arch}-unknown-linux-gnu

# no debug
%global debug_package   %{nil}

# no lto flags
%global _lto_cflags     %{nil}

# The package notes section breaks the linker steps of the browser.
%undefine _package_note_flags
%global _package_note_status 0

# Do not accidentally provide private libs!!!!!!
%global __provides_exclude_from ^%{zendir}
%global __requires_exclude ^(%%(find %{buildroot}%{zendir} -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))

# Zen Browser uses clang and lld, in the same way as upstream does.
%global toolchain clang

Name:           zen-browser
Version:        1.21.16
Release:        1%{?dist}
Summary:        Calm and private web browser that is built on Firefox

License:        MPL-2.0
URL:            https://zen-browser.app

Source0:        %{giturl}/releases/download/%{download_ver}/zen.source.tar.zst
Source1:        zen.sh.in
Source2:        %{appid}.desktop
Source3:        zen-browser-default-prefs.js
Source4:        distribution.ini
Source5:        policies.json
Source6:        %{appid}.metainfo.xml

ExclusiveArch:  x86_64 aarch64

BuildRequires:  anda-srpm-macros
BuildRequires:  terra-appstream-helper
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# Toolchain
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
BuildRequires:  autoconf213

# System libraries
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

Packager:       Riley Loo <dev@zackerthescar.com>

%description
Welcome to a calmer internet.

%prep

%autosetup -c -n %{name}-%{version}

%build
export MOZBUILD_STATE_PATH="%{rpmbuilddir}/mozbuild"
export MOZ_NOSPAM=1
export MOZILLA_OFFICIAL=1
export MOZ_APP_BASENAME=Zen
export MOZ_BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH:-$(date +%%s)}" +%%Y%%m%%d%%H%%M%%S)

# The build system of Mozilla does not accept some of the default flags of
# the distribution. Note: %%gsub is not usable here, because a Lua pattern
# gives a special sense to "-", which each of these flags contains.
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

# Add branding
ac_add_options --with-branding=%{brandingdir}
ac_add_options --with-app-name=%{zen_app_name}
ac_add_options --with-app-basename=Zen
ac_add_options --with-distribution-id=app.zen-browser
ac_add_options --enable-update-channel=release
ac_add_options --with-l10n-base="\$topsrcdir/browser/locales"

# Release build
ac_add_options --enable-release
ac_add_options --enable-optimize
ac_add_options --enable-hardening
ac_add_options --disable-debug
ac_add_options --disable-debug-symbols
ac_add_options --disable-debug-js-modules
ac_add_options --disable-tests
ac_add_options --disable-rust-tests
ac_add_options --disable-geckodriver
ac_add_options --enable-rust-simd
ac_add_options --enable-wasm-simd
ac_add_options --enable-jxl

# Disable the crash reporter, since we're distributing binaries ourselves.
ac_add_options --disable-updater
ac_add_options --disable-crashreporter
ac_add_options --disable-bootstrap

# Disable telemetry.
# Note: MOZ_DATA_REPORTING, MOZ_SERVICES_HEALTHREPORT and MOZ_NORMANDY stay
# on. browser/moz.configure sets these three with imply_option, therefore a
# mozconfig cannot remove them. Zen Browser stops the reports with the
# preferences instead.
ac_add_options MOZ_TELEMETRY_REPORTING=

# Extensions. Zen Browser permits extensions that have no signature.
ac_add_options --with-unsigned-addon-scopes=app,system
ac_add_options --allow-addon-sideload
export MOZ_REQUIRE_SIGNING=

# System libraries
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

# Audio and video
ac_add_options --enable-alsa
ac_add_options --enable-pulseaudio
ac_add_options --enable-necko-wifi

# Fedora has no complete WASI sysroot, therefore the sandboxed libraries
# must stay off.
ac_add_options --without-wasm-sandboxed-libraries
ac_add_options --without-sysroot

# Linker and strip
ac_add_options --enable-linker=lld
ac_add_options --disable-elf-hack
ac_add_options --enable-strip
ac_add_options --enable-install-strip

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
ac_add_options --with-libclang-path=$(llvm-config --libdir)
EOF

echo 'ac_add_options --enable-lto=cross,thin' >> .mozconfig

%ifarch x86_64
echo 'ac_add_options --enable-eme=widevine' >> .mozconfig
%endif

# Give every compiler process 4 GB of memory. The macro reduces the number of
# parallel jobs if the memory is not sufficient.
%constrain_build -m 4096
echo "mk_add_options MOZ_MAKE_FLAGS=\"-j%{_smp_build_ncpus}\"" >> .mozconfig

./mach build

%install
DESTDIR=%{buildroot} ./mach install

# Strip internal updater - Terra manages updates.
%{__rm} -f %{buildroot}%{zendir}/updater \
           %{buildroot}%{zendir}/updater.ini \
           %{buildroot}%{zendir}/update-settings.ini

# Start script. mach installs a symbolic link with the name of the
# application. This package replaces it with the start script.
%{__rm} -f %{buildroot}%{_bindir}/%{zen_app_name}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__sed} -e 's,__PREFIX__,%{_prefix},g' \
         -e 's,__APP_DIR__,%{zen_app_name},g' \
         -e 's,__APP_FILE__,%{zen_app_name},g' \
         -e 's,__APP_NAME__,%{zen_app_name},g' \
         %{S:1} > %{buildroot}%{_bindir}/%{name}
%{__chmod} 755 %{buildroot}%{_bindir}/%{name}
%{__ln_s} -f %{name} %{buildroot}%{_bindir}/%{zen_app_name}

# Desktop entry
%desktop_file_install %{S:2}

# Icons
for size in 16 22 24 32 48 64 128 256; do
    %{__install} -Dpm644 %{brandingdir}/default${size}.png \
        %{buildroot}%{_hicolordir}/${size}x${size}/apps/%{appid}.png
done

# Distribution preferences
%{__install} -Dpm644 %{S:3} \
    %{buildroot}%{zendir}/browser/defaults/preferences/vendor.js
%{__install} -Dpm644 %{S:4} %{buildroot}%{zendir}/distribution/distribution.ini
%{__install} -Dpm644 %{S:5} %{buildroot}%{zendir}/distribution/policies.json

# Use the dictionaries of the system.
%{__rm} -rf %{buildroot}%{zendir}/dictionaries
%{__ln_s} -f %{_datadir}/hunspell %{buildroot}%{zendir}/dictionaries

%terra_appstream -o %{S:6}

%check
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%license LICENSE
%doc README.md
%{zendir}/
%{_bindir}/%{name}
%{_bindir}/%{zen_app_name}
%{_appsdir}/%{appid}.desktop
%{_hicolordir}/*/apps/%{appid}.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Thu Sep 7 2026 Riley Loo <dev@zackerthescar.com> - 1.21.16b-1
- Initial package
