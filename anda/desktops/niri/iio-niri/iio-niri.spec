Name:           iio-niri
Version:        1.3.0
Release:        1%{?dist}
Summary:        Autorotation daemon for niri
URL:            https://github.com/Zhaith-Izaliel/iio-niri
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cargo-rpm-macros
BuildRequires:  dbus-devel
Requires:       iio-sensor-proxy
License:        (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND GPL-3.0-or-later AND MIT OR Apache-2.0 AND (Unlicense OR MIT) 
Packager:       Tulip Blossom <tulilirockz@outlook.com>

%description
%{summary}.

%prep
%autosetup
%cargo_prep_online

%build
%cargo_build
%{cargo_license_online} > LICENSE.dependencies

%install
%crate_install_bin

%files
%doc README.md
%license LICENSE.md LICENSE.dependencies
%{_bindir}/%{name}

%changelog
* Fri Mar 13 2026 Tulip Blossom <tulilirockz@outlook.com>
- Initial commit
