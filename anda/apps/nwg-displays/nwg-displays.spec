%global pypi_name nwg-displays
%global _desc Output management utility for sway, Hyprland, Niri and mangowm, inspired by wdisplays and wlay. Part of the nwg-shell project.

Name:			python-%{pypi_name}
Version:		0.5.0
Release:		1%{?dist}
Summary:		Output management utility for sway, Hyprland, Niri and mangowm
License:		MIT
URL:			https://github.com/nwg-piotr/nwg-displays
Source0:		%{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  anda-srpm-macros
BuildRequires:  desktop-file-utils

Packager:	    Its-J <jonah@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       nwg-displays

Requires:       gtk3
Requires:       gtk-layer-shell
Requires:       python3dist(pygobject)
Requires:       python3dist(i3ipc)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nwg_displays
%desktop_file_install %{pypi_name}.desktop
install -Dm644 %{pypi_name}.svg %{buildroot}%{_scalableiconsdir}/%{pypi_name}.svg

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/nwg-displays
%{_bindir}/nwg-displays-apply
%{_bindir}/nwg-displays-toggle-wallpapers
%{_appsdir}/%{pypi_name}.desktop
%{_scalableiconsdir}/%{pypi_name}.svg

%changelog
* Sun Nov 08 2026 Its-J <jonah@fyralabs.com> - 0.5.0-1
- Initial commit
