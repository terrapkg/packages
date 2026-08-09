%global debug_package %{nil}
%define npm_name @earendil-works/pi-coding-agent

Name:           pi
Version:        0.84.1
Release:        1%{?dist}
Summary:        Coding agent CLI with read, bash, edit, write tools and session management
License:        MIT
URL:            https://pi.dev
Source0:        http://registry.npmjs.org/%{npm_name}/-/pi-coding-agent-%{version}.tgz
ExclusiveArch:  x86_64 aarch64

BuildRequires:  nodejs-packaging
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-license-checker

Requires:       fd-find
Requires:       ripgrep

Packager:       June Fish <june@fyralabs.com>

%ifarch aarch64
%define platform "linux-arm64"
%endif
%ifarch x86_64
%define platform "linux-x64"
%endif

%description
%summary.

%prep
%npm_prep

%build

%install
%npm_install -s pi
ln -sf %{nodejs_sitelib}/%{npm_name}/dist/cli.js %{buildroot}%{_bindir}/pi

%npm_license -o LICENSE.modules

%files
%doc README.md
%license LICENSE.modules
%{nodejs_sitelib}/%{npm_name}/
%{_bindir}/pi

%changelog
* Sat Aug 8 2026 June Fish <june@fyralabs.com> - 0.84.1-1
- Initial Package
