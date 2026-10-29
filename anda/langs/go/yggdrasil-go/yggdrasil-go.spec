%global goipath     github.com/yggdrasil-network/yggdrasil-go
Version:            0.5.15

%global golicenses  LICENSE
%global godocs      README.md

%gometa -f

Name:           yggdrasil-go
Release:        1%{?dist}
Summary:        An experiment in scalable routing as an encrypted IPv6 overlay network
License:        LGPL-3.0-only
URL:            https://yggdrasil-network.github.io/
Source0:        %{gosource}
Source1:        yggdrasil.sysusers
Packager:       Red Earth <redearth@50335033.xyz>

%{?systemd_requires}
BuildRequires:  systemd-rpm-macros
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go-srpm-macros
BuildRequires:  anda-srpm-macros

%description
Yggdrasil is a proof-of-concept to explore a wholly different approach to
network routing. Whereas current computer networks depend heavily on very
centralised design and configuration, Yggdrasil breaks this mould by making
use of a global spanning tree to form a scalable IPv6 encrypted mesh network.

%gopkg

%prep
%goprep_online -A

%build
%global currentgoldflags %{?currentgoldflags} -X github.com/yggdrasil-network/yggdrasil-go/src/version.buildName=yggdrasil
%global currentgoldflags %{?currentgoldflags} -X github.com/yggdrasil-network/yggdrasil-go/src/version.buildVersion=%{version}

for bin in yggdrasil yggdrasilctl genkeys; do
    %gobuild "./cmd/${bin}"
done

%install
install -D -p -m 0755 yggdrasil %{buildroot}%{_bindir}/yggdrasil
install -D -p -m 0755 yggdrasilctl %{buildroot}%{_bindir}/yggdrasilctl
install -D -p -m 0755 genkeys %{buildroot}%{_bindir}/yggdrasil-genkeys

install -D -p -m 0644 contrib/systemd/yggdrasil.service %{buildroot}%{_unitdir}/yggdrasil.service
install -D -p -m 0644 contrib/systemd/yggdrasil-default-config.service %{buildroot}%{_unitdir}/yggdrasil-default-config.service

install -D -p -m 0644 %{S:1} %{buildroot}%{_sysusersdir}/yggdrasil.conf

%check

%pre
%sysusers_create_compat %{S:1}

%post
%systemd_post yggdrasil.service

%preun
%systemd_preun yggdrasil.service

%postun
%systemd_postun_with_restart yggdrasil.service

%files
%license LICENSE
%doc README.md
%{_bindir}/yggdrasil
%{_bindir}/yggdrasilctl
%{_bindir}/yggdrasil-genkeys
%{_unitdir}/yggdrasil.service
%{_unitdir}/yggdrasil-default-config.service
%{_sysusersdir}/yggdrasil.conf

%changelog
* Fri Oct 16 2026 Red Earth <redearth@50335033.xyz> - 0.5.14-1
- Initial package release
