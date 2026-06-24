%define debug_package %{nil}

%global goipath github.com/Adembc/lazyssh
Version:        0.3.0

%gometa -f

Name:           lazyssh
Release:        1%{?dist}
Summary:        A terminal-based SSH manager inspired by lazydocker and k9s - Written in go

License:        Apache-2.0
URL:            https://github.com/Adembc/lazyssh
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang gcc go-rpm-macros
Requires:       glibc

%description
%{summary}.

%gopkg

%prep
%autosetup

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/lazyssh %{goipath}/cmd

%install
install -Dm 0755 %{gobuilddir}/lazyssh %{buildroot}%{_bindir}/lazyssh

%files
%license LICENSE
%doc README.md
%{_bindir}/lazyssh

%changelog
* Sun Jun 14 2026 Owen-sz <owen@fyralabs.com> - 0.3.0-1
- Initial commit
