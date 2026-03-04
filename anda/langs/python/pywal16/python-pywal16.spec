%global pypi_name pywal16
%global _description %{expand:
Pywal is a tool that generates a color palette from the dominant colors in an image. It then applies the colors system-wide and on-the-fly in all of your favourite programs.}

Name:           python-%{pypi_name}
Version:        3.8.14
Release:        1%?dist
Summary:        16 color fork of the original Pywal
License:        MIT
URL:            https://github.com/eylles/pywal16
Source0:        %{pypi_source}
BuildRequires:  ImageMagick
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(colorthief)
BuildRequires:  python3dist(colorz)
BuildRequires:  python3dist(fast-colorthief)
BuildRequires:  python3dist(haishoku)
BuildRequires:  python3dist(modern-colorthief)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
Obsoletes:      python3-pywal < 3.5.0-1
BuildArch:      noarch
Packager:       Gilver E. <roachy@fyralabs.com>

%description
This project is a 16 colors fork of Pywal.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       ImageMagick
Requires:       python3dist(colorz)
Requires:       python3dist(haishoku)
Requires:       (python3dist(modern-colorthief) or python3dist(fast-colorthief) or python3dist(colorthief))
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_build
%else
%pyproject_wheel
%endif

%install
%if 0%{?fedora} <= 41 || 0%{?rhel}
%py3_install
%else
%pyproject_install
%endif

install -Dm644 data/man/man1/wal.1 -t %{buildroot}%{_mandir}/man1

# For some reason this is where the project tries to install the manpage?
rm -rf %{buildroot}%{_prefix}/man

%check
%pytest

%files -n python3-%{pypi_name}
%doc PKG-INFO
%doc README.md
%license LICENSE.md
%{_bindir}/wal
%{_mandir}/man1/wal.1.*
%{python3_sitelib}/pywal/
%if 0%{?fedora} <= 41 || 0%{?rhel}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%else
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%endif

%changelog
* Wed May 28 2025 Gilver E. <rockgrub@disroot.org> - 3.8.6-1
- Initial package.
