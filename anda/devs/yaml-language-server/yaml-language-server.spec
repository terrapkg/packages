%define debug_package %nil
%global npm_name yaml-language-server

Name:           %npm_name
Version:        1.24.0
Release:        1%?dist
Summary:        YAML language server
License:        MIT
URL:            https://github.com/redhat-developer/yaml-language-server
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-license-checker

%description
Provides YAML language features over the Language Server Protocol (LSP), including validation, completion, hover, formatting, document symbols, and schema-based intelligence.

%prep
%npm_prep

%build
%npm_license_summary
%npm_license -o LICENSE.modules

%install
%npm_install

%files
%doc README.md
%license LICENSE LICENSE.modules
%nodejs_sitelib/%npm_name/
%_bindir/%npm_name

%changelog
* Tue Aug 18 2026 madonuko <mado@fyralabs.com> - 1.24.0-1
- Initial package
