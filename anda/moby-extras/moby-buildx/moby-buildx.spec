%define debug_package %{nil}

Name:           moby-buildx
Version:        0.9.1
Release:        1%{?dist}
Summary:        Docker CLI plugin for extended build capabilities with BuildKit

License:        Apache-2.0
URL:            https://github.com/docker/buildx
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  go-rpm-macros
BuildRequires:  git-core
Requires:       docker
Provides:       docker-buildx = %{version}-%{release}



%description


%prep
%autosetup -n buildx-%{version}


%build
go build -v -o docker-buildx ./cmd/buildx


%install
install -D -m 0755 docker-buildx %{buildroot}%{_libexecdir}/docker/cli-plugins/docker-buildx


%files
%license LICENSE
%doc docs
%{_libexecdir}/docker/cli-plugins/docker-buildx


%changelog
* Wed Oct 05 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Release
