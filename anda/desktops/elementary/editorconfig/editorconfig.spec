# build process has race conditions, force single thread
%global _smp_mflags -j1

%global srcname editorconfig-core-c

%global common_description %{expand:
EditorConfig makes it easy to maintain the correct coding style when
switching between different text editors and between different projects.
The EditorConfig project maintains a file format and plugins for various
text editors which allow this file format to be read and used by those
editors.}

Name:           editorconfig
Summary:        Parser for EditorConfig files written in C
Version:        v0.12.5
Release:        1%{?dist}
License:        BSD

URL:            https://github.com/editorconfig/editorconfig-core-c
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  pcre2-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description %common_description


%package        libs
Summary:        Parser library for EditorConfig files (shared library)
%description    libs %common_description

This package contains the shared library.


%package        devel
Summary:        Parser library for EditorConfig files (development files)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake

%description    devel %common_description

This package contains the files needed for development.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%cmake
%cmake_build


%install
%cmake_install

# Remove static library
rm %{buildroot}/%{_libdir}/libeditorconfig_static.a


%files
%doc README.md
%license LICENSE

%{_bindir}/editorconfig
%{_bindir}/editorconfig-%{version}

%{_mandir}/man1/editorconfig.1*

%files libs
%doc README.md
%license LICENSE

%{_libdir}/libeditorconfig.so.0*

%{_mandir}/man3/editorconfig*
%{_mandir}/man5/editorconfig*

%files devel
%{_includedir}/editorconfig/

%{_libdir}/libeditorconfig.so
%{_libdir}/cmake/EditorConfig/
%{_libdir}/pkgconfig/editorconfig.pc


%changelog
* Sun Nov 27 2022 root - v0.12.5-1
- new version

* Sat Oct 15 2022 windowsboy111 <windowsboy111@fyralabs.com>
- Repackaged for Terra

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Fabio Valentini <decathorpe@gmail.com> - 0.12.5-1
- Update to version 0.12.5.

* Thu Feb 04 2021 Fabio Valentini <decathorpe@gmail.com> - 0.12.4-3
- Force single-threaded build to work around race conditions.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Fabio Valentini <decathorpe@gmail.com> - 0.12.4-1
- Update to version 0.12.4.

* Sat Aug 01 2020 Fabio Valentini <decathorpe@gmail.com> - 0.12.3-7
- Adapt to new cmake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Fabio Valentini <decathorpe@gmail.com> - 0.12.3-1
- Update to version 0.12.3.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.12.2-3
- Fix broken ldconfig_scriptlets use.

* Wed May 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.12.2-2
- Use single-job make for building.
- Added missing ldconfig scriptlets.
- Rewritten summaries.

* Thu Mar 22 2018 Fabio Valentini <decathorpe@gmail.com> - 0.12.2-1
- Initial package.

