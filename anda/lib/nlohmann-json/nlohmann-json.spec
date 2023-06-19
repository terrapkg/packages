%global debug_package %{nil}

Name: nlohmann-json
Version: 3.11.2
Release: 1%{?dist}

Summary: JSON for Modern C++ (c++11) ("single header file")


%define desc %{expand:
There are myriads of JSON libraries out there, and each may even have its
reason to exist. Our class had these design goals:
- intuitive syntax.
- Trivial integration.
- Serious testing}

License: MIT
Url: https://github.com/nlohmann/json

Source: https://github.com/nlohmann/json/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cmake gcc-c++

%description
%{desc}

%package devel
Summary: JSON for Modern C++ (c++11) ("single header file")
Group: Development/C++

%description devel
%{desc}

This package contains the single header C++ file and CMake dependency files.

%prep
%autosetup -n json-%{version}

%build
%cmake


%install
%cmake_install

%files devel
%doc README.md
%license LICENSE.MIT
%{_includedir}/nlohmann
%{_datadir}/cmake/nlohmann_json/
%{_datadir}/pkgconfig/nlohmann_json.pc

%changelog
* Mon Dec 26 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 3.11.2-1.um37
- Rebuild for Terra, dependency of libappimageupdate

* Fri Dec 10 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.10.4-alt1.1
- Fixed build for Elbrus.

* Mon Nov 15 2021 Paul Wolneykien <manowar@altlinux.org> 3.10.4-alt1
- new version 3.10.4

* Thu Sep 16 2021 Ivan A. Melnikov <iv@altlinux.org> 3.10.2-alt2
- Disable slower tests on %%mips and riscv64 to avoid timeouts.

* Tue Sep 14 2021 Paul Wolneykien <manowar@altlinux.org> 3.10.2-alt1
- Updated to v3.10.2.

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 3.8.0-alt3.1
- NMU: spec: adapted to new cmake macros.

* Thu Sep 10 2020 Ivan A. Melnikov <iv@altlinux.org> 3.8.0-alt3
- Skip test-unicode on mips*, as it timeouts.

* Fri Jul 03 2020 Paul Wolneykien <manowar@altlinux.org> 3.8.0-alt2
- Added the test data bundle.
- Fix: Run the tests with CMake.
- Skip the cmake_fetch_content test.

* Thu Jul 02 2020 Paul Wolneykien <manowar@altlinux.org> 3.8.0-alt1
- Freshed up to v3.8.0.

* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 3.7.2-alt2
- Run the auto-tests.
- Package CMake dependency files.
- This is now an arch package'nlohmann-json' providing nlohmann-json-devel
  and replacing json-cpp.
- Fixed project lincense: MIT.

* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 3.7.2-alt1
- Upstream version 3.7.2.
- Also install %%_includedir/nlohmann/json.hpp symlink.

* Mon Nov 26 2018 Pavel Vainerman <pv@altlinux.ru> 3.4.0-alt1
- new version

* Sun Mar 19 2017 Pavel Vainerman <pv@altlinux.ru> 2.1.1-alt1
- new version

* Tue Nov 08 2016 Pavel Vainerman <pv@altlinux.ru> 2.0.7-alt1
- new version

* Sun Oct 30 2016 Pavel Vainerman <pv@altlinux.ru> 2.0.6-alt0.1
- initial commit 
