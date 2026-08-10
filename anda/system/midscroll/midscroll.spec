Name:		midscroll
Version:	1.14
Release:        1%{?dist}
Summary:	FOSS Middle Mouse Scroll replacement for Linux
License:	Unlicense
URL:		https://github.com/gnhen/midscroll
Source0:	https://github.com/gnhen/midscroll/archive/refs/tags/v%{version}.tar.gz

%description
%{summary}.

%prep
%autosetup -C

%build

%install
install -Dm755 midscroll.py %{buildroot}%{_bindir}/midscroll
install -Dm755 midscroll-overlay.py %{buildroot}%{_bindir}/midscroll-overlay
install -Dm755 midscroll-settings.py %{buildroot}%{_bindir}/midscroll-settings
install -Dm755 midscroll-apply.py %{buildroot}%{_bindir}/midscroll-apply
install -Dm644 %{appid%.Settings.desktop %{buildroot}%{_appsdir}/%{appid}.Settings.desktop
install -Dm644 %{appid}.policy %{buildroot}%{_datadir}/polkit-1/actions/%{appid%.policy
install -Dm644 systemd/midscroll.service %{buildroot}%{_unitdir}/midscroll.service
install -Dm644 systemd/midscroll-overlay.service %{buildroot}%{_userunitdir}/midscroll-overlay.service
install -Dm644 icons/move-vertical.svg %{buildroot}%{_datadir}/midscroll/move-vertical.svg
install -Dm644 icons/move-vertical.svg %{buildroot}%{_scalableiconsdir}/midscroll.svg
install -Dm644 midscroll.conf %{buildroot}%{_sysconfdir}/midscroll.conf

%files
%license
%doc


%changelog
%autochangelog

