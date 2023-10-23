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

BuildRequires:  rustc cargo anda-srpm-macros gcc-c++ git curl wget nasm yasm gcc gtk3-devel clang libxcb-devel libxdo-devel libXfixes-devel pulseaudio-libs-devel cmake alsa-lib-devel
BuildRequires:  gstreamer1-devel rust-gstreamer-devel pkgconfig(gstreamer-app-1.0)
BuildRequires:  libvpx-devel opus-devel libyuv-devel libaom-devel
Requires:   gtk3 libxcb libxdo libXfixes alsa-lib libappindicator libvdpau1 libva2 pam gstreamer1-plugins-base



%description
The best open-source remote desktop client software, written in Rust.

%prep
%autosetup -n rustdesk-%{version}

%build
cargo build
%global __python %{__python3}

%install
%cargo_install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/lib/rustdesk/
mkdir -p %{buildroot}/usr/share/rustdesk/files/
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps/
install -m 755 target/release/rustdesk %{buildroot}/usr/bin/rustdesk
install %{SOURCE1} %{buildroot}/usr/lib/rustdesk/libsciter-gtk.so
install res/rustdesk.service %{buildroot}/usr/share/rustdesk/files/
install res/128x128@2x.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/rustdesk.png
install res/scalable.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/rustdesk.svg
install res/rustdesk.desktop %{buildroot}/usr/share/rustdesk/files/
install res/rustdesk-link.desktop %{buildroot}/usr/share/rustdesk/files/

%files
/usr/bin/rustdesk
/usr/lib/rustdesk/libsciter-gtk.so
/usr/share/rustdesk/files/rustdesk.service
/usr/share/icons/hicolor/256x256/apps/rustdesk.png
/usr/share/icons/hicolor/scalable/apps/rustdesk.svg
/usr/share/rustdesk/files/rustdesk.desktop
/usr/share/rustdesk/files/rustdesk-link.desktop
/usr/share/rustdesk/files/__pycache__/*



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
cp /usr/share/rustdesk/files/rustdesk.service /etc/systemd/system/rustdesk.service
cp /usr/share/rustdesk/files/rustdesk.desktop /usr/share/applications/
cp /usr/share/rustdesk/files/rustdesk-link.desktop /usr/share/applications/
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
    rm /etc/systemd/system/rustdesk.service || true
  ;;
  1)
    # for upgrade
  ;;
esac

%postun
case "$1" in
  0)
    # for uninstall
    rm /usr/share/applications/rustdesk.desktop || true
    rm /usr/share/applications/rustdesk-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac


%changelog
%autochangelog
