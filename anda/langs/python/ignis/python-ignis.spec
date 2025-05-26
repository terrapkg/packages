Name:           python-ignis
Version:        0.5
Release:        2%{?dist}
Summary:        A widget framework for building desktop shells, written and configurable in Python

License:        LGPL-2.1-or-later
URL:            https://linkfrg.github.io/ignis
Source:         https://github.com/linkfrg/ignis/archive/v%{version}/ignis-%{version}.tar.gz
Packager:       madonuko <mado@fyralabs.com>

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  gcc git-core
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  python3dist(meson-python)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
%summary.}

%description %_description

%package -n python3-ignis
Summary:        %{summary}

%description -n python3-ignis %_description


%prep
%autosetup -p1 -n ignis-%{version}

%if %{?fedora} > 41
%generate_buildrequires
%pyproject_buildrequires -R
%endif

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
%pyproject_save_files 'ignis*'
%endif

%if 0%{?fedora} <= 41 || 0%{?rhel}
%files -n python3-ignis
%doc README.*
%license LICENSE
%{_bindir}/ignis
%{python3_sitearch}/ignis-%{version}-py%{python3_version}.egg-info/
%else
%files -n python3-ignis -f %{pyproject_files}
%doc README.*
%license LICENSE
%{_bindir}/ignis
%endif


%changelog
* Sun May 05 2024 madonuko <mado@fyralabs.com> - 0.5-1
- Initial package.
