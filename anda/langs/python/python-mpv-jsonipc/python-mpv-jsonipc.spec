# Created by pyp2rpm-3.3.10
%global pypi_name python-mpv-jsonipc
%global pypi_version 1.2.0
%global srcname mpv-jsonipc

Name:           python-%{srcname}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python API to MPV using JSON IPC

License:        Apache-2.0
URL:            https://github.com/iwalton3/python-mpv-jsonipc
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Python MPV JSONIPCThis implements an interface similar to python-mpv, but it
uses the JSON IPC protocol instead of the C API. This means you can control
external instances of MPV including players like SMPlayer, and it can use MPV
players that are prebuilt instead of needing libmpv1. It may also be more
resistant to crashes such as Segmentation Faults, but since it isn't
directly...

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
 Python MPV JSONIPCThis implements an interface similar to python-mpv, but it
uses the JSON IPC protocol instead of the C API. This means you can control
external instances of MPV including players like SMPlayer, and it can use MPV
players that are prebuilt instead of needing libmpv1. It may also be more
resistant to crashes such as Segmentation Faults, but since it isn't
directly...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/python_mpv_jsonipc.py
%{python3_sitelib}/python_mpv_jsonipc-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Sun Dec 17 2023 Cappy Ishihara <cappy@cappuchino.xyz> - 1.2.0-1
- Initial package.
