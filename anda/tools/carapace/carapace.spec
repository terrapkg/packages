%define debug_package %{nil}

%global goipath github.com/carapace-sh/carapace-bin
Version:        1.6.0

%gometa -f

Name:           carapace
Release:        1%?dist
Summary:        A multi-shell completion binary

License:        MIT
URL:            https://carapace.sh/
Source0:        https://github.com/carapace-sh/carapace-bin/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang gcc go-rpm-macros
Requires:       glibc

%description
%{summary}.

%gopkg

%prep
%autosetup -n %{name}-bin-%{version}

%build
%define gomodulesmode GO111MODULE=on
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
go generate ./cmd/...
%gobuild -o %{gobuilddir}/cmd/carapace %{goipath}/cmd/carapace

%install
install -Dm 0755 %{gobuilddir}/cmd/carapace %{buildroot}%{_bindir}/carapace

%files
%license LICENSE
%doc README.md
%{_bindir}/carapace

%changelog
* Fri Dec 05 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
