%global goipath github.com/surge-downloader/surge
Version:        0.6.9

%gometa

Name:           surge
Release:        1%?dist
Summary:        Blazing fast TUI download manager built in Go for power users

License:        MIT
URL:            https://github.com/surge-downloader/Surge
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang gcc go-rpm-macros
Requires:       glibc

%description
%{summary}.

%gopkg

%prep
%autosetup -n Surge-%{version}

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/surge %{goipath}

%install
install -Dm755 %{gobuilddir}/bin/surge %{buildroot}%{_bindir}/surge

%files
%license LICENSE
%doc README.md
%{_bindir}/surge

%changelog
* Tue Feb 24 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
