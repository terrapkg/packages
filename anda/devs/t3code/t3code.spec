%global npm_name t3
%define debug_package %nil

Name:           t3code
Version:        0.0.14
Release:        1%?dist
Summary:        Minimal web GUI for coding agents
SourceLicense:  MIT
License:        FIXME
URL:            https://t3.codes
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:		https://raw.githubusercontent.com/pingdotgg/t3code/v%{version}/README.md
Source2:		https://raw.githubusercontent.com/pingdotgg/t3code/v%{version}/LICENSE
Packager:       madonuko <mado@fyralabs.com>
Provides:       t3 = %evr
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-license-checker

%description
T3 Code is a minimal web GUI for coding agents (currently Codex and Claude, more coming soon).

%prep
%npm_prep
cp %{S:1} %{S:2} .

%build

%install
%npm_install

%__npm_license_checker
%npm_license -o LICENSE.modules

%files
%doc README.md
%license LICENSE
%license LICENSE.modules
%{nodejs_sitelib}/%{npm_name}/
%{_bindir}/%{npm_name}

%changelog
* Fri Mar 27 2026 madonuko <mado@fyralabs.com> - 0.0.14-1
- Initial package
