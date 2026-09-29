Name:           codecheck-sarif
Version:        0.1.0
Release:        1%{?dist}
Summary:        C/C++ coding-rule checker that emits SARIF
License:        MIT
URL:            https://github.com/kotaronowwell/codecheck-sarif
Source0:        https://github.com/kotaronowwell/codecheck-sarif/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  anda-srpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-installer
BuildRequires:  pyproject-rpm-macros

Requires:       python3
Requires:       python3-clang

Packager:       Cypress Reed <cypress@fyralabs.com>

%description
Pluggable project-specific coding-rule checker for C and C++, emitting SARIF
2.1.0. It converts clang-tidy output, runs Python/libclang rules, and merges
SARIF produced by other analysis tools.

%prep
%autosetup -n %{name}-%{version}
sed -i '/^[[:space:]]*"libclang",[[:space:]]*$/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files codecheck

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/codecheck

%changelog
* Thu Sep 24 2026 Cypress Reed <cypress@fyralabs.com>
- Initial package
