%global debug_package %{nil}
# Disabled because compiled without debug

%global commit  acb06e831bb7bf0e4b8346c933a14cdaab305a0d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 26.2.2
%global commit_date 20260307

%global goipath         github.com/XTLS/Xray-core
Version:                %{ver}^%{commit_date}git.%{shortcommit}

%global golicenses      LICENSE
%global godocs          README.md SECURITY.md CODE_OF_CONDUCT.md

Name:           xray-nightly
Release:        1%?dist
Summary:        High-performance, open-source network proxy engine and toolset designed to bypass internet censorship and enhance privacy
License:        MPL-2.0
Packager:       veuxit <erroor234@gmail.com>
URL:            https://github.com/XTLS/Xray-core
Conflicts:      Xray-core

Source0:        %{url}/archive/%{commit}/Xray-core-%{commit}.tar.gz

BuildRequires:  golang >= 1.26
BuildRequires:  go-rpm-macros go-srpm-macros anda-srpm-macros

%description
%summary.

%gopkg

%prep

%autosetup -n Xray-core-%{commit}

%goprep_online -Ae

%build
export CGO_ENABLED=0
%gobuild -o xray -trimpath -buildvcs=false -ldflags "-s -w -buildid=" ./main

%install
%gopkginstall
install -Dm755 xray %{buildroot}%{_bindir}/xray

%files
%doc README.md
%doc SECURITY.md
%doc CODE_OF_CONDUCT.md
%license LICENSE
%{_bindir}/xray

%gopkgfiles

%changelog
* Sun Mar 8 2026 veuxit <erroor234@gmail.com> - 
- Initial package release