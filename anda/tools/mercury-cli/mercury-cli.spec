%global goipath github.com/MercuryTechnologies/mercury-cli
Version:        0.11.0

%gometa -f

Name:           mercury-cli
Release:        1%{?dist}
Summary:        A multi-shell completion binary

License:        Apache-2.0
URL:            https://github.com/MercuryTechnologies/mercury-cli
Source0:        %{url}/archive/refs/tags/v%version.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros
Requires:       glibc

%description
%{summary}.

%gopkg

%prep
%autosetup -C

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/cmd/mercury %{goipath}/cmd/mercury

%install
install -Dm 0755 %{gobuilddir}/cmd/mercury %{buildroot}%{_bindir}/mercury-cli

%files
%license LICENSE
%doc README.md
%{_bindir}/mercury-cli

%changelog
* Thu Aug 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
