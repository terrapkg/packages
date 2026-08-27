Name:           unrar
Version:        7.2.7
Release:        1%{?dist}
Summary:        Utility for extracting, testing and viewing RAR archives

License:        LicenseRef-unrar AND BSD-2-Clause AND CC0-1.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://www.rarlab.com/rar_add.htm
Source0:        https://www.rarlab.com/rar/unrarsrc-%{version}.tar.gz
# Man page from debian
Source1:        unrar.1

Packager:       ammix <maxim@ammix.dev>

BuildRequires:  gcc-c++
BuildRequires:  make

%description
The unrar utility is a freeware program for extracting, testing and
viewing the contents of archives created with the RAR archiver.

%prep
%autosetup -n %{name}

%build
%set_build_flags
%make_build -f makefile unrar \
    CXXFLAGS="$CXXFLAGS -std=c++11 -Wno-parentheses -Wno-switch -Wno-sign-compare -Wno-class-memaccess -Wno-unused-variable -Wno-unused-function -Wno-dangling-else" \
    LDFLAGS="$LDFLAGS -pthread" \
    STRIP=:

%install
install -Dpm 0755 unrar %{buildroot}%{_bindir}/unrar
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/unrar.1

%files
%license license.txt acknow.txt
%doc readme.txt
%{_bindir}/unrar
%{_mandir}/man1/unrar.1*

%changelog
* Thu Aug 27 2026 ammix <maxim@ammix.dev> - 7.2.7-1
- Initial package
