%global ver v3.0.0-alpha.74
%global sanitized_ver %(echo %{ver} | sed 's/-/~/g')

%global goipath github.com/wailsapp/wails/v3
Version:        %{sanitized_ver}

%gometa -f

Name:           wails3
Release:        1%?dist
Summary:        Create beautiful applications using Go

License:        MIT
URL:            https://wails.io/

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  gtk3-devel
Requires:       glibc
Requires:       /usr/bin/npm
Requires:       webkit2gtk4.1
Requires:       gtk3
Provides:       wails-v3

%description
%{summary}.

%gopkg

%prep
%git_clone https://github.com/wailsapp/wails v3-alpha

%build
pushd v3/cmd/wails3
GO111MODULE=on %gobuild
popd

%install
install -Dm 0755 v3/cmd/wails3/wails3 %{buildroot}%{_bindir}/wails3

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
%{_bindir}/wails3

%changelog
* Mon Mar 02 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
