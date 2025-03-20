Name:           umu-launcher
Version:        1.2.6
Release:        2%?dist
Summary:        A tool for launching non-steam games with proton

License:        GPL-3.0-only
URL:            https://github.com/Open-Wine-Components/umu-launcher

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
BuildRequires:  python3-pip
BuildRequires:  libzstd-devel
BuildRequires:  python3-hatch-vcs
BuildRequires:  python3-wheel
BuildRequires:  python3-xlib
BuildRequires:  python3-pyzstd
BuildRequires:  cargo
Requires:	python
Requires:	python3
Requires:	python3-xlib
Requires:	python3-filelock


%description
%summary.

%prep
%git_clone %url %version

%build
./configure.sh --prefix=%_prefix --use-system-pyzstd
%{make_build}

%install
%make_install PYTHONDIR=%{python3_sitelib}

%files
%_bindir/umu-run
%_mandir/*
%python3_sitelib/umu*
