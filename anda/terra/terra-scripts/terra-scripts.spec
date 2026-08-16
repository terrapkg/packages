Name:           terra-scripts
Version:        0.2.1
Release:        1%{?dist}
Summary:        Helpful scripts for contributing to Terra
License:        GPL-3.0-or-later
URL:            https://github.com/terrapkg/cli-tools
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Requires:       bash
BuildArch:      noarch
Packager:       Its-J <jonah@fyralabs.com>
Recommends:     podman

%description
%{summary}.

%prep
%autosetup -n cli-tools-%{version}

%install
install -Dm 755 format-license.sh %{buildroot}%{_bindir}/format-license
install -Dm 755 ldd-dnf.sh %{buildroot}%{_bindir}/ldd-dnf
install -Dm 755 changelog.sh %{buildroot}%{_bindir}/changelog
install -Dm 755 getcommit.sh %{buildroot}%{_bindir}/getcommit
install -Dm 755 panda.sh %{buildroot}%{_bindir}/panda

%files
%doc README.md
%license LICENSE
%{_bindir}/format-license
%{_bindir}/ldd-dnf
%{_bindir}/changelog
%{_bindir}/getcommit
%{_bindir}/panda

%changelog
* Fri May 29 2026 Jaiden Riordan <jade@fyralabs.com>
- Add panda.sh
* Sun May 24 2026 Its-J <jonah@fyralabs.com>
- Add getcommit.sh
* Sat May 23 2026 Its-J <jonah@fyralabs.com>
- Package terra-scripts
