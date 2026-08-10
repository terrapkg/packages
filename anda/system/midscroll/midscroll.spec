%global appid io.github.gnhen.midscroll

Name:		midscroll
Version:	1.14
Release:    1%{?dist}
Summary:	FOSS Middle Mouse Scroll replacement for Linux
License:	Unlicense
URL:		https://github.com/gnhen/midscroll
Source0:	%{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:  noarch
Packager:   Owen Zimmerman <owen@fyralabs.com>

Requires:       python3
Requires:       python3-evdev
# Overlay and settings GUI (GTK)
Requires:       python3-gobject
Requires:       python3-cairo
Requires:       gtk4
Requires:       gtk4-layer-shell
Requires:       librsvg2
Requires:       kdotool
# Settings GUI applies changes as root through pkexec
Requires:       polkit
# Focus detection on X11 sessions (app blacklist)
Recommends:     xprop
BuildRequires:  systemd-rpm-macros

%description
%{summary}.

%prep
%autosetup -C

%build

%install
install -Dm755 midscroll.py                         %{buildroot}%{_bindir}/midscroll
install -Dm755 midscroll-overlay.py                 %{buildroot}%{_bindir}/midscroll-overlay
install -Dm755 midscroll-settings.py                %{buildroot}%{_bindir}/midscroll-settings
install -Dm755 midscroll-apply.py                   %{buildroot}%{_bindir}/midscroll-apply
install -Dm644 %{appid}.Settings.desktop            %{buildroot}%{_appsdir}/%{appid}.Settings.desktop
install -Dm644 %{appid}.policy                      %{buildroot}%{_datadir}/polkit-1/actions/%{appid}.policy
install -Dm644 systemd/midscroll.service            %{buildroot}%{_unitdir}/midscroll.service
install -Dm644 systemd/midscroll-overlay.service    %{buildroot}%{_userunitdir}/midscroll-overlay.service
install -Dm644 icons/move-vertical.svg              %{buildroot}%{_datadir}/midscroll/move-vertical.svg
install -Dm644 icons/move-vertical.svg              %{buildroot}%{_scalableiconsdir}/midscroll.svg
install -Dm644 midscroll.conf                       %{buildroot}%{_sysconfdir}/midscroll.conf
install -Dm644 %{appid}.Settings.metainfo.xml       %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml

%post
%systemd_post midscroll.service
%systemd_user_post midscroll-overlay.service

%preun
%systemd_preun midscroll.service
%systemd_user_preun midscroll-overlay.service

%postun
%systemd_postun_with_restart midscroll.service
%systemd_user_postun_with_restart midscroll-overlay.service

%files
%license LICENSE
%doc README.md SECURITY.md
%{_bindir}/midscroll
%{_bindir}/midscroll-overlay
%{_bindir}/midscroll-settings
%{_bindir}/midscroll-apply
%{_appsdir}/%{appid}.Settings.desktop
%{_datadir}/polkit-1/actions/%{appid}.policy
%{_unitdir}/midscroll.service
%{_userunitdir}/midscroll-overlay.service
%{_datadir}/midscroll/move-vertical.svg
%{_scalableiconsdir}/midscroll.svg
%config %{_sysconfdir}/midscroll.conf
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Mon Aug 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
