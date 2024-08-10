#? https://github.com/OpenMandrivaAssociation/lsp-dsp-lib/blob/master/lsp-dsp-lib.spec

#define _empty_manifest_terminate_build 0

Name:           liblsp-dsp
Version:        1.0.25
Release:        1%dist
Summary:        DSP library for signal processing
License:        LGPL-3.0
#Group:          System/Libraries
URL:            https://github.com/sadko4u/lsp-dsp-lib
BuildRequires:  make git-core gcc gcc-c++
Packager:       madonuko <mado@fyralabs.com>

%description
DSP library for digital signal processing (and more).

This library provides set of functions that perform SIMD-optimized 
computing on several hardware architectures.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
DSP library for digital signal processing (and more).

This library provides set of functions that perform SIMD-optimized 
computing on several hardware architectures.

This package contains the development files for the %name package.

%prep
rm -rf * .*
git clone --recurse-submodules -j8 %url -b %version --depth 1 .

%build
make config PREFIX=%{_prefix} LIBDIR=%{_libdir}
make fetch
%make_build

%install
%make_install

%files
%doc README.md
%license COPYING
%_libdir/*.so

%files devel
%_libdir/*.a
%_includedir/lsp-plug.in/
%_libdir/pkgconfig/lsp-dsp-lib.pc

%changelog
* Sat Aug 10 2024 madonuko <mado@fyralabs.com>
- Initial package
