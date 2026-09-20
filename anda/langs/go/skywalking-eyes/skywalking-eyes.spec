%global goipath github.com/apache/skywalking-eyes
Version:        0.9.0

%gometa -f

Name:           skywalking-eyes
Release:        1%{?dist}
Summary:        A full-featured license tool to check and fix license headers and resolve dependencies' licenses
License:        Apache-2.0
URL:            https://github.com/apache/skywalking-eyes
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Its-J <jonah@fyralabs.com>

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  go-rpm-macros

Provides:       skywalking-eye
Provides:       license-eye
Provides:       license-eyes

%description
%{summary}.

%gopkg

%prep
%autosetup -C

%build
%define gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/cmd/license-eye %{goipath}/cmd/license-eye

%install
install -Dm 0755 %{gobuilddir}/cmd/license-eye %{buildroot}%{_bindir}/license-eye
%{__ln_s} -f %{_bindir}/license-eye %{buildroot}%{_bindir}/skywalking-eyes

%files
%license LICENSE
%doc README.md
%{_bindir}/license-eye
%{_bindir}/skywalking-eyes

%changelog
* Wed Sep 16 2026 Its-J <jonah@fyralabs.com> - 0.9.0-1
- Inital commit
