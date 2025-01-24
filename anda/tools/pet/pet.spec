%define debug_package %nil

Name:           pet
Version:        1.0.1
Release:        1%?dist
Summary:        Simple command-line snippet manager
URL:            https://github.com/knqyf263/pet
Source0:        %url/archive/refs/tags/v%version.tar.gz
License:        MIT
BuildRequires:  golang anda-srpm-macros
Packager:       Owen Zimmerman <owen@fyralabs.com>
 
%description
%summary

%prep
%autosetup -n pet-%version
%go_prep_online
 
%build
%go_build_online

%install
install -Dm755 build/bin/pet %{buildroot}%{_bindir}/pet

%files
%license LICENSE
%doc README.md
%{_bindir}/pet
 
%changelog
* Wed Oct 2 2024 Owen-sz <owen@fyralabs.com> - 0.9.0-1
- package pet
