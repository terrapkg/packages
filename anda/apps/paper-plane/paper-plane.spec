%global ver 0.1.0-beta.1

Name:			paper-plane
Version:		%(echo %ver | sed 's/-/~')
Release:		1%?dist
Summary:		Alternative Telegram client in GTK4 and Rust
License:		GPL-3.0
URL:			https://github.com/paper-plane-developers/paper-plane
Source0:		%url/archive/refs/tags/v%ver.tar.gz
BuildRequires:	meson cargo gtk4-devel >= 4.10 libadwaita tdlib
Requires:		gtk4 >= 4.10 gstreamer1-plugin-libav gstreamer1-plugins-good

%description
Paper Plane is an alternative Telegram client. It uses libadwaita for its user
interface and strives to meet the design principles of the GNOME desktop.

%prep
%autosetup -n %name-%ver

%build
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=paper-plane
%meson -Dtg_api_id=22303002 -Dtg_api_hash=3cc0969992690f032197e6609b296599
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING

%changelog
* Tue May 23 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.1.0-beta.1
- Initial package.
