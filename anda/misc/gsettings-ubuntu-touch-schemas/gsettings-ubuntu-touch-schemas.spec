Name:           gsettings-ubuntu-touch-schemas
Version:        0.0.7+21.10.20210712
Release:        %autorelease
Summary:        Shared GSettings schemas for Ubuntu touch and Unity
BuildArch:      noarch

License:        GPL-2.0 AND LGPL-2.0
URL:            https://launchpad.net/gsettings-ubuntu-touch-schemas
Source0:        http://archive.ubuntu.com/ubuntu/pool/main/g/gsettings-ubuntu-touch-schemas/gsettings-ubuntu-touch-schemas_%{version}.orig.tar.gz

BuildRequires: automake libtool gnome-common
BuildRequires: intltool
BuildRequires: make
BuildRequires: gcc
BuildRequires: g++
BuildRequires: glib2-devel
BuildRequires: gsettings-desktop-schemas-devel

%description
gsettings-ubuntu-touch-schemas contains a collection of GSettings schemas for
settings shared by various components of a Ubuntu environment.

%prep
%autosetup -c

%build
NOCONFIGURE=1 \
./autogen.sh

%configure
%make_build

%install
%make_install
rm -fv %{buildroot}%{_libdir}/*.la

%files
%license COPYING
%{_datadir}/accountsservice/interfaces/*.xml
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/pkgconfig/gsettings-unity-schemas.pc
%{_datadir}/polkit-1/actions/com.ubuntu.AccountsService.policy
%{_sharedstatedir}/polkit-1/localauthority/10-vendor.d/50-com.ubuntu.AccountsService.pkla

%changelog
%autochangelog
