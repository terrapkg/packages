%global pypi_name magic-wormhole
%global _desc get things from one computer to another, safely.

Name:			python-%{pypi_name}
Version:		0.22.0
Release:		1%?dist
Summary:		get things from one computer to another, safely
License:		MIT
URL:			https://github.com/magic-wormhole/magic-wormhole
Source0:		%url/archive/refs/tags/%version.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-versioneer

Packager:	    Owen Zimmerman <owen@fyralabs.com>

%description
%_desc

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Provides:       magic-wormhole
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_desc

%pkg_completion -bfzn %{pypi_name} wormhole_complete

%prep
%autosetup -n magic-wormhole-%{version}

%build
%pyproject_wheel

%install
install -Dm644 wormhole_complete.bash %{buildroot}%{bash_completions_dir}/wormhole_complete.bash
install -Dm644 wormhole_complete.fish %{buildroot}%{fish_completions_dir}/wormhole_complete.fish
install -Dm644 wormhole_complete.zsh %{buildroot}%{zsh_completions_dir}/_wormhole_complete
install -Dm644 docs/wormhole.1 %{buildroot}%{_mandir}/man1/wormhole.1
%pyproject_install
%pyproject_save_files wormhole
rm %{buildroot}%{_usr}/wormhole_complete.*

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md docs/*.rst
%license LICENSE
%{_bindir}/magic-wormhole
%{_bindir}/wormhole
%{_mandir}/man1/wormhole.1.gz
%ghost %python3_sitelib/__pycache__/*.cpython-*.pyc
%ghost %python3_sitelib/%{name}/subcommands/__pycache__/*.cpython-*.pyc
%python3_sitelib/magic_wormhole-%version.dist-info/*

%changelog
* Mon Nov 03 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
