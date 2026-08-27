%global commit 8020f9208e6c023086837ea07deaa9210bf50729
%global commit_date 20260827
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global latest_stable_version 2021.01

%global realname openscad
Name:           %{realname}-nightly
Version:        %{latest_stable_version}^%{commit_date}git.%{shortcommit}
Release:        1%{?dist}
Summary:        The Programmers Solid 3D CAD Modeller
# OpenSCAD is GPL-2.0-only WITH CGAL-linking-exception
# Appdata file is CC0-1.0
# Examples are CC0-1.0
License:        GPL-2.0-only WITH CGAL-linking-exception AND CC0-1.0
URL:            https://github.com/openscad/openscad
Packager:       Jan200101 <sentrycraft123@gmail.com>

ExcludeArch:    %{ix86}

BuildRequires:  CGAL-devel >= 3.6
BuildRequires:  ImageMagick
BuildRequires:  bison >= 2.4
BuildRequires:  boost-devel >= 1.35
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  double-conversion-devel
BuildRequires:  eigen3-devel
BuildRequires:  flex >= 2.5.35
BuildRequires:  freetype-devel >= 2.4
BuildRequires:  fontconfig-devel >= 2.10
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glew-devel >= 1.6
BuildRequires:  glib2-devel
BuildRequires:  gmp-devel >= 5.0.0
BuildRequires:  harfbuzz-devel >= 0.9.19
BuildRequires:  libspnav-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mesa-dri-drivers
BuildRequires:  mpfr-devel >= 3.0.0
BuildRequires:  opencsg-devel >= 1.3.2
BuildRequires:  procps-ng
BuildRequires:  python3-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qscintilla-qt6-devel
BuildRequires:  pkgconfig(libzip)
BuildRequires:  lib3mf-devel
BuildRequires:  manifold-devel
BuildRequires:  polyclipping2-devel
BuildRequires:  git-core
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(tbb)

Requires:       font(liberationmono)
Requires:       font(liberationsans)
Requires:       font(liberationserif)
Requires:       hicolor-icon-theme
Recommends:     %{name}-MCAD = %{version}-%{release}

Conflicts:      %{realname}
Provides:       %{realname}

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.

%package        MCAD
Summary:        OpenSCAD Parametric CAD Library
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-only AND LGPL-3.0-or-later AND (GPL-3.0-only OR LGPL-2.1-only) AND (GPL-3.0-or-later OR LGPL-2.1-or-later) AND (CC-BY-SA-3.0 OR LGPL-2.0-or-later) AND CC-BY-3.0 AND BSD-2-Clause AND MIT AND LicenseRef-Fedora-Public-Domain
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    MCAD
This library contains components commonly used in designing and moching up
mechanical designs. It is currently unfinished and you can expect some API    
changes, however many things are already working.

%prep
%setup -Tc
git clone %{URL}.git $PWD
git checkout %{commit}
git submodule update --init --recursive

%conf
%cmake \
    -DUSE_QT6:BOOL=ON \
    -DUSE_MIMALLOC:BOOL=OFF \
    -DUSE_BUILTIN_CLIPPER2:BOOL=OFF \
    -DUSE_CCACHE:BOOL=OFF \
    -DUSE_BUILTIN_MANIFOLD:BOOL=OFF \
    -DUSE_BUILTIN_OPENCSG:BOOL=OFF

%build
%cmake_build

%install
%cmake_install

%__desktop_file_edit --set-key="Name" --set-value="OpenSCAD (Nightly)" %{buildroot}%{_appsdir}/%{realname}.desktop

rm -rf %{buildroot}%{_datadir}/%{realname}/fonts
%find_lang %{realname}

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{realname}.desktop

%files -f %{realname}.lang
%license COPYING
%doc README.md RELEASE_NOTES.md
%attr(755,root,root) %{_bindir}/%{realname}
%{_metainfodir}/*.xml
%{_appsdir}/%{realname}.desktop
%{_hicolordir}/*/apps/%{realname}.png
%{_datadir}/mime/packages/%{realname}.xml
%dir %{_datadir}/%{realname}
%{_datadir}/%{realname}/examples/
%{_datadir}/%{realname}/color-schemes/
%dir %{_datadir}/%{realname}/locale
%dir %{_datadir}/%{realname}/libraries
%{_datadir}/%{realname}/templates/
%{_datadir}/%{realname}/shaders
%{_mandir}/man1/*

%files MCAD
%license libraries/MCAD/lgpl-2.1.txt
%doc libraries/MCAD/README.markdown
%doc libraries/MCAD/TODO
%{_datadir}/%{realname}/libraries/MCAD

%changelog
* Wed Aug 19 2026 Jan200101 <sentrycraft123@gmail.com> - 0~20260819git.1ee676b-1
- Initial package
