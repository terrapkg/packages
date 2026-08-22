Name:		OpenLogi
Version:	0.7.4
Release:        1%{?dist}
Summary:	A native, local-first alternative to Logitech Options+
SourceLicense:	Apache-2.0 AND MIT
License:	Apache-2.0 AND MIT
URL:		https://openlogi.org
Source0:	https://github.com/AprilNEA/OpenLogi/archive/refs/tags/v%{version}.tar.gz
Packager:	Owen Zimmerman <owen@fyralabs.com>
BuildRequires:	cargo-rpm-macros
BuildRequires:	systemd-rpm-macros
BuildRequires:	rustc

Provides:	openlogi

%description
⚡️ A native, local-first alternative to Logitech Options+, written in Rust 🦀.
Unlock the full capabilities of Logitech mice, keyboards, and webcams over HID++ and UVC.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
install -Dm755 target/rpm/openlogi				%{buildroot}%{_bindir}/openlogi
install -Dm755 target/rpm/openlogi-desktop			%{buildroot}%{_bindir}/openlogi-desktop
install -Dm755 target/rpm/openlogi-overlay			%{buildroot}%{_bindir}/openlogi-overlay
install -Dm755 target/rpm/openlogi-agent			%{buildroot}%{_bindir}/openlogi-agent
install -Dm644 packaging/linux/udev/70-openlogi.rules		%{buildroot}%{_udevrulesdir}/70-openlogi.rules
install -Dm644 packaging/linux/systemd/openlogi-agent.service	%{buildroot}%{_userunitdir}/openlogi-agent.service
install -Dm644 packaging/linux/desktop/openlogi.desktop		%{buildroot}%{_appsdir}/openlogi.desktop

%dnl /usr/share/icons/hicolor/1024x1024/apps/openlogi.png

%post
%systemd_user_post openlogi.service

%preun
%systemd_user_preun openlogi.service

%postun
%systemd_user_postun_with_restart openlogi.service

%files
%license LICENSE-APACHE LICENSE-MIT
%doc docs/* README.md CHANGELOG.md
%{_bindir}/openlogi
%{_bindir}/openlogi-desktop
%{_bindir}/openlogi-overlay
%{_bindir}/openlogi-agent
%{_udevrulesdir}/70-openlogi.rules
%{_userunitdir}/openlogi-agent.service
%{_appsdir}/openlogi.desktop

%changelog
* Sat Aug 22 2026 Owen Zimmerman <owen@fyralabs.com> - 0.7.4-1 
- Initial commit

