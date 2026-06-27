Name:           ScopeBuddy
Version:        1.4.0
Release:        2%?dist
Summary:        A manager script to make gamescope easier to use on desktop
License:        Apache-2.0
URL:            https://github.com/OpenGamingCollective/ScopeBuddy
Source0:        %url/archive/refs/tags/%version.tar.gz
BuildArch:      noarch

Requires:       bash
Requires:       perl
Requires:       (gamescope or terra-gamescope)
Suggests:       (kscreen-doctor or gnome-randr)
Suggests:       jq
Provides:       scopebuddy
Provides:       scb

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A manager script to make gamescope easier to use on the desktop (or if you use it in desktop mode and gamemode).

%prep
%autosetup

%install
install -Dpm0755 -t %{buildroot}%{_bindir}/ bin/scopebuddy bin/scb 

%post

%files
%doc README.md
%license LICENSE
%{_bindir}/scopebuddy
%{_bindir}/scb

%changelog
* Thu Feb 05 2025 Tulip Blossom <tulilirockz@outlook.com>
- Move sources to OpenGamingCollective repository instead of personal HikariKnight repo

* Tue Dec 16 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
