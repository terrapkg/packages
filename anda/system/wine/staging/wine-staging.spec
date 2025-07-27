# Terra WINE Staging branch
# Based on WineHQ's WINE builds with changes for our repos and update system

# Gonna be real man, WINE is a mess
%global _default_patch_fuzz 2
# This is unfortunate but a lot of Fedora's/SUSE's hardening flags break WINE
%define _lto_cflags %{nil}

%global flavor %nil
# I love MinGW
%global build_type_safety_c 0

%define compat_package	terra-wine-staging
%define _prefix 	/usr/share/wine-staging
%undefine _hardened_build

%global srcmajor 10.x


Name:       wine-staging
Version:    10.12
Release:    1%?dist
Epoch:      1
Summary:    WINE Is Not An Emulator - runs MS Windows programs
License:    LGPL-2.0-or-later
Group:      Emulators
URL:        https://www.winehq.org

%define lib_major       1
%define lib_name        lib%{name}1
%define lib_name_devel  lib%{name}-devel

%if 0%{?fedora} < 40
%ifarch x86_64
%define wine    %{name}64
%define mark64  ()(64bit)
%else
%define wine    %{name}
%define mark64  %{nil}
%endif
%endif

%if 0%{?fedora} >= 40
%define wine    %{name}
%ifarch x86_64
%define mark64  ()(64bit)
%else
%define mark64  %{nil}
%endif
%endif

Source0:	https://dl.winehq.org/wine/source/%{srcmajor}/wine-%{version}.tar.xz
Source1:	https://dl.winehq.org/wine/source/%{srcmajor}/wine-%{version}.tar.xz.sign

# The official GitLab repo containing the patches does not appear to be downloadable so we have to download them from the mirror. What
Source100:	https://github.com/wine-staging/wine-staging/archive/v%{version}.tar.gz#/wine-staging-%{version}.tar.xz

# Alexandres key
Source99:	wine.keyring

BuildRequires:  alsa-lib-devel
BuildRequires:  audiofile-devel
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  cups-devel
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  fontconfig-devel
BuildRequires:  fontforge
BuildRequires:  fontpackages-devel
BuildRequires:  freeglut-devel
BuildRequires:  freetype-devel
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  giflib-devel
BuildRequires:  gnupg2
BuildRequires:  gnutls-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk3-devel
BuildRequires:  icoutils
BuildRequires:  ImageMagick-devel
BuildRequires:  krb5-devel
BuildRequires:  libattr-devel
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  libieee1284-devel
BuildRequires:  libnetapi-devel
BuildRequires:  libpcap-devel
BuildRequires:  librsvg2
BuildRequires:  librsvg2-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libudev-devel
BuildRequires:  libusb1-devel
BuildRequires:  libv4l-devel
BuildRequires:  libva-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXxf86dga-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  lzma
BuildRequires:  mesa-compat-libOSMesa-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  ncurses-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
BuildRequires:  pcsc-lite-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  samba-devel
BuildRequires:  sane-backends-devel
BuildRequires:  SDL2-devel
BuildRequires:  unixODBC-devel
BuildRequires:  unzip
BuildRequires:  util-linux
BuildRequires:  vulkan-devel
BuildRequires:  xz

%if 0%{?fedora} < 40
%ifarch x86_64
%package -n %{wine}
%endif
%endif

Summary:    WINE Is Not An Emulator - runs MS Windows programs
Group:      Emulators
%ifarch x86_64
Conflicts:  %{name}
%else
Conflicts:  %{name}64
%endif
%if 0%{?fedora} < 40
Requires:   %{name}-common = %{epoch}:%{version}-%{release}
%endif
Requires:   %{compat_package} = %{epoch}:%{version}-%{release}
Provides:   %{lib_name} = %{epoch}:%{version}-%{release}
Obsoletes:  %{lib_name} <= %{epoch}:%{version}-%{release}
Provides:   %{name}-bin = %{epoch}:%{version}-%{release}

%ifarch %{ix86}
%package -n %{name}-common
Summary:    WINE Is Not An Emulator - runs MS Windows programs (32-bit common files)
Group:      Emulators
Requires:   %{name}-bin = %{epoch}:%{version}-%{release}

%description -n %{name}-common
Wine is a program which allows running Microsoft Windows programs
(including DOS, Windows 3.x and Win32 executables) on Unix.

This package contains the files needed to support 32-bit Windows
programs, and is used by both %{name} and %{name}64.
%endif

%define dlopenreq() %(F=/usr/%{_lib}/lib%{1}.so;[ -e $F ] && (file $F|grep -q ASCII && grep -o 'lib[^ ]*' $F|sed -e "s/\$/%{mark64}/"||objdump -p $F | grep SONAME | awk '{ print $2 "%{mark64}" }') || echo "wine-missing-buildrequires-on-%{1}")
Requires:   %dlopenreq asound
Requires:   %dlopenreq attr
Requires:   %dlopenreq cups
Requires:   %dlopenreq dbus-1
Requires:   %dlopenreq fontconfig
Requires:   %dlopenreq freetype
Requires:   %dlopenreq gnutls
Requires:   %dlopenreq krb5
Requires:   %dlopenreq ncurses
Requires:   %dlopenreq odbc
Requires:   %dlopenreq OSMesa
Requires:   %dlopenreq sane
Requires:   %dlopenreq SDL2
Requires:   %dlopenreq v4l1
Requires:   %dlopenreq vulkan
Requires:   %dlopenreq Xcomposite
Requires:   %dlopenreq Xcursor
Requires:   %dlopenreq Xi
Requires:   %dlopenreq Xinerama
Requires:   %dlopenreq Xrandr
Requires:   %dlopenreq Xrender
Requires:   %dlopenreq Xxf86vm
%if 0%{?fedora}
Suggests:   sane-frontends
%endif
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%define desc Wine is a program which allows running Microsoft Windows programs \
(including DOS, Windows 3.x and Win32 executables) on Unix. It \
consists of a program loader which loads and executes a Microsoft \
Windows binary, and a library (called Winelib) that implements Windows \
API calls using their Unix or X11 equivalents.  The library may also \
be used for porting Win32 code into native Unix executables.

%description
%desc

%ifarch x86_64
%description -n %{wine}
%desc
%endif

%package -n %{wine}-devel
Summary:    Static libraries and headers for %{name} (64-bit)
Group:      Development/C
Requires:   %{wine} = %{epoch}:%{version}-%{release}
%ifarch x86_64
Conflicts:  %{name}-devel
%else
Conflicts:  %{name}64-devel
%endif
Provides:   %{lib_name_devel} = %{epoch}:%{version}-%{release}
Obsoletes:  %{lib_name_devel} <= %{epoch}:%{version}-%{release}
%description -n %{wine}-devel
Wine is a program which allows running Microsoft Windows programs
(including DOS, Windows 3.x and Win32 executables) on Unix.

This package contains the libraries and header files needed to
develop programs which make use of Wine.

%package -n %compat_package
Summary:    WINE Is Not An Emulator - runs MS Windows programs
Group:      Emulators
Requires:   %{wine} = %{epoch}:%{version}-%{release}
Conflicts:  wine wine64 wine-core wine-common wine-desktop wine-devel

%description -n %compat_package
Wine is a program which allows running Microsoft Windows programs
(including DOS, Windows 3.x and Win32 executables) on Unix.

This compatibility package allows to use %{wine} system-wide as
the default Wine version.

%prep
# Pull key from key server, if this fails import local copy and then refresh it to make sure it is up to date
gpg --keyserver hkp://keys.gnupg.net --recv-keys CEFAC8EAAF17519D || { gpg --with-fingerprint --import %{SOURCE99} && gpg --refresh-keys; }
gpg --update-trustdb
gpg --verify --with-fingerprint %{SOURCE1} %{SOURCE0}
%setup -n wine-%{version}  -q -T -b0

# apply wine staging patch set on top of the wine release.
tar xf %{SOURCE100}
./wine-staging-%{version}/staging/patchinstall.py --all -W shell32-IconCache -W server-Stored_ACLs

%build
# MinGW GCC does not support these options
%define debug_package %{nil}
export LDFLAGS="$(echo "%{build_ldflags}" | sed -e 's/-Wl,-z,relro//' -e 's/-Wl,--build-id=sha1//' -e 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-package-notes//')"
%ifarch x86_64
export CFLAGS="$(echo "%{optflags}" | sed -e 's/-O2//' -e 's/-Wp,-D_FORTIFY_SOURCE=2//' -e 's/-fcf-protection//' -e 's/-fstack-protector-strong//' -e 's/-fstack-clash-protection//') -O2"
%else
export CFLAGS="$(echo "%{optflags}" | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//' -e 's/-fcf-protection//' -e 's/-fstack-protector-strong//' -e 's/-fstack-clash-protection//')"
%endif
autoreconf -i -f
%configure \
    --with-gstreamer \
    --disable-tests \
    --with-xattr \
    --enable-archs=i386,x86_64 \
    --with-x

make -j4

%install
%makeinstall LDCONFIG=/bin/true

# Compat symlinks for bindir
mkdir -p "%{buildroot}/usr/bin"
for _file in $(ls "%{buildroot}%{_bindir}"); do \
    ln -s "%{_bindir}/$_file" "%{buildroot}/usr/bin/$_file"; \
done

# Compat symlinks for desktop file
mkdir -p "%{buildroot}/usr/share/applications"
for _file in $(ls "%{buildroot}/%{_datadir}/applications"); do \
    ln -s "%{_datadir}/applications/$_file" "%{buildroot}/usr/share/applications/$_file"; \
done

# Compat manpages
%if  0%{?fedora} || 0%{?scientificlinux} || 0%{?centos} >= 700 || 0%{?rhel} >= 700
for _dir in man1 de.UTF-8/man1 fr.UTF-8/man1 pl.UTF-8/man1; do \
	if [ -d "%{buildroot}/%{_mandir}/$_dir" ]; then \
        mkdir -p "$(dirname "%{buildroot}/usr/share/man/$_dir")"; \
		cp -pr "%{buildroot}/%{_mandir}/$_dir" "%{buildroot}/usr/share/man/$_dir"; \
	else \
		mkdir -p "%{buildroot}/usr/share/man/$_dir"; \
	fi; \
done
%else
for _dir in man1 de.UTF-8/man1 fr.UTF-8/man1 pl.UTF-8/man1; do \
        mkdir -p "%{buildroot}/usr/share/man/$_dir"; \
done
%endif

%ifarch x86_64
#install -p -m 0644 loader/wine.man          "%{buildroot}/usr/share/man/man1/wine.1"
#install -p -m 0644 loader/wine.de.UTF-8.man "%{buildroot}/usr/share/man/de.UTF-8/man1/wine.1"
#install -p -m 0644 loader/wine.fr.UTF-8.man "%{buildroot}/usr/share/man/fr.UTF-8/man1/wine.1"
#install -p -m 0644 loader/wine.pl.UTF-8.man "%{buildroot}/usr/share/man/pl.UTF-8/man1/wine.1"
%endif

%files -n %{wine}
%doc ANNOUNCE.md AUTHORS README.md
%license LICENSE

%if 0%{?fedora} < 40
%ifarch x86_64
%{_bindir}/wine64
%{_bindir}/wine64-preloader
%endif
%endif
%{_bindir}/function_grep.pl
%{_bindir}/msidb
%{_bindir}/msiexec
%{_bindir}/notepad
%{_bindir}/regedit
%{_bindir}/regsvr32
%{_bindir}/widl
%{_bindir}/wineboot
%{_bindir}/winebuild
%{_bindir}/winecfg
%{_bindir}/wineconsole*
%{_bindir}/winecpp
%{_bindir}/winedbg
%{_bindir}/winedump
%{_bindir}/winefile
%{_bindir}/wineg++
%{_bindir}/winegcc
%{_bindir}/winemaker
%{_bindir}/winemine
%{_bindir}/winepath
%{_bindir}/wineserver
%{_bindir}/wmc
%{_bindir}/wrc
%lang(de) %{_mandir}/de.UTF-8/man?/winemaker.?*
%lang(de) %{_mandir}/de.UTF-8/man?/wineserver.?*
%lang(fr) %{_mandir}/fr.UTF-8/man?/winemaker.?*
%lang(fr) %{_mandir}/fr.UTF-8/man?/wineserver.?*
%{_mandir}/man?/widl.1*
%{_mandir}/man?/winebuild.1*
%{_mandir}/man?/winecpp.1*
%{_mandir}/man?/winedbg.1*
%{_mandir}/man?/winedump.1*
%{_mandir}/man?/wineg++.1*
%{_mandir}/man?/winegcc.1*
%{_mandir}/man?/winemaker.1*
%{_mandir}/man?/wmc.1*
%{_mandir}/man?/wrc.1*
%{_mandir}/man?/msiexec.?*
%{_mandir}/man?/notepad.?*
%{_mandir}/man?/regedit.?*
%{_mandir}/man?/regsvr32.?*
%{_mandir}/man?/wineboot.?*
%{_mandir}/man?/winecfg.?*
%{_mandir}/man?/wineconsole.?*
%{_mandir}/man?/winefile.?*
%{_mandir}/man?/winemine.?*
%{_mandir}/man?/winepath.?*
%{_mandir}/man?/wineserver.?*
%dir %{_datadir}/wine
%{_datadir}/wine/wine.inf
%{_datadir}/wine/nls/*.nls
%{_datadir}/applications/*.desktop
%dir %{_datadir}/wine/fonts
%{_datadir}/wine/fonts/*
# %{_datadir}/wine/color/*

%if 0%{?fedora} < 40
%ifarch %{ix86}
%files -n %{name}-common
%{_bindir}/wine
%{_bindir}/wine-preloader
%{_mandir}/man?/wine.?*
%lang(de) %{_mandir}/de.UTF-8/man?/wine.?*
%lang(fr) %{_mandir}/fr.UTF-8/man?/wine.?*
%lang(pl) %{_mandir}/pl.UTF-8/man?/wine.?*
%endif
%else
%{_bindir}/wine
#%{_bindir}/wine-preloader
%{_mandir}/man?/wine.?*
%lang(de) %{_mandir}/de.UTF-8/man?/wine.?*
%lang(fr) %{_mandir}/fr.UTF-8/man?/wine.?*
%lang(pl) %{_mandir}/pl.UTF-8/man?/wine.?*
%endif

%if 0%{?fedora} < 40
%ifarch %ix86 x86_64
%{_libdir}/wine/%{_arch}-unix/*.*
%{_libdir}/wine/%{_arch}-windows/*.*
%endif
%else
%{_libdir}/wine/%{_arch}-unix/*
%{_libdir}/wine/i386-windows/*.*
%{_libdir}/wine/x86_64-windows/*.*
%endif

%files -n %{wine}-devel
%{_includedir}/*

%files -n %compat_package
/usr/bin/*
/usr/share/applications/*.desktop
/usr/share/man/man?/*
%lang(de) /usr/share/man/de.UTF-8/man?/*
%lang(fr) /usr/share/man/fr.UTF-8/man?/*
%lang(pl) /usr/share/man/pl.UTF-8/man?/*
