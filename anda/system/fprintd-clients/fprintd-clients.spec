Name:           fprintd-clients
Version:        
Release:        1%{?dist}
Summary:        D-Bus service to access fingerprint readers
License:        GPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/uunicorn/fprintd
Source0:        %{url}/-/archive/%{version}/fprintd-%{version}.tar.gz?ref_type=tags
Patch0:         0001-Remove-ignored-positional-arguments.patch

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libfprint-2)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(pam_wrapper)
BuildRequires:  pam-devel
BuildRequires:  perl-podlators
BuildRequires:  python3-cairo
BuildRequires:  python3-dbus
BuildRequires:  python3-dbusmock
BuildRequires:  python3-libpamtest
BuildRequires:  gettext

%description
%{summary}.

%package        devel
Summary:        Development libraries for %{name}
Requires:       %{name}

%description    devel
This package contains the development files for %{name}.

%prep
%autosetup -C -p1

%conf
%meson

%build
%meson_build

%install
%meson_install

%find_lang fprintd

%files -f fprintd.lang
%doc README
%license COPYING
%config %{_sysconfdir}/fprintd.conf
%{_bindir}/fprintd-delete
%{_bindir}/fprintd-enroll
%{_bindir}/fprintd-list
%{_bindir}/fprintd-verify
%{_unitdir}/fprintd.service
%{_libexecdir}/fprintd
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml
%{_datadir}/dbus-1/system-services/net.reactivated.Fprint.service
%config %{_datadir}/dbus-1/system.d/net.reactivated.Fprint.conf
%{_mandir}/man1/fprintd.1.gz
%{_mandir}/man8/pam_fprintd.8.gz
%{_datadir}/polkit-1/actions/net.reactivated.fprint.device.policy

%files devel
/%{_lib}/security/pam_fprintd.so

%changelog
* Thu Aug 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
