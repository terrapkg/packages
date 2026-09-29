Name:           hexagonrpc
Version:        0.5.0
Release:        1%{?dist}
Summary:        FastRPC library and reverse-tunnel daemon for Qualcomm DSPs

License:        GPL-3.0-or-later
URL:            https://github.com/linux-msm/hexagonrpc
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

Patch1:         0001-data-install-units-to-the-canonical-systemd-unit-dir.patch
Patch2:         0002-use-msm-firmware-loader-dir.patch
Patch3:         0003-run-hexagonrpcd-as-root.patch
Patch4:         0004-bring-hexagonrpcd-back-after-resume.patch
Patch5:         0005-gate-hexagonrpcd-on-staged-hexagonfs-tree.patch

BuildRequires:  gcc
BuildRequires:  meson >= 1.1
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros

Recommends:     msm-firmware-loader

Packager:       Owen Zimmerman <owen@fyralabs.com>

%{?systemd_requires}

%description
HexagonRPC talks FastRPC to the Context Hub Runtime Environment running on a
Qualcomm DSP, serving files to it and relaying its remote procedure calls
back to a listener on the application processor.

%package devel
%pkg_devel_files

%prep
%autosetup -C -p1

%conf
%meson

%build
%meson_build

%install
%meson_install

%post
%systemd_post hexagonrpcd-adsp-rootpd.service hexagonrpcd-adsp-sensorspd.service hexagonrpcd-sdsp.service hexagonrpcd-resume.service

%preun
%systemd_preun hexagonrpcd-adsp-rootpd.service hexagonrpcd-adsp-sensorspd.service hexagonrpcd-sdsp.service hexagonrpcd-resume.service

%postun
%systemd_postun_with_restart hexagonrpcd-adsp-rootpd.service hexagonrpcd-adsp-sensorspd.service hexagonrpcd-sdsp.service hexagonrpcd-resume.service

%files
%license COPYING
%doc README.md
%{_bindir}/hexagonrpcd
%dir %{_libexecdir}/hexagonrpc
%{_libexecdir}/hexagonrpc/chrecd
%{_libdir}/libhexagonrpc.so.0.5
%{_unitdir}/hexagonrpcd-adsp-rootpd.service
%{_unitdir}/hexagonrpcd-adsp-sensorspd.service
%{_unitdir}/hexagonrpcd-sdsp.service
%{_unitdir}/hexagonrpcd-resume.service
%{_mandir}/man1/hexagonrpcd.1*

%changelog
* Tue Sep 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
