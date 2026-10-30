Name:           lito
Version:        0.8.8
Release:        1%{?dist}
License:        MIT OR Apache-2.0
Summary:        Module-first C++ builder and package manager
URL:            https://github.com/litocpp/lito
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake >= 3.29
BuildRequires:  clang >= 22
BuildRequires:  lld
BuildRequires:  sed
BuildRequires:  libcxx-devel
BuildRequires:  llvm
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libzstd)

Packager:       L1oly <lid2011@ukr.net>

%description
Lito is a module-first build tool for C++.
It uses lito.toml to define packages, workspaces, targets, dependencies, and build policy.
It also discovers named module sources and drives Clang, LLD, and LLVM tools.

%prep
%autosetup
sed -i 's/\bartifact_failure\b/registry_blob_failure/g' driver/src/registry/blob.cppm

%conf
CXXFLAGS="${CXXFLAGS//-Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3/}"
%if 0%{?fedora} >= 45
%global _lto_cflags %{nil}
%cmake -G Ninja -DLITO_USE_SYSTEM_ZSTD=ON -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=OFF
# without this doesn't compile on clang 23
%else
%cmake -G Ninja -DLITO_USE_SYSTEM_ZSTD=ON -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++
%endif

%build
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_datadir}/lito/lito.schema.json %{buildroot}%{_datadir}/lito.schema.json

%files
%license LICENSE-MIT LICENSE-APACHE
%license %{_datadir}/licenses/licrypto/LICENSE-MIT
%license %{_datadir}/licenses/licrypto/LICENSE-APACHE
%doc README.md
%{_bindir}/lito
%{_datadir}/lito.schema.json

%changelog
* Mon Oct 26 2026 L1oly <lid2011@ukr.net>
- Initial commit
