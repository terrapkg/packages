%define debug_package %{nil}
%define _build_id_links none

Name:           subatomic
Version:        0.2.6
Release:        2%{?dist}
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


%build
export CGO_ENABLED=1
mkdir -p build/bin
go build -ldflags '-linkmode external -s -w -extldflags "--static-pie"' -buildmode=pie -tags 'osusergo,netgo,static_build' -v -o build/bin/subatomic-cli ./subatomic-cli
go build -ldflags '-linkmode external -s -w -extldflags "--static-pie"' -buildmode=pie -tags 'osusergo,netgo,static_build' -v -o build/bin/subatomic ./server


%install
mkdir -p %{buildroot}%{_bindir}/
install -pm 755 build/bin/subatomic-cli %{buildroot}%{_bindir}/
install -pm 755 build/bin/subatomic %{buildroot}%{_bindir}/


%files
%{_bindir}/subatomic



%changelog
* Fri Sep 30 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 0.1.0.200283ccd3cf7c90b6a9be565ce6ff52bdec977e-1
- Intial release
