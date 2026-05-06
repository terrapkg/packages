# The original is dead and has vulnerabilities due to it, this fork is maintainted
%global npm_name license-checker-rseidelsohn
# Disabled for now. Requires ESLint.
%bcond test 0

Name:          nodejs-license-checker
Version:       4.4.2
Release:       2%{?dist}
Summary:       Check NPM package licenses
SourceLicense: BSD-3-Clause
License:       Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CC-BY-3.0 AND ISC AND (MIT AND CC-BY-3.0) AND MIT
URL:           https://github.com/RSeidelsohn/license-checker-rseidelsohn
BuildRequires: anda-srpm-macros >= 0.2.25
BuildRequires: nodejs-devel
BuildRequires: nodejs-npm
BuildRequires: nodejs-packaging
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Packager:      Gilver E. <roachy@fyralabs.com>

%description
Extract NPM package licenses.
Enhanced and updated fork of Dav Glass' original (but abandoned) license-checker.

%prep
%npm_prep
%if %{with test}
%fetch_node_tests /tests .eslintrc.json .eslintignore
%endif

%build

%install
%npm_install -s license-checker

# Bootstrap the license fetching
# Environment variable is one set during execution of %%npm_install
./bin/%{npm_name}$_js --limitAttributes licenses --out LICENSE.modules

%if %{with test}
%check
%npm_audit
%npm_test
%endif

%files
%license LICENSE
%license LICENSE.modules
%doc CHANGELOG.md
%doc README.md
%doc SECURITY.md
%{_bindir}/license-checker
%{nodejs_sitelib}/%{npm_name}
