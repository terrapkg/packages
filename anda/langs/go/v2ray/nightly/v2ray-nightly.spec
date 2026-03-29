%global commit  cf7577f650f97226d34a4e7ab6e30b765a15677a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver v5.47.0
%global commit_date 20260327

%global goipath         github.com/v2fly/v2ray-core
Version:                %{ver}^%{commit_date}git.%{shortcommit}

%global golicenses      LICENSE
%global godocs          README.md SECURITY.md 

%gometa -f

Name:           v2ray-nightly
Release:        1%{?dist}
Summary:        A platform for building proxies to bypass network restrictions
License:        MIT
Packager:       veuxit <erroor234@gmail.com>
URL:            %{gourl}
Source:         %{gosource}
Conflicts:      v2ray

Requires:       v2ray-geoip v2ray-domain-list-community

BuildRequires:  go go-rpm-macros go-srpm-macros anda-srpm-macros

%description
%summary.

%gopkg

%prep
%goprep_online -A


%build
%gobuild -o v2ray ./main


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
* Sun Mar 8 2026 veuxit <erroor234@gmail.com> - 5.44.1^20260228git.9cf6a45-1
- Initial package release
