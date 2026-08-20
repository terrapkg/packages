Name:   	panel-modeler
Version:	2.1.2
Release:	1%{?dist}
Summary:	Photovoltaic decay modeling through PVWatts

License:	MIT
URL:		https://tangled.org/willowidk.dev/panel-modeler
Source0:	https://tangled.org/willowidk.dev/panel-modeler/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  clang
BuildRequires:  mold
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
A C++ command-line and GUI program that predicts the future power output of solar
panels based on their specifications (reference power, temperature derating
coefficient, and decay rate), along with the number of panels in an array. Given a location's average irradiance and
temperature over a year, it calculates the expected power output a given
number of years into the future.

The program takes two command-line arguments — an input file and an output
file, both in CSV format.

%pkg_completion -bfz

%prep
%autosetup -n panel-modeler-v%{version}

%conf
%meson --native-file clang.ini -Dqt=enabled

%build
%meson_build

%install
%meson_install

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/dev.willowidk.%{name}.metainfo.xml

%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{_datadir}/panel-modeler/
%{bash_completions_dir}/panel-modeler.bash
%{zsh_completions_dir}/_panel-modeler
%{fish_completions_dir}/panel-modeler.fish
%{_docdir}/panel-modeler/
%{_appsdir}/%{name}.desktop
%{_scalableiconsdir}/%{name}.svg
%{_metainfodir}/dev.willowidk.%{name}.metainfo.xml

%changelog
* Thu Aug 20 2026 Cypress Reed <cypress@fyralabs.com>
- Add bash/zsh/fish completions
- Add packages required for v2.1.0

* Thu Jul 30 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
