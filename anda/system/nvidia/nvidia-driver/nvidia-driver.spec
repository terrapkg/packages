%global debug_package %{nil}
%global __brp_strip %{nil}
%global __brp_ldconfig %{nil}
%define _build_id_links none

# systemd 248+
%if 0%{?rhel} == 8
%global _systemd_util_dir %{_prefix}/lib/systemd
%endif

Name:           nvidia-driver
Version:        610.43.03
Release:        1%{?dist}
Summary:        NVIDIA's proprietary display driver for NVIDIA graphic cards
Epoch:          3
License:        NVIDIA License
URL:            http://www.nvidia.com/object/unix.html
Source7:        nvidia-powerd.service
Source8:        70-nvidia-driver.preset
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
Conflicts:      xorg-x11-drv-nvidia
ExclusiveArch:  %{ix86} x86_64 aarch64
Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
This package provides the most recent NVIDIA display driver which allows for
hardware accelerated rendering with recent NVIDIA chipsets.

For the full product support list, please consult the release notes for driver
version %{version}.

%package libs
Summary:        Libraries for %{name}
Requires:       egl-gbm%{?_isa} >= 2:1.1.3
Requires:       egl-wayland2%{?_isa} >= 1.0.0
Requires:       egl-x11%{?_isa} >= 1.0.4
%if %{defined fedora}
%ifarch x86_64
Requires:       (%{name}-libs(x86-32) = %{evr} if steam)
%endif
%endif
Suggests:       egl-wayland%{?_isa} >= 1.1.20
Requires:       egl-x11%{?_isa} >= 1.0.3
Requires:       libvdpau%{?_isa} >= 1.5
Requires:       libglvnd%{?_isa} >= 1.0
Requires:       libglvnd-egl%{?_isa} >= 1.0
Requires:       libglvnd-gles%{?_isa} >= 1.0
Requires:       libglvnd-glx%{?_isa} >= 1.0
Requires:       libglvnd-opengl%{?_isa} >= 1.0
Requires:       vulkan-loader
#  dlopened:
Requires:       %{name}-common%{?_isa} = %{evr}
Conflicts:      nvidia-x11-drv-libs
Conflicts:      xorg-x11-drv-nvidia-libs

%description libs
This package provides the shared libraries for %{name}.

%package cuda-libs
Summary:        Libraries for %{name}-cuda
Requires:       %{name}-common%{?_isa} = %{evr}
# dlopened:
%if %{defined fedora}
%ifarch x86_64
Requires:       (%{name}-cuda-libs(x86-32) = %{evr} if steam)
%endif
%endif
Conflicts:      xorg-x11-drv-nvidia-cuda-libs

%description cuda-libs
This package provides the CUDA libraries for %{name}-cuda.

%package -n libnvidia-fbc
Summary:        NVIDIA OpenGL-based Framebuffer Capture libraries
Provides:       nvidia-driver-NvFBCOpenGL = %{evr}
Obsoletes:      nvidia-driver-NvFBCOpenGL < %{evr}
# dlopened (libnvidia-encode.so):
Requires:       %{name}-cuda-libs%{?_isa} = %{evr}
%if %{defined fedora}
%ifarch x86_64
Requires:       (libnvidia-fbc(x86-32) = %{evr} if steam)
%endif
%endif

%description -n libnvidia-fbc
This library provides a high performance, low latency interface to capture and
optionally encode the composited framebuffer of an X screen. NvFBC are private
APIs that are only available to NVIDIA approved partners for use in remote
graphics scenarios.

%package common
Summary:        Common files and tools for NVIDIA driver
Obsoletes:      libnvidia-cfg < %{evr}
Obsoletes:      libnvidia-gpucomp < %{evr}
Obsoletes:      libnvidia-ml < %{evr}
Provides:       cuda-nvml%{?_isa} = %{evr}
Provides:       libnvidia-cfg = %{evr}
Provides:       libnvidia-gpucomp = %{evr}
Provides:       libnvidia-ml = %{evr}

%description common
This package contains various libraries and tools which are used by other driver
components in both desktop and compute only scenarios.

%ifarch x86_64 aarch64

%package cuda
Summary:        CUDA integration for %{name}
Requires:       %{name}-cuda-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-persistenced = %{?epoch:%{epoch}:}%{version}
Requires:       (ocl-icd or OpenCL-ICD-Loader)
Requires:       opencl-filesystem
Conflicts:      xorg-x11-drv-nvidia-cuda

%description cuda
This package provides the CUDA integration components for %{name}.

%if 0%{?fedora} || 0%{?rhel} < 10
%package -n xorg-x11-nvidia
Summary:        X.org X11 NVIDIA driver and extensions
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}
Requires:       xorg-x11-server-Xorg%{?_isa}
Supplements:    (nvidia-driver and xorg-x11-server-Xorg)
Conflicts:      xorg-x11-drv-nvidia

%description -n xorg-x11-nvidia
The NVIDIA X.org X11 driver and associated components.
%endif

%endif

%prep
source %{SOURCE99}
export VERSION=%{version}
%ifarch %{ix86}
export ARCH=x86_64
%else
export ARCH=%{_arch}
%endif

unpack() {
  set_vars
  run_file_get
  run_file_extract
  cleanup_folder
  create_tarball
}

unpack
%setup -D -T -n %{name}-%{version}-%{_arch}

%ifarch x86_64
%if 0%{?rhel} == 8
rm -f libnvidia-pkcs11-openssl3.so.%{version}
%else
rm -f libnvidia-pkcs11.so.%{version}
%endif
%endif

# Avoid harmless Vulkan loader message:
# WARNING: [Loader Message] Code 0 : Path to given binary /usr/lib64/libGLX_nvidia.so.590.48.01
# was found to differ from OS loaded path /usr/lib64/libGLX_nvidia.so.0
# See also https://github.com/negativo17/nvidia-driver/issues/195
mv libGLX_nvidia.so.%{version} libGLX_nvidia.so.0
ln -sf libGLX_nvidia.so.0 libGLX_nvidia.so.%{version}

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
install -Dpm755 nvidia-{%{dnl bug-report.sh,}debugdump,smi,cuda-mps-control,cuda-mps-server,ngx-updater,powerd} -t %{buildroot}%{_bindir}

# Man pages
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m 0644 nvidia-{smi,cuda-mps-control}*.gz %{buildroot}%{_mandir}/man1/

%if 0%{?fedora} || 0%{?rhel} < 10
# X stuff
install -p -m 0644 -D nvidia-drm-outputclass.conf %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/10-nvidia.conf
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

# Systemd units and script for power management
install -Dpm644 %{SOURCE7} %{buildroot}%{_unitdir}/nvidia-powerd.service
cp -frv systemd/system/systemd-* %{buildroot}%{_unitdir}/
install -Dpm644 nvidia-dbus.conf %{buildroot}%{_datadir}/dbus-1/system.d/nvidia-dbus.conf
install -Dpm644 dlsnetparams.csv %{buildroot}%{_datadir}/nvidia/nvidia-powerd/dlsnetparams.csv
install -Dpm644 %{SOURCE8} %{buildroot}%{_systemd_util_dir}/system-preset/70-nvidia-driver.preset

# Vulkan layer
install -p -m 0644 -D nvidia_layers.json %{buildroot}%{_datadir}/vulkan/implicit_layer.d/nvidia_layers.json

# Install AppData and add modalias provides, do not use appstream-util add-provide as it mangles the xml
install -p -m 0644 -D %{SOURCE40} %{buildroot}%{_metainfodir}/com.nvidia.driver.metainfo.xml
%{SOURCE41} supported-gpus/supported-gpus.json %{buildroot}%{_metainfodir}/com.nvidia.driver.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{SOURCE42} %{buildroot}%{_datadir}/pixmaps/

# nvsandboxutils configuration
install -p -m 0644 -D sandboxutils-filelist.json %{buildroot}%{_datadir}/nvidia/files.d/sandboxutils-filelist.json

# dnf needs-restarting plugin
# dnf4 only for the moment: https://github.com/rpm-software-management/dnf5/issues/1815
%if 0%{?fedora} < 42 || 0%{?rhel}
mkdir -p %{buildroot}%{_sysconfdir}/dnf/plugins/needs-restarting.d
echo %{name} > %{buildroot}%{_sysconfdir}/dnf/plugins/needs-restarting.d/%{name}.conf
echo %{name}-cuda > %{buildroot}%{_sysconfdir}/dnf/plugins/needs-restarting.d/%{name}-cuda.conf
%endif

%check
# Using appstreamcli: appstreamcli validate --strict
# Icon type local is not supported by appstreamcli for drivers
appstream-util validate --nonet %{buildroot}%{_metainfodir}/com.nvidia.driver.metainfo.xml

%endif

%ifarch x86_64 aarch64

%post common
%systemd_post nvidia-powerd.service

%preun common
%systemd_preun nvidia-powerd.service

%postun common
%systemd_postun nvidia-powerd.service

%endif

%ifarch x86_64 aarch64

%files
%license LICENSE
%doc NVIDIA_Changelog README.txt html supported-gpus/supported-gpus.json
%dir %{_sysconfdir}/nvidia
%{_bindir}/nvidia-ngx-updater
%ifarch x86_64
%{_bindir}/nvidia-pcc
%endif
%{_metainfodir}/com.nvidia.driver.metainfo.xml
%{_datadir}/nvidia/nvidia-application-profiles*
%{_datadir}/pixmaps/com.nvidia.driver.png
%dir %{_unitdir}/systemd-suspend.service.d
%{_unitdir}/systemd-suspend.service.d/nvidia-suspend-nofreeze.conf
%dir %{_unitdir}/systemd-hibernate.service.d
%{_unitdir}/systemd-hibernate.service.d/nvidia-suspend-nofreeze.conf
%dir %{_unitdir}/systemd-suspend-then-hibernate.service.d
%{_unitdir}/systemd-suspend-then-hibernate.service.d/nvidia-suspend-nofreeze.conf
%dir %{_unitdir}/systemd-hybrid-sleep.service.d
%{_unitdir}/systemd-hybrid-sleep.service.d/nvidia-suspend-nofreeze.conf
%if 0%{?fedora} < 42 || 0%{?rhel}
%{_sysconfdir}/dnf/plugins/needs-restarting.d/%{name}.conf
%endif

%if 0%{?fedora} || 0%{?rhel} < 10
%files -n xorg-x11-nvidia
%config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/10-nvidia.conf
%{_libdir}/xorg/modules/extensions/libglxserver_nvidia.so
%{_libdir}/xorg/modules/drivers/nvidia_drv.so
%endif

%files cuda
%{_sysconfdir}/OpenCL/vendors/*
%{_bindir}/nvidia-cuda-mps-control
%{_bindir}/nvidia-cuda-mps-server
%{_bindir}/nvidia-debugdump
%{_bindir}/nvidia-smi
%{_datadir}/nvidia/files.d/sandboxutils-filelist.json
%{_mandir}/man1/nvidia-cuda-mps-control.1.*
%{_mandir}/man1/nvidia-smi.*
%{_prefix}/lib/nvidia/alternate-install-present
%if 0%{?fedora} < 42 || 0%{?rhel}
%{_sysconfdir}/dnf/plugins/needs-restarting.d/%{name}-cuda.conf
%endif

%endif

%files common
%ifarch x86_64 aarch64
%{_systemd_util_dir}/system-preset/70-nvidia-driver.preset
%{_unitdir}/nvidia-powerd.service
%dnl %{_bindir}/nvidia-bug-report.sh
%{_bindir}/nvidia-powerd
%{_datadir}/dbus-1/system.d/nvidia-dbus.conf
%{_datadir}/nvidia/nvidia-powerd
%{_libdir}/libnvidia-cfg.so.1
%{_libdir}/libnvidia-cfg.so.%{version}
%endif
%{_libdir}/libnvidia-gpucomp.so.%{version}
%{_libdir}/libnvidia-ml.so.1
%{_libdir}/libnvidia-ml.so.%{version}

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
%{_libdir}/libnvidia-tls.so.%{version}
%{_libdir}/vdpau/libvdpau_nvidia.so.1
%{_libdir}/vdpau/libvdpau_nvidia.so.%{version}
%ifarch x86_64 aarch64
%{_datadir}/nvidia/nvoptix.bin
%{_datadir}/vulkan/implicit_layer.d/nvidia_layers.json
%{_libdir}/libnvidia-api.so.1
%{_libdir}/libnvidia-ngx.so.1
%{_libdir}/libnvidia-ngx.so.%{version}
%{_libdir}/libnvidia-present.so.%{version}
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
%{_libdir}/nvidia/wine/_nvngx.dll
%{_libdir}/nvidia/wine/nvngx.dll
%{_libdir}/nvidia/wine/nvngx_dlssg.dll
%endif

%files cuda-libs
%{_libdir}/libcuda.so
%{_libdir}/libcuda.so.1
%{_libdir}/libcuda.so.%{version}
%ifarch aarch64
%{_libdir}/libnvcuextend.so.1
%{_libdir}/libnvcuextend.so.%{version}
%endif
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
%{_libdir}/libnvidia-tileiras.so.%{version}
%ifarch x86_64 aarch64
%{_libdir}/libcudadebugger.so.1
%{_libdir}/libcudadebugger.so.%{version}
%{_libdir}/libnvidia-nvvm70.so.4
%{_libdir}/libnvidia-sandboxutils.so.1
%{_libdir}/libnvidia-sandboxutils.so.%{version}
%endif
%ifarch x86_64
%if 0%{?rhel} == 8
%{_libdir}/libnvidia-pkcs11.so.%{version}
%else
%{_libdir}/libnvidia-pkcs11-openssl3.so.%{version}
%endif
%endif

%files -n libnvidia-fbc
%{_libdir}/libnvidia-fbc.so.1
%{_libdir}/libnvidia-fbc.so.%{version}

%changelog
* Mon Apr 13 2026 Gilver E. <roachy@fyralabs.com> - 3:595.58.03-2
- Update spec for Terra packaging team
