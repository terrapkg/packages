%global appid com.github.opengamingcollective.cardwire

Name:           cardwire
Version:        0.11.1
Release:        2%{?dist}
Summary:        A GPU Manager for linux that uses eBPF LSM hooks to block GPUs
URL:            https://opengamingcollective.github.io/cardwire/
Source0:        https://github.com/OpenGamingCollective/cardwire/archive/refs/tags/v%{version}.tar.gz
Source1:        %{appid}.metainfo.xml
SourceLicense:  GPL-3.0-or-later
License:        (BSD-3-Clause OR MIT OR Apache-2.0) AND Unlicense AND Apache-2.0 AND MIT AND (MIT OR Apache-2.0 OR Zlib) AND BSD-2-Clause AND Zlib AND MIT AND (Apache-2.0 OR GPL-2.0-only) AND GPL-3.0 AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND MPL-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND CC0-1.0 AND BSL-1.0 AND ISC AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
Provides:       switcheroo-control
Conflicts:      switcheroo-control
BuildRequires:  cargo-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd-devel
BuildRequires:  libbpf-devel
BuildRequires:  clang-devel

Requires: hwdata
Requires: upower

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%package        gui
Summary:        GUI for cardwire
Requires:       %{name} = %{evr}

%description    gui
%{summary}.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build

%install
install -Dm0755 target/rpm/cardwire %{buildroot}%{_bindir}/cardwire
install -Dm0755 target/rpm/cardwired %{buildroot}%{_bindir}/cardwired
install -Dm0644 assets/cardwired.service %{buildroot}%{_unitdir}/cardwired.service
install -Dm0644 assets/com.github.opengamingcollective.cardwire.conf %{buildroot}%{_datadir}/dbus-1/system.d/com.github.opengamingcollective.cardwire.conf
install -Dm755 target/release/cardwire-gui %{buildroot}%{_bindir}/cardwire-gui
install -Dm644 assets/cardwire-gui.desktop %{buildroot}%{_appsdir}/cardwire-gui.desktop
for icon in assets/icons/*.svg; do
	install -Dm644 "$icon" %{buildroot}%{_scalableiconsdir}/$(basename "$icon")
done

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%terra_appstream -o %{S:1}

%post
%systemd_post cardwired.service

%preun
%systemd_preun cardwired.service

%postun
%systemd_postun_with_restart cardwired.service

%files
%license LICENSE
%license LICENSE.dependencies
%{_bindir}/cardwire
%{_bindir}/cardwired
%{_unitdir}/cardwired.service
%config %{_datadir}/dbus-1/system.d/com.github.opengamingcollective.cardwire.conf

%files gui
%{_scalableiconsdir}/*.svg
%{_bindir}/cardwire-gui
%{_appsdir}/cardwire-gui.desktop
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Sat Aug 01 2026 Owen Zimmerman <owen@fyralabs.com>
- Add cardwire-gui subpackage

* Wed May 06 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
