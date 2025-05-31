Name:           python-nautilus-open-any-terminal
Version:        0.6.1
Release:        1%?dist
Summary:        Context-menu entry for opening other terminal in Nautilus
License:        GPL-3.0-only
URL:            https://github.com/Stunkymonkey/nautilus-open-any-terminal
Source0:        %{pypi_source nautilus_open_any_terminal}
Source1:        https://raw.githubusercontent.com/Stunkymonkey/nautilus-open-any-terminal/refs/tags/%version/README.md
Source2:        https://raw.githubusercontent.com/Stunkymonkey/nautilus-open-any-terminal/refs/tags/%version/LICENSE
Packager:       madonuko <mado@fyralabs.com>

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(pip)
BuildRequires:  gettext


%global _description %{expand:
nautilus-open-any-terminal is an extension for nautilus, which adds an context-entry for opening other terminal emulators than `gnome-terminal`.}

%description %_description

%package -n	python3-nautilus-open-any-terminal
Summary:	%{summary}
Provides:	nautilus-open-any-terminal = %evr

%description -n python3-nautilus-open-any-terminal %_description


%prep
%autosetup -n nautilus_open_any_terminal-%version
cp %{S:1} %{S:2} .


#generate_buildrequires
#pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l nautilus_open_any_terminal


#check
#pyproject_check_import


%files -n python3-nautilus-open-any-terminal -f %{pyproject_files}
%doc README.md
%license LICENSE
%_datadir/caja-python/extensions/__pycache__/nautilus_open_any_terminal.cpython-*.pyc
%_datadir/caja-python/extensions/nautilus_open_any_terminal.py
%_datadir/glib-2.0/schemas/com.github.stunkymonkey.nautilus-open-any-terminal.gschema.xml
%_datadir/locale/*/LC_MESSAGES/nautilus-open-any-terminal.mo
%_datadir/nautilus-python/extensions/__pycache__/nautilus_open_any_terminal.cpython-*.pyc
%_datadir/nautilus-python/extensions/nautilus_open_any_terminal.py
