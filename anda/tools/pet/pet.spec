Name:           Pet
Version:        0.9.0
Release:        1%?dist
Summary:        Simple command-line snippet manager
URL:            https://github.com/knqyf263/pet
Source0:        %url/archive/refs/tags/v%version.tar.gz
License:        MIT
BuildRequires:  golang anda-srpm-macros
Requires:       golang glibc
Packager:       Owen Zimmerman <owen@fyralabs.com>
 
%description
%summary

%prep
%autosetup -n pet-%version
 
%build
%global debug_package %{nil}
go build -o pet

%install
install -Dm755 pet %{buildroot}%{_bindir}/pet

%files
%license LICENSE
%doc README.md
%{_bindir}/pet
 
%changelog
* Wed Oct 2 2024 Owen-sz <owen@fyralabs.com>
- package pet
