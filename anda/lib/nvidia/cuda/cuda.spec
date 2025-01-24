%global debug_package %{nil}
%global major_package_version 12-6

Name:           cuda
Version:        12.6.77
Release:        1%{?dist}
Summary:        NVIDIA Compute Unified Device Architecture Toolkit
Epoch:          1
License:        CUDA Toolkit
URL:            https://developer.nvidia.com/cuda-zone
ExclusiveArch:  x86_64 aarch64

# Nvidia really provides the same package for ppc64le, aarch64 and x86_64 but
# it's really the same package.
Source0:        https://developer.download.nvidia.com/compute/cuda/redist/cuda_documentation/linux-x86_64/cuda_documentation-linux-x86_64-%{version}-archive.tar.xz

Source3:        %{name}.sh
Source4:        %{name}.csh
Source21:       cuda.pc

Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-minimal-build-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description
CUDA is a parallel computing platform and programming model that enables
dramatic increases in computing performance by harnessing the power of the
graphics processing unit (GPU).

%package cli-tools
Summary:        Compute Unified Device Architecture command-line tools
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-cupti%{?_isa}
Requires:       %{name}-devel%{?_isa}
Requires:       %{name}-gdb%{?_isa}
Requires:       %{name}-memcheck%{?_isa}
Requires:       %{name}-nvdisasm%{?_isa}
%ifnarch aarch64
Requires:       %{name}-nvprof%{?_isa}
%endif
Requires:       %{name}-nvtx%{?_isa}
Requires:       %{name}-sanitizer%{?_isa}
Requires:       expat >= 1.95
Conflicts:      %{name}-command-line-tools-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description cli-tools
Contains the command line tools to debug and profile CUDA applications.

%package libs
Summary:        Compute Unified Device Architecture native run-time library
Requires(post): ldconfig
Requires:       %{name}-cudart%{?_isa}
Requires:       %{name}-nvrtc%{?_isa}
Requires:       libcublas%{?_isa}
Requires:       libcufft%{?_isa}
Requires:       libcufile%{?_isa}
Requires:       libcurand%{?_isa}
Requires:       libcusolver%{?_isa}
Requires:       libcusparse%{?_isa}
Requires:       libnpp%{?_isa}
Requires:       libnvjpeg%{?_isa}
Conflicts:      %{name}-driver-devel-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      %{name}-libraries-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}
# Explicitly declare the dependency or libcuda.so.1()(64bit) will pull in xorg-x11-drv-cuda-libs
Requires:       nvidia-driver-cuda-libs%{_isa}

%description libs
Contains the CUDA run-time library required to run CUDA application natively.

%package extra-libs
Summary:        All runtime NVIDIA CUDA libraries
Requires(post): ldconfig
Requires:       %{name}-cupti%{?_isa}
Conflicts:      %{name}-runtime-%{major_package_version} < %{?epoch:%{epoch}:}%{version}-%{release}

%description extra-libs
Metapackage that installs all runtime NVIDIA CUDA libraries.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-libs%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-cccl-devel%{?_isa}
Requires:       %{name}-cudart-devel%{?_isa}
Requires:       %{name}-cupti-devel%{?_isa}
Requires:       %{name}-nvcc%{?_isa}
Requires:       %{name}-nvprof-devel%{?_isa}
Requires:       %{name}-nvprune%{?_isa}
Requires:       %{name}-nvml-devel%{?_isa}
Requires:       %{name}-nvrtc-devel%{?_isa}
Requires:       %{name}-nvtx-devel%{?_isa}
Requires:       %{name}-cuobjdump%{?_isa}
Requires:       %{name}-cuxxfilt-devel%{?_isa}
Requires:       libcublas-devel%{?_isa}
Requires:       libcufft-devel%{?_isa}
Requires:       libcufile-devel%{?_isa}
Requires:       libcurand-devel%{?_isa}
Requires:       libcusolver-devel%{?_isa}
Requires:       libcusparse-devel%{?_isa}
Requires:       libnpp-devel%{?_isa}
Requires:       libnvjpeg-devel%{?_isa}
Conflicts:      %{name}-headers-%{major_package_version} < %{?epoch:%{epoch}:}%{version}
Conflicts:      %{name}-libraries-dev-%{major_package_version} < %{?epoch:%{epoch}:}%{version}
Conflicts:      %{name}-misc-headers-%{major_package_version} < %{?epoch:%{epoch}:}%{version}
Conflicts:      %{name}-toolkit-%{major_package_version} < %{?epoch:%{epoch}:}%{version}
Provides:       %{name}-toolkit-%{major_package_version} = %{?epoch:%{epoch}:}%{version}

%description devel
This package provides the development files of the %{name} package.

%prep
%setup -q -n cuda_documentation-linux-x86_64-%{version}-archive

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/

# Environment settings
install -pm 644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_sysconfdir}/profile.d

# pkg-config files
install -pm 644 %{SOURCE21} %{buildroot}/%{_libdir}/pkgconfig

# Set proper variables
sed -i \
    -e 's|CUDA_VERSION|%{version}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDE_DIR|%{_includedir}/cuda|g' \
    %{buildroot}/%{_libdir}/pkgconfig/*.pc

%files
%license LICENSE
%doc CUDA_Toolkit_Release_Notes.txt DOCS EULA.txt README tools
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.*sh

%files cli-tools
# Empty metapackage

%files libs
# Empty metapackage

%files extra-libs
# Empty metapackage

%files devel
%{_libdir}/pkgconfig/cuda.pc

%changelog
%autochangelog
