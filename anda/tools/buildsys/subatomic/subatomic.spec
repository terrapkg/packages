%define debug_package %{nil}

Name:           subatomic
Version:        0.9.1
Release:        1%?dist
Summary:        A modern package delivery system

License:        MIT
URL:            https://github.com/FyraLabs/subatomic
Source0:        %url/archive/refs/tags/v%version.tar.gz

BuildRequires:  go-rpm-macros
BuildRequires:  git-core
BuildRequires:  ostree-devel
BuildRequires:  gcc
Requires:       ostree
Requires:       createrepo_c

%description
Subatomic is a package delivery system which supports multiple package formats.
It manages a repository of packages, handling updating, signing, and other
tasks.

%package cli
Summary:        Client for Subatomic repo manager

%description cli
Client for Subatomic repo manager

%files cli
%{_bindir}/subatomic-cli

%prep
%autosetup
go mod download


%build
mkdir -p build/bin
go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n') -s -w" -buildmode=pie -o build/bin/subatomic-cli ./subatomic-cli
go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n') -s -w" -buildmode=pie -o build/bin/subatomic ./server


%install
mkdir -p %{buildroot}%{_bindir}/
install -pm 755 build/bin/subatomic-cli %{buildroot}%{_bindir}/
install -pm 755 build/bin/subatomic %{buildroot}%{_bindir}/


%files
%{_bindir}/subatomic


%changelog
* Fri Sep 30 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 0.1.0.200283ccd3cf7c90b6a9be565ce6ff52bdec977e-1
- Intial release
