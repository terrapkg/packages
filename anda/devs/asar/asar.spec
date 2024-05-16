%define debug_package %nil
%define __strip /bin/true
%global _build_id_links none

# Exclude private libraries
%global __requires_exclude libffmpeg.so
%global __provides_exclude_from %{_datadir}/%{name}/.*\\.so

Name:           asar
Version:        3.2.10
Release:        1%?dist
Summary:        Simple extensive tar-like archive format with indexing
License:        MIT
URL:            https://github.com/electron/asar
Source0:        %url/archive/refs/tags/v%version.tar.gz
Requires:       nodejs
BuildRequires:  nodejs-npm

%description
Asar is a simple extensive archive format, it works like `tar` that concatenates all files
together without compression, while having random access support.

%prep
%autosetup

%build

%install
mkdir -p %buildroot%_bindir
PATH="$PATH:%buildroot%_bindir"
npm install -g --prefix %buildroot%_prefix %SOURCE0

%files
%doc README.md
%license LICENSE.md
%_bindir/asar
%_prefix/lib/node_modules/@electron/asar/

%changelog
%autochangelog
