Name:           neohtop-cli
Version:        0.1.12
Release:        1%?dist
Summary:        A cross-platform terminal process monitor with btop-style visualizations
License:        MIT
URL:            https://github.com/Abdenasser/neohtop-cli
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>
BuildRequires:  golang

%description
%summary.

%prep
%autosetup

%build
%make_build

%install
%make_install

%files
%doc README.md CONTRIBUTING.md
%license LICENSE
%{_bindir}/neohtop-cli

%changelog
* Sun Mar 29 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
