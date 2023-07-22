%global ver 0.1.0
%global commit 21bdaacae32b16ea40a0e0fbddaa984f01b3a985
%global adw 9c2d9426b0772787796009f03f0eab06612c4a96

Name:			paper-plane
Version:		%ver~%commit
Release:		1%?dist
Summary:		Alternative Telegram client in GTK4 and Rust
License:		GPL-3.0
URL:			https://github.com/paper-plane-developers/paper-plane
Source0:		%url/archive/%commit.tar.gz
Patch0:			0001-remove-libadwaita-dependency.patch
BuildRequires:	meson cargo terra-gtk4-devel >= 4.10 tdlib-nightly-devel libappstream-glib desktop-file-utils terra-blueprint-compiler sassc pkgconfig(appstream) vala pkgconfig(libadwaita-nightly)
Requires:		terra-gtk4 >= 4.10 gstreamer1-plugin-libav gstreamer1-plugins-good libadwaita-nightly

%description
Paper Plane is an alternative Telegram client. It uses libadwaita for its user
interface and strives to meet the design principles of the GNOME desktop.

%prep
%autosetup -n %name-%commit -p1
tar xf %SOURCE1

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
