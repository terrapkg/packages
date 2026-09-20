%global goipath github.com/schachmat/wego
Version:        2.4

%gometa -f

Name:           wego
Release:        1%{?dist}
Summary:        weather app for the terminal

License:        ISC
URL:            https://github.com/schachmat/wego
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros
Requires:       glibc

%description
%{summary}.

%gopkg

%prep
%autosetup

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/wego %{goipath}/

%install
install -Dm755 %{gobuilddir}/wego %{buildroot}%{_bindir}/wego

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/wego

%changelog
* Sun Jul 26 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
