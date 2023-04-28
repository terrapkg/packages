Name:			gtk4-layer-shell
Version:		1.0.0
Release:		1%?dist
Summary:		A library to create panels and other desktop components for Wayland using the Layer Shell protocol and GTK4
License:		MIT
URL:			https://github.com/wmww/gtk4-layer-shell
Source0:		%url/archive/refs/tags/v%version.tar.gz
BuildRequires:	meson ninja-build mold python3.11 vala
BuildRequires:	libwayland-client gtk4-devel gobject-introspection gtk-doc

%description
A library for using the Layer Shell Wayland protocol with GTK4. With this library
you can build desktop shell components such as panels, notifications and wallpapers.
You can use it to anchor your windows to a corner or edge of the output, or stretch
them across the entire output. This Library is compatible with C, C++ and any
language that supports GObject introspection files (Python, Vala, etc).

%prep
%autosetup

%build
%meson -Ddocs=true -Dtests=true
%meson_build

%install
%meson_install

%check
ninja -C build test

%files
%doc README.md
%license LICENSE

%changelog
* Fri Apr 28 2023 windowsboy111 <windowsboy111@fyralabs.com>
- Initial package.
