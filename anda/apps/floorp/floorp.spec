%global giturl          https://github.com/Floorp-Projects/Floorp
%global runtime_repo    https://github.com/Floorp-Projects/Floorp-Runtime
%global runtime_commit  1553b7b550dfe555684628d175e0c1701a785d0b
%global appid           one.ablaze.floorp
%global floorp_app_name floorp
%global floorpdir        %{_libdir}/%{floorp_app_name}
%global brandingdir     browser/branding/floorp-official

%ifarch x86_64
%global moz_target      x86_64-pc-linux-gnu
%global rust_triple     x86_64-unknown-linux-gnu
%elifarch aarch64
%global moz_target      aarch64-unknown-linux-gnu
%global rust_triple     aarch64-unknown-linux-gnu
%endif

%global debug_package   %{nil}
%global _lto_cflags     %{nil}

# Package the browser without advertising bundled private libraries.
%global __provides_exclude_from ^%{floorpdir}
%global __requires_exclude ^(%%(find %{buildroot}%{floorpdir} -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))

%global toolchain clang

Name:           floorp
Version:        12.19.0
Release:        1%{?dist}
Summary:        Privacy-focused web browser based on Firefox

License:        MPL-2.0
URL:            https://floorp.app/

# The commit is pinned by floorp-runtime.lock.json in the matching Floorp tag.
Source0:        %{runtime_repo}/archive/%{runtime_commit}.tar.gz
Source1:        floorp.sh.in
Source2:        %{appid}.desktop
Source3:        floorp-default-prefs.js
Source4:        policies.json
Source5:        %{appid}.metainfo.xml
Source6:        %{giturl}/archive/refs/tags/v%{version}.tar.gz
Patch0:         %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/LocalizationCpp.patch
Patch1:         %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/artifacts.py.patch
Patch2:         %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/bootstrap.py.patch
Patch3:         %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/brandingFileIcon.patch
Patch4:         %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/browser-installer-windows-nsis-shared.nsh.patch
Patch5:         %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/common.nsh.patch
Patch6:         %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/commonupdatedir.cpp.patch
Patch7:         %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/config-external-nspr-pr-moz.build.patch
Patch8:         %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/localizeFfiLib.patch
Patch9:         %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/moz.build.patch
Patch10:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/moz.configure.patch
Patch11:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/nsIUpdateService.idl.patch
Patch12:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/nxXREDirProvider.cpp.patch
Patch13:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/pgo-test-helper-install.patch
Patch14:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/python-mozbuild-mozbuild-repackaging-desktop_file.py.patch
Patch15:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/removed-files.in.patch
Patch16:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/toolkit-crashreporter-google-breakpad-.gitignore.patch
Patch17:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/toolkit-modules-UpdateUtils.sys.mjs.patch
Patch18:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/toolkit-moz.configure.patch
Patch19:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/toolkit-mozapps-update-UpdateService.sys.mjs.patch
Patch20:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/toolkit-mozapps-update-nsIUpdateService.idl.patch
# Refresh upstream's whitespace-stale hunk against the pinned runtime.
Patch21:        toolkit-mozapps-update-tests-data-sharedUpdateXML.js.patch
Patch22:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/toolkit-mozapps-update-tests-unit_aus_update-updateManagerXML.js.patch
Patch23:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/toolkit-tests-gtest-TestXREAppDir.cpp.patch
Patch24:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/toolkit-xre-nsAppRunner.cpp.patch
Patch25:        %{runtime_repo}/raw/%{runtime_commit}/.github/patches/upstream/tools-signing-macos-mach_commands.py.patch

ExclusiveArch:  x86_64 aarch64

BuildRequires:  anda-srpm-macros
BuildRequires:  terra-appstream-helper
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib


# Mozilla/Floorp build toolchain
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  mold
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
BuildRequires:  deno
BuildRequires:  zip
BuildRequires:  unzip
BuildRequires:  autoconf213
BuildRequires:  xorg-x11-server-Xvfb

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

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Floorp is a privacy-focused web browser based on Firefox, with additional
customization and productivity features.

%prep
%autosetup -n Floorp-Runtime-%{runtime_commit} -p1

%{__tar} -xf %{S:6}
mv Floorp-%{version} noraneko
python3 -c 'import json; lock = json.load(open("noraneko/floorp-runtime.lock.json")); assert lock["source"]["commit"] == "%{runtime_commit}", "Floorp runtime lock does not match Source0"'

for patch_file in noraneko/.github/patches/floorp-runtime/common/*.patch; do
    case "$patch_file" in
        */macos-*) continue ;;
    esac
    patch -p1 < "$patch_file"
done

# Restore Gecko's protection, which the runtime's branding patch disables.
%{__sed} -i 's/imply_option("MOZ_BLOCK_PROFILE_DOWNGRADE", False)/imply_option("MOZ_BLOCK_PROFILE_DOWNGRADE", True)/' browser/moz.configure
grep -Fq 'imply_option("MOZ_BLOCK_PROFILE_DOWNGRADE", True)' browser/moz.configure

printf '\nDIRS += ["noraneko"]\n' >> moz.build

%build
export MOZBUILD_STATE_PATH="%{rpmbuilddir}/mozbuild"
export MOZ_NOSPAM=1
export MOZILLA_OFFICIAL=1
export MOZ_APP_BASENAME=Floorp
export MOZ_BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH:-$(date +%%s)}" +%%Y%%m%%d%%H%%M%%S)

# Firefox's build system rejects some distribution hardening flags
moz_filter_flags() {
    %{__sed} -e 's/-Wall//' \
             -e 's/-fexceptions//' \
             -e 's/-Werror=format-security//' \
             -e 's/-fcf-protection//' \
             -e 's/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2/'
}
MOZ_CFLAGS=$(echo "%{build_cflags} -fuse-ld=mold" | moz_filter_flags)
MOZ_CXXFLAGS=$(echo "%{build_cxxflags} -fuse-ld=mold" | moz_filter_flags)

# Floorp branding
cp -r .github/assets/branding/* browser/branding/
cat > .mozconfig <<EOF
ac_add_options --enable-application=browser
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-artifact-build-output

ac_add_options --target=%{moz_target}
ac_add_options --prefix="%{_prefix}"
ac_add_options --libdir="%{_libdir}"

ac_add_options --with-app-name=%{floorp_app_name}
ac_add_options --with-app-basename=Floorp
ac_add_options --with-branding=%{brandingdir}
ac_add_options --with-distribution-id=one.ablaze.floorp
ac_add_options --enable-update-channel=release
ac_add_options --enable-chrome-format=flat
ac_add_options --with-version-file-path=noraneko/static/gecko/config/autogenerated

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
ac_add_options --enable-jxl

# The package manager owns updates and crash reporting.
ac_add_options --disable-updater
ac_add_options --disable-crashreporter
ac_add_options MOZ_TELEMETRY_REPORTING=

# Use distribution system libraries where supported.
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
ac_add_options --with-wasm-sandboxed-libraries=graphite,ogg,hunspell,expat,woff2,soundtouch
ac_add_options --without-sysroot

# Fedora's native toolchain does not include a complete WASI C/C++ sysroot.
ac_add_options --enable-bootstrap=clang,sysroot-wasm32-wasi
export WASM_CC="$MOZBUILD_STATE_PATH/clang/bin/clang"
export WASM_CXX="$MOZBUILD_STATE_PATH/clang/bin/clang++"


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

%ifarch x86_64
echo 'ac_add_options --enable-eme=widevine' >> .mozconfig
%endif

%constrain_build -m 4096
echo "mk_add_options MOZ_MAKE_FLAGS=\"-j%{_smp_build_ncpus}\"" >> .mozconfig

(
    cd noraneko
    deno install --frozen --allow-scripts
    deno task feles-build misc writeVersion
    mkdir -p static/gecko/config/autogenerated
    printf '%%s@%%s\n' "$(cat static/gecko/config/version.txt)" "$(cat ../browser/config/version.txt)" > static/gecko/config/autogenerated/version.txt
    printf '%%s@%%s\n' "$(cat static/gecko/config/version_display.txt)" "$(cat ../browser/config/version_display.txt)" > static/gecko/config/autogenerated/version_display.txt
    NODE_ENV=production deno task feles-build build --phase before-mach
)

# Allow PyO3 to attempt its stable ABI on Python 3.15.
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 xvfb-run -a -s "-screen 0 1024x768x24" ./mach configure
xvfb-run -a -s "-screen 0 1024x768x24" ./mach build

%install
DESTDIR=%{buildroot} ./mach install

# Inject into installed, dereferenced files so mach cannot overwrite the changes.
(
    cd noraneko
    deno run --allow-read --allow-write tools/scripts/xhtml.ts %{buildroot}%{floorpdir}
    for patch_file in tools/patches/*.patch; do
        case "$patch_file" in
            *.windows.patch|*.darwin.patch) continue ;;
        esac
        if ! patch -d %{buildroot}%{floorpdir} -p1 -R --dry-run --batch < "$patch_file"; then
            patch -d %{buildroot}%{floorpdir} -p1 --forward --batch < "$patch_file"
        fi
    done
    bash static/gecko/pref/override.sh %{buildroot}%{floorpdir}/browser/defaults/preferences/firefox.js
    %{__install} -pm644 _dist/buildid2 %{buildroot}%{floorpdir}/browser/buildid2
)
# patch creates backup files when hunks apply with offsets.
find %{buildroot}%{floorpdir} -name '*.orig' -delete

# The package manager controls browser updates.
%{__rm} -f %{buildroot}%{floorpdir}/updater \
           %{buildroot}%{floorpdir}/updater.ini \
           %{buildroot}%{floorpdir}/update-settings.ini

# Replace mach's launcher symlink with the distribution launcher.
%{__rm} -f %{buildroot}%{_bindir}/%{floorp_app_name}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__sed} -e 's,__PREFIX__,%{_prefix},g' \
         -e 's,__APP_DIR__,%{floorp_app_name},g' \
         -e 's,__APP_FILE__,%{floorp_app_name},g' \
         -e 's,__APP_NAME__,%{floorp_app_name},g' \
         %{S:1} > %{buildroot}%{_bindir}/%{name}
%{__chmod} 755 %{buildroot}%{_bindir}/%{name}

%desktop_file_install %{S:2}

# Install Floorp icons shipped with the official branding.
for size in 16 22 24 32 48 64 128 256; do
    %{__install} -Dpm644 %{brandingdir}/default${size}.png \
        %{buildroot}%{_hicolordir}/${size}x${size}/apps/%{appid}.png
done

%{__install} -Dpm644 %{S:3} \
    %{buildroot}%{floorpdir}/browser/defaults/preferences/vendor.js
%{__install} -Dpm644 %{S:4} %{buildroot}%{floorpdir}/distribution/policies.json

%terra_appstream -o %{S:5}

%check
grep -Fq 'chrome://noraneko-startup/content/chrome_root.js' %{buildroot}%{floorpdir}/browser/chrome/browser/content/browser/browser.xhtml
test -s %{buildroot}%{floorpdir}/browser/buildid2
grep -q '^#define MOZ_BLOCK_PROFILE_DOWNGRADE 1$' obj-artifact-build-output/mozilla-config.h
for library in GRAPHITE OGG HUNSPELL EXPAT WOFF2 SOUNDTOUCH; do
    grep -q "^#define MOZ_WASM_SANDBOXING_${library} 1$" obj-artifact-build-output/mozilla-config.h
done
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%files
%license LICENSE noraneko/LICENSE
%doc README.md MOZ_README.md SECURITY.md CODE_OF_CONDUCT.md docs/*
%{floorpdir}/
%{_bindir}/%{name}
%{_appsdir}/%{appid}.desktop
%{_hicolordir}/*/apps/%{appid}.png
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Thu Oct 1 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
