Name:			terra-blueprint-compiler
Version:		0.12.0
Release:		1%?dist
License:		LGPL-3.0-or-later
Summary:		Markup language for GTK user interfaces
URL:			https://jwestman.pages.gitlab.gnome.org/blueprint-compiler/
Source0:		https://gitlab.gnome.org/jwestman/blueprint-compiler/-/archive/v%version/blueprint-compiler-v%version.tar.gz
BuildArch:		noarch
BuildRequires:	meson gtk4-devel python3-devel python3-gobject-devel
Requires:		python3-gobject-devel

%description
GtkBuilder XML format is quite verbose, and many app developers don't like
using WYSIWYG editors for creating UIs. Blueprint files are intended to be a
concise, easy-to-read format that makes it easier to create and edit GTK UIs.
Internally, it compiles to GtkBuilder XML as part of an app's build system. It
adds no new features, just makes the features that exist more accessible.
Another goal is to have excellent developer tooling--including a language
server--so that less knowledge of the format is required. Hopefully this will
increase adoption of cool advanced features like GtkExpression.

%prep
%autosetup -n blueprint-compiler-v%version

%build
%meson
%meson_build

%install
%meson_install

#check
#meson_test

%files
%doc README.md docs/*.rst
%license COPYING
%_bindir/blueprint-compiler
%python3_sitelib/blueprintcompiler
%_datadir/pkgconfig/blueprint-compiler.pc

%changelog
* Tue Jun 13 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.8.0-1
- Initial package
