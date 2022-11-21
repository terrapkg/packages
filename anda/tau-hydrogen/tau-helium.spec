Summary:        tauOS Icon Theme
Name:           tau-hydrogen
Version:        1.0.1
Release:        1%{?dist}
License:        GPLv3
URL:            https://github.com/tau-OS/tau-hydrogen
Source0:        https://github.com/tau-OS/tau-hydrogen/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  ninja-build

%description
Hydrogen is the default icon theme in tauOS

%prep
%autosetup -n tau-hydrogen-%{version}

%build
%meson
%meson_build

%install
# Install licenses
mkdir -p licenses
%meson_install

%files
%license LICENSE
%doc README.md
%{_datadir}/themes/Helium/*
%{_datadir}/themes/Helium-dark/*

%changelog
* Sun Nov 20 2022 Lleyton Gray <lleyton@fyralabs.com> - 1.0.1
- Terra Release
