Name:           nirinit
Version:        0.3.1
Release:        1%{?dist}
Summary:        A session manager for Niri that automatically saves and restores your window layout
URL:            https://github.com/amaanq/nirinit
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
SourceLicense:  MPL-2.0
License:        %{sourcelicense} AND (MIT OR Apache-2.0) AND MIT AND GPL-3.0-or-later AND EUPL-1.2 AND (Unlicense OR MIT)
BuildRequires:  cargo-rpm-macros

Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}
%cargo_prep_online

%build
%cargo_build

%install
install -Dm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
%{cargo_license_online} > LICENSE.dependencies

%files
%{_bindir}/%{name}
%license LICENSE.md LICENSE.dependencies
%doc README.md

%changelog
* Fri Nov 06 2026 Its-J <jonah@fyralabs.com> - 0.3.1-1
- Initial package
