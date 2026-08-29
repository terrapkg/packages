%define debug_package %nil
%global npm_name @devcontainers/cli

Name:           devcontainer
Version:        0.88.0
Release:        1%?dist
Summary:        Dev Containers CLI
SourceLicense:  MIT
License:        MIT
URL:            https://containers.dev
%dnl Source0:        https://github.com/devcontainers/cli/archive/refs/tags/v%version.tar.gz
Packager:       madonuko <mado@fyralabs.com>
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-license-checker

%description
%summary.

%prep
%npm_prep

%build
%npm_license_summary
%npm_license -o LICENSE.modules

%install
%npm_install -s devcontainer

%files
%doc README.md
%license LICENSE.txt LICENSE.modules
%_bindir/%name
%nodejs_sitelib/%npm_name/

%changelog
* Tue Aug 18 2026 madonuko <mado@fyralabs.com> - 0.88.0-1
- Initial package.
