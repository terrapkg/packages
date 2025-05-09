# Created by pyp2rpm-3.3.10
%global pypi_name pywal16
%global _description %{expand:
Pywal is a tool that generates a color palette from the dominant colors in an image. It then applies the colors system-wide and on-the-fly in all of your favourite programs.}

Name:           python-%{pypi_name}
Version:        3.8.6
Release:        1%{?dist}
Summary:        16 color fork of the original Pywal
License:        MIT
URL:            https://github.com/eylles/pywal16
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(colorthief)
BuildRequires:  python3dist(colorz)
BuildRequires:  python3dist(fast-colorthief)
BuildRequires:  python3dist(haishoku)
BuildRequires:  python3dist(modern-colorthief)
BuildRequires:  python3dist(setuptools)
Packager:       Gilver E. <rockgrub@disroot.org>

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3dist(colorthief)
Requires:       python3dist(colorz)
Requires:       python3dist(fast-colorthief)
Requires:       python3dist(haishoku)
Requires:       python3dist(modern-colorthief)

%description -n python3-%{pypi_name}
This project is a 16 colors fork of Pywal.

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{_bindir}/wal
%{python3_sitelib}/pywal
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Fri May 09 2025 Gilver E. <rockgrub@disroot.org> - 3.8.6-1
- Initial package.
