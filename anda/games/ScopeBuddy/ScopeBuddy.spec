Name:           ScopeBuddy
Version:        1.3.0
Release:        1%?dist
Summary:        A manager script to make gamescope easier to use on desktop
License:        Apache-2.0
URL:            https://github.com/HikariKnight/ScopeBuddy
Source0:        %url/archive/refs/tags/%version.tar.gz
BuildArch:      noarch

Requires:       bash
Requires:       perl
Requires:       (gamescope or terra-gamescope)

Provides:       scopebuddy
Provides:       scb

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
A manager script to make gamescope easier to use on the desktop (or if you use it in desktop mode and gamemode).

%prep
%autosetup

%install
install -Dm 755 bin/scopebuddy %{buildroot}%{_bindir}/scopebuddy

%post
%{__ln_s} -f %{_bindir}/scopebuddy %{_bindir}/scb

%files
%doc README.md
%license LICENSE
%{_bindir}/scopebuddy

%changelog
* Tue Dec 16 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
