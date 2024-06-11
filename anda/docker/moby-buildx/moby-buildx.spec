%define debug_package %nil

Name:           moby-buildx
Version:        0.15.0
Release:        1%?dist
Summary:        Docker CLI plugin for extended build capabilities with BuildKit

License:        Apache-2.0
URL:            https://github.com/docker/buildx
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  go-rpm-macros
BuildRequires:  git-core
BuildRequires:  gcc
Requires:       docker
Provides:       docker-buildx = %{version}-%{release}

%description
buildx is a Docker CLI plugin for extended build capabilities with BuildKit.


%prep
%autosetup -n buildx-%{version}
go mod download


%build
export CGO_ENABLED=1
go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n') -s -w -extldflags '--static-pie'" \
  -buildmode=pie -tags 'osusergo,netgo,static_build' -v -x \
  -o docker-buildx ./cmd/buildx


%install
install -D -m 0755 docker-buildx %{buildroot}%{_libexecdir}/docker/cli-plugins/docker-buildx


%files
%license LICENSE
%doc docs
%{_libexecdir}/docker/cli-plugins/docker-buildx


%changelog
* Wed Oct 05 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 0.9.1-1
- Initial Release
