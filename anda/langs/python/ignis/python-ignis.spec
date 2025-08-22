Name:           python-ignis
Version:        0.5.1
Release:        2%?dist
Summary:        A widget framework for building desktop shells, written and configurable in Python

License:        LGPL-2.1-or-later
URL:            https://ignis-sh.github.io/ignis
Source:         https://github.com/linkfrg/ignis/archive/v%{version}/ignis-%{version}.tar.gz
Packager:       madonuko <mado@fyralabs.com>

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  gcc git-core
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  python3dist(meson-python)
BuildRequires:  python3dist(pip)

%global _description %{expand:
%summary.}

%description %_description

%package -n python3-ignis
Summary:        %{summary}

%description -n python3-ignis %_description


%prep
%autosetup -p1 -n ignis-%{version}


%generate_buildrequires
%pyproject_buildrequires -R


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'ignis*'


%files -n python3-ignis -f %{pyproject_files}
%doc README.*
%license LICENSE
%{_bindir}/ignis


%changelog
* Sun May 05 2024 madonuko <mado@fyralabs.com> - 0.5-1
- Initial package.
