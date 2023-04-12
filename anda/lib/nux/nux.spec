%global forgeurl https://gitlab.com/ubuntu-unity/unity-x/nux
%global commit a1cd0bd379000ab8aa159aec48dfae87edb6ad9f
%forgemeta

Name:           nux
Version:        4.0.8
Release:        %autorelease
Summary:        An OpenGL toolkit

License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.0-or-later
URL:            https://gitlab.com/ubuntu-unity/unity-x/nux
Source0:        %{url}/-/archive/%commit/nux-%commit.tar.bz2
Patch0:         https://gitlab.com/cat-master21/nux/-/commit/0e834a556818281b9e023b47f0667e8da0f5cebd.patch

BuildRequires: automake libtool gnome-common
BuildRequires: intltool
BuildRequires: make
BuildRequires: git
BuildRequires: gcc
BuildRequires: g++
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXext-devel
BuildRequires: xorg-x11-server-devel
BuildRequires: libsigc++20-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: cairo-devel
BuildRequires: libpng-devel
BuildRequires: libglvnd-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: glew-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXinerama-devel
BuildRequires: pcre-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: pciutils-devel
BuildRequires: glib2-devel
BuildRequires: ibus-devel
BuildRequires: boost-devel
BuildRequires: geis-devel
BuildRequires: glewmx-devel
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)

%description
Visual rendering toolkit for real-time applications.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%autosetup -n nux-%commit -N
git apply %{PATCH0}

%build
NOCONFIGURE=1 \
./autogen.sh

PYTHON=%{__python3}
export PYTHON

%configure \
  --enable-documentation=no \
  --disable-silent-rules \
  --disable-static

%make_build

%install
%make_install
rm -fv %{buildroot}%{_libdir}/*.la %{buildroot}%{python3_sitearch}/*.la
mkdir -p %{buildroot}%{_sysconfdir}/X11/Xsession.d
install -m 0644 debian/50_check_unity_support -t %{buildroot}%{_sysconfdir}/X11/Xsession.d
# Not needed and out of place
rm -rf %{buildroot}%{_datadir}/nux/gputests

%files
%license COPYING COPYING.gpl COPYING.lgpl-v2.1
%{_sysconfdir}/X11/Xsession.d/50_check_unity_support
%{_libdir}/libnux-4.0.so.*
%{_libdir}/libnux-core-4.0.so.*
%{_libdir}/libnux-graphics-4.0.so.*
%dir %{_libexecdir}/nux
%{_libexecdir}/nux/unity_support_test
%dir %{_datadir}/nux
%dir %{_datadir}/nux/4.0
%{_datadir}/nux/4.0/Fonts/
%{_datadir}/nux/4.0/UITextures/

%files devel
%dir %{_includedir}/Nux-4.0
%{_includedir}/Nux-4.0/Nux/
%{_includedir}/Nux-4.0/NuxCore/
%{_includedir}/Nux-4.0/NuxGraphics/
%{_libdir}/libnux-4.0.so
%{_libdir}/libnux-core-4.0.so
%{_libdir}/libnux-graphics-4.0.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
