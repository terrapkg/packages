# ? https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=zen-browser
# ? https://github.com/zen-browser/desktop/blob/dev/.github/workflows/linux-release-build.yml

%global ver 1.0.2-b.5
%global ff_l10n_commit 78f030ac17c17fdbf66b212ec7b11b3c7291a7da
%global ff_ver 133.0.3
%global langs (zh-CN zh-TW ja)

Name:           zen-browser
Version:        %(echo %ver | sed 's/-/./g')
Release:        1%?dist
Summary:        Experience tranquillity while browsing the web without people tracking you
License:        MPL-2.0
URL:            https://zen-browser.app
%dnl Source0:        https://github.com/zen-browser/desktop/archive/refs/tags/%ver.tar.gz
Source1:        https://github.com/mozilla-l10n/firefox-l10n/archive/%ff_l10n_commit.tar.gz
Source2:        https://archive.mozilla.org/pub/firefox/releases/%ff_ver/source/firefox-%ff_ver.source.tar.xz
Patch1:         0001-fix-desktop.zen.patch
Patch2:         0002-download-lang-packs-withou-git-clone.zen.patch
Patch3:         0003-do-not-disable-system-extensions.zen.patch
Patch4:         0004-assume-fedora.zen.patch
Patch5:         0005-pip3.zen.patch
Patch6:         0006-no-dnf-yum.zen.patch
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  git anda-srpm-macros vips-devel nodejs-npm nodejs
BuildRequires:  ncurses-devel ncurses
BuildRequires:  rsync cbindgen clang-devel clang diffutils imake mold llvm llvm-devel nasm
BuildRequires:  wasi-libc-devel yasm
BuildRequires:  xorg-x11-server-Xvfb dbus-daemon
BuildRequires:  findutils libxml2 m4 make perl perl-FindBin
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(nspr)

%description
%summary.

%{lua:
  function mysplit(inputstr, sep)
    if sep == nil then
      sep = "%s"
    end
    local t = {}
    for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
      table.insert(t, str)
    end
    return t
  end

  local slangs = rpm.expand("%langs")
  local langs = mysplit(slangs:sub(2, (#slangs)-1), " ")
  for k, lang in pairs(langs) do
    print("%package langpack-" .. lang .. "\n")
    print("Summary: Language pack for Zen Browser ("..lang..")\n")
    print(rpm.expand("Requires: zen-browser = %version-%release\n"))
    print(rpm.expand("Supplements: langpacks-"..lang:gsub("-", "_").." = %version-%release\n\n"))
    print("BuildArch: noarch\n")
    print("%description langpack-"..lang.."\n")
    print("Language pack for Zen Browser ("..lang..")\n\n")
    print("%files langpack-"..lang.."\n")
    print("/usr/lib/zen/browser/extensions/langpack-"..lang.."@firefox.mozilla.org.xpi\n")
  end
}

%prep
%git_clone https://github.com/zen-browser/desktop %ver
git config user.name "Raboneko"
git config user.email "raboneko@fyralabs.com"
git config --add safe.directory $(pwd)/..
export MOZBUILD_STATE_PATH=$(pwd)/.mozbuild
# I don't know why but it seems like we need to use this
# or else it would use another python version
export PYENV_ROOT="$(pwd)/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PYENV_VERSION=3.11
curl https://pyenv.run | bash
pyenv install $PYENV_VERSION
eval "$(pyenv init -)"
tar xf %{S:1}
rm -rf l10n/firefox-l10n
mv firefox-l10n-%ff_l10n_commit firefox-l10n
mv firefox-l10n l10n/
%autopatch -p1 -M3
# use the --enable-jack option to keep in sync with the official repository of Firefox
sed -i 's/--enable-pulseaudio/--enable-jack/g' configs/linux/mozconfig

# prepare deps
yes | npx pnpm config set store-dir $(pwd)/pnpm-store
npx pnpm i --frozen-lockfile

npx pnpm surfer ci --brand beta --display-version %ver
install -Dvm644 %SOURCE2 -t ./.surfer/engine
npx pnpm surfer download
npx pnpm surfer import

# bootstrap
%patch 5
cd engine
%patch 4 -p1
%patch 6 -p1
export SURFER_PLATFORM="linux"
git commit -a -m "tmp"

python3.11 -m ensurepip
python3.11 ./mach --no-interactive bootstrap --application-choice browser
cd ..

%build
export PATH="$PATH:$(pwd)/bin/"
export SURFER_PLATFORM="linux"
export MOZBUILD_STATE_PATH=$(pwd)/.mozbuild
cat > mozconfig <<END
# # sccache
# mk_add_options 'export RUSTC_WRAPPER=sccache'
# mk_add_options 'export CCACHE_CPP2=yes'
# ac_add_options --with-ccache=sccache

# ac_add_options --enable-application=browser
# Incompatible with surfer, disable this configuration
mk_add_options MOZ_OBJDIR/%_builddir/desktop/obj

ac_add_options --prefix=%_prefix
# ac_add_options --enable-release
# ac_add_options --enable-hardening
# ac_add_options --enable-optimize
# ac_add_options --enable-rust-simd
ac_add_options --enable-linker=mold
# ac_add_options --disable-install-strip
# ac_add_options --disable-elf-hack
# It seems to be overwritten by surfer internal mozconfg, let's keep it for now
ac_add_options --disable-bootstrap
ac_add_options --with-wasi-sysroot=/usr/share/wasi-sysroot

# Branding
# ac_add_options --enable-official-branding
# ac_add_options --enable-update-channel=release
# ac_add_options --with-distribution-id=org.archlinux
# ac_add_options --with-unsigned-addon-scopes=app,system
ac_add_options --allow-addon-sideload
# export MOZILLA_OFFICIAL=1
export MOZ_APP_REMOTINGNAME=%name

# System libraries
ac_add_options --with-system-nspr
ac_add_options --with-system-nss

# Features
# ac_add_options --enable-alsa
# ac_add_options --enable-jack
# ac_add_options --enable-crashreporter
ac_add_options --disable-updater
# ac_add_options --disable-tests
END

export MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=pip
export MOZBUILD_STATE_PATH="$(pwd)/mozbuild"
MOZ_BUILD_DATE="$(date -u${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH} +%%Y%%m%%d%%H%%M%%S)"
export MOZ_BUILD_DATE
# export MOZ_BUILD_PRIORITY=normal
export MOZ_NOSPAM=1
# malloc_usable_size is used in various parts of the codebase
CFLAGS="${CFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
CXXFLAGS="${CXXFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"

# Breaks compilation since https://bugzilla.mozilla.org/show_bug.cgi?id=1896066
CFLAGS="${CFLAGS/-fexceptions/}"
CXXFLAGS="${CXXFLAGS/-fexceptions/}"

# LTO needs more open files
ulimit -n 4096

export PYENV_ROOT="$(pwd)/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PYENV_VERSION=3.11
eval "$(pyenv init -)"
export SURFER_COMPAT="$CARCH"
export SURFER_PLATFORM=linux
export ZEN_RELEASE=1

npx pnpm surfer bootstrap

dbus-run-session \
  xvfb-run -s "-screen 0 1920x1080x24 -nolisten local" \
  npx pnpm surfer build #--skip-patch-check

echo %ff_ver > engine/browser/config/version.txt
_languages=%langs
for _lang in "${_languages[@]}"; do
  python3.11 engine/mach build "merge-$_lang"
  python3.11 engine/mach build "langpack-$_lang"
done

%install
DESTDIR=%buildroot engine/mach install
ln -srvf %buildroot/usr/lib/zen %buildroot/usr/lib/zen-bin
ln -srvf %buildroot/usr/lib/zen %buildroot%_bindir/zen
install -Dvm644 AppDir/distribution/*.json -t %buildroot/usr/lib/zen/distribution

export _vendorjs=%buildroot/usr/lib/zen/browser/defaults/preferences/vendor.js
install -Dvm644 /dev/stdin "$_vendorjs" <<END
// Use LANG environment variable to choose locale
pref("intl.locale.requested", "");

// Use system-provided dictionaries
pref("spellchecker.dictionary_path", "/usr/share/hunspell");

// Enable extensions in the application directory
pref("extensions.autoDisableScopes", 11);

// TODO: Enable GNOME Shell search provider
// pref("browser.gnome-search-provider.enabled", true);
END

export _distini=%buildroot/usr/lib/zen/distribution/distribution.ini
install -Dvm644 /dev/stdin "$_distini" <<END
[Global]
id=terra
version=1.0
about=Zen Browser (Terra)

[Preferences]
app.distributor=terra
app.distributor.channel=zen-browser
END

for i in 16 32 48 64 128; do
install -d %buildroot%_iconsdir/hicolor/${i}x${i}/apps
ln -srvf \
  "%buildroot/usr/lib/zen/browser/chrome/icons/default/default${i}.png" \
  "%buildroot%_iconsdir/hicolor/${i}x${i}/apps/zen-browser.png"
done
install -Dm0644 docs/assets/zen-black.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -Dvm644 docs/assets/zen-black.svg %buildroot%_iconsdir/hicolor/symbolic/apps/%name-symbolic.svg

install -Dvm644 AppDir/*.desktop %buildroot%_datadir/applications/%name.desktop

_languages=%langs
for _lang in "${_languages[@]}"; do
  install -Dvm644 obj/dist/linux-*/xpi/zen-%ff_ver.$_lang.langpack.xpi \
    "%buildroot/usr/lib/zen/browser/extensions/langpack-%_lang@firefox.mozilla.org.xpi"
done
