%global npm_name backport
# Requires Jest so currently disabled
%bcond test 0

Name:          nodejs-%{npm_name}
Version:       10.2.0
Release:       3%{?dist}
Summary:       Backport GitHub commits
SourceLicense: Apache-2.0
License:       0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT AND (MIT OR CC0-1.0) AND (WTFPL OR ISC)
URL:           https://github.com/sorenlouv/%{npm_name}
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: anda-srpm-macros >= 0.3.0
BuildRequires: nodejs-packaging
BuildRequires: nodejs-npm
BuildRequires: nodejs-license-checker
%if %{with test}
BuildRequires: yarnpkg
%endif
Obsoletes:     node-backport <= 10.2.0
BuildArch:     noarch
Packager:      Gilver E. <roachy@fyralabs.com>

%description
A simple CLI tool that automates the process of backporting commits on a GitHub repo.

%prep
%npm_prep
%fetch_node_tests /src/test/ /tests/

%build
# Empty build section, because RPM reasons

%install
%npm_install

%npm_license_summary
%npm_license -o LICENSE.modules

%if %{with test}
%check
%yarn_test
%endif

%files
%doc README.md
%license LICENSE.txt
%license LICENSE.modules
%{nodejs_sitelib}/%{npm_name}/
%{_bindir}/%{npm_name}

%changelog
* Wed Jan 21 2026 Gilver E. <roachy@fyralabs.com> - 10.2.0-3
- Fixed package name and licenses
* Wed Jul 2 2025 Gilver E. <rockgrub@disroot.org> - 9.6.6-1
- Initial package
