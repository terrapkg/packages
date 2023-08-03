# Compiling the preloader fails with hardening enabled
%undefine _hardened_build

#%%global _smp_mflags -j1

%global no64bit   0
%global winegecko 2.47.4
%global winemono  8.0.0
%global vkd3d     1.8
#global _default_patch_fuzz 2
%ifarch %{ix86}
%global winepedir i386-windows
%global winesodir i386-unix
%endif
%ifarch x86_64
%global winepedir x86_64-windows
%global winesodir x86_64-unix
%endif
%ifarch %{arm}
%global winepedir arm-windows
%global winesodir arm-unix
%endif
%ifarch aarch64
%global winepedir aarch64-windows
%global winesodir aarch64-unix
%global __brp_llvm_compile_lto_elf %nil
%global __brp_strip_lto %nil
%global __brp_strip_static_archive %nil
%endif

# build with wine-staging patches, see:  https://github.com/wine-staging/wine-staging
%if 0%{?fedora} || 0%{?rhel}
%global wine_staging 1
%global staging_version 8.13
%endif
# 0%%{?fedora}

# build with wine-tkg patches on top of wine-staging
%if 0%{?fedora}
%global wine_tkg 1
%global tkg_use_tag 1
# taken from  git tag or https://github.com/Frogging-Family/wine-tkg-git/tags
# or from https://github.com/Frogging-Family/wine-tkg-git/blob/master/wine-tkg-git/PKGBUILD
%global tkg_version 7.x+
%endif
# 0%%{?fedora}

# binfmt macros for RHEL
%if 0%{?rhel} == 7
%global _binfmtdir /usr/lib/binfmt.d
%global binfmt_apply() \
/usr/lib/systemd/systemd-binfmt  %{?*} >/dev/null 2>&1 || : \
%{nil}
%endif

Name:           wine
Version:        8.13
Release:        1%{?wine_tkg:.wine_tkg}%{?dist}
Summary:        A compatibility layer for windows applications (wine_tkg)

License:        LGPL-2.0+
URL:            https://www.winehq.org/

%if 0%{?wine_tkg}
%if 0%{?tkg_use_tag}
Source0:        https://github.com/Frogging-Family/wine-tkg-git/archive/refs/tags/%tkg_version.tar.gz
%endif
Source20:       https://gitlab.winehq.org/wine/wine/-/archive/wine-%version/wine-wine-%version.tar.gz
Source21:       https://gitlab.winehq.org/wine/wine-staging/-/archive/v%staging_version/wine-staging-%staging_version.tar.gz
# wine_tkg customization.cfg prepared for this version
Source22:       customization.cfg
# else regular wine source
%else
Source0:        https://dl.winehq.org/wine/source/8.x/wine-%{version}.tar.xz
Source10:       https://dl.winehq.org/wine/source/8.x/wine-%{version}.tar.xz.sign
%endif

Source1:        wine.systemd
Source2:        wine-README-Fedora
Source3:        wine-32.conf
Source4:        wine-64.conf

# desktop files
Source100:      wine-notepad.desktop
Source101:      wine-regedit.desktop
Source102:      wine-uninstaller.desktop
Source103:      wine-winecfg.desktop
Source104:      wine-winefile.desktop
Source105:      wine-winemine.desktop
Source106:      wine-winhelp.desktop
Source107:      wine-wineboot.desktop
Source108:      wine-wordpad.desktop
Source109:      wine-oleview.desktop

# AppData files
Source150:      wine.appdata.xml

# wine bugs

# desktop dir
Source200:      wine.menu
Source201:      wine.directory

# mime types
Source300:      wine-mime-msi.desktop


# smooth tahoma (#693180)
# disable embedded bitmaps
Source501:      wine-tahoma.conf
# and provide a readme
Source502:      wine-README-tahoma

# Autoconf 2.72 support - https://bugzilla.redhat.com/show_bug.cgi?id=2143724
Patch100:       wine-7.22-autoconf-2.72.patch

Patch511:       wine-cjk.patch

# upstream patches
# https://gitlab.winehq.org/wine/wine/-/commit/710eec8fac7952679e2ddb4eba54367b50c47930
Patch900:       710eec8fac7952679e2ddb4eba54367b50c47930.patch

%if !%{?no64bit}
ExclusiveArch:  %{ix86} x86_64 aarch64
%else
ExclusiveArch:  %{ix86}
%endif

BuildRequires:  bison
BuildRequires:  flex

%if 0%{?wine_tkg}
#BuildRequires:  git-core
BuildRequires:  git
BuildRequires:  vim-minimal
%endif

%ifarch  %{arm} aarch64
BuildRequires:  clang >= 5.0
BuildRequires:  lld
%else
BuildRequires:  gcc
%endif
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  alsa-lib-devel
BuildRequires:  audiofile-devel
BuildRequires:  freeglut-devel
BuildRequires:  libieee1284-devel
BuildRequires:  libgcrypt-devel
#BuildRequires:  libjpeg-devel

BuildRequires:  librsvg2
BuildRequires:  librsvg2-devel
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(libusb-1.0)
%if 0%{?fedora}
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
%endif
BuildRequires:  openldap-devel
BuildRequires:  perl-generators
BuildRequires:  unixODBC-devel
BuildRequires:  sane-backends-devel
BuildRequires:  systemd-devel
BuildRequires:  fontforge freetype-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  libpcap-devel
# modular x
BuildRequires:  libX11-devel
BuildRequires:  mesa-libGL-devel mesa-libGLU-devel mesa-libOSMesa-devel
BuildRequires:  libXxf86dga-devel libXxf86vm-devel
BuildRequires:  libXrandr-devel libXrender-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXpresent-devel
BuildRequires:  fontconfig-devel
BuildRequires:  giflib-devel
BuildRequires:  cups-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXi-devel
BuildRequires:  libXcursor-devel
BuildRequires:  dbus-devel
BuildRequires:  gnutls-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  gsm-devel
BuildRequires:  libv4l-devel
BuildRequires:  fontpackages-devel
BuildRequires:  gettext-devel
BuildRequires:  chrpath
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
%if 0%{?fedora} > 24
BuildRequires:  mpg123-devel
%endif
BuildRequires:  SDL2-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  vulkan-devel
#BuildRequires:  libFAudio-devel
BuildRequires:  libappstream-glib

# Silverlight DRM-stuff needs XATTR enabled.
%if 0%{?wine_staging}
BuildRequires:  gtk3-devel
BuildRequires:  libattr-devel
BuildRequires:  libva-devel
%endif
# 0%%{?wine_staging}

#BuildRequires:  openal-soft-devel
BuildRequires:  icoutils

%ifarch %{ix86} x86_64
BuildRequires:  mingw32-FAudio
BuildRequires:  mingw64-FAudio
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw64-lcms2
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-libpng
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw32-libxslt
BuildRequires:  mingw64-libxslt
BuildRequires:  libvkd3d-devel >= %{vkd3d}
BuildRequires:  libvkd3d-shader-devel >= %{vkd3d}
BuildRequires:  mingw32-spirv-headers
BuildRequires:  mingw32-spirv-tools
BuildRequires:  mingw64-spirv-headers
BuildRequires:  mingw64-spirv-tools
BuildRequires:  mingw32-vkd3d >= %{vkd3d}
BuildRequires:  mingw64-vkd3d >= %{vkd3d}
BuildRequires:  mingw32-vulkan-headers
BuildRequires:  mingw32-vulkan-tools
BuildRequires:  mingw64-vulkan-headers
BuildRequires:  mingw64-vulkan-tools
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
%endif

Requires:       wine-common = %{version}-%{release}
Requires:       wine-desktop = %{version}-%{release}
Requires:       wine-fonts = %{version}-%{release}

# x86-32 parts
%ifarch %{ix86} x86_64
%if 0%{?fedora} || 0%{?rhel} <= 6
Requires:       wine-core(x86-32) = %{version}-%{release}
Requires:       wine-cms(x86-32) = %{version}-%{release}
Requires:       wine-ldap(x86-32) = %{version}-%{release}
Requires:       wine-twain(x86-32) = %{version}-%{release}
Requires:       wine-pulseaudio(x86-32) = %{version}-%{release}
%if 0%{?fedora}
Requires:       wine-opencl(x86-32) = %{version}-%{release}
%endif
%if 0%{?fedora} >= 17
Requires:       mingw32-wine-gecko = %winegecko
Requires:       wine-mono = %winemono
%endif
#  wait for rhbz#968860 to require arch-specific samba-winbind-clients
Requires:       /usr/bin/ntlm_auth
Requires:       mesa-dri-drivers(x86-32)
%endif
%if 0%{?fedora} >= 33
Recommends:     wine-dxvk(x86-32)
Recommends:     dosbox-staging
%endif
Recommends:     gstreamer1-plugins-good(x86-32)
%endif

# x86-64 parts
%ifarch x86_64
Requires:       wine-core(x86-64) = %{version}-%{release}
Requires:       wine-cms(x86-64) = %{version}-%{release}
Requires:       wine-ldap(x86-64) = %{version}-%{release}
Requires:       wine-twain(x86-64) = %{version}-%{release}
Requires:       wine-pulseaudio(x86-64) = %{version}-%{release}
%if 0%{?fedora}
Requires:       wine-opencl(x86-64) = %{version}-%{release}
%endif
%if 0%{?fedora} >= 17
Requires:       mingw64-wine-gecko = %winegecko
Requires:       wine-mono = %winemono
%endif
Requires:       mesa-dri-drivers(x86-64)
%if 0%{?fedora} >= 33
Recommends:     wine-dxvk(x86-64)
Recommends:     dosbox-staging
%endif
Recommends:     gstreamer1-plugins-good(x86-64)
%endif

%description
Wine as a compatibility layer for UNIX to run Windows applications. This
package includes a program loader, which allows unmodified Windows
3.x/9x/NT binaries to run on x86 and x86_64 Unixes. Wine can use native system
.dll files if they are available.

In Fedora wine is a meta-package which will install everything needed for wine
to work smoothly. Smaller setups can be achieved by installing some of the
wine-* sub packages.

%package core
Summary:        Wine core package
Requires(postun): /sbin/ldconfig
Requires(posttrans):   %{_sbindir}/alternatives
Requires(preun):       %{_sbindir}/alternatives

# require -filesystem
Requires:       wine-filesystem = %{version}-%{release}

%ifarch %{ix86}
# CUPS support uses dlopen - rhbz#1367537
Requires:       cups-libs(x86-32)
Requires:       freetype(x86-32)
Requires:       (nss-mdns(x86-32) if nss-mdns(x86-64))
Requires:       gnutls(x86-32)
Requires:       libXcomposite(x86-32)
Requires:       libXcursor(x86-32)
Requires:       libXinerama(x86-32)
Requires:       libXpresent(x86-32)
Requires:       libXrandr(x86-32)
Requires:       libXrender(x86-32)
Requires:       libgcrypt(x86-32)
#dlopen in windowscodesc (fixes rhbz#1085075)
Requires:       libpng(x86-32)
Requires:       libpcap(x86-32)
Requires:       mesa-libOSMesa(x86-32)
Requires:       libv4l(x86-32)
Requires:       unixODBC(x86-32)
Requires:       SDL2(x86-32)
Requires:       vulkan-loader(x86-32)
%if 0%{?wine_staging}
Requires:       libva(x86-32)
%endif
Requires:  mingw32-FAudio
Requires:  mingw32-lcms2
Requires:  mingw32-libjpeg-turbo
Requires:  mingw32-libpng
Requires:  mingw32-libtiff
Requires:  mingw32-libxml2
Requires:  mingw32-libxslt
Requires:  mingw32-vkd3d >= %{vkd3d}
Requires:  mingw32-win-iconv
Requires:  mingw32-zlib
%endif

%ifarch x86_64
# CUPS support uses dlopen - rhbz#1367537
Requires:       cups-libs(x86-64)
Requires:       freetype(x86-64)
Requires:       (nss-mdns(x86-64) if nss-mdns(x86-32))
Requires:       gnutls(x86-64)
Requires:       libXcomposite(x86-64)
Requires:       libXcursor(x86-64)
Requires:       libXinerama(x86-64)
Requires:       libXpresent(x86-64)
Requires:       libXrandr(x86-64)
Requires:       libXrender(x86-64)
Requires:       libgcrypt(x86-64)
#dlopen in windowscodesc (fixes rhbz#1085075)
Requires:       libpng(x86-64)
Requires:       libpcap(x86-64)
Requires:       mesa-libOSMesa(x86-64)
Requires:       libv4l(x86-64)
Requires:       unixODBC(x86-64)
Requires:       SDL2(x86-64)
Requires:       vulkan-loader(x86-64)
%if 0%{?wine_staging}
Requires:       libva(x86-64)
%endif
Requires:  mingw64-FAudio
Requires:  mingw64-lcms2
Requires:  mingw64-libjpeg-turbo
Requires:  mingw64-libpng
Requires:  mingw64-libtiff
Requires:  mingw64-libxml2
Requires:  mingw64-libxslt
Requires:  mingw64-vkd3d >= %{vkd3d}
Requires:  mingw64-win-iconv
Requires:  mingw64-zlib
%endif

%ifarch %{arm} aarch64
# CUPS support uses dlopen - rhbz#1367537
Requires:       cups-libs
Requires:       freetype
Requires:       nss-mdns
Requires:       gnutls
Requires:       libXrender
Requires:       libXcursor
#dlopen in windowscodesc (fixes rhbz#1085075)
Requires:       libpng
Requires:       libpcap
Requires:       mesa-libOSMesa
Requires:       libv4l
Requires:       unixODBC
Requires:       SDL2
Requires:       vulkan-loader
%if 0%{?wine_staging}
Requires:       libva
%endif
%endif

Provides:       bundled(libjpeg) = 9e
Provides:       bundled(mpg123-libs) = 1.29.3

## removed as of 7.21
Obsoletes:      wine-openal < 7.21
Provides:       wine-openal = %{version}-%{release}

%description core
Wine core package includes the basic wine stuff needed by all other packages.

%package systemd
Summary:        Systemd config for the wine binfmt handler
Requires:       systemd >= 23
BuildArch:      noarch
Requires(post):  systemd
Requires(postun): systemd
Obsoletes:      wine-sysvinit < %{version}-%{release}

%description systemd
Register the wine binary handler for windows executables via systemd binfmt
handling. See man binfmt.d for further information.

%package filesystem
Summary:        Filesystem directories for wine
BuildArch:      noarch

%description filesystem
Filesystem directories and basic configuration for wine.

%package common
Summary:        Common files
Requires:       wine-core = %{version}-%{release}
BuildArch:      noarch

%description common
Common wine files and scripts.

%package desktop
Summary:        Desktop integration features for wine
Requires(post): desktop-file-utils >= 0.8
Requires(postun): desktop-file-utils >= 0.8
Requires:       wine-core = %{version}-%{release}
Requires:       wine-common = %{version}-%{release}
Requires:       wine-systemd = %{version}-%{release}
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description desktop
Desktop integration features for wine, including mime-types and a binary format
handler service.

%package fonts
Summary:       Wine font files
BuildArch:     noarch
# arial-fonts are available with wine-staging patchset, only.
%if 0%{?wine_staging}
Requires:      wine-arial-fonts = %{version}-%{release}
%else
# 0%%{?wine_staging}
Obsoletes:     wine-arial-fonts <= %{version}-%{release}
%endif
# 0%%{?wine_staging}
Requires:      wine-courier-fonts = %{version}-%{release}
Requires:      wine-fixedsys-fonts = %{version}-%{release}
Requires:      wine-small-fonts = %{version}-%{release}
Requires:      wine-system-fonts = %{version}-%{release}
Requires:      wine-marlett-fonts = %{version}-%{release}
Requires:      wine-ms-sans-serif-fonts = %{version}-%{release}
Requires:      wine-tahoma-fonts = %{version}-%{release}
# times-new-roman-fonts are available with wine_staging-patchset, only.
%if 0%{?wine_staging}
Requires:      wine-times-new-roman-fonts = %{version}-%{release}
%else
# 0%%{?wine_staging}
Obsoletes:     wine-times-new-roman-fonts <= %{version}-%{release}
Obsoletes:     wine-times-new-roman-fonts-system <= %{version}-%{release}
%endif
# 0%%{?wine_staging}
Requires:      wine-symbol-fonts = %{version}-%{release}
Requires:      wine-webdings-fonts = %{version}-%{release}
Requires:      wine-wingdings-fonts = %{version}-%{release}
# intermediate fix for #593140
Requires:      liberation-sans-fonts liberation-serif-fonts liberation-mono-fonts
Requires:      liberation-narrow-fonts

%description fonts
%{summary}

%if 0%{?wine_staging}
%package arial-fonts
Summary:       Wine Arial font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description arial-fonts
%{summary}
%endif
# 0%%{?wine_staging}

%package courier-fonts
Summary:       Wine Courier font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description courier-fonts
%{summary}

%package fixedsys-fonts
Summary:       Wine Fixedsys font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description fixedsys-fonts
%{summary}

%package small-fonts
Summary:       Wine Small font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description small-fonts
%{summary}

%package system-fonts
Summary:       Wine System font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description system-fonts
%{summary}


%package marlett-fonts
Summary:       Wine Marlett font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description marlett-fonts
%{summary}


%package ms-sans-serif-fonts
Summary:       Wine MS Sans Serif font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description ms-sans-serif-fonts
%{summary}

# rhbz#693180
# http://lists.fedoraproject.org/pipermail/devel/2012-June/168153.html
%package tahoma-fonts
Summary:       Wine Tahoma font family
BuildArch:     noarch
Requires:      wine-filesystem = %{version}-%{release}

%description tahoma-fonts
%{summary}
Please note: If you want system integration for wine tahoma fonts install the
wine-tahoma-fonts-system package.

%package tahoma-fonts-system
Summary:       Wine Tahoma font family system integration
BuildArch:     noarch
Requires:      fontpackages-filesystem
Requires:      wine-tahoma-fonts = %{version}-%{release}

%description tahoma-fonts-system
%{summary}

%if 0%{?wine_staging}
%package times-new-roman-fonts
Summary:       Wine Times New Roman font family
BuildArch:     noarch
Requires:      wine-filesystem = %{version}-%{release}

%description times-new-roman-fonts
%{summary}
Please note: If you want system integration for wine times new roman fonts install the
wine-times-new-roman-fonts-system package.

%package times-new-roman-fonts-system
Summary:       Wine Times New Roman font family system integration
BuildArch:     noarch
Requires:      fontpackages-filesystem
Requires:      wine-times-new-roman-fonts = %{version}-%{release}

%description times-new-roman-fonts-system
%{summary}
%endif

%package symbol-fonts
Summary:       Wine Symbol font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description symbol-fonts
%{summary}

%package webdings-fonts
Summary:       Wine Webdings font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description webdings-fonts
%{summary}

%package wingdings-fonts
Summary:       Wine Wingdings font family
BuildArch:     noarch
Requires:      fontpackages-filesystem

%description wingdings-fonts
%{summary}
Please note: If you want system integration for wine wingdings fonts install the
wine-wingdings-fonts-system package.

%package wingdings-fonts-system
Summary:       Wine Wingdings font family system integration
BuildArch:     noarch
Requires:      fontpackages-filesystem
Requires:      wine-wingdings-fonts = %{version}-%{release}

%description wingdings-fonts-system
%{summary}


%package ldap
Summary: LDAP support for wine
Requires: wine-core = %{version}-%{release}

%description ldap
LDAP support for wine

%package cms
Summary: Color Management for wine
Requires: wine-core = %{version}-%{release}

%description cms
Color Management for wine

%package twain
Summary: Twain support for wine
Requires: wine-core = %{version}-%{release}
%ifarch %{ix86}
Requires: sane-backends-libs(x86-32)
%endif
%ifarch x86_64
Requires: sane-backends-libs(x86-64)
%endif
%ifarch %{arm} aarch64
Requires: sane-backends-libs
%endif

%description twain
Twain support for wine

%package devel
Summary: Wine development environment
Requires: wine-core = %{version}-%{release}

%description devel
Header, include files and library definition files for developing applications
with the Wine Windows(TM) emulation libraries.

%package pulseaudio
Summary: Pulseaudio support for wine
Requires: wine-core = %{version}-%{release}
# midi output
Requires: wine-alsa%{?_isa} = %{version}-%{release}

%description pulseaudio
This package adds a pulseaudio driver for wine.

%package alsa
Summary: Alsa support for wine
Requires: wine-core = %{version}-%{release}

%description alsa
This package adds an alsa driver for wine.

#%%if 0%%{?fedora} >= 10 || 0%%{?rhel} >= 6
#%%package openal
#Summary: Openal support for wine
#Requires: wine-core = %%{version}-%%{release}

#%%description openal
#This package adds an openal driver for wine.
#%%endif

%if 0%{?fedora}
%package opencl
Summary: OpenCL support for wine
Requires: wine-core = %{version}-%{release}

%Description opencl
This package adds the opencl driver for wine.
%endif

#%%package widl
#Summary: Wine Interface Definition Language (IDL) compiler

#%%Description widl
#Wine Interface Definition Language (IDL) compiler.


%prep
# regular wine build setup
%if !%{?wine_tkg}
%setup -qn wine-%{version}
#%%patch100 -p1 -b.cross
%patch -P 100 -p1 -b.autoconf
%patch -P 511 -p1 -b.cjk

# upstream patches
%patch -P 900 -p1 -b.link_folder

%if 0%{?wine_staging}
# setup and apply wine-staging patches
gzip -dc %{SOURCE900} | tar -xf - --strip-components=1

staging/patchinstall.py DESTDIR="`pwd`" --all

# required to pick up new protocol definitions (fsync/futex)
tools/make_requests
autoreconf -vfi
%endif
# 0%%{?wine_staging}
%endif
# end regular wine build setup

# wine_tkg build setup
%if 0%{?wine_tkg}
%setup -qn wine-tkg-git-%(echo %tkg_version | sed 's@+@-@g')

# set git info for next step
git config --global user.email "patrick@laimbock.com"
git config --global user.name "Patrick Laimbock"

# prevent git errors
git config --global --add safe.directory .
git config --global --add safe.directory /builddir/build/BUILD/wine-tkg-git/wine-tkg-git/wine-git
git config --global --add safe.directory /builddir/build/BUILD/wine-tkg-git/wine-tkg-git/wine-staging-git
git config --global --add safe.directory /builddir/build/BUILD/wine-tkg-git/wine-tkg-git/src/wine-git
git config --global --add safe.directory /builddir/build/BUILD/wine-tkg-git/wine-tkg-git/src/wine-staging-git

mkdir -p wine-tkg-git/src

pushd wine-tkg-git
tar -xzf %{SOURCE20}
tar -xzf %{SOURCE21}

cd src
# in src create a worktree from the wine-git mirror
git clone ../wine-*
# git clone ../wine-staging-v@version-*
cd ..

mv customization.cfg customization.cfg.org
cp %{SOURCE22} customization.cfg
sed -i 's/@version/%version/g' customization.cfg
#mv wine-tkg-profiles/advanced-customization.cfg \
#     wine-tkg-profiles/advanced-customization.cfg.org
#touch wine-tkg-profiles/advanced-customization.cfg

# disable installing dependencies
sed -i -e's|_DEPSHELPER=1|_DEPSHELPER=0|' non-makepkg-build.sh
sed -i -e's|_fedora_6432| echo DISABLED _fedora_6432|' non-makepkg-build.sh

# prevent configure from running after prepare.sh
sed -i -e's|\./configure|echo DISABLED ./configure|g' non-makepkg-build.sh

## don't build
sed -i -e's|_build|echo DISABLED _build|' non-makepkg-build.sh

# don't install
sed -i -e's|_package_nomakepkg|echo DISABLED _package_nomakepkg|' non-makepkg-build.sh

# show the filename of the patch being applied
sed -i -e's|_patchmsg="|_patchmsg="${_patchname} - |g' wine-tkg-scripts/prepare.sh

# commit after each patch is applied so we exactly know what it's doing
sed -i -e's|nonuser_patcher|nonuser_patcher \&\& git commit -a -m"\${_patchmsg}"|g' wine-tkg-scripts/prepare.sh

# remove game-related hotfixes
rm -v wine-tkg-patches/hotfixes/GetMappedFileName/Return_nt_filename_and_resolve_DOS_drive_path.mypatch
rm -v wine-tkg-patches/hotfixes/NosTale/nostale_mouse_fix.mypatch
sed -i -e's|true|YES_I_WANT_STEAM|' wine-tkg-patches/misc/steam/steam

# run non-makepkg-build.sh which applies all patches
./non-makepkg-build.sh

popd

pushd wine-tkg-git/src/wine-wine-%version

# git commit
echo "wine-tkg: commit wine-tkg changes by prepare.sh and extra patches"
git add . && git commit -a -m "Commit wine-tkg changes by prepare.sh and extra patches"

popd

# link the wine-tkg patched src to the root dir for easier access
ln -s wine-tkg-git/src/wine-git wine-tkg-src

%endif
# 0%%{?wine_tkg}


%build
# This package uses top level ASM constructs which are incompatible with LTO.
# Top level ASMs are often used to implement symbol versioning.  gcc-10
# introduces a new mechanism for symbol versioning which works with LTO.
# Converting packages to use that mechanism instead of toplevel ASMs is
# recommended.
# Disable LTO
%define _lto_cflags %{nil}

# disable fortify as it breaks wine
# http://bugs.winehq.org/show_bug.cgi?id=24606
# http://bugs.winehq.org/show_bug.cgi?id=25073
%undefine _fortify_level
# Disable Red Hat specs for package notes (Fedora 38+) and annobin.
# MinGW GCC does not support these options.
%if 0%{?fedora_version} == 36
export LDFLAGS="$(echo "%{build_ldflags}" | sed -e 's/-Wl,-z,relro//' -e 's/-Wl,--build-id=sha1//' -e 's/-Wl,-dT,\/home\/abuild\/rpmbuild\/BUILD\/wine.*//' -e 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//')"
%else
export LDFLAGS="$(echo "%{build_ldflags}" | sed -e 's/-Wl,-z,relro//' -e 's/-Wl,--build-id=sha1//' -e 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-package-notes//' -e 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//')"
%endif
%ifarch x86_64
export CFLAGS="$(echo "%{optflags}" | sed -e 's/-O2//' -e 's/-Wp,-D_FORTIFY_SOURCE=2//' -e 's/-fcf-protection//' -e 's/-fstack-protector-strong//' -e 's/-fstack-clash-protection//' -e 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//') -O2"
%else
export CFLAGS="$(echo "%{optflags}" | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//' -e 's/-fcf-protection//' -e 's/-fstack-protector-strong//' -e 's/-fstack-clash-protection//' -e 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//')"
%endif
#export CFLAGS="`echo $RPM_OPT_FLAGS | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//'` -Wno-error"

%ifarch  %{arm} aarch64
%if 0%{?fedora} >= 33
%global toolchain clang
%else
# ARM64 now requires clang
# https://source.winehq.org/git/wine.git/commit/8fb8cc03c3edb599dd98f369e14a08f899cbff95
export CC="/usr/bin/clang"
# Fedora's default compiler flags now conflict with what clang supports
# https://bugzilla.redhat.com/show_bug.cgi?id=1658311
export CFLAGS="`echo $CFLAGS | sed -e 's/-fstack-clash-protection//'`"
%endif
%endif
%ifarch armv7hl
export CFLAGS="`echo $CFLAGS | sed -e 's/-fexceptions//'`"
%endif

# required so that both Linux and Windows development files can be found
unset PKG_CONFIG_PATH

%if 0%{?wine_tkg}
echo ""
echo "==================================================="
echo "Building wine-tkg"
echo "==================================================="
echo ""
pushd wine-tkg-src

%else

echo ""
echo "==================================================="
echo "Building wine"
echo "==================================================="
echo ""

%endif

%configure \
 --sysconfdir=%{_sysconfdir}/wine \
 --x-includes=%{_includedir} --x-libraries=%{_libdir} \
 --with-dbus \
 --with-x \
%ifarch %{arm}
 --with-float-abi=hard \
%endif
%ifarch x86_64 aarch64
 --enable-win64 \
%ifarch x86_64
 --with-system-dllpath=%{mingw64_bindir} \
%endif
%endif
%ifarch %{ix86}
 --with-system-dllpath=%{mingw32_bindir} \
%endif
%{?wine_staging: --with-xattr} \
 --disable-tests \
 --enable-tools \
 --enable-widl \
 VKD3D_PE_CFLAGS="-I%{_includedir}/vulkan -I%{_includedir}/vkd3d" \
 VKD3D_PE_LIBS="-L%{_libdir} -lvkd3d -lvkd3d-shader"

#%%ifarch x86_64
# XML2_PE_CFLAGS="-I%%{mingw64_includedir}/libxml2" \
# XML2_PE_LIBS="-L%%{mingw64_libdir}"
#%%endif
#%%ifarch %%{ix86}
# XML2_PE_CFLAGS="-I%%{mingw32_includedir}/libxml2" \
# XML2_PE_LIBS="-L%%{mingw32_libdir}"
#%%endif

# https://wiki.winehq.org/Building_a_MinGW_WoW64_Wine_with_a_custom_vkd3d_build


%make_build TARGETFLAGS=""

%if 0%{?wine_tkg}
popd
%endif


%install
%if 0%{?wine_tkg}
pushd wine-tkg-src
echo ""
echo "==================================================="
echo "Installing wine-tkg"
echo "==================================================="
echo ""

%else

echo ""
echo "==================================================="
echo "Installing wine"
echo "==================================================="
echo ""

%endif


# do not change this to make_install
%makeinstall \
        includedir=%{buildroot}%{_includedir} \
        sysconfdir=%{buildroot}%{_sysconfdir}/wine \
        dlldir=%{buildroot}%{_libdir}/wine \
        LDCONFIG=/bin/true \
        UPDATE_DESKTOP_DATABASE=/bin/true

%if 0%{?wine_tkg}
popd
%endif

# setup for alternatives usage
%ifarch x86_64 aarch64
%ifarch aarch64
mv %{buildroot}%{_bindir}/wine %{buildroot}%{_bindir}/wine64
mv %{buildroot}%{_bindir}/wine-preloader %{buildroot}%{_bindir}/wine64-preloader
%endif
mv %{buildroot}%{_bindir}/wineserver %{buildroot}%{_bindir}/wineserver64
%endif
%ifarch %{ix86} %{arm}
mv %{buildroot}%{_bindir}/wine %{buildroot}%{_bindir}/wine32
mv %{buildroot}%{_bindir}/wineserver %{buildroot}%{_bindir}/wineserver32
%endif
%ifnarch aarch64 x86_64
mv %{buildroot}%{_bindir}/wine-preloader %{buildroot}%{_bindir}/wine32-preloader
%endif
touch %{buildroot}%{_bindir}/wine
touch %{buildroot}%{_bindir}/wine-preloader
touch %{buildroot}%{_bindir}/wineserver
# DISABLE FOR DXVK
#mv %{buildroot}%{_libdir}/wine/%{winepedir}/dxgi.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-dxgi.dll
#mv %{buildroot}%{_libdir}/wine/%{winepedir}/d3d9.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-d3d9.dll
#mv %{buildroot}%{_libdir}/wine/%{winepedir}/d3d10.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-d3d10.dll
#mv %{buildroot}%{_libdir}/wine/%{winepedir}/d3d10_1.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-d3d10_1.dll
#mv %{buildroot}%{_libdir}/wine/%{winepedir}/d3d10core.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-d3d10core.dll
#mv %{buildroot}%{_libdir}/wine/%{winepedir}/d3d11.dll %{buildroot}%{_libdir}/wine/%{winepedir}/wine-d3d11.dll
#touch %{buildroot}%{_libdir}/wine/%{winepedir}/dxgi.dll
#touch %{buildroot}%{_libdir}/wine/%{winepedir}/d3d9.dll
#touch %{buildroot}%{_libdir}/wine/%{winepedir}/d3d10.dll
#touch %{buildroot}%{_libdir}/wine/%{winepedir}/d3d10_1.dll
#touch %{buildroot}%{_libdir}/wine/%{winepedir}/d3d10core.dll
#touch %{buildroot}%{_libdir}/wine/%{winepedir}/d3d11.dll

# remove rpath
chrpath --delete %{buildroot}%{_bindir}/wmc
chrpath --delete %{buildroot}%{_bindir}/wrc
%ifarch x86_64 aarch64
chrpath --delete %{buildroot}%{_bindir}/wine64
chrpath --delete %{buildroot}%{_bindir}/wineserver64
%else
chrpath --delete %{buildroot}%{_bindir}/wine32
chrpath --delete %{buildroot}%{_bindir}/wineserver32
%endif

mkdir -p %{buildroot}%{_sysconfdir}/wine

# Allow users to launch Windows programs by just clicking on the .exe file...
mkdir -p %{buildroot}%{_binfmtdir}
install -p -c -m 644 %{SOURCE1} %{buildroot}%{_binfmtdir}/wine.conf

# add wine dir to desktop
mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
install -p -m 644 %{SOURCE200} \
%{buildroot}%{_sysconfdir}/xdg/menus/applications-merged/wine.menu
mkdir -p %{buildroot}%{_datadir}/desktop-directories
install -p -m 644 %{SOURCE201} \
%{buildroot}%{_datadir}/desktop-directories/Wine.directory

# add gecko dir
mkdir -p %{buildroot}%{_datadir}/wine/gecko

# add mono dir
mkdir -p %{buildroot}%{_datadir}/wine/mono

# extract and install icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

# This replacement masks a composite program icon .SVG down
# so that only its full-size scalable icon is visible
PROGRAM_ICONFIX='s/height="272"/height="256"/;'\
's/width="632"/width="256"\n'\
'   x="368"\n'\
'   y="8"\n'\
'   viewBox="368, 8, 256, 256"/;'
MAIN_ICONFIX='s/height="272"/height="256"/;'\
's/width="632"/width="256"\n'\
'   x="8"\n'\
'   y="8"\n'\
'   viewBox="8, 8, 256, 256"/;'

# This icon file is still in the legacy format
%if 0%{?wine_tkg}
pushd wine-tkg-src
%endif
install -p -m 644 dlls/user32/resources/oic_winlogo.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/wine.svg
sed -i -e "$MAIN_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/wine.svg

# The rest come from programs/, and contain larger scalable icons
# with a new layout that requires the PROGRAM_ICONFIX sed adjustment
install -p -m 644 programs/notepad/notepad.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/notepad.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/notepad.svg

install -p -m 644 programs/regedit/regedit.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/regedit.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/regedit.svg

install -p -m 644 programs/msiexec/msiexec.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/msiexec.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/msiexec.svg

install -p -m 644 programs/winecfg/winecfg.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winecfg.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winecfg.svg

install -p -m 644 programs/winefile/winefile.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winefile.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winefile.svg

install -p -m 644 programs/winemine/winemine.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winemine.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winemine.svg

install -p -m 644 programs/winhlp32/winhelp.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winhelp.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/winhelp.svg

install -p -m 644 programs/wordpad/wordpad.svg \
 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/wordpad.svg
sed -i -e "$PROGRAM_ICONFIX" %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/wordpad.svg

%if 0%{?wine_tkg}
popd
%endif

# install desktop files
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE100}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE101}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE102}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE103}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE104}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE105}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE106}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE107}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE108}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE109}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  --delete-original \
  %{buildroot}%{_datadir}/applications/wine.desktop

#mime-types
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE300}

%if 0%{?wine_tkg}
pushd wine-tkg-src
%endif
cp -p %{SOURCE2} README-FEDORA

cp -p %{SOURCE502} README-tahoma
%if 0%{?wine_tkg}
popd
%endif

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/

%ifarch %{ix86} %{arm}
install -p -m644 %{SOURCE3} %{buildroot}%{_sysconfdir}/ld.so.conf.d/
%endif

%ifarch x86_64 aarch64
install -p -m644 %{SOURCE4} %{buildroot}%{_sysconfdir}/ld.so.conf.d/
%endif


# install Tahoma font for system package
install -p -m 0755 -d %{buildroot}/%{_datadir}/fonts/wine-tahoma-fonts
pushd %{buildroot}/%{_datadir}/fonts/wine-tahoma-fonts
ln -s ../../wine/fonts/tahoma.ttf tahoma.ttf
ln -s ../../wine/fonts/tahomabd.ttf tahomabd.ttf
popd

# add config and readme for tahoma
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -p -m 0644 %{SOURCE501} %{buildroot}%{_fontconfig_templatedir}/20-wine-tahoma-nobitmaps.conf

ln -s %{_fontconfig_templatedir}/20-wine-tahoma-nobitmaps.conf \
      %{buildroot}%{_fontconfig_confdir}/20-wine-tahoma-nobitmaps.conf

%if 0%{?wine_staging}
# install Times New Roman font for system package
install -p -m 0755 -d %{buildroot}/%{_datadir}/fonts/wine-times-new-roman-fonts
pushd %{buildroot}/%{_datadir}/fonts/wine-times-new-roman-fonts
ln -s ../../wine/fonts/times.ttf times.ttf
popd
%endif

# install Wingdings font for system package
install -p -m 0755 -d %{buildroot}/%{_datadir}/fonts/wine-wingdings-fonts
pushd %{buildroot}/%{_datadir}/fonts/wine-wingdings-fonts
ln -s ../../wine/fonts/wingding.ttf wingding.ttf
popd

# clean readme files
%if 0%{?wine_tkg}
pushd wine-tkg-src/documentation
%else
pushd documentation
%endif
for lang in it hu sv es pt pt_br;
do iconv -f iso8859-1 -t utf-8 README.$lang > \
 README.$lang.conv && mv -f README.$lang.conv README.$lang
done;
popd

rm -f %{buildroot}%{_initrddir}/wine

# wine makefiles are currently broken and don't install the wine man page
%if 0%{?wine_tkg}
pushd wine-tkg-src
%endif
install -p -m 0644 loader/wine.man %{buildroot}%{_mandir}/man1/wine.1
install -p -m 0644 loader/wine.de.UTF-8.man %{buildroot}%{_mandir}/de.UTF-8/man1/wine.1
install -p -m 0644 loader/wine.fr.UTF-8.man %{buildroot}%{_mandir}/fr.UTF-8/man1/wine.1
mkdir -p %{buildroot}%{_mandir}/pl.UTF-8/man1
install -p -m 0644 loader/wine.pl.UTF-8.man %{buildroot}%{_mandir}/pl.UTF-8/man1/wine.1
%if 0%{?wine_tkg}
popd
%endif

# install and validate AppData file
mkdir -p %{buildroot}/%{_metainfodir}/
install -p -m 0644 %{SOURCE150} %{buildroot}/%{_metainfodir}/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml

# install widl
%if 0%{?wine_tkg}
pushd wine-tkg-src/tools/widl
%else
pushd tools/widl
%endif
%make_install
popd


%post systemd
%binfmt_apply wine.conf

%postun systemd
if [ $1 -eq 0 ]; then
/bin/systemctl try-restart systemd-binfmt.service
fi

%ldconfig_post core

%posttrans core
# handle upgrades for a few package updates
%{_sbindir}/alternatives --remove 'wine-dxgi%{?_isa}' %{_libdir}/wine/wine-dxgi.dll 2>/dev/null || :
%{_sbindir}/alternatives --remove 'wine-d3d9%{?_isa}' %{_libdir}/wine/wine-d3d9.dll 2>/dev/null || :
%{_sbindir}/alternatives --remove 'wine-d3d10%{?_isa}' %{_libdir}/wine/wine-d3d10.dll 2>/dev/null || :
%{_sbindir}/alternatives --remove 'wine-d3d11%{?_isa}' %{_libdir}/wine/wine-d3d11.dll 2>/dev/null || :

%ifarch x86_64 aarch64
%{_sbindir}/alternatives --install %{_bindir}/wine \
  wine %{_bindir}/wine64 10 \
  --slave %{_bindir}/wine-preloader wine-preloader %{_bindir}/wine64-preloader
%{_sbindir}/alternatives --install %{_bindir}/wineserver \
  wineserver %{_bindir}/wineserver64 20
%else
%{_sbindir}/alternatives --install %{_bindir}/wine \
  wine %{_bindir}/wine32 20 \
  --slave %{_bindir}/wine-preloader wine-preloader %{_bindir}/wine32-preloader
%{_sbindir}/alternatives --install %{_bindir}/wineserver \
  wineserver %{_bindir}/wineserver32 10
%endif

##%%{_sbindir}/alternatives --install %%{_libdir}/wine/%{winepedir}/dxgi.dll \
##  'wine-dxgi%%{?_isa}' %%{_libdir}/wine/%%{winepedir}/wine-dxgi.dll 10
##%%{_sbindir}/alternatives --install %%{_libdir}/wine/%%{winepedir}/d3d9.dll \
##  'wine-d3d9%%{?_isa}' %%{_libdir}/wine/%%{winepedir}/wine-d3d9.dll 10
##%%{_sbindir}/alternatives --install %%{_libdir}/wine/%%{winepedir}/d3d10.dll \
##  'wine-d3d10%%{?_isa}' %%{_libdir}/wine/%%{winepedir}/wine-d3d10.dll 10 \
##  --slave  %%{_libdir}/wine/%%{winepedir}/d3d10_1.dll 'wine-d3d10_1%%{?_isa}' %%{_libdir}/wine/%%{winepedir}/wine-d3d10_1.dll \
##  --slave  %%{_libdir}/wine/%%{winepedir}/d3d10core.dll 'wine-d3d10core%%{?_isa}' %%{_libdir}/wine/%%{winepedir}/wine-d3d10core.dll
##%%{_sbindir}/alternatives --install %%{_libdir}/wine/%%{winepedir}/d3d11.dll \
##  'wine-d3d11%{?_isa}' %%{_libdir}/wine/%%{winepedir}/wine-d3d11.dll 10

%postun core
%{?ldconfig}
# uninstall
if [ $1 -eq 0 ] ; then
%ifarch x86_64 aarch64
  %{_sbindir}/alternatives --remove wine %{_bindir}/wine64
  %{_sbindir}/alternatives --remove wineserver %{_bindir}/wineserver64
%else
  %{_sbindir}/alternatives --remove wine %{_bindir}/wine32
  %{_sbindir}/alternatives --remove wineserver %{_bindir}/wineserver32
%endif
  %{_sbindir}/alternatives --remove 'wine-dxgi%{?_isa}' %{_libdir}/wine/%{winepedir}/wine-dxgi.dll || :
  %{_sbindir}/alternatives --remove 'wine-d3d9%{?_isa}' %{_libdir}/wine/%{winepedir}/wine-d3d9.dll || :
  %{_sbindir}/alternatives --remove 'wine-d3d10%{?_isa}' %{_libdir}/wine/%{winepedir}/wine-d3d10.dll || :
  %{_sbindir}/alternatives --remove 'wine-d3d11%{?_isa}' %{_libdir}/wine/%{winepedir}/wine-d3d11.dll || :
fi

%ldconfig_scriptlets ldap

%ldconfig_scriptlets cms

%ldconfig_scriptlets twain

%ldconfig_scriptlets alsa

#%%if 0%%{?fedora} >= 10 || 0%%{?rhel} >= 6
#%%ldconfig_scriptlets openal
#%%endif

%files
# meta package

%files core
%doc %{?wine_tkg:wine-tkg-src/}ANNOUNCE
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%doc %{?wine_tkg:wine-tkg-src/}LICENSE
%doc %{?wine_tkg:wine-tkg-src/}LICENSE.OLD
%doc %{?wine_tkg:wine-tkg-src/}AUTHORS
%doc %{?wine_tkg:wine-tkg-src/}README-FEDORA
%doc %{?wine_tkg:wine-tkg-src/}README
%doc %{?wine_tkg:wine-tkg-src/}VERSION
# do not include huge changelogs .OLD .ALPHA .BETA (#204302)
%doc %{?wine_tkg:wine-tkg-src/}documentation/README.*
%{_bindir}/msidb
%{_bindir}/winedump
%{_libdir}/wine/%{winepedir}/explorer.exe
%{_libdir}/wine/%{winepedir}/cabarc.exe
%{_libdir}/wine/%{winepedir}/certutil.exe
%{_libdir}/wine/%{winepedir}/control.exe
%{_libdir}/wine/%{winepedir}/cmd.exe
%{_libdir}/wine/%{winepedir}/dxdiag.exe
%{_libdir}/wine/%{winepedir}/notepad.exe
%{_libdir}/wine/%{winepedir}/plugplay.exe
%{_libdir}/wine/%{winepedir}/pnputil.exe
%{_libdir}/wine/%{winepedir}/progman.exe
%{_libdir}/wine/%{winepedir}/setx.exe
%{_libdir}/wine/%{winepedir}/taskmgr.exe
%{_libdir}/wine/%{winepedir}/winedbg.exe
%{_libdir}/wine/%{winepedir}/winefile.exe
%{_libdir}/wine/%{winepedir}/winemine.exe
%{_libdir}/wine/%{winepedir}/winemsibuilder.exe
%{_libdir}/wine/%{winepedir}/winepath.exe
%{_libdir}/wine/%{winepedir}/winmgmt.exe
%{_libdir}/wine/%{winepedir}/winver.exe
%{_libdir}/wine/%{winepedir}/wordpad.exe
%{_libdir}/wine/%{winepedir}/write.exe
%{_libdir}/wine/%{winepedir}/wusa.exe

%ifarch %{ix86} %{arm}
%{_bindir}/wine32
%{_bindir}/wine32-preloader
%{_bindir}/wineserver32
%config %{_sysconfdir}/ld.so.conf.d/wine-32.conf
%endif

%ifarch x86_64 aarch64
%{_bindir}/wine64
%{_bindir}/wineserver64
%config %{_sysconfdir}/ld.so.conf.d/wine-64.conf
%endif
%ifarch x86_64 aarch64
%{_bindir}/wine64-preloader
%endif

%ghost %{_bindir}/wine
%ghost %{_bindir}/wine-preloader
%ghost %{_bindir}/wineserver

%dir %{_libdir}/wine

%{_libdir}/wine/%{winepedir}/attrib.exe
%{_libdir}/wine/%{winepedir}/arp.exe
%{_libdir}/wine/%{winepedir}/aspnet_regiis.exe
##%%{_libdir}/wine/%%{winepedir}/belauncher.exe
%{_libdir}/wine/%{winepedir}/cacls.exe
%{_libdir}/wine/%{winepedir}/conhost.exe
%{_libdir}/wine/%{winepedir}/cscript.exe
%{_libdir}/wine/%{winepedir}/dism.exe
%{_libdir}/wine/%{winepedir}/dllhost.exe
%{_libdir}/wine/%{winepedir}/dplaysvr.exe
%{_libdir}/wine/%{winepedir}/dpnsvr.exe
%{_libdir}/wine/%{winepedir}/dpvsetup.exe
%{_libdir}/wine/%{winepedir}/eject.exe
%{_libdir}/wine/%{winepedir}/expand.exe
%{_libdir}/wine/%{winepedir}/extrac32.exe
%{_libdir}/wine/%{winepedir}/fc.exe
%{_libdir}/wine/%{winepedir}/find.exe
%{_libdir}/wine/%{winepedir}/findstr.exe
%{_libdir}/wine/%{winepedir}/fsutil.exe
%{_libdir}/wine/%{winepedir}/hostname.exe
%{_libdir}/wine/%{winepedir}/ipconfig.exe
%{_libdir}/wine/%{winepedir}/klist.exe
%{_libdir}/wine/%{winepedir}/mshta.exe
%{_libdir}/wine/%{winepedir}/msidb.exe
%{_libdir}/wine/%{winepedir}/msiexec.exe
%{_libdir}/wine/%{winepedir}/net.exe
%{_libdir}/wine/%{winepedir}/netstat.exe
%{_libdir}/wine/%{winepedir}/ngen.exe
%{_libdir}/wine/%{winepedir}/ntoskrnl.exe
%{_libdir}/wine/%{winepedir}/oleview.exe
%{_libdir}/wine/%{winepedir}/ping.exe
%{_libdir}/wine/%{winepedir}/powershell.exe
%{_libdir}/wine/%{winepedir}/reg.exe
%{_libdir}/wine/%{winepedir}/regasm.exe
%{_libdir}/wine/%{winepedir}/regedit.exe
%{_libdir}/wine/%{winepedir}/regsvcs.exe
%{_libdir}/wine/%{winepedir}/regsvr32.exe
%{_libdir}/wine/%{winepedir}/rpcss.exe
%{_libdir}/wine/%{winepedir}/rundll32.exe
%{_libdir}/wine/%{winepedir}/schtasks.exe
%{_libdir}/wine/%{winepedir}/sdbinst.exe
%{_libdir}/wine/%{winepedir}/secedit.exe
%{_libdir}/wine/%{winepedir}/servicemodelreg.exe
%{_libdir}/wine/%{winepedir}/services.exe
%{_libdir}/wine/%{winepedir}/start.exe
%{_libdir}/wine/%{winepedir}/tasklist.exe
%{_libdir}/wine/%{winepedir}/termsv.exe
%{_libdir}/wine/%{winepedir}/view.exe
%{_libdir}/wine/%{winepedir}/wevtutil.exe
%{_libdir}/wine/%{winepedir}/where.exe
%{_libdir}/wine/%{winepedir}/whoami.exe
%{_libdir}/wine/%{winepedir}/wineboot.exe
%{_libdir}/wine/%{winepedir}/winebrowser.exe
%{_libdir}/wine/%{winepedir}/wineconsole.exe
%{_libdir}/wine/%{winepedir}/winemenubuilder.exe
%{_libdir}/wine/%{winepedir}/winecfg.exe
%{_libdir}/wine/%{winepedir}/winedevice.exe
%{_libdir}/wine/%{winepedir}/winhlp32.exe
%{_libdir}/wine/%{winepedir}/wmplayer.exe
%{_libdir}/wine/%{winepedir}/wscript.exe
%{_libdir}/wine/%{winepedir}/uninstaller.exe

%{_libdir}/wine/%{winepedir}/acledit.dll
%{_libdir}/wine/%{winepedir}/aclui.dll
%{_libdir}/wine/%{winepedir}/activeds.dll
%{_libdir}/wine/%{winepedir}/activeds.tlb
%{_libdir}/wine/%{winepedir}/actxprxy.dll
%{_libdir}/wine/%{winepedir}/adsldp.dll
%{_libdir}/wine/%{winepedir}/adsldpc.dll
%{_libdir}/wine/%{winepedir}/advapi32.dll
%{_libdir}/wine/%{winepedir}/advpack.dll
%{_libdir}/wine/%{winepedir}/amsi.dll
%{_libdir}/wine/%{winepedir}/amstream.dll
%{_libdir}/wine/%{winepedir}/apisetschema.dll
%{_libdir}/wine/%{winepedir}/apphelp.dll
%{_libdir}/wine/%{winepedir}/appwiz.cpl
%{_libdir}/wine/%{winepedir}/atl.dll
%{_libdir}/wine/%{winepedir}/atl80.dll
%{_libdir}/wine/%{winepedir}/atl90.dll
%{_libdir}/wine/%{winepedir}/atl100.dll
%{_libdir}/wine/%{winepedir}/atl110.dll
%{_libdir}/wine/%{winepedir}/atlthunk.dll
%{_libdir}/wine/%{winepedir}/atmlib.dll
%{_libdir}/wine/%{winepedir}/authz.dll
%{_libdir}/wine/%{winepedir}/avicap32.dll
%{_libdir}/wine/%{winesodir}/avicap32.so
%{_libdir}/wine/%{winepedir}/avifil32.dll
%{_libdir}/wine/%{winepedir}/avrt.dll
%{_libdir}/wine/%{winesodir}/bcrypt.so
%{_libdir}/wine/%{winepedir}/bcrypt.dll
%{_libdir}/wine/%{winepedir}/bcryptprimitives.dll
%{_libdir}/wine/%{winepedir}/bluetoothapis.dll
%{_libdir}/wine/%{winepedir}/browseui.dll
%{_libdir}/wine/%{winepedir}/bthprops.cpl
%{_libdir}/wine/%{winepedir}/cabinet.dll
%{_libdir}/wine/%{winepedir}/cards.dll
%{_libdir}/wine/%{winepedir}/cdosys.dll
%{_libdir}/wine/%{winepedir}/cfgmgr32.dll
%{_libdir}/wine/%{winepedir}/chcp.com
%{_libdir}/wine/%{winepedir}/clock.exe
%{_libdir}/wine/%{winepedir}/clusapi.dll
%{_libdir}/wine/%{winepedir}/cng.sys
%{_libdir}/wine/%{winepedir}/combase.dll
%{_libdir}/wine/%{winepedir}/comcat.dll
%{_libdir}/wine/%{winepedir}/comctl32.dll
%{_libdir}/wine/%{winepedir}/comdlg32.dll
%{_libdir}/wine/%{winepedir}/compstui.dll
%{_libdir}/wine/%{winepedir}/comsvcs.dll
%{_libdir}/wine/%{winepedir}/concrt140.dll
%{_libdir}/wine/%{winepedir}/connect.dll
%{_libdir}/wine/%{winepedir}/credui.dll
%{_libdir}/wine/%{winepedir}/crtdll.dll
%{_libdir}/wine/%{winesodir}/crypt32.so
%{_libdir}/wine/%{winepedir}/crypt32.dll
%{_libdir}/wine/%{winepedir}/cryptdlg.dll
%{_libdir}/wine/%{winepedir}/cryptdll.dll
%{_libdir}/wine/%{winepedir}/cryptext.dll
%{_libdir}/wine/%{winepedir}/cryptnet.dll
%{_libdir}/wine/%{winepedir}/cryptowinrt.dll
%{_libdir}/wine/%{winepedir}/cryptsp.dll
%{_libdir}/wine/%{winepedir}/cryptui.dll
%{_libdir}/wine/%{winepedir}/ctapi32.dll
%{_libdir}/wine/%{winesodir}/ctapi32.so
%{_libdir}/wine/%{winepedir}/ctl3d32.dll
%{_libdir}/wine/%{winepedir}/d2d1.dll

# DISABLE FOR DXVK
#%%ghost %%{_libdir}/wine/%%{winepedir}/d3d10.dll
#%%ghost %%{_libdir}/wine/%%{winepedir}/d3d10_1.dll
#%%ghost %%{_libdir}/wine/%%{winepedir}/d3d10core.dll
#%%{_libdir}/wine/%%{winepedir}/wine-d3d10.dll
#%%{_libdir}/wine/%%{winepedir}/wine-d3d10_1.dll
#%%{_libdir}/wine/%%{winepedir}/wine-d3d10core.dll
#%%ghost %%{_libdir}/wine/%%{winepedir}/d3d11.dll
#%%{_libdir}/wine/%%{winepedir}/wine-d3d11.dll
%{_libdir}/wine/%{winepedir}/d3d10.dll
%{_libdir}/wine/%{winepedir}/d3d10_1.dll
%{_libdir}/wine/%{winepedir}/d3d10core.dll
%{_libdir}/wine/%{winepedir}/d3d11.dll
# END DXVK

%{_libdir}/wine/%{winepedir}/d3d12.dll
%{_libdir}/wine/%{winepedir}/d3d12core.dll
%{_libdir}/wine/%{winepedir}/d3dcompiler_*.dll
%{_libdir}/wine/%{winepedir}/d3dim.dll
%{_libdir}/wine/%{winepedir}/d3dim700.dll
%{_libdir}/wine/%{winepedir}/d3drm.dll
%{_libdir}/wine/%{winepedir}/d3dx9_*.dll
%{_libdir}/wine/%{winepedir}/d3dx10_*.dll
%{_libdir}/wine/%{winepedir}/d3dx11_42.dll
%{_libdir}/wine/%{winepedir}/d3dx11_43.dll
%{_libdir}/wine/%{winepedir}/d3dxof.dll
%{_libdir}/wine/%{winepedir}/davclnt.dll
%{_libdir}/wine/%{winepedir}/dbgeng.dll
%{_libdir}/wine/%{winepedir}/dbghelp.dll
%{_libdir}/wine/%{winepedir}/dciman32.dll
%{_libdir}/wine/%{winepedir}/dcomp.dll
%{_libdir}/wine/%{winepedir}/ddraw.dll
%{_libdir}/wine/%{winepedir}/ddrawex.dll
%{_libdir}/wine/%{winepedir}/devenum.dll
%{_libdir}/wine/%{winepedir}/dhcpcsvc.dll
%{_libdir}/wine/%{winepedir}/dhcpcsvc6.dll
%{_libdir}/wine/%{winepedir}/dhtmled.ocx
%{_libdir}/wine/%{winepedir}/diasymreader.dll
%{_libdir}/wine/%{winepedir}/difxapi.dll
%{_libdir}/wine/%{winepedir}/dinput.dll
%{_libdir}/wine/%{winepedir}/dinput8.dll
%{_libdir}/wine/%{winepedir}/directmanipulation.dll
%{_libdir}/wine/%{winepedir}/dispex.dll
%{_libdir}/wine/%{winepedir}/dmband.dll
%{_libdir}/wine/%{winepedir}/dmcompos.dll
%{_libdir}/wine/%{winepedir}/dmime.dll
%{_libdir}/wine/%{winepedir}/dmloader.dll
%{_libdir}/wine/%{winepedir}/dmscript.dll
%{_libdir}/wine/%{winepedir}/dmstyle.dll
%{_libdir}/wine/%{winepedir}/dmsynth.dll
%{_libdir}/wine/%{winepedir}/dmusic.dll
%{_libdir}/wine/%{winepedir}/dmusic32.dll
%{_libdir}/wine/%{winepedir}/dplay.dll
%{_libdir}/wine/%{winepedir}/dplayx.dll
%{_libdir}/wine/%{winepedir}/dpnaddr.dll
%{_libdir}/wine/%{winepedir}/dpnet.dll
%{_libdir}/wine/%{winepedir}/dpnhpast.dll
%{_libdir}/wine/%{winepedir}/dpnhupnp.dll
%{_libdir}/wine/%{winepedir}/dpnlobby.dll
%{_libdir}/wine/%{winepedir}/dpvoice.dll
%{_libdir}/wine/%{winepedir}/dpwsockx.dll
%{_libdir}/wine/%{winepedir}/drmclien.dll
%{_libdir}/wine/%{winepedir}/dsound.dll
%{_libdir}/wine/%{winepedir}/dsdmo.dll
%{_libdir}/wine/%{winepedir}/dsquery.dll
%{_libdir}/wine/%{winepedir}/dssenh.dll
%{_libdir}/wine/%{winepedir}/dsuiext.dll
%{_libdir}/wine/%{winepedir}/dswave.dll
%{_libdir}/wine/%{winepedir}/dwmapi.dll
%{_libdir}/wine/%{winepedir}/dwrite.dll
%{_libdir}/wine/%{winesodir}/dwrite.so
%{_libdir}/wine/%{winepedir}/dx8vb.dll
%{_libdir}/wine/%{winepedir}/dxdiagn.dll

# DISABLE FOR DXVK
#%%ghost %%{_libdir}/wine/%%{winepedir}/dxgi.dll
#%%{_libdir}/wine/%%{winepedir}/wine-dxgi.dll
%{_libdir}/wine/%{winepedir}/dxgi.dll
# END DXVK

%if 0%{?wine_staging}
%{_libdir}/wine/%{winepedir}/dxgkrnl.sys
%{_libdir}/wine/%{winepedir}/dxgmms1.sys
%endif
%{_libdir}/wine/%{winepedir}/dxtrans.dll
%{_libdir}/wine/%{winepedir}/dxva2.dll
%{_libdir}/wine/%{winepedir}/esent.dll
%{_libdir}/wine/%{winepedir}/evr.dll
%{_libdir}/wine/%{winepedir}/explorerframe.dll
%{_libdir}/wine/%{winepedir}/faultrep.dll
%{_libdir}/wine/%{winepedir}/feclient.dll
%{_libdir}/wine/%{winepedir}/fltlib.dll
%{_libdir}/wine/%{winepedir}/fltmgr.sys
%{_libdir}/wine/%{winepedir}/fntcache.dll
%{_libdir}/wine/%{winepedir}/fontsub.dll
%{_libdir}/wine/%{winepedir}/fusion.dll
%{_libdir}/wine/%{winepedir}/fwpuclnt.dll
%{_libdir}/wine/%{winepedir}/gameux.dll
%{_libdir}/wine/%{winepedir}/gamingtcui.dll
%{_libdir}/wine/%{winepedir}/gdi32.dll
%{_libdir}/wine/%{winepedir}/gdiplus.dll
%{_libdir}/wine/%{winepedir}/geolocation.dll
%{_libdir}/wine/%{winepedir}/glu32.dll
%{_libdir}/wine/%{winepedir}/gphoto2.ds
%{_libdir}/wine/%{winesodir}/gphoto2.so
%{_libdir}/wine/%{winepedir}/gpkcsp.dll
%{_libdir}/wine/%{winepedir}/graphicscapture.dll
%{_libdir}/wine/%{winepedir}/hal.dll
%{_libdir}/wine/%{winepedir}/hh.exe
%{_libdir}/wine/%{winepedir}/hhctrl.ocx
%{_libdir}/wine/%{winepedir}/hid.dll
%{_libdir}/wine/%{winepedir}/hidclass.sys
%{_libdir}/wine/%{winepedir}/hidparse.sys
%{_libdir}/wine/%{winepedir}/hlink.dll
%{_libdir}/wine/%{winepedir}/hnetcfg.dll
%{_libdir}/wine/%{winepedir}/hrtfapo.dll
%{_libdir}/wine/%{winepedir}/http.sys
%{_libdir}/wine/%{winepedir}/httpapi.dll
%{_libdir}/wine/%{winepedir}/ia2comproxy.dll
%{_libdir}/wine/%{winepedir}/icacls.exe
%{_libdir}/wine/%{winepedir}/iccvid.dll
%{_libdir}/wine/%{winepedir}/icinfo.exe
%{_libdir}/wine/%{winepedir}/icmp.dll
%{_libdir}/wine/%{winepedir}/ieframe.dll
%{_libdir}/wine/%{winepedir}/ieproxy.dll
%{_libdir}/wine/%{winepedir}/imaadp32.acm
%{_libdir}/wine/%{winepedir}/imagehlp.dll
%{_libdir}/wine/%{winepedir}/imm32.dll
%{_libdir}/wine/%{winepedir}/inetcomm.dll
%{_libdir}/wine/%{winepedir}/inetcpl.cpl
%{_libdir}/wine/%{winepedir}/inetmib1.dll
%{_libdir}/wine/%{winepedir}/infosoft.dll
%{_libdir}/wine/%{winepedir}/initpki.dll
%{_libdir}/wine/%{winepedir}/inkobj.dll
%{_libdir}/wine/%{winepedir}/inseng.dll
%{_libdir}/wine/%{winepedir}/iphlpapi.dll
%{_libdir}/wine/%{winepedir}/iprop.dll
%{_libdir}/wine/%{winepedir}/irprops.cpl
%{_libdir}/wine/%{winepedir}/ir50_32.dll
%{_libdir}/wine/%{winepedir}/itircl.dll
%{_libdir}/wine/%{winepedir}/itss.dll
%{_libdir}/wine/%{winepedir}/joy.cpl
%{_libdir}/wine/%{winepedir}/jscript.dll
%{_libdir}/wine/%{winepedir}/jsproxy.dll
%{_libdir}/wine/%{winesodir}/kerberos.so
%{_libdir}/wine/%{winepedir}/kerberos.dll
%{_libdir}/wine/%{winepedir}/kernel32.dll
%{_libdir}/wine/%{winepedir}/kernelbase.dll
%{_libdir}/wine/%{winepedir}/ksecdd.sys
%{_libdir}/wine/%{winepedir}/ksproxy.ax
%{_libdir}/wine/%{winepedir}/ksuser.dll
%{_libdir}/wine/%{winepedir}/ktmw32.dll
%{_libdir}/wine/%{winepedir}/l3codeca.acm
%{_libdir}/wine/%{winepedir}/light.msstyles
%{_libdir}/wine/%{winepedir}/loadperf.dll
%{_libdir}/wine/%{winepedir}/localspl.dll
%{_libdir}/wine/%{winesodir}/localspl.so
%{_libdir}/wine/%{winepedir}/localui.dll
%{_libdir}/wine/%{winepedir}/lodctr.exe
%{_libdir}/wine/%{winepedir}/lz32.dll
%{_libdir}/wine/%{winepedir}/mapi32.dll
%{_libdir}/wine/%{winepedir}/mapistub.dll
%{_libdir}/wine/%{winepedir}/mciavi32.dll
%{_libdir}/wine/%{winepedir}/mcicda.dll
%{_libdir}/wine/%{winepedir}/mciqtz32.dll
%{_libdir}/wine/%{winepedir}/mciseq.dll
%{_libdir}/wine/%{winepedir}/mciwave.dll
%{_libdir}/wine/%{winepedir}/mf.dll
%{_libdir}/wine/%{winepedir}/mf3216.dll
%{_libdir}/wine/%{winepedir}/mferror.dll
%{_libdir}/wine/%{winepedir}/mfmediaengine.dll
%{_libdir}/wine/%{winepedir}/mfplat.dll
%{_libdir}/wine/%{winepedir}/mfplay.dll
%{_libdir}/wine/%{winepedir}/mfreadwrite.dll
%{_libdir}/wine/%{winepedir}/mfsrcsnk.dll
%{_libdir}/wine/%{winepedir}/mgmtapi.dll
%{_libdir}/wine/%{winepedir}/midimap.dll
%{_libdir}/wine/%{winepedir}/mlang.dll
%{_libdir}/wine/%{winepedir}/mmcndmgr.dll
%{_libdir}/wine/%{winepedir}/mmdevapi.dll
%{_libdir}/wine/%{winepedir}/mofcomp.exe
%{_libdir}/wine/%{winesodir}/mountmgr.so
%{_libdir}/wine/%{winepedir}/mountmgr.sys
%{_libdir}/wine/%{winepedir}/mp3dmod.dll
%{_libdir}/wine/%{winepedir}/mpr.dll
%{_libdir}/wine/%{winepedir}/mprapi.dll
%{_libdir}/wine/%{winepedir}/msacm32.dll
%{_libdir}/wine/%{winepedir}/msacm32.drv
%{_libdir}/wine/%{winepedir}/msado15.dll
%{_libdir}/wine/%{winepedir}/msadp32.acm
%{_libdir}/wine/%{winepedir}/msasn1.dll
%{_libdir}/wine/%{winepedir}/msauddecmft.dll
%{_libdir}/wine/%{winepedir}/mscat32.dll
%{_libdir}/wine/%{winepedir}/mscoree.dll
%{_libdir}/wine/%{winepedir}/mscorwks.dll
%{_libdir}/wine/%{winepedir}/msctf.dll
%{_libdir}/wine/%{winepedir}/msctfmonitor.dll
%{_libdir}/wine/%{winepedir}/msctfp.dll
%{_libdir}/wine/%{winepedir}/msdaps.dll
%{_libdir}/wine/%{winepedir}/msdasql.dll
%{_libdir}/wine/%{winepedir}/msdelta.dll
%{_libdir}/wine/%{winepedir}/msdmo.dll
%{_libdir}/wine/%{winepedir}/msdrm.dll
%{_libdir}/wine/%{winepedir}/msftedit.dll
%{_libdir}/wine/%{winepedir}/msg711.acm
%{_libdir}/wine/%{winepedir}/msgsm32.acm
%{_libdir}/wine/%{winepedir}/mshtml.dll
%{_libdir}/wine/%{winepedir}/mshtml.tlb
%{_libdir}/wine/%{winepedir}/msi.dll
%{_libdir}/wine/%{winepedir}/msident.dll
%{_libdir}/wine/%{winepedir}/msimtf.dll
%{_libdir}/wine/%{winepedir}/msimg32.dll
%{_libdir}/wine/%{winepedir}/msimsg.dll
%{_libdir}/wine/%{winepedir}/msinfo32.exe
%{_libdir}/wine/%{winepedir}/msisip.dll
%{_libdir}/wine/%{winepedir}/msisys.ocx
%{_libdir}/wine/%{winepedir}/msls31.dll
%{_libdir}/wine/%{winepedir}/msmpeg2vdec.dll
%{_libdir}/wine/%{winepedir}/msnet32.dll
%{_libdir}/wine/%{winepedir}/mspatcha.dll
%{_libdir}/wine/%{winepedir}/msports.dll
%{_libdir}/wine/%{winepedir}/msscript.ocx
%{_libdir}/wine/%{winepedir}/mssign32.dll
%{_libdir}/wine/%{winepedir}/mssip32.dll
%{_libdir}/wine/%{winepedir}/msrle32.dll
%{_libdir}/wine/%{winepedir}/mstask.dll
%{_libdir}/wine/%{winepedir}/msv1_0.dll
%{_libdir}/wine/%{winesodir}/msv1_0.so
%{_libdir}/wine/%{winepedir}/msvcirt.dll
%{_libdir}/wine/%{winepedir}/msvcm80.dll
%{_libdir}/wine/%{winepedir}/msvcm90.dll
%{_libdir}/wine/%{winepedir}/msvcp_win.dll
%{_libdir}/wine/%{winepedir}/msvcp60.dll
%{_libdir}/wine/%{winepedir}/msvcp70.dll
%{_libdir}/wine/%{winepedir}/msvcp71.dll
%{_libdir}/wine/%{winepedir}/msvcp80.dll
%{_libdir}/wine/%{winepedir}/msvcp90.dll
%{_libdir}/wine/%{winepedir}/msvcp100.dll
%{_libdir}/wine/%{winepedir}/msvcp110.dll
%{_libdir}/wine/%{winepedir}/msvcp120.dll
%{_libdir}/wine/%{winepedir}/msvcp120_app.dll
%{_libdir}/wine/%{winepedir}/msvcp140.dll
%{_libdir}/wine/%{winepedir}/msvcp140_1.dll
%{_libdir}/wine/%{winepedir}/msvcp140_2.dll
%{_libdir}/wine/%{winepedir}/msvcp140_atomic_wait.dll
%{_libdir}/wine/%{winepedir}/msvcr70.dll
%{_libdir}/wine/%{winepedir}/msvcr71.dll
%{_libdir}/wine/%{winepedir}/msvcr80.dll
%{_libdir}/wine/%{winepedir}/msvcr90.dll
%{_libdir}/wine/%{winepedir}/msvcr100.dll
%{_libdir}/wine/%{winepedir}/msvcr110.dll
%{_libdir}/wine/%{winepedir}/msvcr120.dll
%{_libdir}/wine/%{winepedir}/msvcr120_app.dll
%{_libdir}/wine/%{winepedir}/msvcrt.dll
%{_libdir}/wine/%{winepedir}/msvcrt20.dll
%{_libdir}/wine/%{winepedir}/msvcrt40.dll
%{_libdir}/wine/%{winepedir}/msvcrtd.dll
%{_libdir}/wine/%{winepedir}/msvfw32.dll
%{_libdir}/wine/%{winepedir}/msvidc32.dll
%{_libdir}/wine/%{winepedir}/mswsock.dll
%{_libdir}/wine/%{winepedir}/msxml.dll
%{_libdir}/wine/%{winepedir}/msxml2.dll
%{_libdir}/wine/%{winepedir}/msxml3.dll
%{_libdir}/wine/%{winepedir}/msxml4.dll
%{_libdir}/wine/%{winepedir}/msxml6.dll
%{_libdir}/wine/%{winepedir}/mtxdm.dll
%{_libdir}/wine/%{winepedir}/nddeapi.dll
%{_libdir}/wine/%{winepedir}/ncrypt.dll
%{_libdir}/wine/%{winepedir}/ndis.sys
%{_libdir}/wine/%{winesodir}/netapi32.so
%{_libdir}/wine/%{winepedir}/netapi32.dll
%{_libdir}/wine/%{winepedir}/netcfgx.dll
%{_libdir}/wine/%{winepedir}/netio.sys
%{_libdir}/wine/%{winepedir}/netprofm.dll
%{_libdir}/wine/%{winepedir}/netsh.exe
%{_libdir}/wine/%{winepedir}/netutils.dll
%{_libdir}/wine/%{winepedir}/newdev.dll
%{_libdir}/wine/%{winepedir}/ninput.dll
%{_libdir}/wine/%{winepedir}/normaliz.dll
%{_libdir}/wine/%{winepedir}/npmshtml.dll
%{_libdir}/wine/%{winepedir}/npptools.dll
%{_libdir}/wine/%{winepedir}/nsi.dll
%{_libdir}/wine/%{winesodir}/nsiproxy.so
%{_libdir}/wine/%{winepedir}/nsiproxy.sys
%{_libdir}/wine/%{winesodir}/ntdll.so
%{_libdir}/wine/%{winepedir}/ntdll.dll
%{_libdir}/wine/%{winepedir}/ntdsapi.dll
%{_libdir}/wine/%{winepedir}/ntprint.dll
#%%if 0%%{?wine_staging}
#%%{_libdir}/wine/%%{winepedir}/nvcuda.dll
#%%{_libdir}/wine/%%{winesodir}/nvcuda.dll.so
#%%{_libdir}/wine/%%{winepedir}/nvcuvid.dll
#%%{_libdir}/wine/%%{winesodir}/nvcuvid.dll.so
#%%endif
%{_libdir}/wine/%{winepedir}/objsel.dll
%{_libdir}/wine/%{winesodir}/odbc32.so
%{_libdir}/wine/%{winepedir}/odbc32.dll
%{_libdir}/wine/%{winepedir}/odbcbcp.dll
%{_libdir}/wine/%{winepedir}/odbccp32.dll
%{_libdir}/wine/%{winepedir}/odbccu32.dll
%{_libdir}/wine/%{winepedir}/ole32.dll
%{_libdir}/wine/%{winepedir}/oleacc.dll
%{_libdir}/wine/%{winepedir}/oleaut32.dll
%{_libdir}/wine/%{winepedir}/olecli32.dll
%{_libdir}/wine/%{winepedir}/oledb32.dll
%{_libdir}/wine/%{winepedir}/oledlg.dll
%{_libdir}/wine/%{winepedir}/olepro32.dll
%{_libdir}/wine/%{winepedir}/olesvr32.dll
%{_libdir}/wine/%{winepedir}/olethk32.dll
%{_libdir}/wine/%{winepedir}/opcservices.dll
%{_libdir}/wine/%{winepedir}/packager.dll
%{_libdir}/wine/%{winepedir}/pdh.dll
%{_libdir}/wine/%{winepedir}/photometadatahandler.dll
%{_libdir}/wine/%{winepedir}/pidgen.dll
%{_libdir}/wine/%{winepedir}/powrprof.dll
%{_libdir}/wine/%{winepedir}/presentationfontcache.exe
%{_libdir}/wine/%{winepedir}/printui.dll
%{_libdir}/wine/%{winepedir}/prntvpt.dll
%{_libdir}/wine/%{winepedir}/propsys.dll
%{_libdir}/wine/%{winepedir}/psapi.dll
%{_libdir}/wine/%{winepedir}/pstorec.dll
%{_libdir}/wine/%{winepedir}/pwrshplugin.dll
%{_libdir}/wine/%{winepedir}/qasf.dll
%{_libdir}/wine/%{winepedir}/qcap.dll
%{_libdir}/wine/%{winesodir}/qcap.so
%{_libdir}/wine/%{winepedir}/qdvd.dll
%{_libdir}/wine/%{winepedir}/qedit.dll
%{_libdir}/wine/%{winepedir}/qmgr.dll
%{_libdir}/wine/%{winepedir}/qmgrprxy.dll
%{_libdir}/wine/%{winepedir}/quartz.dll
%{_libdir}/wine/%{winepedir}/query.dll
%{_libdir}/wine/%{winepedir}/qwave.dll
%{_libdir}/wine/%{winepedir}/rasapi32.dll
%{_libdir}/wine/%{winepedir}/rasdlg.dll
%{_libdir}/wine/%{winepedir}/regapi.dll
%{_libdir}/wine/%{winepedir}/regini.exe
%{_libdir}/wine/%{winepedir}/resutils.dll
%{_libdir}/wine/%{winepedir}/riched20.dll
%{_libdir}/wine/%{winepedir}/riched32.dll
%{_libdir}/wine/%{winepedir}/robocopy.exe
%{_libdir}/wine/%{winepedir}/rpcrt4.dll
%{_libdir}/wine/%{winepedir}/rsabase.dll
%{_libdir}/wine/%{winepedir}/rsaenh.dll
%{_libdir}/wine/%{winepedir}/rstrtmgr.dll
%{_libdir}/wine/%{winepedir}/rtutils.dll
%{_libdir}/wine/%{winepedir}/rtworkq.dll
%{_libdir}/wine/%{winepedir}/samlib.dll
%{_libdir}/wine/%{winepedir}/sapi.dll
%{_libdir}/wine/%{winepedir}/sas.dll
%{_libdir}/wine/%{winepedir}/sc.exe
%{_libdir}/wine/%{winepedir}/scarddlg.dll
%{_libdir}/wine/%{winepedir}/scardsvr.dll
%{_libdir}/wine/%{winepedir}/sccbase.dll
%{_libdir}/wine/%{winepedir}/schannel.dll
%{_libdir}/wine/%{winepedir}/scrobj.dll
%{_libdir}/wine/%{winepedir}/scrrun.dll
%{_libdir}/wine/%{winepedir}/scsiport.sys
%{_libdir}/wine/%{winepedir}/sechost.dll
%{_libdir}/wine/%{winepedir}/secur32.dll
%{_libdir}/wine/%{winesodir}/secur32.so
%{_libdir}/wine/%{winepedir}/sensapi.dll
%{_libdir}/wine/%{winepedir}/serialui.dll
%{_libdir}/wine/%{winepedir}/setupapi.dll
%{_libdir}/wine/%{winepedir}/sfc_os.dll
%{_libdir}/wine/%{winepedir}/shcore.dll
%{_libdir}/wine/%{winepedir}/shdoclc.dll
%{_libdir}/wine/%{winepedir}/shdocvw.dll
%{_libdir}/wine/%{winepedir}/schedsvc.dll
%{_libdir}/wine/%{winepedir}/shell32.dll
%{_libdir}/wine/%{winepedir}/shfolder.dll
%{_libdir}/wine/%{winepedir}/shlwapi.dll
%{_libdir}/wine/%{winepedir}/shutdown.exe
%{_libdir}/wine/%{winepedir}/slbcsp.dll
%{_libdir}/wine/%{winepedir}/slc.dll
%{_libdir}/wine/%{winepedir}/snmpapi.dll
%{_libdir}/wine/%{winepedir}/softpub.dll
%{_libdir}/wine/%{winepedir}/spoolsv.exe
%{_libdir}/wine/%{winepedir}/sppc.dll
%{_libdir}/wine/%{winepedir}/srclient.dll
%{_libdir}/wine/%{winepedir}/srvcli.dll
%{_libdir}/wine/%{winepedir}/sspicli.dll
%{_libdir}/wine/%{winepedir}/stdole2.tlb
%{_libdir}/wine/%{winepedir}/stdole32.tlb
%{_libdir}/wine/%{winepedir}/sti.dll
%{_libdir}/wine/%{winepedir}/strmdll.dll
%{_libdir}/wine/%{winepedir}/subst.exe
%{_libdir}/wine/%{winepedir}/svchost.exe
%{_libdir}/wine/%{winepedir}/svrapi.dll
%{_libdir}/wine/%{winepedir}/sxs.dll
%{_libdir}/wine/%{winepedir}/systeminfo.exe
%{_libdir}/wine/%{winepedir}/t2embed.dll
%{_libdir}/wine/%{winepedir}/tapi32.dll
%{_libdir}/wine/%{winepedir}/taskkill.exe
%{_libdir}/wine/%{winepedir}/taskschd.dll
%{_libdir}/wine/%{winepedir}/tbs.dll
%{_libdir}/wine/%{winepedir}/tdh.dll
%{_libdir}/wine/%{winepedir}/tdi.sys
%{_libdir}/wine/%{winepedir}/threadpoolwinrt.dll
%{_libdir}/wine/%{winepedir}/traffic.dll
%{_libdir}/wine/%{winepedir}/twinapi.appcore.dll
%{_libdir}/wine/%{winepedir}/tzres.dll
%{_libdir}/wine/%{winepedir}/ucrtbase.dll
%{_libdir}/wine/%{winepedir}/uianimation.dll
%{_libdir}/wine/%{winepedir}/uiautomationcore.dll
%{_libdir}/wine/%{winepedir}/uiribbon.dll
%{_libdir}/wine/%{winepedir}/unicows.dll
%{_libdir}/wine/%{winepedir}/unlodctr.exe
%{_libdir}/wine/%{winepedir}/updspapi.dll
%{_libdir}/wine/%{winepedir}/url.dll
%{_libdir}/wine/%{winepedir}/urlmon.dll
%{_libdir}/wine/%{winepedir}/usbd.sys
%{_libdir}/wine/%{winepedir}/user32.dll
%{_libdir}/wine/%{winepedir}/usp10.dll
%{_libdir}/wine/%{winepedir}/utildll.dll
%{_libdir}/wine/%{winepedir}/uxtheme.dll
%{_libdir}/wine/%{winepedir}/userenv.dll
%{_libdir}/wine/%{winepedir}/vbscript.dll
%{_libdir}/wine/%{winepedir}/vcomp.dll
%{_libdir}/wine/%{winepedir}/vcomp90.dll
%{_libdir}/wine/%{winepedir}/vcomp100.dll
%{_libdir}/wine/%{winepedir}/vcomp110.dll
%{_libdir}/wine/%{winepedir}/vcomp120.dll
%{_libdir}/wine/%{winepedir}/vcomp140.dll
%{_libdir}/wine/%{winepedir}/vcruntime140.dll
%{_libdir}/wine/%{winepedir}/vcruntime140_1.dll
%{_libdir}/wine/%{winepedir}/vdmdbg.dll
%{_libdir}/wine/%{winepedir}/version.dll
%{_libdir}/wine/%{winepedir}/vga.dll
%{_libdir}/wine/%{winepedir}/virtdisk.dll
%{_libdir}/wine/%{winepedir}/vssapi.dll
%{_libdir}/wine/%{winepedir}/vulkan-1.dll
%{_libdir}/wine/%{winepedir}/wbemdisp.dll
%{_libdir}/wine/%{winepedir}/wbemprox.dll
%{_libdir}/wine/%{winepedir}/wdscore.dll
%{_libdir}/wine/%{winepedir}/webservices.dll
%{_libdir}/wine/%{winepedir}/websocket.dll
%{_libdir}/wine/%{winepedir}/wer.dll
%{_libdir}/wine/%{winepedir}/wevtapi.dll
%{_libdir}/wine/%{winepedir}/wevtsvc.dll
%{_libdir}/wine/%{winepedir}/wiaservc.dll
%{_libdir}/wine/%{winepedir}/wimgapi.dll
%if 0%{?wine_staging}
%{_libdir}/wine/%{winepedir}/win32k.sys
%endif
%{_libdir}/wine/%{winepedir}/win32u.dll
%{_libdir}/wine/%{winepedir}/windows.devices.bluetooth.dll
%{_libdir}/wine/%{winepedir}/windows.devices.enumeration.dll
#%%{_libdir}/wine/%%{winepedir}/windows.devices.geolocation.geolocator.dll
%{_libdir}/wine/%{winepedir}/windows.gaming.ui.gamebar.dll
%{_libdir}/wine/%{winepedir}/windows.gaming.input.dll
%{_libdir}/wine/%{winepedir}/windows.globalization.dll
%{_libdir}/wine/%{winepedir}/windows.media.speech.dll
%{_libdir}/wine/%{winepedir}/windows.media.dll
%{_libdir}/wine/%{winepedir}/windows.media.devices.dll
%if 0%{?wine_staging}
%{_libdir}/wine/%{winepedir}/windows.networking.connectivity
%endif
%{_libdir}/wine/%{winepedir}/windows.networking.dll
%{_libdir}/wine/%{winepedir}/windows.networking.hostname.dll
%{_libdir}/wine/%{winepedir}/windows.perception.stub.dll
%{_libdir}/wine/%{winepedir}/windows.system.profile.systemmanufacturers.dll
%{_libdir}/wine/%{winepedir}/windows.ui.dll
%{_libdir}/wine/%{winepedir}/windowscodecs.dll
%{_libdir}/wine/%{winepedir}/windowscodecsext.dll
%{_libdir}/wine/%{winepedir}/winebus.sys
%{_libdir}/wine/%{winesodir}/winegstreamer.so
%{_libdir}/wine/%{winepedir}/winegstreamer.dll
%{_libdir}/wine/%{winepedir}/winehid.sys
%{_libdir}/wine/%{winepedir}/winemapi.dll
%{_libdir}/wine/%{winepedir}/wineusb.sys
%{_libdir}/wine/%{winesodir}/wineusb.so
%{_libdir}/wine/%{winesodir}/winevulkan.so
%{_libdir}/wine/%{winepedir}/winevulkan.dll
%{_libdir}/wine/%{winepedir}/winewayland.drv
%{_libdir}/wine/%{winesodir}/winewayland.so
%{_libdir}/wine/%{winepedir}/winex11.drv
%{_libdir}/wine/%{winesodir}/winex11.so
%{_libdir}/wine/%{winepedir}/wing32.dll
%{_libdir}/wine/%{winepedir}/winhttp.dll
%{_libdir}/wine/%{winepedir}/wininet.dll
%{_libdir}/wine/%{winepedir}/winmm.dll
%{_libdir}/wine/%{winepedir}/winnls32.dll
%{_libdir}/wine/%{winepedir}/winprint.dll
%{_libdir}/wine/%{winepedir}/winspool.drv
%{_libdir}/wine/%{winesodir}/winspool.so
%{_libdir}/wine/%{winepedir}/winsta.dll
%{_libdir}/wine/%{winepedir}/wintypes.dll
%{_libdir}/wine/%{winepedir}/wmasf.dll
%{_libdir}/wine/%{winepedir}/wmi.dll
%{_libdir}/wine/%{winepedir}/wmic.exe
%{_libdir}/wine/%{winepedir}/wmiutils.dll
%{_libdir}/wine/%{winepedir}/wmp.dll
%{_libdir}/wine/%{winepedir}/wmvcore.dll
%{_libdir}/wine/%{winepedir}/spoolss.dll
%{_libdir}/wine/%{winesodir}/win32u.so
%{_libdir}/wine/%{winesodir}/winebus.so
%{_libdir}/wine/%{winepedir}/winexinput.sys
%{_libdir}/wine/%{winepedir}/wintab32.dll
%{_libdir}/wine/%{winepedir}/wintrust.dll
%{_libdir}/wine/%{winepedir}/winusb.dll
%{_libdir}/wine/%{winepedir}/wlanapi.dll
%{_libdir}/wine/%{winepedir}/wlanui.dll
%{_libdir}/wine/%{winepedir}/wmphoto.dll
%{_libdir}/wine/%{winepedir}/wnaspi32.dll
%{_libdir}/wine/%{winepedir}/wofutil.dll
%ifarch x86_64 aarch64
%{_libdir}/wine/%{winepedir}/wow64.dll
%{_libdir}/wine/%{winepedir}/wow64win.dll
%endif
%ifarch x86_64
%{_libdir}/wine/%{winepedir}/wow64cpu.dll
%endif
%{_libdir}/wine/%{winepedir}/wpc.dll
%{_libdir}/wine/%{winepedir}/wpcap.dll
%{_libdir}/wine/%{winesodir}/wpcap.so
%{_libdir}/wine/%{winepedir}/ws2_32.dll
%{_libdir}/wine/%{winesodir}/ws2_32.so
%{_libdir}/wine/%{winepedir}/wsdapi.dll
%{_libdir}/wine/%{winepedir}/wshom.ocx
%{_libdir}/wine/%{winepedir}/wsnmp32.dll
%{_libdir}/wine/%{winepedir}/wsock32.dll
%{_libdir}/wine/%{winepedir}/wtsapi32.dll
%{_libdir}/wine/%{winepedir}/wuapi.dll
%{_libdir}/wine/%{winepedir}/wuaueng.dll
%{_libdir}/wine/%{winepedir}/wuauserv.exe
%ifarch %{arm}
%{_libdir}/wine/%{winesodir}/wuauserv.exe.so
%endif
%{_libdir}/wine/%{winepedir}/security.dll
%{_libdir}/wine/%{winepedir}/sfc.dll
%{_libdir}/wine/%{winepedir}/wineps.drv
%{_libdir}/wine/%{winesodir}/wineps.so
%{_libdir}/wine/%{winepedir}/d3d8.dll
%{_libdir}/wine/%{winepedir}/d3d8thk.dll

# DISABLE FOR DXVK
#%%ghost %%{_libdir}/wine/%%{winepedir}/d3d9.dll
#%%{_libdir}/wine/%%{winepedir}/wine-d3d9.dll
%{_libdir}/wine/%{winepedir}/d3d9.dll
# END DXVK

%{_libdir}/wine/%{winepedir}/opengl32.dll
%{_libdir}/wine/%{winesodir}/opengl32.so
%{_libdir}/wine/%{winepedir}/wined3d.dll
%{_libdir}/wine/%{winepedir}/dnsapi.dll
%{_libdir}/wine/%{winesodir}/dnsapi.so
%{_libdir}/wine/%{winepedir}/iexplore.exe
%{_libdir}/wine/%{winepedir}/x3daudio1_0.dll
%{_libdir}/wine/%{winepedir}/x3daudio1_1.dll
%{_libdir}/wine/%{winepedir}/x3daudio1_2.dll
%{_libdir}/wine/%{winepedir}/x3daudio1_3.dll
%{_libdir}/wine/%{winepedir}/x3daudio1_4.dll
%{_libdir}/wine/%{winepedir}/x3daudio1_5.dll
%{_libdir}/wine/%{winepedir}/x3daudio1_6.dll
%{_libdir}/wine/%{winepedir}/x3daudio1_7.dll
%{_libdir}/wine/%{winepedir}/xactengine2_0.dll
%{_libdir}/wine/%{winepedir}/xactengine2_4.dll
%{_libdir}/wine/%{winepedir}/xactengine2_7.dll
%{_libdir}/wine/%{winepedir}/xactengine2_9.dll
%{_libdir}/wine/%{winepedir}/xactengine3_0.dll
%{_libdir}/wine/%{winepedir}/xactengine3_1.dll
%{_libdir}/wine/%{winepedir}/xactengine3_2.dll
%{_libdir}/wine/%{winepedir}/xactengine3_3.dll
%{_libdir}/wine/%{winepedir}/xactengine3_4.dll
%{_libdir}/wine/%{winepedir}/xactengine3_5.dll
%{_libdir}/wine/%{winepedir}/xactengine3_6.dll
%{_libdir}/wine/%{winepedir}/xactengine3_7.dll
%{_libdir}/wine/%{winepedir}/xapofx1_1.dll
%{_libdir}/wine/%{winepedir}/xapofx1_2.dll
%{_libdir}/wine/%{winepedir}/xapofx1_3.dll
%{_libdir}/wine/%{winepedir}/xapofx1_4.dll
%{_libdir}/wine/%{winepedir}/xapofx1_5.dll
%{_libdir}/wine/%{winepedir}/xaudio2_0.dll
%{_libdir}/wine/%{winepedir}/xaudio2_1.dll
%{_libdir}/wine/%{winepedir}/xaudio2_2.dll
%{_libdir}/wine/%{winepedir}/xaudio2_3.dll
%{_libdir}/wine/%{winepedir}/xaudio2_4.dll
%{_libdir}/wine/%{winepedir}/xaudio2_5.dll
%{_libdir}/wine/%{winepedir}/xaudio2_6.dll
%{_libdir}/wine/%{winepedir}/xaudio2_7.dll
%{_libdir}/wine/%{winepedir}/xaudio2_8.dll
%{_libdir}/wine/%{winepedir}/xaudio2_9.dll
%{_libdir}/wine/%{winepedir}/xcopy.exe
%{_libdir}/wine/%{winepedir}/xinputuap.dll
%{_libdir}/wine/%{winepedir}/xinput1_1.dll
%{_libdir}/wine/%{winepedir}/xinput1_2.dll
%{_libdir}/wine/%{winepedir}/xinput1_3.dll
%{_libdir}/wine/%{winepedir}/xinput1_4.dll
%{_libdir}/wine/%{winepedir}/xinput9_1_0.dll
%{_libdir}/wine/%{winepedir}/xmllite.dll
%{_libdir}/wine/%{winepedir}/xolehlp.dll
%{_libdir}/wine/%{winepedir}/xpsprint.dll
%{_libdir}/wine/%{winepedir}/xpssvcs.dll

#%%if 0%%{?wine_staging}
#%%ifarch x86_64 aarch64
#%%{_libdir}/wine/%%{winepedir}/nvapi64.dll
#%%{_libdir}/wine/%%{winepedir}/nvencodeapi64.dll
#%%{_libdir}/wine/%%{winesodir}/nvencodeapi64.dll.so
#%%else
#%%{_libdir}/wine/%%{winepedir}/nvapi.dll
#%%ifarch %%{arm}
#%%{_libdir}/wine/%%{winesodir}/nvapi.dll.so
#%%endif
#%%{_libdir}/wine/%%{winepedir}/nvencodeapi.dll
#%%{_libdir}/wine/%%{winesodir}/nvencodeapi.dll.so
#%%endif
#%%endif

# 16 bit and other non 64bit stuff
%ifnarch x86_64 %{arm} aarch64
%{_libdir}/wine/%{winepedir}/winevdm.exe
%{_libdir}/wine/%{winepedir}/ifsmgr.vxd
%{_libdir}/wine/%{winepedir}/mmdevldr.vxd
%{_libdir}/wine/%{winepedir}/monodebg.vxd
%{_libdir}/wine/%{winepedir}/rundll.exe16
%{_libdir}/wine/%{winepedir}/vdhcp.vxd
%{_libdir}/wine/%{winepedir}/user.exe16
%{_libdir}/wine/%{winepedir}/vmm.vxd
%{_libdir}/wine/%{winepedir}/vnbt.vxd
%{_libdir}/wine/%{winepedir}/vnetbios.vxd
%{_libdir}/wine/%{winepedir}/vtdapi.vxd
%{_libdir}/wine/%{winepedir}/vwin32.vxd
%{_libdir}/wine/%{winepedir}/w32skrnl.dll
%{_libdir}/wine/%{winepedir}/avifile.dll16
%{_libdir}/wine/%{winepedir}/comm.drv16
%{_libdir}/wine/%{winepedir}/commdlg.dll16
%{_libdir}/wine/%{winepedir}/compobj.dll16
%{_libdir}/wine/%{winepedir}/ctl3d.dll16
%{_libdir}/wine/%{winepedir}/ctl3dv2.dll16
%{_libdir}/wine/%{winepedir}/ddeml.dll16
%{_libdir}/wine/%{winepedir}/dispdib.dll16
%{_libdir}/wine/%{winepedir}/display.drv16
%{_libdir}/wine/%{winepedir}/gdi.exe16
%{_libdir}/wine/%{winepedir}/imm.dll16
%{_libdir}/wine/%{winepedir}/krnl386.exe16
%{_libdir}/wine/%{winepedir}/keyboard.drv16
%{_libdir}/wine/%{winepedir}/lzexpand.dll16
%{_libdir}/wine/%{winepedir}/mmsystem.dll16
%{_libdir}/wine/%{winepedir}/mouse.drv16
%{_libdir}/wine/%{winepedir}/msacm.dll16
%{_libdir}/wine/%{winepedir}/msvideo.dll16
%{_libdir}/wine/%{winepedir}/ole2.dll16
%{_libdir}/wine/%{winepedir}/ole2conv.dll16
%{_libdir}/wine/%{winepedir}/ole2disp.dll16
%{_libdir}/wine/%{winepedir}/ole2nls.dll16
%{_libdir}/wine/%{winepedir}/ole2prox.dll16
%{_libdir}/wine/%{winepedir}/ole2thk.dll16
%{_libdir}/wine/%{winepedir}/olecli.dll16
%{_libdir}/wine/%{winepedir}/olesvr.dll16
%{_libdir}/wine/%{winepedir}/rasapi16.dll16
%{_libdir}/wine/%{winepedir}/setupx.dll16
%{_libdir}/wine/%{winepedir}/shell.dll16
%{_libdir}/wine/%{winepedir}/sound.drv16
%{_libdir}/wine/%{winepedir}/storage.dll16
%{_libdir}/wine/%{winepedir}/stress.dll16
%{_libdir}/wine/%{winepedir}/system.drv16
%{_libdir}/wine/%{winepedir}/toolhelp.dll16
%{_libdir}/wine/%{winepedir}/twain.dll16
%{_libdir}/wine/%{winepedir}/typelib.dll16
%{_libdir}/wine/%{winepedir}/ver.dll16
%{_libdir}/wine/%{winepedir}/w32sys.dll16
%{_libdir}/wine/%{winepedir}/win32s16.dll16
%{_libdir}/wine/%{winepedir}/win87em.dll16
%{_libdir}/wine/%{winepedir}/winaspi.dll16
%{_libdir}/wine/%{winepedir}/windebug.dll16
%{_libdir}/wine/%{winepedir}/wineps16.drv16
%{_libdir}/wine/%{winepedir}/wing.dll16
%{_libdir}/wine/%{winepedir}/winhelp.exe16
%{_libdir}/wine/%{winepedir}/winnls.dll16
%{_libdir}/wine/%{winepedir}/winoldap.mod16
%{_libdir}/wine/%{winepedir}/winsock.dll16
%{_libdir}/wine/%{winepedir}/wintab.dll16
%{_libdir}/wine/%{winepedir}/wow32.dll
%endif

%files filesystem
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%dir %{_datadir}/wine
%dir %{_datadir}/wine/gecko
%dir %{_datadir}/wine/mono
%dir %{_datadir}/wine/fonts
%{_datadir}/wine/wine.inf
%{_datadir}/wine/nls/

%files common
%{_bindir}/notepad
%{_bindir}/winedbg
%{_bindir}/winefile
%{_bindir}/winemine
%{_bindir}/winemaker
%{_bindir}/winepath
%{_bindir}/msiexec
%{_bindir}/regedit
%{_bindir}/regsvr32
%{_bindir}/wineboot
%{_bindir}/wineconsole
%{_bindir}/winecfg
%{_mandir}/man1/wine.1*
%{_mandir}/man1/wineserver.1*
%{_mandir}/man1/msiexec.1*
%{_mandir}/man1/notepad.1*
%{_mandir}/man1/regedit.1*
%{_mandir}/man1/regsvr32.1*
%{_mandir}/man1/wineboot.1*
%{_mandir}/man1/winecfg.1*
%{_mandir}/man1/wineconsole.1*
%{_mandir}/man1/winefile.1*
%{_mandir}/man1/winemine.1*
%{_mandir}/man1/winepath.1*
%lang(de) %{_mandir}/de.UTF-8/man1/wine.1*
%lang(de) %{_mandir}/de.UTF-8/man1/wineserver.1*
%lang(fr) %{_mandir}/fr.UTF-8/man1/wine.1*
%lang(fr) %{_mandir}/fr.UTF-8/man1/wineserver.1*
%lang(pl) %{_mandir}/pl.UTF-8/man1/wine.1*

%files fonts
# meta package

%if 0%{?wine_staging}
%files arial-fonts
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%{_datadir}/wine/fonts/arial*
%endif
#0%%{?wine_staging}

%files courier-fonts
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%{_datadir}/wine/fonts/cou*

%files fixedsys-fonts
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%{_datadir}/wine/fonts/*vgafix.fon

%files system-fonts
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%{_datadir}/wine/fonts/cvgasys.fon
%{_datadir}/wine/fonts/hvgasys.fon
%{_datadir}/wine/fonts/jvgasys.fon
%{_datadir}/wine/fonts/svgasys.fon
%{_datadir}/wine/fonts/vgas1255.fon
%{_datadir}/wine/fonts/vgas1256.fon
%{_datadir}/wine/fonts/vgas1257.fon
%{_datadir}/wine/fonts/vgas874.fon
%{_datadir}/wine/fonts/vgasys.fon
%{_datadir}/wine/fonts/vgasyse.fon
%{_datadir}/wine/fonts/vgasysg.fon
%{_datadir}/wine/fonts/vgasysr.fon
%{_datadir}/wine/fonts/vgasyst.fon

%files small-fonts
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%{_datadir}/wine/fonts/sma*
%{_datadir}/wine/fonts/jsma*

%files marlett-fonts
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%{_datadir}/wine/fonts/marlett.ttf

%files ms-sans-serif-fonts
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%{_datadir}/wine/fonts/sse*
%if 0%{?wine_staging}
%{_datadir}/wine/fonts/msyh.ttf
%endif

%files tahoma-fonts
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%{_datadir}/wine/fonts/tahoma*ttf

%files tahoma-fonts-system
%doc %{?wine_tkg:wine-tkg-src/}README-tahoma
%{_datadir}/fonts/wine-tahoma-fonts
%{_fontconfig_confdir}/20-wine-tahoma*conf
%{_fontconfig_templatedir}/20-wine-tahoma*conf

%if 0%{?wine_staging}
%files times-new-roman-fonts
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%{_datadir}/wine/fonts/times.ttf

%files times-new-roman-fonts-system
%{_datadir}/fonts/wine-times-new-roman-fonts
%endif

%files symbol-fonts
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%{_datadir}/wine/fonts/symbol.ttf

%files webdings-fonts
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%{_datadir}/wine/fonts/webdings.ttf

%files wingdings-fonts
%doc %{?wine_tkg:wine-tkg-src/}COPYING.LIB
%{_datadir}/wine/fonts/wingding.ttf

%files wingdings-fonts-system
%{_datadir}/fonts/wine-wingdings-fonts

%files desktop
%{_datadir}/applications/wine-notepad.desktop
%{_datadir}/applications/wine-winefile.desktop
%{_datadir}/applications/wine-winemine.desktop
%{_datadir}/applications/wine-mime-msi.desktop
%{_datadir}/applications/wine.desktop
%{_datadir}/applications/wine-regedit.desktop
%{_datadir}/applications/wine-uninstaller.desktop
%{_datadir}/applications/wine-winecfg.desktop
%{_datadir}/applications/wine-wineboot.desktop
%{_datadir}/applications/wine-winhelp.desktop
%{_datadir}/applications/wine-wordpad.desktop
%{_datadir}/applications/wine-oleview.desktop
%{_datadir}/desktop-directories/Wine.directory
%config %{_sysconfdir}/xdg/menus/applications-merged/wine.menu
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/*svg

%files systemd
%config %{_binfmtdir}/wine.conf

# ldap subpackage
%files ldap
#%%{_libdir}/wine/%%{winesodir}/wldap32.so
%{_libdir}/wine/%{winepedir}/wldap32.dll
%ifarch %{arm}
%{_libdir}/wine/%{winesodir}/wldap32.dll.so
%endif

# cms subpackage
%files cms
%{_libdir}/wine/%{winepedir}/mscms.dll
%ifarch %{arm}
%{_libdir}/wine/%{winesodir}/mscms.dll.so
%endif

# twain subpackage
%files twain
%{_libdir}/wine/%{winepedir}/twain_32.dll
%ifarch %{arm}
%{_libdir}/wine/%{winesodir}/twain_32.dll.so
%endif
%{_libdir}/wine/%{winepedir}/sane.ds
%ifarch %{arm}
%{_libdir}/wine/%{winesodir}/sane.ds.so
%endif
%{_libdir}/wine/%{winesodir}/sane.so

%files devel
%{_bindir}/function_grep.pl
%{_bindir}/widl
%{_bindir}/winebuild
%{_bindir}/winecpp
%{_bindir}/winedump
%{_bindir}/wineg++
%{_bindir}/winegcc
%{_bindir}/winemaker
%{_bindir}/wmc
%{_bindir}/wrc
%{_mandir}/man1/widl.1*
%{_mandir}/man1/winebuild.1*
%{_mandir}/man1/winecpp.1*
%{_mandir}/man1/winedump.1*
%{_mandir}/man1/winegcc.1*
%{_mandir}/man1/winemaker.1*
%{_mandir}/man1/wmc.1*
%{_mandir}/man1/wrc.1*
%{_mandir}/man1/winedbg.1*
%{_mandir}/man1/wineg++.1*
%lang(de) %{_mandir}/de.UTF-8/man1/winemaker.1*
%lang(fr) %{_mandir}/fr.UTF-8/man1/winemaker.1*
%attr(0755, root, root) %dir %{_includedir}/wine
%{_includedir}/wine/*
%ifarch %{ix86} x86_64 aarch64
%{_libdir}/wine/%{winepedir}/*.a
%endif
%ifarch %{ix86} x86_64
%{_libdir}/wine/%{winesodir}/*.a
%endif

%files pulseaudio
%{_libdir}/wine/%{winepedir}/winepulse.drv
%{_libdir}/wine/%{winesodir}/winepulse.so
%ifarch %{arm}
%{_libdir}/wine/%{winesodir}/winepulse.drv.so
%endif

%files alsa
%{_libdir}/wine/%{winepedir}/winealsa.drv
%{_libdir}/wine/%{winesodir}/winealsa.so
%ifarch %{arm}
%{_libdir}/wine/%{winesodir}/winealsa.drv.so
%endif

#%%if 0%%{?fedora} >= 10 || 0%%{?rhel} >= 6
#%%files openal
#%%{_libdir}/wine/%%{winepedir}/openal32.dll
#%%{_libdir}/wine/%%{winesodir}/openal32.dll.so
#%%endif

%if 0%{?fedora}
%files opencl
%{_libdir}/wine/%{winepedir}/opencl.dll
%ifarch %{arm}
%{_libdir}/wine/%{winesodir}/opencl.dll.so
%endif
%{_libdir}/wine/%{winesodir}/opencl.so
%endif

#%%files widl
#%%{_bindir}/widl
#%%{_mandir}/man1/widl.1*


%changelog
* Sun Jul 23 2023 Patrick Laimbock <patrick@laimbock.com> - 8.13-10
- update to version 8.13

* Thu Jul 20 2023 Patrick Laimbock <patrick@laimbock.com> - 8.12.-14
- enable childwindow patch again

* Mon Jul 17 2023 Patrick Laimbock <patrick@laimbock.com> - 8.12.-13
- test build: disable childwindow patch

* Mon Jul 17 2023 Patrick Laimbock <patrick@laimbock.com> - 8.12.-12
- remove more lingering alternatives logic
- prevent alternatives removal from failing

* Mon Jul 17 2023 Patrick Laimbock <patrick@laimbock.com> - 8.12.-11
- add 710eec8fac7952679e2ddb4eba54367b50c47930.patch

* Sun Jul 09 2023 Patrick Laimbock <patrick@laimbock.com> - 8.12-10
- update to version 8.12

* Sat Jul 01 2023 Patrick Laimbock <patrick@laimbock.com> - 8.11-10
* Sat Jul 01 2023 Patrick Laimbock <patrick@laimbock.com> - 8.11-10
- update to version 8.11
- build against wine-mono-8.0.0
- build against vkd3d-1.8

* Sun Jun 11 2023 Patrick Laimbock <patrick@laimbock.com> - 8.10-10
- update to version 8.10

* Mon May 15 2023 Patrick Laimbock <patrick@laimbock.com> - 8.8-12
- disable the GloriousEggroll game patches
- disable steam.patch
- disable Return_nt_filename_and_resolve_DOS_drive_path.mypatch
- disable nostale_mouse_fix.mypatch

* Mon May 15 2023 Patrick Laimbock <patrick@laimbock.com> - 8.8-11
- use properly tagged source for wine-staging
- set game related options to false in customization-8.8

* Sat May 13 2023 Patrick Laimbock <patrick@laimbock.com> - 8.8-10
- update to version 8.8

* Wed May 03 2023 Patrick Laimbock <patrick@laimbock.com> - 8.7-11
- rebuild against wine-gecko-2.47.3

* Wed Apr 19 2023 Patrick Laimbock <patrick@laimbock.com> - 8.7-10
- update to wine(-staging)-8.7
- build against wine-gecko 2.47.4

* Wed Apr 19 2023 Patrick Laimbock <patrick@laimbock.com> - 8.6-11
- update to wine-8.6 and wine-staging-8.6.1
- require winegecko 2.47.3 due to https://bugs.winehq.org/show_bug.cgi?id=53400
- sync with wine.spec on koji
- remove separate wine-widl subpackage, just use wine-devel for widl

* Sat Apr 01 2023 Patrick Laimbock <patrick@laimbock.com> - 8.5-10
- update to wine-8.5
- temporarily remove wine-tkg-patches/hotfixes/ow2
- see https://github.com/Frogging-Family/wine-tkg-git/issues/979

* Thu Mar 30 2023 Patrick Laimbock <patrick@laimbock.com> - 8.4-10
- update to wine-8.4
- build against vkd3d-1.7

* Wed Feb 22 2023 Patrick Laimbock <patrick@laimbock.com> - 8.2-10
- update to wine-8.2

* Tue Feb 07 2023 Patrick Laimbock <patrick@laimbock.com> - 8.1-10
- update to wine-8.1

* Wed Jan 25 2023 Patrick Laimbock <patrick@laimbock.com> - 8.0-10
- update to wine-8.0

* Sun Jan 22 2023 Patrick Laimbock <patrick@laimbock.com> - 8.0-0.7
- build against latest vkd3d

* Sun Jan 22 2023 Patrick Laimbock <patrick@laimbock.com> - 8.0-0.6
- update to 8.0-rc5

* Mon Jan 16 2023 Patrick Laimbock <patrick@laimbock.com> - 8.0-0.5
- update to 8.0-rc4

* Sun Jan 08 2023 Patrick Laimbock <patrick@laimbock.com> - 8.0-0.4
- add libgcrypt-devel and libXpresent to BRs

* Sun Jan 08 2023 Patrick Laimbock <patrick@laimbock.com> - 8.0-0.3
- update to 8.0-rc3

* Mon Dec 26 2022 Patrick Laimbock <patrick@laimbock.com> - 8.0-0.2
- rebuild against vkd3d-1.6-1

* Mon Dec 26 2022 Patrick Laimbock <patrick@laimbock.com> - 8.0-0.1
- update to version 8.0-rc2
- require vkd3d-1.6

* Fri Nov 18 2022 Patrick Laimbock <patrick@laimbock.com> - 7.20-11
- bootstrap build against vkd3d-1.5

* Wed Nov 02 2022 Patrick Laimbock <patrick@laimbock.com> - 7.20-10
- update to version 7.20
- require winemono 7.4.0

* Sat Oct 01 2022 Patrick Laimbock <patrick@laimbock.com> - 7.18-10
- update to version 7.18
- set _LOCAL_PRESET="default-tkg"
- require vkd3d >= 1.5

* Sat Sep 10 2022 Patrick Laimbock <patrick@laimbock.com> - 7.17-10
- update to version 7.17
- disable _proton_battleye_support and _proton_eac_support in customization.cfg

* Sun Aug 28 2022 Patrick Laimbock <patrick@laimbock.com> - 7.16-10
- update to version 7.16

* Sun Aug 14 2022 Patrick Laimbock <patrick@laimbock.com> - 7.15-10
- update to version 7.15

* Sat Jul 30 2022 Patrick Laimbock <patrick@laimbock.com> - 7.14-10
- update to version 7.14

* Wed Jul 20 2022 Patrick Laimbock <patrick@laimbock.com> - 7.13-12
- add logic to build a wine_tkg version

* Sun Jul 17 2022 Patrick Laimbock <patrick@laimbock.com> - 7.13-11
- also build and package widl (needed to build external vkd3d)
- add mingw{32,64}-vkd3d requires

* Sat Jul 16 2022 Patrick Laimbock <patrick@laimbock.com> - 7.13-10
- update to version 7.13
- remove global _smp_mflags -j1 as parallel builds seem to work
- update wine-gecko version to 2.47.3
- remove lowlatency_audio_pulse_rebased.patch
- in files section remove {_libdir}/wine/{winesodir}/wineusb.sys.so
- in files section add {_libdir}/wine/{winepedir}/msvcp140_2.dll

* Sat Jul 09 2022 Patrick Laimbock <patrick@laimbock.com> - 7.12-10
- add several patches from wine-tkg aimed at music production
- add robocopy patches

* Tue Jul 05 2022 Michael Cronenworth <mike@cchtml.com> - 7.12-1
- versuon update
- Unbundle vkd3d

* Wed Jun 22 2022 Michael Cronenworth <mike@cchtml.com> - 7.11-1
- version update

* Mon Jun 06 2022 Michael Cronenworth <mike@cchtml.com> - 7.10-2
- Require new Mono

* Mon Jun 06 2022 Michael Cronenworth <mike@cchtml.com> - 7.10-1
- version update

* Mon May 23 2022 Michael Cronenworth <mike@cchtml.com> - 7.9-1
- version update

* Tue Mar 29 2022 Michael Cronenworth <mike@cchtml.com> - 7.5-1
- version update
- drop 32-bit ARM
- require on Fedora MinGW dependencies

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 7.3-2
- Rebuild with mingw-gcc-12

* Fri Mar 11 2022 Michael Cronenworth <mike@cchtml.com> - 7.3-1
- version update

* Sun Feb 13 2022 Björn Esser <besser82@fedoraproject.org> - 7.2-1
- version update

* Mon Jan 31 2022 Björn Esser <besser82@fedoraproject.org> - 7.1-2
- Revert to wine-mono 7.0.0

* Sat Jan 29 2022 Björn Esser <besser82@fedoraproject.org> - 7.1-1
- version update

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Björn Esser <besser82@fedoraproject.org> - 7.0-1
- version update

* Sat Jan 15 2022 Björn Esser <besser82@fedoraproject.org> - 7.0-0.6rc6
- version update

* Sun Jan 09 2022 Björn Esser <besser82@fedoraproject.org> - 7.0-0.5rc5
- version update

* Mon Jan 03 2022 Michael Cronenworth <mike@cchtml.com> 7.0-0.4rc4
- version update

* Mon Jan 03 2022 FeRD (Frank Dana) <ferdnyc@gmail.com> 7.0-0.3rc3
- Silence messages from expected failures during rpm scriptlets

* Mon Dec 27 2021 Björn Esser <besser82@fedoraproject.org> - 7.0-0.2rc3
- version update

* Mon Dec 20 2021 Michael Cronenworth <mike@cchtml.com> 7.0-0.1rc2
- version update

* Wed Nov 10 2021 Michael Cronenworth <mike@cchtml.com> 6.21-1
- version update

* Mon Oct 04 2021 Michael Cronenworth <mike@cchtml.com> 6.18-1
- version update

* Mon Aug 30 2021 Michael Cronenworth <mike@cchtml.com> 6.16-1
- version update

* Wed Jul 07 2021 Michael Cronenworth <mike@cchtml.com> 6.12-1
- version update

* Sat Jun 19 2021 Michael Cronenworth <mike@cchtml.com> 6.11-1
- version update

* Mon Jun 07 2021 Michael Cronenworth <mike@cchtml.com> 6.10-1
- version update

* Mon May 24 2021 Michael Cronenworth <mike@cchtml.com> 6.9-1
- version update

* Sat May 08 2021 Michael Cronenworth <mike@cchtml.com> 6.8-1
- version update

* Sat Apr 24 2021 Michael Cronenworth <mike@cchtml.com> 6.7-1
- version update

* Sun Apr 11 2021 Michael Cronenworth <mike@cchtml.com> 6.6-1
- version update

* Mon Mar 15 2021 Michael Cronenworth <mike@cchtml.com> 6.4-1
- version update

* Sat Feb 27 2021 Michael Cronenworth <mike@cchtml.com> 6.3-1
- version update

* Sat Feb 13 2021 Michael Cronenworth <mike@cchtml.com> 6.2-1
- version update

* Mon Feb 01 2021 Michael Cronenworth <mike@cchtml.com> 6.1-1
- version update

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Michael Cronenworth <mike@cchtml.com> 6.0-1
- version update

* Sun Jan 10 2021 Michael Cronenworth <mike@cchtml.com> 6.0-0.6rc6
- version update

* Thu Jan 07 2021 Michael Cronenworth <mike@cchtml.com> 6.0-0.5rc5
- version update

* Sat Dec 26 2020 Michael Cronenworth <mike@cchtml.com> 6.0-0.4rc4
- version update

* Sat Dec 19 2020 Michael Cronenworth <mike@cchtml.com> 6.0-0.3rc3
- version update

* Sat Dec 12 2020 Michael Cronenworth <mike@cchtml.com> 6.0-0.2rc2
- version update

* Tue Dec 08 2020 Michael Cronenworth <mike@cchtml.com> 6.0-0.1rc1
- version update

* Sat Nov 21 2020 Michael Cronenworth <mike@cchtml.com> 5.22-1
- version update

* Tue Nov 10 2020 Michael Cronenworth <mike@cchtml.com> 5.21-1
- version update

* Sat Oct 24 2020 Michael Cronenworth <mike@cchtml.com> 5.20-1
- version update

* Sat Oct 10 2020 Michael Cronenworth <mike@cchtml.com> 5.19-1
- version update

* Mon Sep 28 2020 Michael Cronenworth <mike@cchtml.com> 5.18-2
- Enable vkd3d shader support

* Mon Sep 28 2020 Michael Cronenworth <mike@cchtml.com> 5.18-1
- version update

* Tue Sep 15 2020 Michael Cronenworth <mike@cchtml.com> 5.17-1
- version update

* Tue Sep 01 2020 Michael Cronenworth <mike@cchtml.com> 5.16-1
- version update

* Sun Aug 16 2020 Michael Cronenworth <mike@cchtml.com> 5.15-1
- version update

* Mon Aug 10 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.14-2
- Recommend wine-dxvk as part of https://fedoraproject.org/wiki/Changes/DXVKwined3d

* Mon Aug 03 2020 Michael Cronenworth <mike@cchtml.com> 5.14-1
- version update

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Michael Cronenworth <mike@cchtml.com> 5.13-1
- version update

* Tue Jul 14 2020 Michael Cronenworth <mike@cchtml.com> 5.12-1
- version update

* Wed Jul 01 2020 Jeff Law <law@redhat.com> 5.10-2
- Disable LTO

* Sun Jun 07 2020 Michael Cronenworth <mike@cchtml.com> 5.10-1
- version update

* Tue Jun 02 2020 Michael Cronenworth <mike@cchtml.com> 5.9-2
- drop typelibs from 32-bit devel package
- add patch for wine bug 49208

* Fri May 29 2020 Michael Cronenworth <mike@cchtml.com> 5.9-1
- version update

* Sat May 02 2020 Michael Cronenworth <mike@cchtml.com> 5.7-2
- fix crash in wineserver affecting many apps and games (RHBZ#1829956)

* Sun Apr 26 2020 Michael Cronenworth <mike@cchtml.com> 5.7-1
- version update

* Sat Apr 11 2020 Michael Cronenworth <mike@cchtml.com> 5.6-1
- version update

* Sun Mar 29 2020 Michael Cronenworth <mike@cchtml.com> 5.5-1
- version update

* Mon Mar 16 2020 Michael Cronenworth <mike@cchtml.com> 5.4-1
- version update

* Mon Mar 02 2020 Michael Cronenworth <mike@cchtml.com> 5.3-1
- version update

* Tue Feb 18 2020 Michael Cronenworth <mike@cchtml.com> 5.2-1
- version update

* Mon Feb 03 2020 Michael Cronenworth <mike@cchtml.com> 5.1-1
- version update

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Michael Cronenworth <mike@cchtml.com> 5.0-1
- version update

* Mon Jan 13 2020 Michael Cronenworth <mike@cchtml.com> 5.0-0.rc5.0
- version update

* Mon Jan 06 2020 Michael Cronenworth <mike@cchtml.com> 5.0-0.rc4.0
- version update

* Mon Dec 30 2019 Michael Cronenworth <mike@cchtml.com> 5.0-0.rc3.0
- version update

* Sat Nov 30 2019 Michael Cronenworth <mike@cchtml.com> 4.21-1
- version update

* Sat Nov 16 2019 Michael Cronenworth <mike@cchtml.com> 4.20-1
- version and wine-mono update

* Sat Nov 02 2019 Michael Cronenworth <mike@cchtml.com> 4.19-1
- version update

* Mon Oct 21 2019 Michael Cronenworth <mike@cchtml.com> 4.18-1
- version update

* Sun Sep 29 2019 Michael Cronenworth <mike@cchtml.com> 4.17-2
- sync wine-mono version

* Sat Sep 28 2019 Michael Cronenworth <mike@cchtml.com> 4.17-1
- version update

* Thu Sep 26 2019 Michael Cronenworth <mike@cchtml.com> 4.16-2
- Drop isdn4k-utils BR (RHBZ#1756118)

* Sat Sep 14 2019 Michael Cronenworth <mike@cchtml.com> 4.16-1
- version update

* Sun Sep 01 2019 Michael Cronenworth <mike@cchtml.com> 4.15-1
- version update

* Mon Aug 19 2019 Michael Cronenworth <mike@cchtml.com> 4.14-2
- sync wine-mono version

* Mon Aug 19 2019 Michael Cronenworth <mike@cchtml.com> 4.14-1
- version update

* Sun Aug 11 2019 Michael Cronenworth <mike@cchtml.com> 4.13-5
- remove correct dlls on upgrade

* Thu Aug 08 2019 Michael Cronenworth <mike@cchtml.com> 4.13-4
- support upgrades in new alternatives

* Wed Aug 07 2019 Michael Cronenworth <mike@cchtml.com> 4.13-3
- fix slave alternatives for d3d dlls

* Mon Aug 05 2019 Michael Cronenworth <mike@cchtml.com> 4.13-2
- fix alternatives for d3d dlls

* Sun Aug 04 2019 Michael Cronenworth <mike@cchtml.com> 4.13-1
- version update
- add alternatives for d3d dlls to play with dxvk

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Michael Cronenworth <mike@cchtml.com> 4.12.1-1
- version update

* Sun Jun 23 2019 Michael Cronenworth <mike@cchtml.com> 4.11-1
- version update

* Thu Jun 13 2019 Michael Cronenworth <mike@cchtml.com> 4.10-1
- version update
- compile with MinGW support

* Sun May 26 2019 Michael Cronenworth <mike@cchtml.com> 4.9-1
- version update

* Wed May 15 2019 Michael Cronenworth <mike@cchtml.com> 4.8-2
- Fix default wine svg (RHBZ#1598994)

* Tue May 14 2019 Michael Cronenworth <mike@cchtml.com> 4.8-1
- version update

* Sun Apr 28 2019 Michael Cronenworth <mike@cchtml.com> 4.7-1
- version update

* Sun Apr 14 2019 Michael Cronenworth <mike@cchtml.com> 4.6-1
- version update

* Tue Apr 02 2019 Michael Cronenworth <mike@cchtml.com> 4.5-1
- version update

* Tue Mar 19 2019 Michael Cronenworth <mike@cchtml.com> 4.4-1
- version update

* Sun Mar 03 2019 Michael Cronenworth <mike@cchtml.com> 4.3-1
- version update

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 4.2-3
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Björn Esser <besser82@fedoraproject.org> - 4.2-2
- Fix version requirement on wine-mono

* Sun Feb 17 2019 Michael Cronenworth <mike@cchtml.com> 4.2-1
- version update

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Michael Cronenworth <mike@cchtml.com> 4.0-1
- version update
