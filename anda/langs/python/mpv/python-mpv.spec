%define debug_package %nil

Name:			python3-mpv
Version:		1.0.7
Release:		1%?dist
Summary:		Python interface to the awesome mpv media player
License:		GPL-2.0+ OR LGPL-2.1+
URL:			https://github.com/jaseg/python-mpv
Source0:		https://github.com/jaseg/python-mpv/archive/refs/tags/v%version.tar.gz
Requires:       mpv-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
python-mpv is a ctypes-based python interface to the mpv media player.
It gives you more or less full control of all features of the player, just as the lua interface does.

%prep
%autosetup -n python-mpv-%version
cat<<EOL > setup.py
from setuptools import setup

setup()
EOL

%build
%py3_build

%install
%py3_install

%files
%doc README.rst
%license LICENSE.GPL LICENSE.LGPL
%ghost %python3_sitelib/__pycache__/mpv.cpython-*.pyc
%python3_sitelib/mpv-%version-py%python3_version.egg-info/
%python3_sitelib/mpv.py

%changelog
%autochangelog
