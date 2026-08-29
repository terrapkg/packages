%global pypi_name ytm_player
%global _desc Terminal (TUI) YouTube Music client built with Textual.

Name:			python-%{pypi_name}
Version:		2.0.0
Release:		1%{?dist}
Summary:		Terminal YouTube Music player with synced lyrics
BuildArch:		noarch

License:		MIT
URL:			https://github.com/peternaame-boop/ytm-player
Source0:		%{pypi_source}

Packager:		Caio Bruno <cbrunofb@gmail.com>

BuildRequires:	python3-devel
BuildRequires:	python3-pip
BuildRequires:	python3-wheel
BuildRequires:	python3-hatchling

%description
%_desc

%package -n		python3-%{pypi_name}
Summary:		%{summary}
Requires:		libmpv.so.2
Provides:		ytm-player = %{evr}
Provides:		ytm = %{evr}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n	python3-%{pypi_name}
%_desc

%prep
%autosetup -n ytm_player-%{version}
sed -i 's/python-mpv/mpv/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n		python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/ytm

%changelog
* Fri Jul 31 2026 Caio Bruno <cbrunofb@gmail.com> - 2.0.0-1
- Initial package
