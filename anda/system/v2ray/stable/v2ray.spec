%global goipath         github.com/v2fly/v2ray-core
Version:                5.44.1

%global golicenses      LICENSE
%global godocs          README.md SECURITY.md 

Name:           v2ray
Release:        1%?dist
Summary:        A platform for building proxies to bypass network restrictions
License:        MIT
Packager:       veuxit <erroor234@gmail.com>
URL:            https://github.com/v2fly/v2ray-core
Conflicts:      v2ray-nightly

Source0:        https://github.com/v2fly/v2ray-core/archive/refs/tags/v%{version}.tar.gz

Requires:       v2ray-geoip v2ray-domain-list-community

BuildRequires:  go go-rpm-macros go-srpm-macros anda-srpm-macros

%description
%summary.

%gopkg

%prep
%goprep_online -Ae
%autosetup -n v2ray-core-%{version}


%build
export CGO_ENABLED=0
%define gomodulesmode GO111MODULE=on
%gobuild -o v2ray -trimpath -ldflags "-s -w -buildid=" ./main


%install
%gopkginstall
install -Dm755 v2ray %{buildroot}%{_bindir}/v2ray

install -Dm644 release/config/systemd/system/v2ray.service -t %{buildroot}%{_unitdir}/
install -Dm644 release/config/systemd/system/v2ray@.service -t %{buildroot}%{_unitdir}/
install -Dm644 release/config/*.json -t %{buildroot}/%{_sysconfdir}/v2ray/

%post
%systemd_post v2ray.service

%preun
%systemd_preun v2ray.service

%postun
%systemd_postun_with_restart v2ray.service

%files
%doc README.md
%doc SECURITY.md
%license LICENSE
%{_bindir}/v2ray
%{_unitdir}/v2ray.service
%{_unitdir}/v2ray@.service
%{_sysconfdir}/v2ray/config.json
%{_sysconfdir}/v2ray/vpoint_socks_vmess.json
%{_sysconfdir}/v2ray/vpoint_vmess_freedom.json

%gopkgfiles

%changelog
* Sun Mar 8 2026 veuxit <erroor234@gmail.com> - 5.44.1-1
- Initial package release
