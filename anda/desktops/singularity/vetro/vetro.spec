%global commit 0a7bd367676f67e1c15a304ba135fe6fecdbc604
%global commit_date 20260605
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global goipath github.com/singularityos-lab/vetro
Version:        0~%{commit_date}git.%{shortcommit}

%gometa -f

Name:           vetro
Release:        1%{?dist}
Summary:        Declarative GTK4 UI transpiler with a built-in Language Server Protocol (LSP) server
URL:            https://github.com/singularityos-lab/vetro
Source0:        %{url}/archive/%{commit}/vetro-%{commit}.tar.gz
License:        MIT
BuildRequires:  golang

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%gopkg

%prep
%autosetup -n vetro-%{commit}

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/vetro .

%install
install -Dm755 %{gobuilddir}/bin/vetro %{buildroot}%{_bindir}/vetro

%files
%{_bindir}/vetro
%license LICENSE
%doc README.md

%changelog
* Sat May 16 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
