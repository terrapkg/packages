%define debug_package %{nil}

Name:           moby-compose
Version:        2.11.2
Release:        1%{?dist}
Summary:        Define and run multi-container applications with Docker

License:        Apache-2.0
URL:            https://github.com/docker/compose/
Source0:        %{url}archive/refs/tags/v%{version}.tar.gz
# Source1:        https://github.com/docker/buildx/releases/download/v0.9.1/buildx-v0.9.1.linux-amd64

BuildRequires:  go-rpm-macros
BuildRequires:  git-core
BuildRequires:  docker
Requires:       docker
Provides:       docker-compose = %{version}-%{release}
Provides:       docker-compose-cli

%description


%prep
%autosetup -n compose-%{version}


%build
%make_build


%install
mkdir -p %{buildroot}%{_libexecdir}/docker/cli-plugins
install -m 0755 bin/build/docker-compose %{buildroot}%{_libexecdir}/docker/cli-plugins/docker-compose

%files
%license LICENSE
%doc docs

%{_libexecdir}/docker/cli-plugins/docker-compose

%changelog
* Tue Oct 04 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
