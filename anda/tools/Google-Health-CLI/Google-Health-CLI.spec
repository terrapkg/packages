%global goipath github.com/rudrankriyam/Google-Health-CLI
Version:        1.0.0

%gometa -f

Name:           google-health-cli
Release:        1%{?dist}
Summary:        Unofficial Google-Health-CLI for the Google Health API, written in Go

License:        MIT
URL:            https://github.com/rudrankriyam/Google-Health-CLI
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros
Requires:       glibc

Provides:       Google-Health-CLI

%description
%{summary}.

%gopkg

%prep
%autosetup -n Google-Health-CLI-%{version}

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/cmd/ghealth %{goipath}

%install
install -Dm 0755 %{gobuilddir}/cmd/ghealth %{buildroot}%{_bindir}/ghealth

%files
%license LICENSE
%doc README.md CONTRIBUTING.md CHANGELOG.md SECURITY.md
%{_bindir}/ghealth

%changelog
* Sat May 09 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
