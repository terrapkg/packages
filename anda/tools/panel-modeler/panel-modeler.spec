Name:   	panel-modeler
Version:	1.0.0
Release:	1%{?dist}
Summary:	Photovoltaic decay modeling through PVWatts

License:	MIT
URL:		https://github.com/halfcyan/panel-modeler
Source0:	https://github.com/halfcyan/panel-modeler/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  clang
BuildRequires:  mold
BuildRequires:  ninja-build

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
A C++ command-line program that predicts the future power output of solar
panels based on their specifications (reference power, temperature derating
coefficient, and decay rate). Given a location's average irradiance and
temperature over a year, it calculates the expected power output a given
number of years into the future.

The program takes two command-line arguments — an input file and an output
file, both in CSV format.

%prep
%autosetup

%conf
%meson --native-file clang.ini

%build
%meson_build

%install
install -Dm0755 %{_vpath_builddir}/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Thu Jul 30 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
