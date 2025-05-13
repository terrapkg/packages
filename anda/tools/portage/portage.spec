%global __brp_mangle_shebangs /bin/true
%global __python python3
%global _binaries_in_noarch_packages_terminate_build    0
%global _unpackaged_files_terminate_build               0
Name:           portage
Version:        3.0.68
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Portage is the package management and distribution system for Gentoo

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPLv2
URL:            https://github.com/gentoo/portage
Source:         https://codeload.github.com/gentoo/portage/tar.gz/refs/tags/portage-3.0.68#/%{name}-%{version}.tar.gz

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  xmlto
BuildRequires:  python3-sphinx
BuildRequires:  fdupes
Requires:       bash
Requires:       (coreutils or env)
Requires:       (python-unversioned-command or python)
Requires(post): shadow-utils
Requires(post): sed
Requires(post): coreutils
BuildArch:      noarch
Packager:       bunzuhbu <g89156436@gmail.com>

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
[![CI](https://github.com/gentoo/portage/actions/workflows/ci.yml/badge.svg)](https://github.com/gentoo/portage/actions/workflows/ci.yml)

About Portage
=============

Portage is a package management system based on ports collections. The
Package Manager Specification Project (PMS) standardises and documents
the behaviour of Portage so that ebuild repositories can be used by
other package managers.

Contributing
============

Contributions are always welcome! We've started using
[black](https://pypi.org/project/black/) to format the code base. Please make
sure you run it against any PR's prior to submitting (otherwise we'll probably
reject it).

There are [ways to
integrate](https://black.readthedocs.io/en/stable/integrations/editors.html)
black into your text editor and/or IDE.

You can also set up a git hook to check your commits, in case you don't want
editor integration. Something like this:

```sh
# .git/hooks/pre-commit (don't forget to chmod +x)

#!/bin/bash
black --check --diff .
```

One can also use pre-commit to run the configured pre-commit
hooks. Utilizing pre-commit has the advantage of running the linter
over only the changed files, resulting in a much faster pre-commit
hook. To use, install pre-commit and then install the hook to your
.git:

```sh
emerge dev-vcs/pre-commit
pre-commit install
```

To ignore commit 1bb64ff452 (and other reformatting commits) which is a
massive commit that simply formatted the code base using black - you can do
the following:

```sh
git config blame.ignoreRevsFile .git-blame-ignore-revs
```

Dependencies
============

Python and Bash should be the only hard dependencies. Python 3.9 is the
minimum supported version.

Native Extensions
=================

Portage includes some optional native extensions which can be built
in the source tree by running the following command:

    python setup.py build_ext --inplace --portage-ext-modules

The following setup.cfg settings can be used to enable building of
native extensions for all invocations of the build_ext command (the
build_ext command is invoked automatically by other build commands):

```
   [build_ext]
   portage_ext_modules=true
```

Currently, the native extensions only include libc bindings which are
used to validate LC_CTYPE and LC_COLLATE behavior for EAPI 6. If the
native extensions have not been built, then portage will use ctypes
instead.

Licensing and Legalese
=======================

Portage is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
version 2 as published by the Free Software Foundation.

Portage is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Portage; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.


More information
================

- DEVELOPING contains some code guidelines.
- LICENSE contains the GNU General Public License version 2.
- NEWS contains new features/major bug fixes for each version.
- RELEASE NOTES contains mainly upgrade information for each version.
- TEST-NOTES contains Portage unit test information.


Links
=====

- Gentoo project page: https://wiki.gentoo.org/wiki/Project:Portage
- PMS: https://dev.gentoo.org/~ulm/pms/head/pms.html
- PMS git repo: https://gitweb.gentoo.org/proj/pms.git/
}

%description %_description

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

%build
%meson
%meson_build


%install
%meson_install

%post
useradd -r -u 250 -g 250 -d /var/tmp/portage -s /bin/false portage
groupadd -g 250 portage
mkdir -pv %{_sysconfdir}
cp -RTfvpu %{_datadir}/%{name}/config %{_sysconfdir}/%{name}
dir="$(cat %{_sysconfdir}/%{name}/repos.conf | sed -n 's~location\s*=\s*\(.*\)\s*~\1~pg;')/profiles"
mkdir -pv "${dir}"


%files
%{_bindir}/*
%{python_sitearch}/%{name}
%{_prefix}/lib/%{name}
%{python_sitelib}/*
%{_datadir}/%{name}
%{_sysconfdir}/*
%{_mandir}/man*/*

%changelog
%autochangelog
