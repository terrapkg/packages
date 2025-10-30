Name:           lily
Summary:        Interpreted language focused on expressiveness and type safety
Version:        2.2
Release:        1%?dist
License:        MIT
URL:            https://github.com/fascinatedbox/lily
Source0:        %url/archive/refs/tags/v%version.tar.gz
Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md RELEASES.md
%license LICENSE.txt
%{_bindir}/lily
/usr/lib/liblily.so
%{_includedir}/lily/lily.h

%changelog
* Thu Oct 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial package
