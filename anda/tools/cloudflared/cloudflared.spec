%global goipath         github.com/cloudflare/cloudflared
Version:                2026.10.7

%gometa -f

# Older Fedora and RHEL's debugedit can't parse the DWARF from the Go 1.27 toolchain
%if 0%{?fedora} && 0%{?fedora} < 45 || 0%{?rhel}
%global debug_package %{nil}
%endif

Name:           cloudflared
Release:        1%{?dist}
Summary:        Cloudflare Tunnel client

License:        Apache-2.0
URL:            https://github.com/cloudflare/cloudflared
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Source1:        cloudflared.service

BuildRequires:  anda-srpm-macros
BuildRequires:  systemd-rpm-macros

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
cloudflared is the command-line client for Cloudflare Tunnel, a tunneling
daemon that proxies traffic from the Cloudflare network to your origins.

%prep
%goprep_online -A

%build
export GOFIPS140=off
# go.mod may require a newer Go than older Fedora releases ship; let Go fetch it
export GOTOOLCHAIN=auto
export GOPROXY=https://proxy.golang.org,direct
%global build_date %(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} '+%%Y-%%m-%%dT%%H:%%MZ')
%define currentgoldflags -X main.Version=%{version} -X main.BuildTime=%{build_date} -X %{goipath}/cmd/cloudflared/updater.BuiltForPackageManager=dnf
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd/%{name}
sed -e 's/\${VERSION}/%{version}/; s/\${DATE}/%{build_date}/' cloudflared_man_template > cloudflared.1

%install
install -Dm755 %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 cloudflared.1 %{buildroot}%{_mandir}/man1/cloudflared.1
install -Dm644 %{SOURCE1} %{buildroot}%{_unitdir}/cloudflared.service
install -dm755 %{buildroot}%{_sysconfdir}/cloudflared

%post
%systemd_post cloudflared.service

%preun
%systemd_preun cloudflared.service

%postun
%systemd_postun_with_restart cloudflared.service

%files
%license LICENSE
%doc README.md RELEASE_NOTES
%{_bindir}/cloudflared
%{_mandir}/man1/cloudflared.1*
%{_unitdir}/cloudflared.service
%dir %{_sysconfdir}/cloudflared

%changelog
* Sat Oct 17 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
