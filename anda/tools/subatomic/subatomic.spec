%define debug_package %{nil}
%define _build_id_links none
%global commit b0543ca6dc977f486dc37c0418fb9c1cbf83adf7

Name:           subatomic
Version:        0.1.0.%{commit}
Release:        1%{?dist}
Summary:        A modern package delivery system

License:        MIT
URL:            https://github.com/FyraLabs/subatomic
Source0:        https://github.com/FyraLabs/subatomic/archive/%{commit}.zip

BuildRequires:  go-rpm-macros
BuildRequires:  git-core
BuildRequires:  ostree-devel
Requires:       ostree
Requires:       createrepo_c

%description
Subatomic is a package delivery system which supports multiple package formats.
It manages a repository of packages, handling updating, signing, and other tasks.

%package cli
Summary:        Client for Subatomic repo manager

%description cli
Client for Subatomic repo manager

%files cli
%{_bindir}/subatomic-cli

%prep
%autosetup -n subatomic-%{commit}


%build

mkdir -p build/bin
go build -v -o build/bin/subatomic-cli ./subatomic-cli
go build -v -o build/bin/subatomic ./server


%install
mkdir -p %{buildroot}%{_bindir}/
install -pm 755 build/bin/subatomic-cli %{buildroot}%{_bindir}/
install -pm 755 build/bin/subatomic %{buildroot}%{_bindir}/


%files
%{_bindir}/subatomic



%changelog
* Fri Sep 30 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Intial release
