Name:           unrar
Version:        7.2.7
Release:        2%{?dist}
Summary:        Utility for extracting, testing and viewing RAR archives

License:        LicenseRef-unrar AND BSD-2-Clause AND CC0-1.0 AND LicenseRef-Fedora-Public-Domain
URL:            https://www.rarlab.com/rar_add.htm
Source0:        https://www.rarlab.com/rar/unrarsrc-%{version}.tar.gz
# Man page from debian
Source1:        https://raw.githubusercontent.com/debian-calibre/unrar-nonfree/master/debian/unrar-nonfree.1

Packager:       ammix <maxim@ammix.dev>

BuildRequires:  gcc-c++
BuildRequires:  make

%description
The unrar utility is a freeware program for extracting, testing and
viewing the contents of archives created with the RAR archiver.

%package -n libunrar
Summary:        Library for extracting RAR archives

%description -n libunrar
The libunrar library allows applications linking against it to extract
files from RAR archives.

%package -n libunrar-devel
Summary:        Development files for libunrar
Requires:       libunrar%{?_isa} = %{version}-%{release}

%description -n libunrar-devel
The libunrar-devel package contains the headers needed to develop
applications that use libunrar.

%prep
%autosetup -n %{name}

%build
%set_build_flags
CXXFLAGS="$CXXFLAGS -std=c++11 -Wno-parentheses -Wno-switch -Wno-sign-compare -Wno-class-memaccess -Wno-unused-variable -Wno-unused-function -Wno-dangling-else"
%make_build -f makefile unrar \
    CXXFLAGS="$CXXFLAGS" \
    LDFLAGS="$LDFLAGS -pthread" \
    STRIP=:
rm -f *.o
%make_build -f makefile lib \
    CXXFLAGS="$CXXFLAGS -fPIC -DPIC" \
    LDFLAGS="$LDFLAGS -pthread" \
    STRIP=:

%install
install -Dpm 0755 unrar %{buildroot}%{_bindir}/unrar
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/unrar.1
install -Dpm 0755 libunrar.so %{buildroot}%{_libdir}/libunrar.so
install -dpm 0755 %{buildroot}%{_includedir}/unrar
install -pm 0644 *.hpp %{buildroot}%{_includedir}/unrar/
install -Dpm 0644 /dev/null %{buildroot}%{_rpmmacrodir}/macros.unrar
echo "%%unrar_version %{version}" > %{buildroot}%{_rpmmacrodir}/macros.unrar

%ldconfig_scriptlets -n libunrar

%files
%license license.txt acknow.txt
%doc readme.txt
%{_bindir}/unrar
%{_mandir}/man1/unrar.1*

%files -n libunrar
%license license.txt acknow.txt
%doc readme.txt
%{_libdir}/libunrar.so

%files -n libunrar-devel
%license license.txt acknow.txt
%doc readme.txt
%{_includedir}/unrar/
%{_rpmmacrodir}/macros.unrar

%changelog
* Thu Aug 27 2026 ammix <maxim@ammix.dev> - 7.2.7-2
- Add libunrar and libunrar-devel subpackages

* Thu Aug 27 2026 ammix <maxim@ammix.dev> - 7.2.7-1
- Initial package
