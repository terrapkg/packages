Name:           nirinit
Version:        0.3.1
Release:        1%{?dist}
Summary:        A session manager for Niri that automatically saves and restores your window layout
URL:            https://github.com/amaanq/nirinit
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
SourceLicense:  MPL-2.0
License:        %{sourcelicense} AND (MIT OR Apache-2.0) AND MIT AND GPL-3.0-or-later AND EUPL-1.2 AND (Unlicense OR MIT)
BuildSystem:    terra_cargo
BuildRequires:  cargo-rpm-macros

# Temporary
BuildRequires:  cargo4rpm

Packager:       Its-J <jonah@fyralabs.com>

%description
%{summary}.

%files
%{_bindir}/%{name}
%license LICENSE.md LICENSE.dependencies
%doc README.md

%changelog
* Fri Nov 06 2026 Its-J <jonah@fyralabs.com> - 0.3.1-1
- Initial package
