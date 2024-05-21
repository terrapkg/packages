# Based on https://src.fedoraproject.org/rpms/vala/blob/rawhide/f/vala.spec
%global api_ver 0.58
%global priority 90

%global real_name vala
%global commit ed0077a101ddc5abe39045c36f8aeb053e5c34dd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global repo https://gitlab.gnome.org/GNOME/%{real_name}.git

%global commit_date 20240520
%global snapshot_info %{commit_date}.%{shortcommit}

Name:           vala-nightly
Version:        0.58.0^%{snapshot_info}
Release:        1%?dist
Summary:        A modern programming language for GNOME

# Most files are LGPLv2.1+, curses.vapi is 2-clause BSD
License:        LGPL-2.1-or-later AND BSD-2-Clause
URL:            https://wiki.gnome.org/Projects/Vala

BuildRequires:  git
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gobject-introspection-devel
BuildRequires:  graphviz-devel
BuildRequires:  libxslt
BuildRequires:  autoconf-archive
BuildRequires:  make
BuildRequires:  pkgconfig(gobject-2.0)
# only if Vala source files are patched
BuildRequires:  vala

# for tests
BuildRequires:  dbus-x11

Requires: libvala-nightly%{?_isa} = %{version}-%{release}

# For GLib-2.0 and GObject-2.0 .gir files
Requires: gobject-introspection-devel

Conflicts:      vala

%description
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

valac, the Vala compiler, is a self-hosting compiler that translates
Vala source code into C source and header files. It uses the GObject
type system to create classes and interfaces declared in the Vala source
code. It's also planned to generate GIDL files when gobject-
introspection is ready.

The syntax of Vala is similar to C#, modified to better fit the GObject
type system.


%package -n     libvala-nightly
Summary:        Vala compiler library

Conflicts:      libvala

%description -n libvala-nightly
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains the shared libvala library.


%package -n     libvala-nightly-devel
Summary:        Development files for libvala
Requires:       libvala%{?_isa} = %{version}-%{release}

Conflicts:      libvala-devel

%description -n libvala-nightly-devel
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains development files for libvala. This is not
necessary for using the %{name} compiler.

# TODO: currently the docs aren't included in the default build (they were before, even with sphinx installed)
# I think this is because they recently changed to using sphinx, which they're still working on
# I'll try to get this working again, but for now I'll just disable it until they're ready
# %package        doc
# Summary:        Documentation for %{name}
# BuildArch:      noarch
# Requires:       %{name} = %{version}-%{release}
# Requires:       devhelp

# Conflicts:      vala-doc

# %description    doc
# Vala is a new programming language that aims to bring modern programming
# language features to GNOME developers without imposing any additional
# runtime requirements and without using a different ABI compared to
# applications and libraries written in C.

# This package contains documentation in a devhelp HTML book.


%package -n     valadoc-nightly
Summary:        Vala documentation generator
Requires:       %{name}%{?_isa} = %{version}-%{release}

Conflicts:      valadoc

%description -n valadoc-nightly
Valadoc is a documentation generator for generating API documentation from Vala
source code.


%package -n     valadoc-nightly-devel
Summary:        Development files for valadoc
Requires:       valadoc%{?_isa} = %{version}-%{release}

Conflicts:      valadoc-devel

%description -n valadoc-nightly-devel
Valadoc is a documentation generator for generating API documentation from Vala
source code.

The valadoc-devel package contains libraries and header files for
developing applications that use valadoc.


%prep
rm -rf %{real_name}-%{commit}
git clone %{repo} %{real_name}-%{commit}
cd %{real_name}-%{commit}
git checkout %{commit}


%build
cd %{real_name}-%{commit}
./autogen.sh --help
%configure
# Don't use rpath!
sed -i 's|/lib /usr/lib|/lib /usr/lib /lib64 /usr/lib64|' libtool
%make_build

%install
cd %{real_name}-%{commit}
%make_install
# Avoid multilib conflicts in vala-gen-introspect
mv %{buildroot}%{_bindir}/vala-gen-introspect-%{api_ver}{,-`uname -m`}
echo -e '#!/bin/sh\nexec %{_bindir}/vala-gen-introspect-%{api_ver}-`uname -m` "$@"' > \
  %{buildroot}%{_bindir}/vala-gen-introspect-%{api_ver}
  chmod +x %{buildroot}%{_bindir}/vala-gen-introspect-%{api_ver}

find %{buildroot} -name '*.la' -delete

install -D -m 644 COPYING %{buildroot}%{_datadir}/licenses/%{real_name}/COPYING
install -D -m 644 NEWS %{buildroot}%{_docdir}/%{real_name}/NEWS
install -D -m 644 README.md %{buildroot}%{_docdir}/%{real_name}/README.md

%check
cd %{real_name}-%{commit}
# https://gitlab.gnome.org/GNOME/vala/-/issues/1416
export -n VALAFLAGS
%make_build check


%files
%license %{_datadir}/licenses/%{real_name}/COPYING
%doc %{_docdir}/%{real_name}/NEWS
%doc %{_docdir}/%{real_name}/README.md
%{_bindir}/vala
%{_bindir}/vala-%{api_ver}
%{_bindir}/valac
%{_bindir}/valac-%{api_ver}
%{_bindir}/vala-gen-introspect
%{_bindir}/vala-gen-introspect-%{api_ver}*
%{_bindir}/vapigen
%{_bindir}/vapigen-%{api_ver}
%{_libdir}/pkgconfig/vapigen*.pc
%{_libdir}/vala-%{api_ver}/
%{_datadir}/aclocal/vala.m4
%{_datadir}/aclocal/vapigen.m4
%{_datadir}/vala/
%{_datadir}/vala-%{api_ver}/
%{_mandir}/man1/valac.1*
%{_mandir}/man1/valac-%{api_ver}.1*
%{_mandir}/man1/vala-gen-introspect.1*
%{_mandir}/man1/vala-gen-introspect-%{api_ver}.1*
%{_mandir}/man1/vapigen.1*
%{_mandir}/man1/vapigen-%{api_ver}.1*

%files -n libvala-nightly
%license %{_datadir}/licenses/%{real_name}/COPYING
%{_libdir}/libvala-%{api_ver}.so.*

%files -n libvala-nightly-devel
%{_includedir}/vala-%{api_ver}
%{_libdir}/libvala-%{api_ver}.so
%{_libdir}/pkgconfig/libvala-%{api_ver}.pc

# %files doc
# %doc %{_datadir}/devhelp/books/vala-%{api_ver}

%files -n valadoc-nightly
%{_bindir}/valadoc
%{_bindir}/valadoc-%{api_ver}
%{_libdir}/libvaladoc-%{api_ver}.so.0*
%{_libdir}/valadoc-%{api_ver}/
%{_datadir}/valadoc-%{api_ver}/
%{_mandir}/man1/valadoc-%{api_ver}.1*
%{_mandir}/man1/valadoc.1*

%files -n valadoc-nightly-devel
%{_includedir}/valadoc-%{api_ver}/
%{_libdir}/libvaladoc-%{api_ver}.so
%{_libdir}/pkgconfig/valadoc-%{api_ver}.pc


%changelog
* Wed May 10 2023 Lleyton Gray <lleyton@fyralabs.com> - 0.58.0
- Initial Package
