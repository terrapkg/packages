%dnl %define debug_package %{nil}

%global goipath github.com/showwin/speedtest-go
Version:        1.8.3

%gometa -f

Name:           speedtest-go
Release:        1%{?dist}
Summary:        CLI and Go API to Test Internet Speed using speedtest.net

License:        MIT
URL:            https://github.com/showwin/speedtest-go
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros

%description
%{summary}.

%gopkg

%prep
%autosetup -C

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/ %{goipath}/

%install
install -Dm 0755 %{gobuilddir}/speedtest-go %{buildroot}%{_bindir}/speedtest-go

%files
%license LICENSE
%doc README.md docs/*
%{_bindir}/speedtest-go

%changelog
* Sun Sep 06 2026 Owen Zimmerman <owen@fyralabs.com> - 1.8.3-1
- Initial commit
