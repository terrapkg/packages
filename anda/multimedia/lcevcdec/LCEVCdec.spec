# This information is required if not building from a GIT checkout.
# See cmake/modules/VNovaSetup.cmake:
%global gitlonghash bf7e0d91c969502e90a925942510a1ca8088afec
%global gitdate 20250320
%global githash %(c=%{gitlonghash}; echo ${c:0:7})
%global gitbranch main

# Tests require network, as described in src/func_tests/README.md, and each test type
# (Qualcomm dev kit, Ubuntu, etc.) requires the download of a few gigabytes of videos
# from https://lcevcdec.nbg1.your-objectstorage.com. The videos used for testing
# are described in the "Content attribution" paragraph of the README.md file.
# So disable tests by default:
%bcond python_tests 0

# python3-sphinxcontrib-plantuml currently missing from Fedora:
%bcond docs 0

Name:           LCEVCdec
Version:        3.3.8
Release:        1%?dist
Summary:        MPEG-5 LCEVC Decoder
License:        BSD-3-Clause-Clear
URL:            https://docs.v-nova.com/v-nova/lcevc/lcevc-sdk-overview

Source0:        https://github.com/v-novaltd/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         %{name}-soversion.patch

BuildRequires:  cmake
BuildRequires:  cmake(CLI11)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(range-v3)
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(gtest)

%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  sphinx
BuildRequires:  plantuml
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-plantuml
%endif

%if %{with tests}
BuildRequires:  python3
BuildRequires:  python3-GitPython
BuildRequires:  python3-numpy
BuildRequires:  python3-requests
%endif

%description
Low Complexity Enhancement Video Codec Decoder (LCEVCdec) is the primary MPEG-5
Part 2 decoder SDK repository maintained by V-Nova.

Features:
 - Decode LCEVC compliant bitstreams
 - Support for a range of formats including YUV, NV12 and RGBA
 - Support for a range of colour formats including BT709 and BT2020
 - Support for HDR and 10-bit streams
 - Support for ABR ladders
 - CPU pixel processing stage
 - Extensive API

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       plutovg-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    static
Static library files for %{name}.

%package        samples
Summary:        Sample programs for %{name}

%description    samples
Sample programs that use %{name}.

%prep
%autosetup -p1

# This information is required if not building from a GIT checkout.
# See cmake/modules/VNovaSetup.cmake:
echo -n %{gitlonghash} > .gitlonghash
echo -n %{gitdate} | date +%Y-%m-%d > .gitdate
echo -n %{githash} > .githash
echo -n %{gitbranch} > .gitbranch
echo -n %{version} > .gitversion
echo -n %(echo %version | cut -d. -f1) > .gitshortversion

%if %{with tests}
# Adjust configuration file for tests:
sed -i \
    -e 's/BIN_DIR = build/BIN_DIR = %{_vpath_builddir}/g' \
    src/func_tests/config.ini
%endif

%build
%cmake \
  -DBUILD_SHARED_LIBS=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DVN_SDK_EXECUTABLES=ON \
  -DVN_SDK_UNIT_TESTS=ON \
  -DVN_SDK_API_LAYER=ON \
  -DVN_SDK_JSON_CONFIG=ON \
%if %{with docs}
  -DVN_SDK_DOCS=ON
%else
  -DVN_SDK_DOCS=OFF
%endif

%cmake_build

%install
%cmake_install

%ifnarch %ix86
mv %{buildroot}%{_prefix}/lib/*.a %{buildroot}%{_libdir}/
rm -fr %{buildroot}%{_prefix}/lib
%endif

# Let RPM pick up docs in the files section
rm -fr %{buildroot}%{_docdir} %{buildroot}%{_prefix}/licenses

%if %{with tests}
%check
python3 src/func_tests/run_tests.py
%endif

%files
%license LICENSE.md COPYING
%doc README.md
%{_libdir}/liblcevc_dec_api.so.3
%{_libdir}/liblcevc_dec_api.so.%{version}
%{_libdir}/liblcevc_dec_core.so.3
%{_libdir}/liblcevc_dec_core.so.%{version}

%files devel
%{_includedir}/LCEVC
#{_includedir}/lcevc_config.h
%{_libdir}/liblcevc_dec_api.so
%{_libdir}/liblcevc_dec_core.so
%{_libdir}/pkgconfig/lcevc_dec.pc

%files static
%{_libdir}/liblcevc_dec_api_static.a
%{_libdir}/liblcevc_dec_api_utility.a
%{_libdir}/liblcevc_dec_core_sequencing.a
%{_libdir}/liblcevc_dec_core_static.a
%{_libdir}/liblcevc_dec_enhancement_cpu.a
%{_libdir}/liblcevc_dec_overlay_images.a
%{_libdir}/liblcevc_dec_unit_test_utilities.a
%{_libdir}/liblcevc_dec_utility.a

%files samples
%{_bindir}/lcevc_dec_sample
%{_bindir}/lcevc_dec_test_harness
%{_bindir}/lcevc_dec_test_unit
%{_bindir}/lcevc_dec_utility_test_unit
%{_bindir}/lcevc_core_test_unit
%{_bindir}/lcevc_core_sequencing_test_unit

%changelog
%autochangelog
