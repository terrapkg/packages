# Disabled because compiled without debug

%global goipath         github.com/XTLS/Xray-core
Version:                26.2.6

%global golicenses      LICENSE
%global godocs          README.md SECURITY.md CODE_OF_CONDUCT.md

Name:           xray
Release:        1%?dist
Summary:        High-performance, open-source network proxy engine and toolset designed to bypass internet censorship and enhance privacy
License:        MPL-2.0
Packager:       veuxit <erroor234@gmail.com>
URL:            https://github.com/XTLS/Xray-core
Conflicts:      xray-nightly

Source0:        https://github.com/XTLS/Xray-core/archive/refs/tags/v%{version}.tar.gz
Source1:        xray.service
Source2:        xray@.service
Source3:        xray.sysusers
Source4:        xray.tmpfiles

Requires:       v2ray-geoip v2ray-domain-list-community

BuildRequires:  go go-rpm-macros go-srpm-macros anda-srpm-macros

%description
%summary.

%gopkg

%prep
%goprep_online -Ae
%autosetup -n Xray-core-%{version}


%build
%define gomodulesmode GO111MODULE=on
%gobuild -o xray ./main

%install
%gopkginstall
install -Dm755 xray %{buildroot}%{_bindir}/xray
install -d "%{buildroot}/etc/xray" "%{buildroot}%{_datadir}/xray"
ln -s %{_datadir}/v2ray/geo{ip,site}.dat -t "%{buildroot}%{_datadir}/xray"
install -Dm644 %{SOURCE1} -t %{buildroot}/%{_unitdir}
install -Dm644 %{SOURCE2} -t %{buildroot}/%{_unitdir}
install -Dm644 %{SOURCE3} %{buildroot}/%{_sysusersdir}/xray.conf
install -Dm644 %{SOURCE4} %{buildroot}/usr/lib/tmpfiles.d/xray.conf

%post
%systemd_post xray.service

%preun
%systemd_preun xray.service

%postun
%systemd_postun_with_restart xray.service

%files
%doc README.md
%doc SECURITY.md
%doc CODE_OF_CONDUCT.md
%license LICENSE
%{_bindir}/xray
%{_datadir}/xray/geoip.dat
%{_datadir}/xray/geosite.dat
%{_unitdir}/xray.service
%{_unitdir}/xray@.service
%{_sysusersdir}/xray.conf
/usr/lib/tmpfiles.d/xray.conf

%gopkgfiles

%changelog
* Sun Mar 8 2026 veuxit <erroor234@gmail.com> - 26.2.6-1
- Initial package release
