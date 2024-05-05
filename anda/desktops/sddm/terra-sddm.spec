# Disable X11 for RHEL 10+
%bcond x11 %[%{undefined rhel} || 0%{?rhel} < 10]

Name:           terra-sddm
Version:        0.21.0
Release:        5%{?dist}
License:        GPL-2.0-or-later
Summary:        QML based desktop and login manager
Provides:       sddm = %version-%release

URL:            https://github.com/sddm/sddm
Source0:        %{url}/archive/v%{version}/sddm-%{version}.tar.gz

## upstream patches
# Port all themes to Qt 6
# Submitted: https://github.com/sddm/sddm/pull/1876
Patch1:         sddm-PR1876.patch

## upstreamable patches
# Fix race with logind restart, and start seat0 if !CanGraphical on timer
# https://bugzilla.redhat.com/show_bug.cgi?id=2011991
# https://bugzilla.redhat.com/show_bug.cgi?id=2016310
# Submmited: https://github.com/sddm/sddm/pull/1494
Patch11:        0001-Delay-for-logind-and-fallback-to-seat0.patch

## downstream patches
Patch101:       sddm-0.20.0-fedora_config.patch

# sddm.service: +EnvironmentFile=-/etc/sysconfig/sddm
Patch103:       sddm-0.18.0-environment_file.patch

# Workaround for https://pagure.io/fedora-kde/SIG/issue/87
Patch104:       sddm-rpmostree-tmpfiles-hack.patch

# Workaround lack of Qt 5 greeter build
Patch105:       sddm-0.21.0-qt6greeter.patch

# https://github.com/sddm/sddm/pull/1779
Patch106:       https://github.com/sddm/sddm/pull/1779.patch

# Shamelessly stolen from gdm
Source10:       sddm.pam
# Shamelessly stolen from gdm
Source11:       sddm-autologin.pam
# Previously included in sddm sources
Source12:       sddm-greeter.pam
# sample sddm.conf generated with sddm --example-config, and entries commented-out
Source13:       sddm.conf
# README.scripts
Source14:       README.scripts
# sysconfig snippet
Source15:       sddm.sysconfig
# sddm x11 override config
Source16:       sddm-x11.conf
# sysusers config file. note these are shipped in the upstream tarball
# but we cannot use the files from the tarball for %pre scriptlet
# generation, so we duplicate them as source files for that purpose;
# this is an ugly hack that should be removed if it becomes possible.
# see https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/TFDMAU7KLMSQTKPJELHSM6PFVXIZ56GK/
Source17:       sddm-systemd-sysusers.conf


Provides: service(graphical-login) = sddm

BuildRequires:  cmake >= 2.8.8
BuildRequires:  extra-cmake-modules
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)
# sometimes python-docutils, sometimes python2-docutils, sometimes python3-docutils.
# use path then for sanity
BuildRequires:  /usr/bin/rst2man
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6QuickTest)
# verify presence to pull defaults from /etc/login.defs
BuildRequires:  shadow-utils
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros

Obsoletes: kde-settings-sddm < 20-5

%if 0%{?fedora}
# for /usr/share/backgrounds/default.png
BuildRequires: desktop-backgrounds-compat
BuildRequires: GraphicsMagick
Requires: desktop-backgrounds-compat
# for /usr/share/pixmaps/system-logo-white.png
Requires: system-logos
%endif
Requires: systemd
%if %{with x11}
Requires: xorg-x11-xinit
%endif
%{?systemd_requires}

Requires(pre): shadow-utils

# Virtual dependency for sddm greeter setup
Requires: sddm-greeter-displayserver
Suggests: sddm-wayland-generic

%description
SDDM is a modern graphical display manager aiming to be fast, simple and
beautiful. It uses modern technologies like QtQuick, which in turn gives the
designer the ability to create smooth, animated user interfaces.

%package wayland-generic
Summary: Generic Wayland SDDM greeter configuration
Provides: sddm-greeter-displayserver
Conflicts: sddm-greeter-displayserver
Requires: weston
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description wayland-generic
This package contains configuration and dependencies for SDDM
to use Weston for the greeter display server.

This is the generic default Wayland configuration provided
by SDDM.

%if %{with x11}
%package x11
Summary: X11 SDDM greeter configuration
Provides: sddm-greeter-displayserver
Conflicts: sddm-greeter-displayserver
# This will eventually go away...
Provides: deprecated()
Requires: xorg-x11-server-Xorg
Requires: %{name} = %{version}-%{release}
Recommends: qt6-qtvirtualkeyboard
BuildArch: noarch

%description x11
This package contains configuration and dependencies for SDDM
to use X11 for the greeter display server.
%endif

%package themes
Summary: SDDM Themes
# for upgrade path
Obsoletes: sddm < 0.2.0-0.12
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description themes
A collection of sddm themes, including: elarun, maldives, maya


%prep
%autosetup -p1 %{?commitdate:-n sddm-%{commit}} -n sddm-%version

%if 0%{?fedora}
#FIXME/TODO: use version on filesystem instead of using a bundled copy
cp -v /usr/share/backgrounds/default.png  \
      src/greeter/theme/background.png
ls -sh src/greeter/theme/background.png
gm mogrify -resize 1920x1200 src/greeter/theme/background.png
ls -sh src/greeter/theme/background.png
%endif


%build
%cmake \
  -DBUILD_WITH_QT6:BOOL=ON \
  -DBUILD_MAN_PAGES:BOOL=ON \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DENABLE_JOURNALD:BOOL=ON \
  -DSESSION_COMMAND:PATH=/etc/X11/xinit/Xsession \
  -DWAYLAND_SESSION_COMMAND:PATH=/etc/sddm/wayland-session

%cmake_build


%install
%cmake_install

mkdir -p %{buildroot}%{_sysconfdir}/sddm.conf.d
mkdir -p %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d
install -Dpm 644 %{SOURCE10} %{buildroot}%{_sysconfdir}/pam.d/sddm
install -Dpm 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/pam.d/sddm-autologin
install -Dpm 644 %{SOURCE12} %{buildroot}%{_sysconfdir}/pam.d/sddm-greeter
install -Dpm 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/sddm.conf
install -Dpm 644 %{SOURCE14} %{buildroot}%{_datadir}/sddm/scripts/README.scripts
install -Dpm 644 %{SOURCE15} %{buildroot}%{_sysconfdir}/sysconfig/sddm
%if %{with x11}
install -Dpm 644 %{SOURCE16} %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/x11.conf
%endif
mkdir -p %{buildroot}/run/sddm
mkdir -p %{buildroot}%{_localstatedir}/lib/sddm
mkdir -p %{buildroot}%{_sysconfdir}/sddm/
cp -a %{buildroot}%{_datadir}/sddm/scripts/* \
      %{buildroot}%{_sysconfdir}/sddm/
# we're using /etc/X11/xinit/Xsession (by default) instead
rm -fv %{buildroot}%{_sysconfdir}/sddm/Xsession

# De-conflict the dbus file
mv %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf \
   %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-sddm.conf

%if 0%{?fedora} && 0%{?fedora} < 43
# Provide unversioned greeter until F40 is EOL
ln -sr %{buildroot}%{_bindir}/sddm-greeter-qt6 %{buildroot}%{_bindir}/sddm-greeter
%endif


%pre
%sysusers_create_compat %{SOURCE17}

%post
%systemd_post sddm.service
# handle incompatible configuration changes
(grep \
   -e '^Current=fedora$' \
   -e '^\[XDisplay\]$' \
   -e '^\[WaylandDisplay\]$' \
   %{_sysconfdir}/sddm.conf > /dev/null && \
 sed -i.rpmsave \
   -e 's|^Current=fedora$|#Current=01-breeze-fedora|' \
   -e 's|^\[XDisplay\]$|\[X11\]|' \
   -e 's|^\[WaylandDisplay\]$|\[Wayland\]|' \
   %{_sysconfdir}/sddm.conf
) ||:


%preun
%systemd_preun sddm.service


%postun
%systemd_postun sddm.service


%files
%license LICENSE
%doc README.md CONTRIBUTORS
%dir %{_sysconfdir}/sddm/
%dir %{_sysconfdir}/sddm.conf.d
%dir %{_prefix}/lib/sddm/sddm.conf.d
%config(noreplace)   %{_sysconfdir}/sddm/*
%config(noreplace)   %{_sysconfdir}/sddm.conf
%config(noreplace) %{_sysconfdir}/sysconfig/sddm
%config(noreplace) %{_sysconfdir}/pam.d/sddm*
%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-sddm.conf
%{_bindir}/sddm
%{_bindir}/sddm-greeter*
%{_libexecdir}/sddm-helper
%{_libexecdir}/sddm-helper-start-wayland
%{_libexecdir}/sddm-helper-start-x11user
%{_tmpfilesdir}/sddm.conf
%{_sysusersdir}/sddm.conf
%attr(0711, root, sddm) %dir /run/sddm
%attr(1770, sddm, sddm) %dir %{_localstatedir}/lib/sddm
%{_unitdir}/sddm.service
%{_qt6_archdatadir}/qml/SddmComponents/
%dir %{_datadir}/sddm
%{_datadir}/sddm/faces/
%{_datadir}/sddm/flags/
%{_datadir}/sddm/scripts/
%dir %{_datadir}/sddm/themes/
# %%lang'ify? they're small, probably not worth it -- rex
%{_datadir}/sddm/translations*/
%{_mandir}/man1/sddm.1*
%{_mandir}/man1/sddm-greeter.1*
%{_mandir}/man5/sddm.conf.5*
%{_mandir}/man5/sddm-state.conf.5*


%files wayland-generic
# No files since default configuration


%if %{with x11}
%files x11
%{_prefix}/lib/sddm/sddm.conf.d/x11.conf
%endif


%files themes
%{_datadir}/sddm/themes/elarun/
%{_datadir}/sddm/themes/maldives/
%{_datadir}/sddm/themes/maya/


%changelog
%autochangelog
