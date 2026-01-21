# https://github.com/nats-io/natscli
%global goipath         github.com/nats-io/natscli
%global commit          dc7e74221bda20def8b66706c99bfcc50b919aca
%global commit_date     20260121
%global shortcommit     %{sub %{commit} 1 7}

%gometa -f

Name:           natscli
Version:        0~%{commit_date}git.%shortcommit
Release:        1%?dist
Summary:        The NATS Command Line Interface

License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

Packager:       Ruka <pkgs@ruka.red>

BuildRequires:  go
BuildRequires:  git
BuildRequires:  anda-srpm-macros

%description
A command line utility to interact with and manage NATS.

%prep
%goprep -A

%build
%define currentgoldflags -X main.version=%{version} -X main.commit=%{commit} -X main.date=%{commit_date}
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/nats %{goipath}/nats

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md AUTH.md LOCAL_DEVELOPMENT.md cli/cheats/*
%{_bindir}/nats

%changelog
* Fri Sep 19 2025 Ruka <pkgs@ruka.red> - 0~20250919git.607ceaa-1
- Initial packaging for Terra PKG
