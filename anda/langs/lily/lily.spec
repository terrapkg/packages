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

%package       devel
Summary:       Development files for lily
Requires:      %{name}
%pkg_devel_files

%prep
%autosetup -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
install -Dm644 redhat-linux-build/lib/liblily.so %{buildroot}/usr/lib64/liblily.so
%cmake_install

%files
%doc README.md RELEASES.md
%license LICENSE.txt
%{_bindir}/lily

%files devel
/usr/lib64/liblily.so
%ghost /usr/lib/liblily.so
%{_includedir}/lily/lily.h

%changelog
* Thu Oct 30 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial package
