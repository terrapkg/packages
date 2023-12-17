# Created by pyp2rpm-3.3.10
%global pypi_name jellyfin-mpv-shim
%global pypi_version 2.6.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Cast media from Jellyfin Mobile and Web apps to MPV

License:        GPLv3
URL:            https://github.com/jellyfin/jellyfin-mpv-shim
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
Provides:       %{pypi_name} = %{pypi_version}

%description
Jellyfin MPV Shim is a cross-platform cast client for Jellyfin. It has
support for all your advanced media files without transcoding.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(jellyfin-apiclient-python) >= 1.9.2
Requires:       python3dist(jinja2)
Requires:       python3dist(jinja2)
Requires:       python3dist(pillow)
Requires:       python3dist(pillow)
Requires:       python3dist(pypresence)
Requires:       python3dist(pypresence)
Requires:       python3dist(pystray)
Requires:       python3dist(pystray)
Requires:       python3dist(tkinter)
Requires:       python3dist(python-mpv)
Requires:       python3dist(python-mpv-jsonipc) >= 1.2
Requires:       python3dist(pywebview) >= 3.3.1
Requires:       python3dist(pywebview) >= 3.3.1
Requires:       python3dist(requests)
Requires:       python3dist(setuptools)
Requires:       mpv
%description -n python3-%{pypi_name}
Jellyfin MPV Shim is a cross-platform cast client for Jellyfin. It has
support for all your advanced media files without transcoding.


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license jellyfin_mpv_shim/default_shader_pack/LICENSE.md
%doc README.md jellyfin_mpv_shim/default_shader_pack/README.md
%{_bindir}/jellyfin-mpv-shim
%{python3_sitelib}/jellyfin_mpv_shim
%{python3_sitelib}/jellyfin_mpv_shim-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Sun Dec 17 2023 Cappy Ishihara <cappy@cappuchino.xyz> - 2.6.0-1
- Initial package.
