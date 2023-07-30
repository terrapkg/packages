%define debug_package %nil
%global ver 0.1.0-beta.3

Name:			paper-plane
Version:		0.1.0~beta.3
Release:		1%?dist
Summary:		Alternative Telegram client in GTK4 and Rust
License:		GPL-3.0
URL:			https://github.com/paper-plane-developers/paper-plane
Source0:		%url/archive/v%ver.tar.gz
BuildRequires:	meson cargo terra-gtk4-devel tdlib-paper-plane-devel libappstream-glib desktop-file-utils terra-blueprint-compiler sassc pkgconfig(appstream) vala libadwaita-nightly-devel rlottie-devel clang-devel desktop-file-utils libappstream-glib
Requires:		terra-gtk4 >= 4.10 gstreamer1-plugin-libav gstreamer1-plugins-good libadwaita-nightly tdlib-paper-plane

%description
Paper Plane is an alternative Telegram client. It uses libadwaita for its user
interface and strives to meet the design principles of the GNOME desktop.

%prep
%autosetup -n %name-%ver
cp /%_libdir/pkgconfig/libadwaita-nightly.pc /%_libdir/pkgconfig/libadwaita-1.pc

%build
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=paper-plane
%meson -Dtg_api_id=22303002 -Dtg_api_hash=3cc0969992690f032197e6609b296599
%meson_build

%install
%meson_install

%check
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/app.drey.PaperPlane.metainfo.xml
desktop-file-validate %buildroot%_datadir/applications/app.drey.PaperPlane.desktop

%files
%doc README.md
%license COPYING
%_bindir/paper-plane
%_datadir/applications/app.drey.PaperPlane.desktop
%_datadir/glib-2.0/schemas/app.drey.PaperPlane.gschema.xml
%_datadir/icons/hicolor/scalable/apps/app.drey.PaperPlane.svg
%_datadir/icons/hicolor/symbolic/apps/app.drey.PaperPlane-symbolic.svg
%_datadir/locale/*/LC_MESSAGES/paper-plane.mo
%_datadir/metainfo/app.drey.PaperPlane.metainfo.xml
%_datadir/paper-plane/resources.gresource

%changelog
* Tue May 23 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.1.0-beta.1
- Initial package.
