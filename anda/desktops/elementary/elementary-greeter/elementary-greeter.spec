%global srcname greeter
%global appname io.elementary.greeter

Name:           elementary-greeter
Summary:        LightDM Login Screen for the elementary desktop
Version:        7.0.0
Release:        1%{?dist}
License:        GPL-3.0

URL:            https://github.com/elementary/greeter
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Source1:        40-%{appname}.conf

Patch0:         https://github.com/elementary/greeter/compare/7.0.0..42320c266395606b0c20782603e7407124c3f7a4.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  mesa-libEGL-devel

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite) >= 5.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(liblightdm-gobject-1)
BuildRequires:  pkgconfig(mutter-clutter-14)
BuildRequires:  pkgconfig(mutter-cogl-14)
BuildRequires:  pkgconfig(mutter-cogl-pango-14)
BuildRequires:  pkgconfig(x11)

Provides:       pantheon-greeter = %{version}-%{release}
Obsoletes:      pantheon-greeter < 3.2.0-7

Requires:       lightdm%{?_isa}
Requires:       wingpanel%{?_isa}

# runtime requirement for numlock capture
Requires:       numlockx

# requirements for default artwork
Requires:       elementary-icon-theme
Requires:       elementary-theme-gtk3
Requires:       elementary-wallpapers

# requirements for accountsservice extension
Requires:       pantheon-session-settings >= 30.90

# all LightDM greeters provide this
Provides:       lightdm-greeter = 1.2

# alternate descriptive names
Provides:       lightdm-%{name} = %{version}-%{release}
Provides:       lightdm-%{name}%{?_isa} = %{version}-%{release}

%description
The elementary Greeter is a styled Login Screen for LightDM.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# install LightDM configuration file
mkdir -p %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d
install -pm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml


%files -f %{appname}.lang
%doc README.md
%license LICENSE

%config(noreplace) %{_sysconfdir}/lightdm/%{appname}.conf
%config(noreplace) %{_sysconfdir}/lightdm/lightdm.conf.d/40-%{appname}.conf

%{_bindir}/%{appname}-compositor
%{_sbindir}/%{appname}

%{_datadir}/xgreeters/%{appname}.desktop
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/lightdm/lightdm.conf.d/40-%appname.conf


%changelog
* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com> - 6.1.0-1
- Repackaged for Terra
