%global real_name vala-language-server

%global commit 31cb5116a4a138365feb709ebb7b8670db604991
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global commit_date 20240605
%global snapshot_info %{commit_date}.%{shortcommit}
%global verrel 0.48.7

Name:			vala-language-server-nightly
Summary:		Language server for the Vala programming language
Version:		0.48.7^%{snapshot_info}
Release:		1%?dist
# The entire source is LGPLv2+, except plugins/gnome-builder/vala_langserv.py, which is GPLv3+.
# It is not installed when the "plugins" meson option is set to false.
# Since GNOME Builder 41, the VLS the plugin has been included.
License:		LGPL-2.0+

URL:			https://github.com/vala-lang/vala-language-server
Source0:		https://github.com/vala-lang/vala-language-server/archive/%{commit}/%{real_name}-%{shortcommit}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	ninja-build
BuildRequires:	vala		>= 0.56.4
BuildRequires:	vala-devel	>= 0.56.4

BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(json-glib-1.0)    >= 1.4.4
BuildRequires:	pkgconfig(jsonrpc-glib-1.0) >= 3.28
BuildRequires:	pkgconfig(scdoc)

Requires:		glib2-static%{?_isa}
Requires:		json-glib%{?_isa}
Requires:		jsonrpc-glib%{?_isa}
Requires:		libgee%{?_isa}
Requires:		libvala%{?_isa}

Recommends:		gobject-introspection-devel

Suggests:		gnome-builder

Conflicts:		vala-language-server

%description
Provides code intelligence for Vala (and also Genie).
Used with an editor and a plugin that supports the Language Server Protocol.


%prep
%autosetup -n %{real_name}-%{commit}

%build
%meson -Dplugins=false
%meson_build
%install
%meson_install
%files
%license COPYING
%doc README.md

%{_bindir}/%{real_name}
%{_mandir}/man1/%{real_name}.1*

%changelog
* Sat Jan 14 2023 lleyton <lleyton@fyralabs.com>
- Initial package
