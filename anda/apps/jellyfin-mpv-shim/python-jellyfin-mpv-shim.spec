Name:           python-jellyfin-mpv-shim
Version:        3.3.0
Release:        1%{?dist}
Summary:        Cast media from Jellyfin Mobile and Web apps to MPV.

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

%global _description %{expand:
This is package 'jellyfin-mpv-shim' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-jellyfin-mpv-shim
Summary:        %{summary}

%description -n python3-jellyfin-mpv-shim %_description

%pyproject_extras_subpkg -n python3-jellyfin-mpv-shim all,discord,gui,systray

%prep
%autosetup -p1 -n jellyfin_mpv_shim-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l jellyfin_mpv_shim

%check
%pyproject_check_import

%files -n python3-jellyfin-mpv-shim -f %{pyproject_files}
%{_bindir}/jellyfin-mpv-shim

%changelog
* Fri Nov 06 2026 kiritanya <kiritanya@proton.me> - 3.3.0-1
- initial package
