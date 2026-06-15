%global pypi_name arctis-sound-manager
%global _desc Linux GUI for SteelSeries Arctis headsets — Nova Pro Wireless & Wired, Nova Pro Omni, Nova Elite, Nova 7/7P/5/3, Arctis 7/7+/9/Pro Wireless. Device settings, Sonar EQ, 4-channel Game/Chat/Media mixer, PipeWire routing.

Name:			python-%{pypi_name}
Version:		1.1.74
Release:		1%{?dist}
Summary:		GUI for SteelSeries Arctis headsets
License:		GPL-3.0-or-later
# GitHub pages URL 404s
URL:			https://github.com/loteran/Arctis-Sound-Manager
Source0:		%{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-importlib-metadata
BuildRequires:  python3-uv-build

Packager:	    Owen Zimmerman <owen@fyralabs.com>

BuildArch:      noarch

Provides:       Arctis-Sound-Manager

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n Arctis-Sound-Manager-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files arctis_sound_manager

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CONTRIBUTING.md CHANGELOG.md
%license LICENSE
%{_bindir}/asm-cli
%{_bindir}/asm-daemon
%{_bindir}/asm-diag-dinit
%{_bindir}/asm-gui
%{_bindir}/asm-router
%{_bindir}/asm-setup

%changelog
* Mon Jun 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
