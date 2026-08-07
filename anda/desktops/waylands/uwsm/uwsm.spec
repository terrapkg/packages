Name:           uwsm
Version:        0.26.6
Release:        1%{?dist}
Summary:        Universal Wayland Session Manager
URL:            https://github.com/Vladimir-csp/uwsm
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch


License:        MIT
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-dbus
BuildRequires:  python3-pyxdg
BuildRequires:  scdoc
BuildRequires:  systemd-rpm-macros

Requires:       python3
Requires:       python3-dbus
Requires:       python3-pyxdg
Requires:       util-linux

Recommends:     /usr/bin/notify-send
Recommends:     /bin/whiptail
Recommends:     wofi

# We require you to add yourself as the packager here (if this is an issue for you, let us know):
Packager:       Marcelo dos Santos Mafra <msmafra@gmail.com>

%description
Universal Wayland Session Manager
Provides a set of Systemd units and helpers to set up the environment and
manage standalone Wayland compositor sessions.

%prep
%autosetup

%conf
%meson -Duuctl=enabled -Dfumon=enabled -Duwsm-app=enabled

%build
%meson_build

%install
%meson_install
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/modules

%check
%desktop_file_validate %{buildroot}%{_datadir}/applications/*.desktop

%post
%systemd_user_post fumon.service

%preun
%systemd_user_preun fumon.service

%postun
%systemd_user_postun fumon.service


%files
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/example-units/
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-app
%{_bindir}/%{name}-terminal
%{_bindir}/%{name}-terminal-scope
%{_bindir}/%{name}-terminal-service
%{_bindir}/fumon
%{_bindir}/uuctl
%{_libexecdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/uuctl.desktop
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-app.1*
%{_mandir}/man1/fumon.1*
%{_mandir}/man1/uuctl.1*
%{_mandir}/man3/%{name}-plugins.3*
%{_userunitdir}/fumon.service
%{_userunitdir}/*-graphical.slice
%{_userunitdir}/wayland-*.service
%{_userunitdir}/wayland-*.target
%{_userpresetdir}/80-fumon.preset

%changelog
* Tue Jul 14 2026 Marcelo dos Santos Mafra <msmafra@gmail.com> - 0.26.6-3
- Initial package
