%define debug_package %{nil}

Name:           moby-compose
Version:        2.29.6
Release:        1%?dist
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
Provides:       docker-compose-cli = %{version}-%{release}

%description
A tool for running multi-container applications using the Compose file format.


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
* Tue Dec 06 2022 root - 2.14.0-1
- new version

* Tue Oct 04 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
