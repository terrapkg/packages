%global appid dev.khcrysalis.PlumeImpactor

Name:           plumeimpactor
Version:        2.6.0
Release:        1%{?dist}
Summary:        Cross-platform & feature rich iOS/iPadOS/tvOS sideloading application
URL:            https://github.com/claration/Impactor
Source0:        %url/archive/refs/tags/v%version.tar.gz
SourceLicense:  MIT AND BSD-3-Clause
License:        MIT AND BSD-3-Clause
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -C
%cargo_prep_online

%build
%cargo_build

%install
%make_install PROFILE=rpm PREFIX=%{_prefix}

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%files
%doc README.md SECURITY.md
%license LICENSE LICENSE_ELLEKIT
%{appid}.desktop

%changelog
* Mon Aug 10 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
