Name:           niri-autostart
Version:        0.3.2
Release:        1%{?dist}
Summary:        Declarative autostart and layout restoration for niri
SourceLicense:  GPL-3.0-or-later
License:        %{SourceLicense} AND (Apache-2.0 OR MIT) AND MIT AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND Apache-2.0 AND (Unlicense OR MIT)
URL:            https://github.com/partanskiy/niri-autostart
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Packager:       Its-J <jonah@fyralabs.com>

BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
Requires:       niri

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies
%cargo_build

%install
install -Dm 755 target/rpm/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/niri-autostart

%changelog
* Sun Sep 06 2026 Its-J <jonah@fyralabs.com> - 0.3.2-1
- Initial package
