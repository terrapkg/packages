Name:           nirius
Version:        0.6.1
Release:        1%{?dist}
Summary:        Utility commands for niri

License:        GPL-3.0-or-later AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND MIT AND (Unlicense OR MIT)
URL:            https://git.sr.ht/~tsdh/nirius
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

Packager:       metcya <metcya@gmail.com>

BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  mold
Requires:       niri

%description
Some utility commands for the niri wayland compositor. You have to start the
niriusd daemon and then issue commands using the nirius utility. The daemon is
best started by adding spawn-at-startup "niriusd" to niri's config.kdl.

%prep
%autosetup -n %{name}-%{name}-%{version}
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies
%cargo_build

%install
install -Dm 755 target/rpm/nirius %{buildroot}%{_bindir}/nirius
install -Dm 755 target/rpm/niriusd %{buildroot}%{_bindir}/niriusd

%files
%license LICENSE 
%license LICENSE.dependencies
%doc README.md
%{_bindir}/nirius
%{_bindir}/niriusd

%changelog
* Thu Jan 22 2026 metcya <metcya@gmail.com>
- Initial package
