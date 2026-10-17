%global goipath         github.com/cloudflare/cloudflared
Version:                2026.10.1

%gometa -f

Name:           cloudflared
Release:        1%{?dist}
Summary:        Cloudflare Tunnel client

License:        Apache-2.0
URL:            https://github.com/cloudflare/cloudflared
Source:         %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  anda-srpm-macros

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
cloudflared is the command-line client for Cloudflare Tunnel, a tunneling
daemon that proxies traffic from the Cloudflare network to your origins.

%prep
%goprep_online -A

%build
export GOFIPS140=off
%global build_date %(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} '+%%Y-%%m-%%dT%%H:%%MZ')
%define currentgoldflags -X main.Version=%{version} -X main.BuildTime=%{build_date} -X %{goipath}/cmd/cloudflared/updater.BuiltForPackageManager=dnf
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd/%{name}
sed -e 's/\${VERSION}/%{version}/; s/\${DATE}/%{build_date}/' cloudflared_man_template > cloudflared.1

%install
install -Dm755 %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 cloudflared.1 %{buildroot}%{_mandir}/man1/cloudflared.1

%files
%license LICENSE
%doc README.md RELEASE_NOTES
%{_bindir}/cloudflared
%{_mandir}/man1/cloudflared.1*

%changelog
* Sat Oct 17 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
