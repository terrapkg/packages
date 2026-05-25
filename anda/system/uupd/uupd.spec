Name:           uupd
Version:        1.3.0
Release:        1%?dist
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
install -Dpm0644 -t %{buildroot}%{_unitdir}/ %{name}.service %{name}.timer
install -Dpm0644 -t %{buildroot}%{_sysconfdir}/polkit-1/rules.d/%{name}.rules %{name}.rules

%post
%systemd_post %{name}.timer

%preun
%systemd_preun %{name}.timer

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%{_sysconfdir}/polkit-1/rules.d/%{name}.rules

%changelog
* Sun Apr 19 2026 Tulip Blossom <tulilirockz@outlook.com>
- Initial commit
