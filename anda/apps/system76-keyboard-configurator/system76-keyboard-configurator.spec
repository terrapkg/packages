Name:          system76-keyboard-configurator
Version:       1.3.12
Release:       1%{dist}
Summary:       System76 Keyboard Configurator

License:       GPL-3.0-or-later AND Apache-2.0 AND MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL:           https://github.com/pop-os/keyboard-configurator
Source:        https://github.com/pop-os/keyboard-configurator/archive/refs/tags/v1.3.12.tar.gz


BuildRequires: anda-srpm-macros
BuildRequires: desktop-file-utils
BuildRequires: cargo-rpm-macros
BuildRequires: gtk3-devel
BuildRequires: cargo
BuildRequires: rust
BuildRequires: gtk4-devel
BuildRequires: libusb1-devel


%description
Application for configuration of System76 keyboard firmware.


%prep
%autosetup -n keyboard-configurator-%{version}
%cargo_prep_online

%install
%cargo_install
%__install -D -m 0644 -vp linux/com.system76.keyboardconfigurator.desktop                %{buildroot}%{_datadir}/applications/com.system76.keyboardconfigurator.desktop
%__install -D -m 0644 -vp linux/com.system76.keyboardconfigurator.appdata.xml            %{buildroot}%{_datadir}/metainfo/com.system76.keyboardconfigurator.appdata.xml
%__install -D -m 0644 -vp data/icons/scalable/apps/com.system76.keyboardconfigurator.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.system76.keyboardconfigurator.svg
%__install -D -m 0644 -vp debian/com.system76.pkexec.keyboardconfigurator.policy         %{buildroot}%{_datadir}/polkit-1/actions/com.system76.pkexec.keyboardconfigurator.policy

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/com.system76.keyboardconfigurator.desktop
%{_datadir}/metainfo/com.system76.keyboardconfigurator.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/com.system76.keyboardconfigurator.svg
%{_datadir}/polkit-1/actions/com.system76.pkexec.keyboardconfigurator.policy


%changelog
* Sun Feb 15 2026 Jaiden Riordan <jade@fyralabs.com> - 1.3.12
- Port to Terra
