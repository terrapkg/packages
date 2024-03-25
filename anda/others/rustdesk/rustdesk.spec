#global pamsys_ver v1.0.0-alpha5
#global pamsys 1.0.0-alpha5
#global pam_ver v0.7.0
#global pam 0.7.0

%ifarch x86_64
%global scarch x64
%else
%ifarch aarch64
%global scarch arm64
%endif
%endif

Name:       rustdesk
Version:	1.2.3
Release:	1%{?dist}
Summary:	An open-source remote desktop, and alternative to TeamViewer.

Group:	    System Environment/Base
License:	GPLv2+	
URL:		http://rustdesk.com
Source0:	https://github.com/rustdesk/rustdesk/archive/refs/tags/%{version}.tar.gz
Source1:    https://github.com/c-smile/sciter-sdk/raw/master/bin.lnx/%{scarch}/libsciter-gtk.so
%dnl Source2:    https://github.com/fufesou/pam/archive/refs/tags/%{pam_ver}.tar.gz
%dnl Source3:    https://github.com/1wilkens/pam-sys/archive/refs/tags/%{pamsys_ver}.tar.gz
%dnl Patch0:     pam-deps.diff
%dnl Patch1:     pam-sys-build.patch
%dnl Patch2:     rustdesk-deps.diff

BuildRequires:  rust-packaging anda-srpm-macros gcc-c++ git curl wget nasm yasm gcc gtk3-devel clang libxcb-devel libxdo-devel libXfixes-devel pulseaudio-libs-devel cmake alsa-lib-devel
BuildRequires:  gstreamer1-devel rust-gstreamer-devel pkgconfig(gstreamer-app-1.0)
BuildRequires:  libvpx-devel opus-devel libyuv-devel libaom-devel pam-devel clang-devel
Requires:   gtk3 libxcb libxdo libXfixes alsa-lib libappindicator libvdpau1 libva2 pam gstreamer1-plugins-base



%description
The best open-source remote desktop client software, written in Rust.

%prep
%setup -q -n rustdesk-%version
%{dnl:
%patch 2 -p1
tar xf %SOURCE2
mv pam-%pam pam
cd pam
git apply %PATCH0
tar xf %SOURCE3
mv pam-sys-%pamsys pam-sys
cd pam-sys
git apply %PATCH1
cd ../..
}
%cargo_prep_online


%build
%cargo_build -a
%global __python %{__python3}


%install
%cargo_install -a
mkdir -p %buildroot/usr/lib/rustdesk/
mkdir -p %buildroot%_datadir/rustdesk/files/
mkdir -p %buildroot%_datadir/icons/hicolor/{256x256,scalable}/apps/
install %SOURCE1 %buildroot/usr/lib/rustdesk/libsciter-gtk.so
install res/rustdesk.service %buildroot%_datadir/rustdesk/files/
install res/128x128@2x.png %buildroot%_datadir/icons/hicolor/256x256/apps/rustdesk.png
install res/scalable.svg %buildroot%_datadir/icons/hicolor/scalable/apps/rustdesk.svg
install res/rustdesk.desktop %buildroot%_datadir/rustdesk/files/
install res/rustdesk-link.desktop %buildroot%_datadir/rustdesk/files/
install -d %buildroot%_datadir/applications/
install res/rustdesk.desktop %buildroot%_datadir/applications/
install res/rustdesk-link.desktop %buildroot%_datadir/applications/
install -d %buildroot%_unitdir
install res/rustdesk.service %buildroot%_unitdir/rustdesk.service

%files
%_bindir/rustdesk
%_bindir/naming
/usr/lib/rustdesk/libsciter-gtk.so
%_datadir/rustdesk/files/rustdesk.service
%_datadir/icons/hicolor/256x256/apps/rustdesk.png
%_datadir/icons/hicolor/scalable/apps/rustdesk.svg
%_datadir/rustdesk/files/rustdesk.desktop
%_datadir/rustdesk/files/rustdesk-link.desktop

%_datadir/applications/rustdesk.desktop
%_datadir/applications/rustdesk-link.desktop
%_unitdir/rustdesk.service


%pre
# can do something for centos7
case "$1" in
  1)
    # for install
  ;;
  2)
    # for upgrade
    systemctl stop rustdesk || true
  ;;
esac

%post
systemctl daemon-reload
systemctl enable rustdesk
systemctl start rustdesk
update-desktop-database

%preun
case "$1" in
  0)
    # for uninstall
    systemctl stop rustdesk || true
    systemctl disable rustdesk || true
  ;;
  1)
    # for upgrade
  ;;
esac

%postun
case "$1" in
  0)
    # for uninstall
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac


%changelog
%autochangelog
