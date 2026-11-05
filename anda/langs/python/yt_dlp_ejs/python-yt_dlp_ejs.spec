%define debug_package %nil
%global pypi_name yt_dlp_ejs
%global _desc External JavaScript for yt-dlp supporting many runtimes

Name:			      python-%{pypi_name}
Version:		    0.8.0
Release:		    1%?dist
Summary:		    External JavaScript for yt-dlp supporting many runtimes
License:		    Unlicense
URL:			      https://pypi.org/project/yt-dlp-ejs
Source0:        %{pypi_source}
Packager:       kiritanya
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  bun-bin

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%prep
%autosetup -n %pypi_name-%version

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files
%license LICENSE
%doc README.md

%files -n python3-%pypi_name -f %pyproject_files
%license LICENSE
%doc README.md
