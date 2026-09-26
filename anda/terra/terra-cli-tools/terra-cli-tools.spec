Name:           terra-cli-tools
Version:        0.3.2
Release:        3%{?dist}
Summary:        Helpful scripts for contributing to Terra
License:        AGPL-3.0-or-later
URL:            https://github.com/terrapkg/cli-tools
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Requires:       bash
BuildArch:      noarch
Packager:       Its-J <jonah@fyralabs.com>
Recommends:     podman
Recommends:     /usr/bin/tar
Recommends:     /usr/bin/which
Recommends:     /usr/bin/grep
Recommends:     /usr/bin/cp
Recommends:     git
Obsoletes:      terra-scripts <= 0.3.0-1

%description
%{summary}.

%package -n terra-maintainer-cli-tools
Summary:    Helpful scripts for maintaining Terra and its infrastructure
Requires:   %{name} = %{evr}
Requires:   /usr/bin/rg
Requires:   /usr/bin/cat
Requires:   /usr/bin/rm
Requires:   fish
Requires:   subatomic-cli
Requires:   python3
Requires:   git
Requires:   anda
Requires:   gh
Requires:   jq

%description -n terra-maintainer-cli-tools
%{summary}.

%prep
%autosetup -n cli-tools-%{version}

%install
install -Dm 755 format-license.sh       %{buildroot}%{_bindir}/format-license
install -Dm 755 ldd-dnf.sh              %{buildroot}%{_bindir}/ldd-dnf
install -Dm 755 changelog.sh            %{buildroot}%{_bindir}/changelog
install -Dm 755 getcommit.sh            %{buildroot}%{_bindir}/getcommit
install -Dm 755 panda.sh                %{buildroot}%{_bindir}/panda
install -Dm 755 icedtea-fetch.sh        %{buildroot}%{_bindir}/icedtea-fetch
install -Dm 644 changelog.conf          %{buildroot}%{_sysconfdir}/xdg/terra-scripts/changelog.conf

# Maintainer scripts
install -Dm 755 satm-grepdel.fish       %{buildroot}%{_bindir}/satm-grepdel
install -Dm 755 satm-rm-stdin.sh        %{buildroot}%{_bindir}/satm-rm-stdin
install -Dm 755 sync-branches-ssh.sh    %{buildroot}%{_bindir}/sync-branches-ssh
install -Dm 755 sync-branches.sh        %{buildroot}%{_bindir}/sync-branches
install -Dm 755 terra-subtree-build.sh  %{buildroot}%{_bindir}/terra-subtree-build
install -Dm 755 terra_mass_rebuild.py   %{buildroot}%{_bindir}/terra_mass_rebuild
install -Dm 755 backports.sh            %{buildroot}%{_bindir}/backports

%files
%doc README.md
%license LICENSE
%{_bindir}/format-license
%{_bindir}/ldd-dnf
%{_bindir}/changelog
%{_bindir}/getcommit
%{_bindir}/panda
%{_bindir}/icedtea-fetch
%{_sysconfdir}/xdg/terra-scripts/changelog.conf

%files -n terra-maintainer-cli-tools
%{_bindir}/backports
%{_bindir}/satm-grepdel
%{_bindir}/satm-rm-stdin
%{_bindir}/sync-branches-ssh
%{_bindir}/sync-branches
%{_bindir}/terra-subtree-build
%{_bindir}/terra_mass_rebuild

%changelog
* Fri Sep 25 2026 Owen Zimmerman <owen@fyralabs.com>
- Update for 0.3.0, change name to terra-cli-tools

* Wed Sep 23 2026 Owen Zimmerman <owen@fyralabs.com>
- Update for 0.2.3

* Fri May 29 2026 Jaiden Riordan <jade@fyralabs.com>
- Add panda.sh

* Sun May 24 2026 Its-J <jonah@fyralabs.com>
- Add getcommit.sh

* Sat May 23 2026 Its-J <jonah@fyralabs.com>
- Package terra-scripts
