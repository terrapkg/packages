%global goipath github.com/wailsapp/wails/v2
Version:        2.11.0

%gometa -f

Name:           wails
Release:        1%?dist
Summary:        Create beautiful applications using Go

License:        MIT
URL:            https://wails.io/
Source0:        https://github.com/wailsapp/wails/archive/refs/tags/v%{version}.tar.gz

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros
Requires:       glibc
Requires:       /usr/bin/npm
Requires:       webkit2gtk4.1
Requires:       gtk3

%description
%{summary}.

%gopkg

%prep
%goprep

%build
pushd v2/cmd/wails
GO111MODULE=on %gobuild
popd

%install
install -Dm 0755 v2/cmd/wails/wails %{buildroot}%{_bindir}/wails

%files
%license LICENSE
%doc README.md CONTRIBUTING.md CONTRIBUTORS.md CHANGELOG.md SECURITY.md
%lang(de) %doc README.de.md
%lang(es) %doc README.es.md
%lang(fr) %doc README.fr.md
%lang(ja) %doc README.ja.md
%lang(ko) %doc README.ko.md
%lang(pt_BR) %doc README.pt-br.md
%lang(ru) %doc README.ru.md
%lang(tr) %doc README.tr.md
%lang(uz) %doc README.uz.md
%lang(zh_CN) %doc README.zh-Hans.md
%{_bindir}/wails

%changelog
* Mon Mar 02 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
