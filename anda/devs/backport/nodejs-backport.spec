%global debug_package %{nil}
%global module backport
%bcond test 1

Name:          node-%{module}
Version:       10.0.1
Release:       1%?dist
Summary:       Backport GitHub commits
SourceLicense: Apache-2.0
License:       Apache-2.0 AND
URL:           https://github.com/sorenlouv/%{module}
%dnl Source0:       http://registry.npmjs.org/%{module}/-/%{module}-%{version}.tgz
# Source the tests
Source1:       tests-%{version}.tar.bz2
BuildRequires: bsdtar
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: nodejs-npm
ExclusiveArch: %{nodejs_arches} noarch
Packager:      Gilver E. <rockgrub@disroot.org>

%description
A simple CLI tool that automates the process of backporting commits on a GitHub repo.

%prep
# Maybe I should make some NodeJS online macros...
# Global flag is needed or the module WILL NOT WORK via commandline without some manual intervention
npm install -g %{module}@%{version} --prefix=.
%setup -T -D -n lib/node_modules/%{module}
tar xjf %{SOURCE1}

%build
# Empty build section, because RPM reasons

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module}
mkdir -p %{buildroot}%{_bindir}
cp -r ./* -t %{buildroot}%{nodejs_sitelib}/%{module}
ln -sf %{nodejs_sitelib}/%{module}/bin/%{module}  %{buildroot}%{_bindir}/%{module}

# Should maybe package this so it's easier to call...
npm install -g license-checker --prefix=.
# This could also be made into a macro maybe?
bin/license-checker | sed '/.*repository:.*/d;/.*publisher:.*/d;/.*email:.*/d;/.*url:.*/d;/.*path:.*/d;/.*licenseFile:.*/d;/.*noticeFile:.*/d' > LICENSE.modules

%check
%if %{with test}
NODE_ENV=test %{builddir}/bin/%{module} -R tests
%endif

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE.txt
%license LICENSE.modules
%{nodejs_sitelib}/%{module}/
%{_bindir}/%{module}

%changelog
* Wed Jul 2 2025 Gilver E. <rockgrub@disroot.org> - 9.6.6-1
- Initial package
