%global commit 607ceaac6bb542dacadb52573fb20bedc5b6228b
%global commit_date 20250919
%global shortcommit %{sub %{commit} 1 7}

Name:           natscli
Version:        0~%{commit_date}git.%shortcommit
Release:        1%{?dist}
Summary:        The NATS Command Line Interface

License:        Apache-2.0
URL:            https://github.com/nats-io/natscli
Source0:        %{url}/archive/%{commit}/natscli-%{commit}.tar.gz

BuildRequires:  go
BuildRequires:  git

%description
A command line utility to interact with and manage NATS.

%prep
%autosetup -n natscli-%{commit}

%build
cd nats && go build -o nats .

%install
install -Dm755 nats/nats "%{buildroot}%{_bindir}/nats"

%files
%license LICENSE
%doc README.md AUTH.md LOCAL_DEVELOPMENT.md cli/cheats/*
%{_bindir}/nats

%changelog
* Fri Sep 19 2025 Ruka <pkgs@ruka.red> - 0~20250919git.607ceaa-1
- Initial packaging for Terra PKG
