%global goipath github.com/max-baz/yubikey-touch-detector
Version:        1.13.0

%gometa

Name:           yubikey-touch-detector
Release:        1%{?dist}
Summary:        A tool to detect when your YubiKey is waiting for a touch

License:        ISC
URL:            https://github.com/max-baz/yubikey-touch-detector
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

Packager:       metcya <metcya@gmail.com>

BuildRequires:  go-rpm-macros
BuildRequires:  scdoc
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  systemd-rpm-macros

%description
This is a tool that can detect when YubiKey is waiting for your touch. It is
designed to be integrated with other UI components to display a visible
indicator.

%prep
%goprep

%build
%global gomodulesmode GO111MODULE=on
%gobuild -o %{name}
scdoc < %{name}.1.scd > %{name}.1

%install
install -Dm 755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm 644 %{name}.png %{buildroot}%{_hicolordir}/128x128/apps/%{name}.png
install -Dm 644 %{name}.service %{buildroot}%{_userunitdir}/%{name}.service
install -Dm 644 %{name}.socket %{buildroot}%{_userunitdir}/%{name}.socket
install -Dm 644 service.conf.example %{buildroot}%{_sysconfdir}/%{name}/service.conf

%preun
%systemd_user_preun %{name}.service
%systemd_user_preun %{name}.socket

%post
%systemd_user_post %{name}.service
%systemd_user_post %{name}.socket

%postun
%systemd_user_postun %{name}.service
%systemd_user_postun %{name}.socket

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_hicolordir}/128x128/apps/%{name}.png
%{_userunitdir}/%{name}.service
%{_userunitdir}/%{name}.socket
%{_sysconfdir}/%{name}/service.conf

%changelog
* Wed Mar 18 2026 metcya <metcya@gmail.com>
- Initial package
