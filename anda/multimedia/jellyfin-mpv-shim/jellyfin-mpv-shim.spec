# Created by pyp2rpm-3.3.10
%global pypi_name jellyfin-mpv-shim
%global pypi_version 2.9.0
%global pypi_install_name %(echo %pypi_name | sed -e 's/-/_/g')

Name:           %{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Cast media from Jellyfin Mobile and Web apps to MPV

License:        GPLv3
URL:            https://github.com/jellyfin/jellyfin-mpv-shim
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3dist(setuptools)

%description
Jellyfin MPV Shim is a cross-platform cast client for Jellyfin. It has
support for all your advanced media files without transcoding, as well as tons
of features which set it apart from other multimedia clients.

%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_install_name}

%files -f %{pyproject_files}
%license LICENSE.md jellyfin_mpv_shim/default_shader_pack/LICENSE.md
%doc README.md jellyfin_mpv_shim/default_shader_pack/README.md
%{_bindir}/jellyfin-mpv-shim

%changelog
* Sun Dec 07 2025 metcya <metcya@gmail.com> - 2.9.0-1
- Initial package.
