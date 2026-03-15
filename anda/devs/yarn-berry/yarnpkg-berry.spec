%bcond bootstrap 0

Name:          yarnpkg-berry
Version:       4.12.0
Release:       5%{?dist}
Summary:       Active development version of Yarn
License:       BSD-2-Clause
URL:           https://yarnpkg.com
Source0:       https://github.com/yarnpkg/berry/archive/refs/tags/@yarnpkg/cli/%{version}.tar.gz
Patch0:        setup-ts-cache.patch
BuildRequires: anda-srpm-macros
BuildRequires: nodejs
BuildRequires: nodejs-packaging
%if %{with bootstrap}
BuildRequires: yarnpkg
%else
BuildRequires: %{name}
%endif
Provides:      yarn-berry
Conflicts:     yarnpkg
BuildArch:     noarch
Packager:      Gilver E. <roachy@fyralabs.com>

%description
The next, actively developed version of Yarn.

%package       doc
Summary:       Extra documentation and contributor guides for Yarn Berry.

%description   doc
This package contains extra doc files as well as contributor material for Yarn Berry.

%prep
%autosetup -p1 -n berry--yarnpkg-cli-%{version}

%build
%{__yarn} build:cli

%install
# Yarn cannot be installed in nodejs_sitelib due to using TypeScript runtimes and NodeJS changes disallowing TypeScript in node_modules
mkdir -p {%{buildroot}%{_bindir},%{buildroot}%{_libdir}/yarn-berry}
cp -pr {scripts,packages,.pnp.cjs,.pnp.loader.mjs,.yarn} -t %{buildroot}%{_libdir}/yarn-berry

for bin in yarn yarnpkg; do
   ln -sfr %{buildroot}%{_libdir}/yarn-berry/scripts/bin/$bin %{buildroot}%{_bindir}/$bin
done

%files
%license LICENSE.md
%license CODEOWNERS
%doc README.md
%doc CHANGELOG.md
%doc SECURITY.md
%{_bindir}/yarn
%{_bindir}/yarnpkg
%{_libdir}/yarn-berry/

%files doc
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc HISTORY.md
%doc GOVERNANCE.md

%changelog
* Sun Nov 23 2025 Gilver E. <rockgrub@disroot.org> - 4.12.0-3
- First build without bootstrap
* Thu Nov 20 2025 Gilver E. <rockgrub@disroot.org> - 4.11.0-1
- Initial build
