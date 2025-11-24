%global debug_package %{nil}
%bcond bootstrap 1

Name:          yarnpkg-berry
Version:       4.12.0
Release:       1%?dist
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
Requires:      nodejs
Provides:      yarn-berry
Provides:      yarnpkg = %{evr}
BuildArch:     noarch
Packager:      Gilver E. <rockgrub@disroot.org>

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
mkdir -p {%{buildroot}%{nodejs_sitelib}/yarn-berry,%{buildroot}%{_bindir}}
cp -pr {scripts,packages,.pnp.cjs,.pnp.loader.mjs,.yarn} -t %{buildroot}%{nodejs_sitelib}/yarn-berry

for bin in yarn yarnpkg; do
   ln -sfr %{buildroot}%{nodejs_sitelib}/yarn-berry/scripts/bin/$bin %{buildroot}%{_bindir}/$bin
done

%files
%license LICENSE.md
%license CODEOWNERS
%doc README.md
%doc CHANGELOG.md
%doc SECURITY.md
%{_bindir}/yarn
%{_bindir}/yarnpkg
%{nodejs_sitelib}/yarn-berry/

%files doc
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc HISTORY.md
%doc GOVERNANCE.md

%changelog
* Thu Nov 20 2025 Gilver E. <rockgrub@disroot.org> - 4.11.0-1
- Initial build
