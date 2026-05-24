Name:           terra-scripts
Version:        0.1.4
Release:        1%{?dist}
Summary:        Helpful scripts for contributing to Terra
License:        GPL-3.0-or-later
URL:            https://github.com/terrapkg/cli-tools
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Requires:       bash
BuildArch:      noarch
Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n cli-tools-%{version}

%install
install -Dm 755 format-license.sh %{buildroot}%{_bindir}/format-license
install -Dm 755 ldd-dnf.sh %{buildroot}%{_bindir}/ldd-dnf
install -Dm 755 changelog.sh %{buildroot}%{_bindir}/changelog
install -Dm 755 getcommit.sh %{buildroot}%{_bindir}/getcommit

%files
%doc README.md
%license LICENSE
%{_bindir}/format-license
%{_bindir}/ldd-dnf
%{_bindir}/changelog
%{_bindir}/getcommit

%changelog
* Sun May 24 2026 Its-J <jonah@fyralabs.com>
- Add getcommit.sh
* Sat May 23 2026 Its-J <jonah@fyralabs.com>
- Package terra-scripts
