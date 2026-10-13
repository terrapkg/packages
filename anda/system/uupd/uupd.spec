Name:           uupd
Version:        1.5.0
Release:        3%{?dist}
Summary:        Centralized update service/checker made for Universal Blue
License:        Apache-2.0
URL:            https://github.com/ublue-os/uupd
Source0:        %url/archive/refs/tags/v%version.tar.gz
BuildRequires:  golang
BuildRequires:  go-rpm-macros
BuildRequires:  systemd-rpm-macros
Recommends:     bootc
Packager:       Tulip Blossom <tulilirockz@outlook.com>

%description
%{summary}.

%gopkg
%global goipath github.com/ublue-os/uupd
%gometa -f

%prep
%goprep

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{name}

%install
install -Dpm0755 -t %{buildroot}%{_bindir}/ %{name}
install -Dpm0644 -t %{buildroot}%{_unitdir}/ %{name}.service
install -Dpm0644 -t %{buildroot}%{_unitdir}/ %{name}-manual.service
install -Dpm0644 -t %{buildroot}%{_unitdir}/ %{name}.timer
install -Dpm0644 -t %{buildroot}%{_datadir}/polkit-1/rules.d/ %{name}.rules
install -Dpm0644 -t %{buildroot}/%{_sysconfdir}/%{name}/ config.json

%check
go test -v ./...

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%{_unitdir}/%{name}-manual.service
%{_datadir}/polkit-1/rules.d/%{name}.rules
%config(noreplace) %{_sysconfdir}/%{name}/config.json

%changelog
* Tue Oct 13 2026 renner <renner0@posteo.de> - 1.5.0-3
- Retroactively import changelogs for better chunkah stability calculation

* Mon Oct 12 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 1.5.0-2
- add uupd-manual

* Sun Oct 11 2026 Raboneko <raboneko@fyralabs.com> - 1.5.0-1
- Upstream Release v1.5.0

* Sun Sep 6 2026 Owen Zimmerman <owen@fyralabs.com> 1.4.0-3
- call correct systemd unit in post macros

* Sat Sep 5 2026 Hec <hec@heccraft.com> - 1.4.0-2
- Fix location of uupd.rules polkit file

* Mon May 18 2026 Raboneko <raboneko@fyralabs.com> - 1.4.0-1
- Upstream Release v1.4.0

* Sun Apr 19 2026 Tulip Blossom <tulilirockz@outlook.com> - 1.3.0-1
- Initial commit

* Mon Jan 26 2026 Raboneko <raboneko@fyralabs.com> - 1.3.0-1
- Upstream Release v1.3.0
