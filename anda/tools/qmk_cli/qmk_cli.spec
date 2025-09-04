%define debug_package %nil

Name:			qmk_cli
Version:		1.1.8
Release:		1%?dist
Summary:		A program to help users work with QMK
License:		MIT
URL:			https://github.com/qmk/qmk_cli
Source0:		%url/archive/refs/tags/%version.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3dist(setuptools)
BuildRequires:  git
BuildRequires:  python3-devel

Requires:       python3
Requires:       python-platformdirs
Requires:       python-argcomplete
Requires:       python-colorama
Requires:       python-jsonschema
Requires:       git
Requires:       avr-gcc
Requires:       arm-none-eabi-gcc
Requires:       avr-libc
Requires:       arm-none-eabi-binutils
Requires:       arm-none-eabi-newlib
Requires:       avr-binutils
Requires:       dfu-programmer
Requires:       dfu-util
Requires:       avrdude
Requires:       python-hjson
Requires:       python-pygments
Requires:       python-hid
Requires:       python-pyusb
Requires:       python-pyserial
Requires:       python-pillow

Provides:       qmk

%description
The QMK CLI (command line interface) makes building and working with QMK keyboards easier.
We have provided a number of commands to simplify and streamline tasks such as obtaining and compiling the QMK firmware, creating keymaps, and more.

%prep
%autosetup -n qmk_cli-%version

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files qmk_cli

%files
%doc README.md SECURITY.md
%license LICENSE
%{_bindir}/qmk
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/qmk-%version.dist-info/*
%{python3_sitelib}/%{name}/git.py
%{python3_sitelib}/%{name}/helpers.py
%{python3_sitelib}/%{name}/script_qmk.py
%{python3_sitelib}/%{name}/__init__.py
%{python3_sitelib}/%{name}/subcommands/__init__.py
%{python3_sitelib}/%{name}/subcommands/clone.py
%{python3_sitelib}/%{name}/subcommands/console.py
%{python3_sitelib}/%{name}/subcommands/env.py
%{python3_sitelib}/%{name}/subcommands/setup.py
%{python3_sitelib}/%{name}/__pycache__/*.pyc

%changelog
* Thur Sep 04 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
