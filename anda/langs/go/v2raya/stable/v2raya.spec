%global goipath         github.com/v2rayA/v2rayA
Version:                2.3.4

%global golicenses      LICENSE
%global godocs          README.md 

%gometa -f

Name:           v2raya
Release:        1%{?dist}
Summary:        A web GUI client of Project V which supports VMess, VLESS, SS, SSR, Trojan, Tuic and Juicity protocols
License:        AGPL-3.0-only
URL:            %{gourl}
Source:         %{gosource}
Packager:       veuxit <erroor234@gmail.com>
Conflicts:      v2raya-nightly

Requires:       v2ray-geoip v2ray-domain-list-community ((v2ray or v2ray-nightly) or (xray or xray-nightly))

BuildRequires:  go go-rpm-macros go-srpm-macros anda-srpm-macros nodejs yarnpkg desktop-file-utils

%description
%summary.

%gopkg

%prep
%goprep_online -A

%build
pushd gui
yarn --ignore-engines && OUTPUT_DIR=$(pwd)/../service/server/router/web yarn --ignore-engines build
popd

pushd service
%define gomodulesmode GO111MODULE=on
%define currentgoldflags -X github.com/v2rayA/v2rayA/conf.Version=%{version}
export GO_BUILDTAGS="with_gvisor"
%gobuild -o ../v2raya

%install
%gopkginstall
install -Dm 755 v2raya -t %{buildroot}/%{_bindir}
install -Dm 644 install/universal/v2raya.desktop -t %{buildroot}/%{_appsdir}/
install -Dm 644 install/universal/v2raya.service -t %{buildroot}/%{_unitdir}/
install -Dm 644 install/universal/v2raya-lite.service -t %{buildroot}/%{_userunitdir}/
install -Dm 644 install/universal/v2raya.default -t %{buildroot}/%{_sysconfdir}/default/v2raya.conf
install -Dm 644 gui/public/img/icons/android-chrome-512x512.png %{buildroot}/%{_hicolordir}/512x512/apps/v2raya.png

%check
%desktop_file_validate %{buildroot}/%{_appsdir}/v2raya.desktop

%post
%systemd_post v2raya.service

%preun
%systemd_preun v2raya.service

%postun
%systemd_postun_with_restart v2raya.service

%files
%doc README.md
%license LICENSE
%{_bindir}/v2raya
%{_unitdir}/v2raya.service
%{_userunitdir}/v2raya-lite.service
%{_sysconfdir}/default/v2raya.conf
%{_appsdir}/v2raya.desktop
%{_hicolordir}/512x512/apps/v2raya.png

%gopkgfiles

%changelog
* Sun Mar 8 2026 veuxit <erroor234@gmail.com> - 2.2.7.5-1
- Initial package release
