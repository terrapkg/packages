%define debug_package %{nil}

%global goipath github.com/abdenasser/neohtop-cli
Version:        0.1.13

%gometa -f

Name:           neohtop-cli
Release:        1%{?dist}
Summary:        A cross-platform terminal process monitor with btop-style visualizations
License:        MIT
URL:            https://github.com/Abdenasser/neohtop-cli
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>
BuildRequires:  go-rpm-macros

%description
%summary.

%gopkg

%prep
%autosetup

%build
%define gomodulesmode GO111MODULE=on
pushd cli
%gobuild -o %{gobuilddir}/../neohtop-cli %{goipath}/
popd

%install
install -Dm 0755 cli/neohtop-cli %{buildroot}%{_bindir}/neohtop-cli

%files
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/neohtop-cli

%changelog
* Sun Jun 14 2026 Owen Zimmerman <owen@fyralabs.com>
- Use go packaging

* Sun Mar 29 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
