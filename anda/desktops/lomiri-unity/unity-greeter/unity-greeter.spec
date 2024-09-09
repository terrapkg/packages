%global rn 1

Name:           unity-greeter
Version:        24.10.1
Release:        1%?dist
Summary:        Unity Greeter for Lightdm

License:        GPL-3.0
URL:            https://launchpad.net/unity-greeter
Source0:        http://archive.ubuntu.com/ubuntu/pool/universe/u/unity-greeter/unity-greeter_%version-0ubuntu%rn.tar.xz
Patch1:         0001-Remove-libido.patch

BuildRequires: automake libtool gnome-common
BuildRequires: intltool
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gdk-x11-3.0)
BuildRequires: pkgconfig(indicator3-0.4)
BuildRequires: pkgconfig(liblightdm-gobject-1)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(cairo-ft)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: vala
BuildRequires: unity-settings-daemon-devel
Requires:      unity-shell
Requires:      unity-settings-daemon
Requires:      lightdm%{?_isa}

%description
The greeter (login screen) application for Unity.
It is implemented as a LightDM greeter.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 \
./autogen.sh

%configure --disable-static

%make_build

%install
%make_install

%find_lang %{name}

%ldconfig_post

%pre
%{_sbindir}/update-alternatives \
  --remove lightdm-greeter \
  %{_datadir}/xgreeters/unity-greeter.desktop 2> /dev/null ||:

%postun
if [ ${1} -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files -f %{name}.lang
%doc NEWS
%license COPYING
%{_sbindir}/unity-greeter
%{_datadir}/glib-2.0/schemas/com.canonical.unity-greeter.gschema.xml
%dir %{_datadir}/unity-greeter
%{_datadir}/unity-greeter/*.png
%{_datadir}/unity-greeter/*.svg
%{_datadir}/xgreeters/unity-greeter.desktop
%{_mandir}/man1/unity-greeter.1.gz

%changelog
%autochangelog
