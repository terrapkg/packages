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

%if 0%{?fedora} >= 44
%global with_wasi_sdk 1
%else
%global with_wasi_sdk 0
%endif

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
%if %{with_wasi_sdk}
Source7:        https://src.fedoraproject.org/rpms/firefox/raw/rawhide/f/wasi.patch.template
Source8:        https://src.fedoraproject.org/repo/pkgs/rpms/firefox/wasi-sdk-30.tar.gz/sha512/c08b2ddb5d5cf5b48c5baba80c65c485a3049b473d2f2dd2babb402243a7709633c695dfee5f9cbba52fa25ad832f02f3b73d9ba1141c4d44dc30db70292a04d/wasi-sdk-30.tar.gz
Source9:        https://src.fedoraproject.org/repo/pkgs/rpms/firefox/wasm-component-ld-vendor.tar.xz/sha512/356dc09502052198e99745199b8e10d803da9492ce34e41c6ae02cb8674fcc640cd5eafe68a03e4e61c984f7f6c7c8e5cdc3551251556fb3ae4631a340358fc0/wasm-component-ld-vendor.tar.xz
Source10:       https://src.fedoraproject.org/repo/pkgs/rpms/firefox/wasm-tools-vendor.tar.xz/sha512/502be0020d1828b75128e6127eb7bd77835ccebe4e5c179abc38d881bb1d1f8e15d2284796cd83574536c7c919a3e820e0952d323e8a3977e94bdef89cd8266a/wasm-tools-vendor.tar.xz
%endif
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
%if %{with_wasi_sdk}
Patch26:        https://src.fedoraproject.org/rpms/firefox/raw/rawhide/f/build-wasm32-wasip1.patch
%endif

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
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  perl-interpreter
BuildRequires:  python3-devel
BuildRequires:  python3.11-devel
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

%if %{with_wasi_sdk}
%{__tar} -xf %{S:8}
%{__sed} "s|LIBCLANG_RT_PLACEHOLDER|$(pwd)/wasi-sdk-30/build/sysroot/install/wasi-resource-dir/lib/wasm32-unknown-wasip1/libclang_rt.builtins.a|" %{S:7} > wasi.patch
patch -p1 < wasi.patch
%endif
%{__sed} -i -e 's|#!/usr/bin/env python3|#!/usr/bin/env python3.11|' mach

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
ac_add_options --disable-bootstrap
%if %{with_wasi_sdk}
ac_add_options --with-wasm-sandboxed-libraries=graphite,ogg,hunspell,expat,woff2,soundtouch
ac_add_options --with-wasi-sysroot="$(pwd)/wasi-sdk-30/build/sysroot/install/share/wasi-sysroot"
export WASM_CC="%{__cc}"
export WASM_CXX="%{__cxx}"
%else
ac_add_options --without-wasm-sandboxed-libraries
ac_add_options --without-sysroot
%endif


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

%if %{with_wasi_sdk}
pushd wasi-sdk-30
mkdir -p my_rust_vendor_wasm_tools
cd my_rust_vendor_wasm_tools
tar xf %{S:10}
mkdir -p .cargo
cat > .cargo/config <<EOL
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "$(pwd)"
EOL
env CARGO_HOME=.cargo cargo install wasm-tools
export PATH="$(pwd)/.cargo/bin:$PATH"
cd ..

mkdir -p my_rust_vendor
cd my_rust_vendor
tar xf %{S:9}
mkdir -p .cargo
cat > .cargo/config <<EOL
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "$(pwd)"
EOL
cd ..

CARGO_HOME="$(pwd)/my_rust_vendor/.cargo" NINJA_FLAGS=-v CC=clang CXX=clang++ \
    env -u CFLAGS -u CXXFLAGS -u FFLAGS -u FCFLAGS -u RUSTFLAGS -u LDFLAGS \
    -u LT_SYS_LIBRARY_PATH cmake -G Ninja -B build/toolchain -S . \
    -DWASI_SDK_BUILD_TOOLCHAIN=ON -DCMAKE_INSTALL_PREFIX=build/install
CARGO_HOME="$(pwd)/my_rust_vendor/.cargo" NINJA_FLAGS=-v CC=clang CXX=clang++ \
    env -u CFLAGS -u CXXFLAGS -u FFLAGS -u FCFLAGS -u RUSTFLAGS -u LDFLAGS \
    -u LT_SYS_LIBRARY_PATH cmake --build build/toolchain --target install
CARGO_HOME="$(pwd)/my_rust_vendor/.cargo" NINJA_FLAGS=-v CC=clang CXX=clang++ \
    env -u CFLAGS -u CXXFLAGS -u FFLAGS -u FCFLAGS -u RUSTFLAGS -u LDFLAGS \
    -u LT_SYS_LIBRARY_PATH cmake -G Ninja -B build/sysroot -S . \
    -DCMAKE_INSTALL_PREFIX=build/install \
    -DCMAKE_TOOLCHAIN_FILE=build/install/share/cmake/wasi-sdk.cmake \
    -DCMAKE_C_COMPILER_WORKS=ON -DCMAKE_CXX_COMPILER_WORKS=ON
CARGO_HOME="$(pwd)/my_rust_vendor/.cargo" NINJA_FLAGS=-v CC=clang CXX=clang++ \
    env -u CFLAGS -u CXXFLAGS -u FFLAGS -u FCFLAGS -u RUSTFLAGS -u LDFLAGS \
    -u LT_SYS_LIBRARY_PATH cmake --build build/sysroot --target install
popd
%endif

xvfb-run -a -s "-screen 0 1024x768x24" ./mach configure
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
%if %{with_wasi_sdk}
for library in GRAPHITE OGG HUNSPELL EXPAT WOFF2 SOUNDTOUCH; do
    grep -q "^#define MOZ_WASM_SANDBOXING_${library} 1$" obj-artifact-build-output/mozilla-config.h
done
%else
for library in GRAPHITE OGG HUNSPELL EXPAT WOFF2 SOUNDTOUCH; do
    if grep -q "^#define MOZ_WASM_SANDBOXING_${library} 1$" obj-artifact-build-output/mozilla-config.h; then
        echo "Unexpected WASM sandboxing enabled for ${library}" >&2
        exit 1
    fi
done
%endif

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
