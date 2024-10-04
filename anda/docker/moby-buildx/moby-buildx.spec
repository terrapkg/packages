%define debug_package %nil

Name:           moby-buildx
Version:        0.17.1
Release:        1%?dist
Summary:        Docker CLI plugin for extended build capabilities with BuildKit

License:        Apache-2.0
URL:            https://github.com/docker/buildx
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  go-rpm-macros
BuildRequires:  git-core
BuildRequires:  gcc
BuildRequires:  anda-srpm-macros

Provides:       docker-buildx = %{version}-%{release}
Provides:       docker-buildx-cli = %{version}-%{release}


%description
buildx is a Docker CLI plugin for extended build capabilities with BuildKit.


%prep
%autosetup -n buildx-%{version}


%build
export CGO_ENABLED=1
%go_build_online ./cmd/buildx


%install
install -D -m 0755 build/bin/cmd/buildx %{buildroot}%{_libexecdir}/docker/cli-plugins/docker-buildx


%files
%license LICENSE
%doc docs
%{_libexecdir}/docker/cli-plugins/docker-buildx


%changelog
* Wed Oct 05 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 0.9.1-1
- Initial Release
