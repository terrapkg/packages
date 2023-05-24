%global ver 1.3.2
%global commit f0dd780a40707044edc45fc4c6129e4c88fe2d38

Name:			libadwaita-nightly
Version:		%ver^%commit
Release:		1%?dist
Summary:		Building blocks for modern GNOME applications
License:		LGPL-2.1+
URL:			https://gnome.pages.gitlab.gnome.org/libadwaita/
Source0:		https://gitlab.gnome.org/GNOME/libadwaita/-/archive/%commit/libadwaita-%commit.tar.gz
BuildRequires:	meson vala cmake gi-docgen git gobject-introspection sassc terra-gtk4-devel
Requires:		gtk4

%description
%summary.


%package doc
Summary: Documentations for libadwaita-nightly

%description doc
This package contains the documentations for libadwaita-nightly.


%prep
%autosetup -n libadwaita-%commit

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING

%changelog
* Tue May 23 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.1.0-beta.1
- Initial package.
