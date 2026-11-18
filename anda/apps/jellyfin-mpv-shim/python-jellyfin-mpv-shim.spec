%global pypi_name jellyfin-mpv-shim

Name:           python-jellyfin-mpv-shim
Version:        3.3.0
Release:        1%{?dist}
Summary:        Cast media from Jellyfin Mobile and Web apps to MPV

License:        GPL-3.0-or-later
Packager:       kiritanya <kiritanya@proton.me>
URL:            https://github.com/jellyfin/jellyfin-mpv-shim
Source:         %{pypi_source jellyfin_mpv_shim}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  (python3dist(tomli) if python3-devel < 3.11)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip) >= 19
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(mpv) >= 1.0.8
BuildRequires:  python3dist(jellyfin-apiclient-python) >= 1.20.2
BuildRequires:  python3dist(python-mpv-jsonipc) >= 1.5
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(pypresence)
BuildRequires:  mpv-devel

%global _description %{expand:
Jellyfin MPV Shim is a fully featured Jellyfin client built on top of MPV with
support for offline sync, media browsing, background casting, syncplay, music,
live TV, books, and photos. It does not depend on or use a webview and doesn't
mess with MPV's video output pipeline, allowing for HDR and tone mapping
support.}

%description %_description

%package -n     python3-jellyfin-mpv-shim
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       %{pypi_name} = %{evr}

%description -n python3-jellyfin-mpv-shim %_description

%pyproject_extras_subpkg -n python3-jellyfin-mpv-shim all,discord,gui,systray

%prep
%autosetup -p1 -n jellyfin_mpv_shim-%{version}
sed -i \
    -e 's/"python-mpv>=/"mpv>=/' \
    -e 's/"certifi>=[^"]*"/"certifi"/' \
    pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l jellyfin_mpv_shim

%check
%pyproject_check_import -t

%files -n python3-jellyfin-mpv-shim -f %{pyproject_files}
%{_bindir}/jellyfin-mpv-shim

%changelog
* Fri Nov 06 2026 kiritanya <kiritanya@proton.me> - 3.3.0-1
- initial package
