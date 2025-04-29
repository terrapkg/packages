%global real_name cuda_nvcc

%global debug_package %{nil}
%global __strip /bin/true
%global _missing_build_ids_terminate_build 0
%global _build_id_links none
%global major_package_version 12-8

Name:           %(echo %real_name | tr '_' '-')
Epoch:          1
Version:        12.8.61
Release:        2%{?dist}
Summary:        CUDA Compiler (NVCC)
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-toolkit
ExclusiveArch:  x86_64 aarch64

Source0:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-x86_64/%{real_name}-linux-x86_64-%{version}-archive.tar.xz
Source1:        https://developer.download.nvidia.com/compute/cuda/redist/%{real_name}/linux-sbsa/%{real_name}-linux-sbsa-%{version}-archive.tar.xz
Source3:        nvcc.profile

Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

# CUDA 12.8 does not support GCC 15+:
%if 0%{?fedora} >= 42
Requires:       cuda-gcc
%else
# CUDA 12.8 supports GCC 14:
Obsoletes:      cuda-gcc
Provides:       cuda-gcc
%endif

%description
The compilation trajectory involves several splitting, compilation,
preprocessing, and merging steps for each CUDA source file. It is the purpose of
nvcc, the CUDA compiler driver, to hide the intricate details of CUDA
compilation from developers. It accepts a range of conventional compiler
options, such as for defining macros and include/library paths, and for steering
the compilation process. All non-CUDA compilation steps are forwarded to a C++
host compiler that is supported by nvcc, and nvcc translates its options to
appropriate host compiler command line options.

NVVM IR is a compiler IR (intermediate representation) based on the LLVM IR.
The NVVM IR is designed to represent GPU compute kernels (for example, CUDA
kernels). High-level language front-ends, like the CUDA C compiler front-end,
can generate NVVM IR. The NVVM compiler (which is based on LLVM) generates PTX
code from NVVM IR.

%prep
%ifarch x86_64
%setup -q -n %{real_name}-linux-x86_64-%{version}-archive
%endif

%ifarch aarch64
%setup -q -T -b 1 -n %{real_name}-linux-sbsa-%{version}-archive
%endif

%install
mkdir -p %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/nvcc/

cp -fr bin/* nvvm/bin/* %{buildroot}%{_bindir}/
cp -fr include/* nvvm/include/* %{buildroot}%{_includedir}/
cp -fr lib/* nvvm/lib64/* %{buildroot}%{_libdir}/
cp -fr nvvm/libdevice/* %{buildroot}%{_datadir}/nvcc/

cp -f %{SOURCE3} %{buildroot}%{_bindir}/

# Set proper variables
sed -i \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDE_DIR|%{_includedir}/cuda|g' \
    %{buildroot}/%{_bindir}/nvcc.profile

%files
%license LICENSE
%{_bindir}/bin2c
%{_bindir}/cicc
%dir %{_bindir}/crt/
%{_bindir}/crt/link.stub
%{_bindir}/crt/prelink.stub
%{_bindir}/cudafe++
%{_bindir}/fatbinary
%{_bindir}/nvcc
%{_bindir}/__nvcc_device_query
%{_bindir}/nvcc.profile
%{_bindir}/nvlink
%{_bindir}/ptxas
%dir %{_datadir}/nvcc/
%{_datadir}/nvcc/libdevice.10.bc
%dir %{_includedir}/crt/
%{_includedir}/crt/common_functions.h
%{_includedir}/crt/cudacc_ext.h
%{_includedir}/crt/device_double_functions.h
%{_includedir}/crt/device_double_functions.hpp
%{_includedir}/crt/device_fp128_functions.h
%{_includedir}/crt/device_functions.h
%{_includedir}/crt/device_functions.hpp
%{_includedir}/crt/func_macro.h
%{_includedir}/crt/host_config.h
%{_includedir}/crt/host_defines.h
%{_includedir}/crt/host_runtime.h
%{_includedir}/crt/math_functions.h
%{_includedir}/crt/math_functions.hpp
%{_includedir}/crt/mma.h
%{_includedir}/crt/mma.hpp
%{_includedir}/crt/nvfunctional
%{_includedir}/crt/sm_70_rt.h
%{_includedir}/crt/sm_70_rt.hpp
%{_includedir}/crt/sm_80_rt.h
%{_includedir}/crt/sm_80_rt.hpp
%{_includedir}/crt/sm_90_rt.h
%{_includedir}/crt/sm_90_rt.hpp
%{_includedir}/crt/sm_100_rt.h
%{_includedir}/crt/sm_100_rt.hpp
%{_includedir}/crt/storage_class.h
%{_includedir}/fatbinary_section.h
%{_includedir}/nvPTXCompiler.h
%{_includedir}/nvvm.h

%{_libdir}/libnvptxcompiler_static.a
%{_libdir}/libnvvm.so
%{_libdir}/libnvvm.so.4
%{_libdir}/libnvvm.so.4.0.0

%changelog
%autochangelog
