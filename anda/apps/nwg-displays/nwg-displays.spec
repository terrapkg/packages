Name:			nwg-displays
Version:		0.5.0
Release:		1%{?dist}
Summary:		Output management utility for Sway, Hyprland, Niri and MangoWM
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

Requires:       gtk3
Requires:       gtk-layer-shell
Requires:       python3dist(pygobject)
Requires:       python3dist(i3ipc)

Packager:	    Its-J <jonah@fyralabs.com>

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nwg_displays
%desktop_file_install %{name}.desktop
install -Dm644 %{name}.svg %{buildroot}%{_scalableiconsdir}/%{name}.svg

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/nwg-displays
%{_bindir}/nwg-displays-apply
%{_bindir}/nwg-displays-toggle-wallpapers
%{_appsdir}/%{name}.desktop
%{_scalableiconsdir}/%{name}.svg

%changelog
* Sun Nov 08 2026 Its-J <jonah@fyralabs.com> - 0.5.0-1
- Initial commit
