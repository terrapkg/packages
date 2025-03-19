%global debug_package %{nil}
%global __strip /bin/true
%global __brp_ldconfig %{nil}
%define _build_id_links none

# systemd 248+
%if 0%{?rhel} == 8
%global _systemd_util_dir %{_prefix}/lib/systemd
%endif

Name:           nvidia-driver
Version:        570.133.07
Release:        1%?dist
Summary:        NVIDIA's proprietary display driver for NVIDIA graphic cards
Epoch:          3
License:        NVIDIA License
URL:            http://www.nvidia.com/object/unix.html
ExclusiveArch:  %{ix86} x86_64 aarch64

%dnl Source0:        %{name}-%{version}-i386.tar.xz
%dnl Source1:        %{name}-%{version}-x86_64.tar.xz
%dnl Source2:        %{name}-%{version}-aarch64.tar.xz
Source8:        70-nvidia-driver.preset
Source9:        70-nvidia-driver-cuda.preset
Source10:       10-nvidia.conf
Source13:       alternate-install-present

Source40:       com.nvidia.driver.metainfo.xml
Source41:       parse-supported-gpus.py
Source42:       com.nvidia.driver.png

Source99:       nvidia-generate-tarballs.sh

%ifarch x86_64 aarch64
BuildRequires:  libappstream-glib
%if 0%{?rhel} == 8
# xml.etree.ElementTree has indent only from 3.9+:
BuildRequires:  python(abi) >= 3.9
%else
BuildRequires:  python3
%endif
BuildRequires:  systemd-rpm-macros
%endif

BuildRequires:  wget
BuildRequires:  coreutils

Requires:       nvidia-driver-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-kmod-common = %{?epoch:%{epoch}:}%{version}

Conflicts:      nvidia-x11-drv
Conflicts:      nvidia-x11-drv-470xx
Conflicts:      xorg-x11-drv-nvidia
Conflicts:      xorg-x11-drv-nvidia-470xx

%description
This package provides the most recent NVIDIA display driver which allows for
hardware accelerated rendering with recent NVIDIA chipsets.

For the full product support list, please consult the release notes for driver
version %{version}.

%package libs
Summary:        Libraries for %{name}
Requires:       egl-gbm%{?_isa} >= 2:1.1.2
Requires:       egl-wayland%{?_isa} >= 1.1.13.1
Requires:       egl-x11%{?_isa}
Requires:       libvdpau%{?_isa} >= 0.5
Requires:       libglvnd%{?_isa} >= 1.0
Requires:       libglvnd-egl%{?_isa} >= 1.0
Requires:       libglvnd-gles%{?_isa} >= 1.0
Requires:       libglvnd-glx%{?_isa} >= 1.0
Requires:       libglvnd-opengl%{?_isa} >= 1.0
Requires:       libnvidia-ml%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       vulkan-loader

Conflicts:      nvidia-x11-drv-libs
Conflicts:      nvidia-x11-drv-470xx-libs
Conflicts:      xorg-x11-drv-nvidia-libs
Conflicts:      xorg-x11-drv-nvidia-470xx-libs

%description libs
This package provides the shared libraries for %{name}.

%package cuda-libs
Summary:        Libraries for %{name}-cuda
Provides:       %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libnvidia-ml = %{?epoch:%{epoch}:}%{version}-%{release}

%ifarch x86_64 aarch64
Requires:       libnvidia-cfg = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

Conflicts:      xorg-x11-drv-nvidia-cuda-libs
Conflicts:      xorg-x11-drv-nvidia-470xx-cuda-libs

%description cuda-libs
This package provides the CUDA libraries for %{name}-cuda.

%package -n libnvidia-fbc
Summary:        NVIDIA OpenGL-based Framebuffer Capture libraries
Provides:       nvidia-driver-NvFBCOpenGL = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      nvidia-driver-NvFBCOpenGL < %{?epoch:%{epoch}:}%{version}-%{release}
# Loads libnvidia-encode.so at runtime
Requires:       %{name}-cuda-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libnvidia-fbc
This library provides a high performance, low latency interface to capture and
optionally encode the composited framebuffer of an X screen. NvFBC are private
APIs that are only available to NVIDIA approved partners for use in remote
graphics scenarios.

%package -n libnvidia-ml
Summary:        NVIDIA Management Library (NVML)
Provides:       cuda-nvml%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       nvidia-driver-NVML = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      nvidia-driver-NVML < %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libnvidia-ml
A C-based API for monitoring and managing various states of the NVIDIA GPU
devices. It provides a direct access to the queries and commands exposed via
nvidia-smi. The run-time version of NVML ships with the NVIDIA display driver,
and the SDK provides the appropriate header, stub libraries and sample
applications. Each new version of NVML is backwards compatible and is intended
to be a platform for building 3rd party applications.

%ifarch x86_64 aarch64

%package -n libnvidia-cfg
Summary:        NVIDIA Config public interface (nvcfg)

%description -n libnvidia-cfg
This package contains the private libnvidia-cfg runtime library which is used by
other driver components.

%package cuda
Summary:        CUDA integration for %{name}
Requires:       %{name}-cuda-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-persistenced = %{?epoch:%{epoch}:}%{version}
Requires:       opencl-filesystem
Requires:       ocl-icd

Conflicts:      xorg-x11-drv-nvidia-cuda
Conflicts:      xorg-x11-drv-nvidia-470xx-cuda

%description cuda
This package provides the CUDA integration components for %{name}.

%if 0%{?fedora} || 0%{?rhel} < 10
%package -n xorg-x11-nvidia
Summary:        X.org X11 NVIDIA driver and extensions
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}
Requires:       xorg-x11-server-Xorg%{?_isa}
Supplements:    (nvidia-driver and xorg-x11-server-Xorg)

Conflicts:      xorg-x11-drv-nvidia
Conflicts:      xorg-x11-drv-nvidia-470xx

%description -n xorg-x11-nvidia
The NVIDIA X.org X11 driver and associated components.
%endif

%endif
 
%prep
source %{SOURCE99}
export VERSION=%{version}

unpack() {
  set_vars
  run_file_get
  run_file_extract
  cleanup_folder
  create_tarball
}

%ifarch %{ix86}
export ARCH=x86_64
unpack
%setup -D -T -n %{name}-%{version}-i386
%endif

%ifarch x86_64
export ARCH=x86_64
unpack
%setup -D -T -n %{name}-%{version}-x86_64
%endif

%ifarch aarch64
export ARCH=aarch64
unpack
%setup -D -T -n %{name}-%{version}-aarch64
%endif

%ifarch x86_64
%if 0%{?rhel} == 8
rm -f libnvidia-pkcs11-openssl3.so.%{version}
%else
rm -f libnvidia-pkcs11.so.%{version}
%endif
%endif

# Create symlinks for shared objects
ldconfig -vn .

# Required for building gstreamer 1.0 NVENC plugins
ln -sf libnvidia-encode.so.%{version} libnvidia-encode.so

# Required for building ffmpeg 3.1 Nvidia CUVID
ln -sf libnvcuvid.so.%{version} libnvcuvid.so

# Required for building against CUDA
ln -sf libcuda.so.%{version} libcuda.so

%build

%install
# EGL loader
install -p -m 0644 -D 10_nvidia.json %{buildroot}%{_datadir}/glvnd/egl_vendor.d/10_nvidia.json

# Vulkan loader
install -p -m 0644 -D nvidia_icd.json %{buildroot}%{_datadir}/vulkan/icd.d/nvidia_icd.%{_target_cpu}.json
sed -i -e 's|libGLX_nvidia|%{_libdir}/libGLX_nvidia|g' %{buildroot}%{_datadir}/vulkan/icd.d/nvidia_icd.%{_target_cpu}.json

%ifarch x86_64
# Vulkan SC loader and compiler
install -p -m 0644 -D nvidia_icd_vksc.json %{buildroot}%{_datadir}/vulkansc/icd.d/nvidia_icd.%{_target_cpu}.json
sed -i -e 's|libnvidia-vksc-core|%{_libdir}/libnvidia-vksc-core|g' %{buildroot}%{_datadir}/vulkansc/icd.d/nvidia_icd.%{_target_cpu}.json
install -p -m 0755 -D nvidia-pcc %{buildroot}%{_bindir}/nvidia-pcc
%endif

# Unique libraries
mkdir -p %{buildroot}%{_libdir}/vdpau/
cp -a lib*GL*_nvidia.so* libcuda*.so* libnv*.so* %{buildroot}%{_libdir}/
cp -a libvdpau_nvidia.so* %{buildroot}%{_libdir}/vdpau/

%if 0%{?fedora} || 0%{?rhel} >= 9
# GBM loader
mkdir -p %{buildroot}%{_libdir}/gbm/
ln -sf ../libnvidia-allocator.so.%{version} %{buildroot}%{_libdir}/gbm/nvidia-drm_gbm.so
%endif

%ifarch x86_64

# NGX Proton/Wine library
mkdir -p %{buildroot}%{_libdir}/nvidia/wine/
cp -a *.dll %{buildroot}%{_libdir}/nvidia/wine/

%endif

%ifarch x86_64 aarch64

# alternate-install-present file triggers runfile warning
install -m 0755 -d %{buildroot}/usr/lib/nvidia/
install -p -m 0644 %{SOURCE13} %{buildroot}/usr/lib/nvidia/

# Empty?
mkdir -p %{buildroot}%{_sysconfdir}/nvidia/

# OpenCL config
install -p -m 0755 -D nvidia.icd %{buildroot}%{_sysconfdir}/OpenCL/vendors/nvidia.icd

# Binaries
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 nvidia-{debugdump,smi,cuda-mps-control,cuda-mps-server,bug-report.sh,ngx-updater,powerd} %{buildroot}%{_bindir}

# Man pages
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m 0644 nvidia-{smi,cuda-mps-control}*.gz %{buildroot}%{_mandir}/man1/

%if 0%{?fedora} || 0%{?rhel} < 10
# X stuff
install -p -m 0644 -D %{SOURCE10} %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/10-nvidia.conf
install -p -m 0755 -D nvidia_drv.so %{buildroot}%{_libdir}/xorg/modules/drivers/nvidia_drv.so
install -p -m 0755 -D libglxserver_nvidia.so.%{version} %{buildroot}%{_libdir}/xorg/modules/extensions/libglxserver_nvidia.so
%endif

# NVIDIA specific configuration files
mkdir -p %{buildroot}%{_datadir}/nvidia/
install -p -m 0644 nvidia-application-profiles-%{version}-key-documentation \
    %{buildroot}%{_datadir}/nvidia/
install -p -m 0644 nvidia-application-profiles-%{version}-rc \
    %{buildroot}%{_datadir}/nvidia/

# OptiX
install -p -m 0644 nvoptix.bin %{buildroot}%{_datadir}/nvidia/

# Systemd units and script for suspending/resuming
mkdir -p %{buildroot}%{_systemd_util_dir}/system-preset/
install -p -m 0644 %{SOURCE8} %{SOURCE9} %{buildroot}%{_systemd_util_dir}/system-preset/
mkdir -p %{buildroot}%{_unitdir}/
install -p -m 0644 systemd/system/*.service %{buildroot}%{_unitdir}/
install -p -m 0755 systemd/nvidia-sleep.sh %{buildroot}%{_bindir}/
install -p -m 0755 -D systemd/system-sleep/nvidia %{buildroot}%{_systemd_util_dir}/system-sleep/nvidia
install -p -m 0644 -D nvidia-dbus.conf %{buildroot}%{_datadir}/dbus-1/system.d/nvidia-dbus.conf

%if 0%{?fedora} >= 41
mkdir -p %{buildroot}%{_unitdir}/systemd-suspend.service.d/
cat > %{buildroot}%{_unitdir}/systemd-suspend.service.d/10-nvidia.conf << EOF
[Service]
Environment="SYSTEMD_SLEEP_FREEZE_USER_SESSIONS=false"
EOF
mkdir -p %{buildroot}%{_unitdir}/systemd-homed.service.d/
cat > %{buildroot}%{_unitdir}/systemd-homed.service.d/10-nvidia.conf << EOF
[Service]
Environment="SYSTEMD_HOME_LOCK_FREEZE_SESSION=false"
EOF
%endif

# Ignore powerd binary exiting if hardware is not present
# We should check for information in the DMI table
sed -i -e 's/ExecStart=/ExecStart=-/g' %{buildroot}%{_unitdir}/nvidia-powerd.service

# Vulkan layer
install -p -m 0644 -D nvidia_layers.json %{buildroot}%{_datadir}/vulkan/implicit_layer.d/nvidia_layers.json

# Install AppData and add modalias provides, do not use appstream-util add-provide as it mangles the xml
install -p -m 0644 -D %{SOURCE40} %{buildroot}%{_metainfodir}/com.nvidia.driver.metainfo.xml
%{SOURCE41} supported-gpus/supported-gpus.json %{buildroot}%{_metainfodir}/com.nvidia.driver.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{SOURCE42} %{buildroot}%{_datadir}/pixmaps/

%check
# Using appstreamcli: appstreamcli validate --strict
# Icon type local is not supported by appstreamcli for drivers
appstream-util validate --nonet %{buildroot}%{_metainfodir}/com.nvidia.driver.metainfo.xml

%endif

%ifarch x86_64 aarch64

%post
%systemd_post nvidia-hibernate.service
%systemd_post nvidia-powerd.service
%systemd_post nvidia-resume.service
%systemd_post nvidia-suspend.service
%systemd_post nvidia-suspend-then-hibernate.service

%preun
%systemd_preun nvidia-hibernate.service
%systemd_preun nvidia-powerd.service
%systemd_preun nvidia-resume.service
%systemd_preun nvidia-suspend.service
%systemd_post nvidia-suspend-then-hibernate.service

%postun
%systemd_postun nvidia-hibernate.service
%systemd_postun nvidia-powerd.service
%systemd_postun nvidia-resume.service
%systemd_postun nvidia-suspend.service
%systemd_post nvidia-suspend-then-hibernate.service

%endif

%ifarch x86_64 aarch64

%files
%license LICENSE
%doc NVIDIA_Changelog README.txt html supported-gpus/supported-gpus.json
%dir %{_sysconfdir}/nvidia
%{_bindir}/nvidia-bug-report.sh
%{_bindir}/nvidia-ngx-updater
%ifarch x86_64
%{_bindir}/nvidia-pcc
%endif
%{_bindir}/nvidia-powerd
%{_bindir}/nvidia-sleep.sh
%{_metainfodir}/com.nvidia.driver.metainfo.xml
%{_datadir}/dbus-1/system.d/nvidia-dbus.conf
%{_datadir}/nvidia/nvidia-application-profiles*
%{_datadir}/pixmaps/com.nvidia.driver.png
%{_systemd_util_dir}/system-preset/70-nvidia-driver.preset
%{_systemd_util_dir}/system-sleep/nvidia
%{_unitdir}/nvidia-hibernate.service
%{_unitdir}/nvidia-powerd.service
%{_unitdir}/nvidia-resume.service
%{_unitdir}/nvidia-suspend.service
%{_unitdir}/nvidia-suspend-then-hibernate.service
%if 0%{?fedora} >= 41
%{_unitdir}/systemd-suspend.service.d/10-nvidia.conf
%{_unitdir}/systemd-homed.service.d/10-nvidia.conf
%endif

%if 0%{?fedora} || 0%{?rhel} < 10
%files -n xorg-x11-nvidia
%config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/10-nvidia.conf
%{_libdir}/xorg/modules/extensions/libglxserver_nvidia.so
%{_libdir}/xorg/modules/drivers/nvidia_drv.so
%endif

%files -n libnvidia-cfg
%{_libdir}/libnvidia-cfg.so.1
%{_libdir}/libnvidia-cfg.so.%{version}

%files cuda
%{_sysconfdir}/OpenCL/vendors/*
%{_bindir}/nvidia-cuda-mps-control
%{_bindir}/nvidia-cuda-mps-server
%{_bindir}/nvidia-debugdump
%{_bindir}/nvidia-smi
%{_mandir}/man1/nvidia-cuda-mps-control.1.*
%{_mandir}/man1/nvidia-smi.*
%{_prefix}/lib/nvidia/alternate-install-present
%{_systemd_util_dir}/system-preset/70-nvidia-driver-cuda.preset

%endif

%files libs
%{_datadir}/glvnd/egl_vendor.d/10_nvidia.json
%{_datadir}/vulkan/icd.d/nvidia_icd.%{_target_cpu}.json
%if 0%{?fedora} || 0%{?rhel} >= 9
%dir %{_libdir}/gbm
%{_libdir}/gbm/nvidia-drm_gbm.so
%endif
%{_libdir}/libEGL_nvidia.so.0
%{_libdir}/libEGL_nvidia.so.%{version}
%{_libdir}/libGLESv1_CM_nvidia.so.1
%{_libdir}/libGLESv1_CM_nvidia.so.%{version}
%{_libdir}/libGLESv2_nvidia.so.2
%{_libdir}/libGLESv2_nvidia.so.%{version}
%{_libdir}/libGLX_nvidia.so.0
%{_libdir}/libGLX_nvidia.so.%{version}
%{_libdir}/libnvidia-allocator.so.1
%{_libdir}/libnvidia-allocator.so.%{version}
%{_libdir}/libnvidia-eglcore.so.%{version}
%{_libdir}/libnvidia-glcore.so.%{version}
%{_libdir}/libnvidia-glsi.so.%{version}
%{_libdir}/libnvidia-glvkspirv.so.%{version}
%{_libdir}/libnvidia-gpucomp.so.%{version}
%{_libdir}/libnvidia-tls.so.%{version}
%{_libdir}/vdpau/libvdpau_nvidia.so.1
%{_libdir}/vdpau/libvdpau_nvidia.so.%{version}
%ifarch x86_64 aarch64
%{_datadir}/nvidia/nvoptix.bin
%{_datadir}/vulkan/implicit_layer.d/nvidia_layers.json
%{_libdir}/libnvidia-api.so.1
%{_libdir}/libnvidia-ngx.so.1
%{_libdir}/libnvidia-ngx.so.%{version}
%{_libdir}/libnvidia-rtcore.so.%{version}
%{_libdir}/libnvoptix.so.1
%{_libdir}/libnvoptix.so.%{version}
%endif
%ifarch x86_64
%{_datadir}/vulkansc/icd.d/nvidia_icd.%{_target_cpu}.json
%{_libdir}/libnvidia-vksc-core.so.1
%{_libdir}/libnvidia-vksc-core.so.%{version}
%dir %{_libdir}/nvidia
%dir %{_libdir}/nvidia/wine
%{_libdir}/nvidia/wine/*.dll
%endif

%files cuda-libs
%{_libdir}/libcuda.so
%{_libdir}/libcuda.so.1
%{_libdir}/libcuda.so.%{version}
%{_libdir}/libnvcuvid.so
%{_libdir}/libnvcuvid.so.1
%{_libdir}/libnvcuvid.so.%{version}
%{_libdir}/libnvidia-encode.so
%{_libdir}/libnvidia-encode.so.1
%{_libdir}/libnvidia-encode.so.%{version}
%{_libdir}/libnvidia-nvvm.so.4
%{_libdir}/libnvidia-nvvm.so.%{version}
%{_libdir}/libnvidia-opencl.so.1
%{_libdir}/libnvidia-opencl.so.%{version}
%{_libdir}/libnvidia-opticalflow.so.1
%{_libdir}/libnvidia-opticalflow.so.%{version}
%{_libdir}/libnvidia-ptxjitcompiler.so.1
%{_libdir}/libnvidia-ptxjitcompiler.so.%{version}
%ifarch x86_64 aarch64
%{_libdir}/libcudadebugger.so.1
%{_libdir}/libcudadebugger.so.%{version}
%endif
%ifarch x86_64
%if 0%{?rhel} == 8
%{_libdir}/libnvidia-pkcs11.so.%{version}
%else
%{_libdir}/libnvidia-pkcs11-openssl3.so.%{version}
%endif
%{_libdir}/libnvidia-sandboxutils.so.1
%{_libdir}/libnvidia-sandboxutils.so.%{version}
%endif

%files -n libnvidia-fbc
%{_libdir}/libnvidia-fbc.so.1
%{_libdir}/libnvidia-fbc.so.%{version}

%files -n libnvidia-ml
%{_libdir}/libnvidia-ml.so.1
%{_libdir}/libnvidia-ml.so.%{version}

%changelog
%autochangelog
