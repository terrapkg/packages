%global lw_release      1
%global lw_app_name     librewolf
%global lwdir           %{_libdir}/%{lw_app_name}
%global brandingdir     browser/branding/librewolf
%global appid           librewolf
%global name_pretty     LibreWolf
%global appstream_component desktop-application

%global rust_triple     %{_arch}-unknown-linux-gnu

%global debug_package   %{nil}
%global _lto_cflags     %{nil}
%undefine _package_note_flags
%global _package_note_status 0

%global __provides_exclude_from ^%{lwdir}
%global __requires_exclude ^(%%(find %{buildroot}%{lwdir} -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))

%global toolchain clang

Name:           librewolf
Version:        160.0.1
Release:        1%{?dist}
Summary:        Custom version of Firefox focused on privacy, security and freedom

License:        MPL-2.0
URL:            https://librewolf.net

Source0:        https://librewolf.dev/api/packages/librewolf/generic/librewolf-source/%{version}-%{lw_release}/librewolf-%{version}-%{lw_release}.source.tar.gz
Source1:        librewolf.sh.in
Source2:        librewolf.desktop
Source3:        librewolf-default-prefs.js
Source4:        distribution.ini
Source5:        librewolf.metainfo.xml

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
BuildRequires:  libstdc++-static

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

Recommends:     (ffmpeg-free or ffmpeg)
Recommends:     libva
Recommends:     libnotify
Recommends:     xdg-desktop-portal
Recommends:     speech-dispatcher
Suggests:       hunspell

Provides:       webclient

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
LibreWolf is a custom version of Firefox, focused on privacy, security and
freedom. It removes telemetry, ships uBlock Origin, and uses hardened defaults.

%prep
%autosetup -n librewolf-%{version}-%{lw_release}

%build
export MOZBUILD_STATE_PATH="%{_builddir}/mozbuild"
export MOZ_NOSPAM=1
export MOZ_BUILD_DATE=$(date -u +%%Y%%m%%d%%H%%M%%S)

moz_filter_flags() {
    %{__sed} -e 's/-Wall//' \
             -e 's/-fexceptions//' \
             -e 's/-Werror=format-security//' \
             -e 's/-fcf-protection//' \
             -e 's/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2/'
}
export CC="%{__cc}"
export CXX="%{__cxx}"
export AR="llvm-ar"
export NM="llvm-nm"
export RANLIB="llvm-ranlib"
export CFLAGS=$(echo "%{build_cflags}" | moz_filter_flags)
export CXXFLAGS=$(echo "%{build_cxxflags}" | moz_filter_flags)
export LDFLAGS="%{build_ldflags}"

cat >> mozconfig <<EOF
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/objdir

ac_add_options --host=%{rust_triple}
ac_add_options --target=%{rust_triple}
ac_add_options --prefix="%{_prefix}"
ac_add_options --libdir="%{_libdir}"

ac_add_options --disable-debug-symbols
ac_add_options --disable-debug-js-modules
ac_add_options --disable-rust-tests
ac_add_options --disable-geckodriver
ac_add_options --disable-bootstrap
ac_add_options --enable-jxl

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
EOF

%constrain_build -m 4096
echo "mk_add_options MOZ_MAKE_FLAGS=\"-j%{_smp_build_ncpus}\"" >> mozconfig

./mach build

%install
DESTDIR=%{buildroot} ./mach install

test -f %{buildroot}%{lwdir}/librewolf.cfg
test -f %{buildroot}%{lwdir}/distribution/policies.json
%{__install} -Dpm644 lw/local-settings.js %{buildroot}%{lwdir}/defaults/pref/local-settings.js

%{__rm} -f %{buildroot}%{lwdir}/updater \
           %{buildroot}%{lwdir}/updater.ini \
           %{buildroot}%{lwdir}/update-settings.ini

%{__rm} -f %{buildroot}%{_bindir}/%{lw_app_name}
%{__sed} -e 's,__PREFIX__,%{_prefix},g' \
         -e 's,__LIBDIR__,%{_libdir},g' \
         -e 's,__APP_DIR__,%{lw_app_name},g' \
         -e 's,__APP_FILE__,%{lw_app_name},g' \
         -e 's,__APP_NAME__,%{lw_app_name},g' \
         %{S:1} | %{__install} -Dm755 /dev/stdin %{buildroot}%{_bindir}/%{lw_app_name}

%desktop_file_install %{S:2}

for size in 16 22 24 32 48 64 128 256; do
    %{__install} -Dpm644 %{brandingdir}/default${size}.png \
        %{buildroot}%{_hicolordir}/${size}x${size}/apps/%{appid}.png
done

%{__install} -Dpm644 %{S:3} %{buildroot}%{lwdir}/browser/defaults/preferences/vendor.js
%{__install} -Dpm644 %{S:4} %{buildroot}%{lwdir}/distribution/distribution.ini

%{__rm} -rf %{buildroot}%{lwdir}/dictionaries
%{__ln_s} -f %{_datadir}/hunspell %{buildroot}%{lwdir}/dictionaries

%terra_appstream -o %{S:5}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%license LICENSE
%doc README.md
%{lwdir}/
%{_bindir}/%{lw_app_name}
%{_appsdir}/%{appid}.desktop
%{_hicolordir}/*/apps/%{appid}.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sun Nov 22 2026 Cypress Reed <cypress@fyralabs.com> - 160.0.1-1
- Initial package
