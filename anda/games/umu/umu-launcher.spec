Name:           umu-launcher
Version:        1.2.1
Release:        1%?dist
Summary:        A tool for launching non-steam games with proton

License:        GPL-3.0-only
URL:            https://github.com/Open-Wine-Components/umu-launcher

BuildArch:      noarch
BuildRequires:  anda-srpm-macros
BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  g++
BuildRequires:  gcc-c++
BuildRequires:  scdoc
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-hatchling
BuildRequires:  python
BuildRequires:  python3

Requires:	python
Requires:	python3
Requires:	python3-xlib
Requires:	python3-filelock


%description
%summary.

%prep
%git_clone %url %version

%build
./configure.sh --prefix=%_prefix
%make_build

%install
%make_install PYTHONDIR=%python3_sitelib

%files
%_bindir/umu-run
%_mandir/*
%_datadir/steam/compatibilitytools.d/umu-launcher/
%python3_sitelib/umu*
