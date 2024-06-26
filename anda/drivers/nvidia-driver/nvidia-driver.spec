# from https://github.com/negativo17/nvidia-driver
%global debug_package %{nil}
%global __strip /bin/true
%global __brp_ldconfig %{nil}

# systemd 248+
%if 0%{?rhel} == 7 || 0%{?rhel} == 8
%global _systemd_util_dir %{_prefix}/lib/systemd
%endif

Name:           nvidia-driver
Version:        535.104.05
Release:        1%{?dist}
Summary:        NVIDIA's proprietary display driver for NVIDIA graphic cards
Epoch:          3
License:        NVIDIA License
URL:            http://www.nvidia.com/object/unix.html
ExclusiveArch:  %{ix86} x86_64 ppc64le aarch64

Source0:        %{name}-%{version}-i386.tar.xz
Source1:        %{name}-%{version}-x86_64.tar.xz
Source9:        70-nvidia.preset
# For servers with OutputClass device options (el7+)
Source10:       10-nvidia.conf.outputclass-device

Source40:       com.nvidia.driver.metainfo.xml
Source41:       parse-supported-gpus.py

Source99:       nvidia-generate-tarballs.sh

%ifarch x86_64

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  libappstream-glib
BuildRequires:  python3
BuildRequires:  systemd-rpm-macros
%else
BuildRequires:  systemd
%endif

%endif

Requires:       nvidia-driver-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       xorg-x11-server-Xorg%{?_isa}

Conflicts:      catalyst-x11-drv
Conflicts:      fglrx-x11-drv
Conflicts:      nvidia-x11-drv
Conflicts:      nvidia-x11-drv-340xx
Conflicts:      nvidia-x11-drv-390xx
Conflicts:      nvidia-x11-drv-470xx
Conflicts:      xorg-x11-drv-nvidia
Conflicts:      xorg-x11-drv-nvidia-340xx
Conflicts:      xorg-x11-drv-nvidia-390xx
Conflicts:      xorg-x11-drv-nvidia-470xx

%description
This package provides the most recent NVIDIA display driver which allows for
hardware accelerated rendering with recent NVIDIA chipsets.

For the full product support list, please consult the release notes for driver
version %{version}.

%package libs
Summary:        Libraries for %{name}
Requires:       libvdpau%{?_isa} >= 0.5
Requires:       libglvnd%{?_isa} >= 1.0
Requires:       libglvnd-egl%{?_isa} >= 1.0
Requires:       libglvnd-gles%{?_isa} >= 1.0
Requires:       libglvnd-glx%{?_isa} >= 1.0
Requires:       libglvnd-opengl%{?_isa} >= 1.0

%ifnarch %{ix86}
%if 0%{?fedora} || 0%{?rhel} >= 9
Requires:       egl-gbm%{?_isa} >= 1.1.0
%endif
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:       vulkan-loader
%else
Requires:       vulkan-filesystem
%endif

Conflicts:      nvidia-x11-drv-libs
Conflicts:      nvidia-x11-drv-libs-340xx
Conflicts:      nvidia-x11-drv-libs-390xx
Conflicts:      nvidia-x11-drv-libs-470xx
Conflicts:      xorg-x11-drv-nvidia-gl
Conflicts:      xorg-x11-drv-nvidia-libs
Conflicts:      xorg-x11-drv-nvidia-libs-340xx
Conflicts:      xorg-x11-drv-nvidia-libs-390xx
Conflicts:      xorg-x11-drv-nvidia-libs-470xx

%description libs
This package provides the shared libraries for %{name}.

%package cuda-libs
Summary:        Libraries for %{name}-cuda
Provides:       %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description cuda-libs
This package provides the CUDA libraries for %{name}-cuda.

%package NvFBCOpenGL
Summary:        NVIDIA OpenGL-based Framebuffer Capture libraries
# Loads libnvidia-encode.so at runtime
Requires:       %{name}-cuda-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description NvFBCOpenGL
This library provides a high performance, low latency interface to capture and
optionally encode the composited framebuffer of an X screen. NvFBC are private
APIs that are only available to NVIDIA approved partners for use in remote
graphics scenarios.

%package NVML
Summary:        NVIDIA Management Library (NVML)
Provides:       cuda-nvml%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description NVML
A C-based API for monitoring and managing various states of the NVIDIA GPU
devices. It provides a direct access to the queries and commands exposed via
nvidia-smi. The run-time version of NVML ships with the NVIDIA display driver,
and the SDK provides the appropriate header, stub libraries and sample
applications. Each new version of NVML is backwards compatible and is intended
to be a platform for building 3rd party applications.

%ifarch x86_64

%package cuda
Summary:        CUDA integration for %{name}
Conflicts:      xorg-x11-drv-nvidia-cuda
Requires:       nvidia-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       %{name}-cuda-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}
Requires:       %{name}-NVML%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       nvidia-persistenced = %{?epoch:%{epoch}:}%{version}
Requires:       opencl-filesystem
Requires:       ocl-icd

%description cuda
This package provides the CUDA integration components for %{name}.

%endif
 
%prep
%ifarch %{ix86}
%setup -q -n %{name}-%{version}-i386
%endif

%ifarch x86_64
%setup -q -T -b 1 -n %{name}-%{version}-x86_64
%endif

%if 0%{?rhel} == 7 || 0%{?rhel} == 8
rm -f libnvidia-pkcs11-openssl3.so.%{version}
%else
rm -f libnvidia-pkcs11.so.%{version}
%endif

# Create symlinks for shared objects
ldconfig -vn .

# Required for building gstreamer 1.0 NVENC plugins
ln -sf libnvidia-encode.so.%{version} libnvidia-encode.so
# Required for building ffmpeg 3.1 Nvidia CUVID
ln -sf libnvcuvid.so.%{version} libnvcuvid.so

# Required for building against CUDA
ln -sf libcuda.so.%{version} libcuda.so
# libglvnd indirect entry point
ln -sf libGLX_nvidia.so.%{version} libGLX_indirect.so.0

%ifarch x86_64
# Required by Vulkan on Wayland. Wrongly named library / missing SONAME so
# ldconfig does not create the appropriate symlinks.
# strings libnvidia-eglcore.so.515.43.04 libnvidia-glcore.so.515.43.04 | grep vulkan-producer
mv libnvidia-vulkan-producer.so.%{version} libnvidia-vulkan-producer.so
%endif

%build
# Nothing to build

%install
# Unique libraries
mkdir -p %{buildroot}%{_libdir}/vdpau/
cp -a lib*GL*_nvidia.so* libcuda*.so* libnv*.so* %{buildroot}%{_libdir}/
cp -a libvdpau_nvidia.so* %{buildroot}%{_libdir}/vdpau/

%ifarch x86_64

## Maybe exclusive?
# EGL loader
install -p -m 0644 -D 10_nvidia.json %{buildroot}%{_datadir}/glvnd/egl_vendor.d/10_nvidia.json

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

# X stuff
install -p -m 0644 -D %{SOURCE10} %{buildroot}%{_sysconfdir}/X11/xorg.conf.d/10-nvidia.conf
install -p -m 0755 -D nvidia_drv.so %{buildroot}%{_libdir}/xorg/modules/drivers/nvidia_drv.so
install -p -m 0755 -D libglxserver_nvidia.so.%{version} %{buildroot}%{_libdir}/xorg/modules/extensions/libglxserver_nvidia.so

# NVIDIA specific configuration files
mkdir -p %{buildroot}%{_datadir}/nvidia/
install -p -m 0644 nvidia-application-profiles-%{version}-key-documentation \
    %{buildroot}%{_datadir}/nvidia/
install -p -m 0644 nvidia-application-profiles-%{version}-rc \
    %{buildroot}%{_datadir}/nvidia/

# Vulkan loader
install -p -m 0644 -D nvidia_icd.json %{buildroot}%{_datadir}/vulkan/icd.d/nvidia_icd.json

# NGX Proton/Wine library
mkdir -p %{buildroot}%{_libdir}/nvidia/wine/
cp -a *.dll %{buildroot}%{_libdir}/nvidia/wine/

# OptiX
install -p -m 0644 nvoptix.bin %{buildroot}%{_datadir}/nvidia/

# Systemd units and script for suspending/resuming
install -p -m 0644 -D %{SOURCE9} %{buildroot}%{_systemd_util_dir}/system-preset/70-nvidia.preset
mkdir -p %{buildroot}%{_unitdir}/
install -p -m 0644 systemd/system/*.service %{buildroot}%{_unitdir}/
install -p -m 0755 systemd/nvidia-sleep.sh %{buildroot}%{_bindir}/
install -p -m 0755 -D systemd/system-sleep/nvidia %{buildroot}%{_systemd_util_dir}/system-sleep/nvidia
install -p -m 0644 -D nvidia-dbus.conf %{buildroot}%{_datadir}/dbus-1/system.d/nvidia-dbus.conf

%if 0%{?fedora} || 0%{?rhel} >= 9
# GBM loader
mkdir -p %{buildroot}%{_libdir}/gbm/
ln -sf ../libnvidia-allocator.so.%{version} %{buildroot}%{_libdir}/gbm/nvidia-drm_gbm.so
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
# Vulkan layer
install -p -m 0644 -D nvidia_layers.json %{buildroot}%{_datadir}/vulkan/implicit_layer.d/nvidia_layers.json

# install AppData and add modalias provides
install -p -m 0644 -D %{SOURCE40} %{buildroot}%{_metainfodir}/com.nvidia.driver.metainfo.xml
%{SOURCE41} supported-gpus/supported-gpus.json | xargs appstream-util add-provide %{buildroot}%{_metainfodir}/com.nvidia.driver.metainfo.xml modalias

%check
appstream-util validate --nonet %{buildroot}%{_metainfodir}/com.nvidia.driver.metainfo.xml
%endif

%endif

%ldconfig_scriptlets libs

%ldconfig_scriptlets cuda-libs

%ldconfig_scriptlets NvFBCOpenGL

%ldconfig_scriptlets NVML

%ifarch x86_64

%post
%systemd_post nvidia-hibernate.service
%systemd_post nvidia-powerd.service
%systemd_post nvidia-resume.service
%systemd_post nvidia-suspend.service

%preun
%systemd_preun nvidia-hibernate.service
%systemd_preun nvidia-powerd.service
%systemd_preun nvidia-resume.service
%systemd_preun nvidia-suspend.service

%postun
%systemd_postun nvidia-hibernate.service
%systemd_postun nvidia-powerd.service
%systemd_postun nvidia-resume.service
%systemd_postun nvidia-suspend.service

%files
%license LICENSE
%doc NVIDIA_Changelog README.txt html supported-gpus/supported-gpus.json
%dir %{_sysconfdir}/nvidia
%config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/10-nvidia.conf
%{_bindir}/nvidia-bug-report.sh
%{_bindir}/nvidia-powerd
%if 0%{?fedora} || 0%{?rhel} >= 8
%{_metainfodir}/com.nvidia.driver.metainfo.xml
%endif
%{_datadir}/dbus-1/system.d/nvidia-dbus.conf
%{_datadir}/nvidia
%{_libdir}/xorg/modules/extensions/libglxserver_nvidia.so
%{_libdir}/xorg/modules/drivers/nvidia_drv.so
%{_bindir}/nvidia-sleep.sh
%{_systemd_util_dir}/system-preset/70-nvidia.preset
%{_systemd_util_dir}/system-sleep/nvidia
%{_unitdir}/nvidia-hibernate.service
%{_unitdir}/nvidia-powerd.service
%{_unitdir}/nvidia-resume.service
%{_unitdir}/nvidia-suspend.service

%files cuda
%{_sysconfdir}/OpenCL/vendors/*
%{_bindir}/nvidia-cuda-mps-control
%{_bindir}/nvidia-cuda-mps-server
%{_bindir}/nvidia-debugdump
%{_bindir}/nvidia-ngx-updater
%{_bindir}/nvidia-smi
%{_mandir}/man1/nvidia-cuda-mps-control.1.*
%{_mandir}/man1/nvidia-smi.*

%endif

%files libs
%{_datadir}/glvnd/egl_vendor.d/10_nvidia.json
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

%ifarch x86_64

%{_datadir}/vulkan/icd.d/nvidia_icd.json
%if 0%{?fedora} || 0%{?rhel} >= 8
%{_datadir}/vulkan/implicit_layer.d/nvidia_layers.json
%endif
%if 0%{?fedora} || 0%{?rhel} >= 9
%{_libdir}/gbm/nvidia-drm_gbm.so
%endif
%{_libdir}/libnvidia-api.so.1
%{_libdir}/libnvidia-cfg.so.1
%{_libdir}/libnvidia-cfg.so.%{version}
%{_libdir}/libnvidia-ngx.so.1
%{_libdir}/libnvidia-ngx.so.%{version}
%{_libdir}/libnvidia-rtcore.so.%{version}
%{_libdir}/libnvidia-vulkan-producer.so
%{_libdir}/libnvoptix.so.1
%{_libdir}/libnvoptix.so.%{version}
# Wine libraries
%{_libdir}/nvidia/

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
%ifarch x86_64
%{_libdir}/libcudadebugger.so.1
%{_libdir}/libcudadebugger.so.%{version}
%if 0%{?rhel} ==7 || 0%{?rhel} == 8
%{_libdir}/libnvidia-pkcs11.so.%{version}
%else
%{_libdir}/libnvidia-pkcs11-openssl3.so.%{version}
%endif
%endif

%files NvFBCOpenGL
%{_libdir}/libnvidia-fbc.so.1
%{_libdir}/libnvidia-fbc.so.%{version}

%files NVML
%{_libdir}/libnvidia-ml.so.1
%{_libdir}/libnvidia-ml.so.%{version}

%changelog
* Thu Aug 24 2023 Simone Caronni <negativo17@gmail.com> - 3:535.104.05-1
- Update to 535.104.05.

* Wed Aug 09 2023 Simone Caronni <negativo17@gmail.com> - 3:535.98-1
- Update to 535.98.

* Wed Jul 19 2023 Simone Caronni <negativo17@gmail.com> - 3:535.86.05-1
- Update to 535.86.05.

* Thu Jun 15 2023 Simone Caronni <negativo17@gmail.com> - 3:535.54.03-1
- Update to 535.54.03.

* Tue Jun 13 2023 Simone Caronni <negativo17@gmail.com> - 3:535.43.02-1
- Update to 535.43.02.

* Fri Mar 24 2023 Simone Caronni <negativo17@gmail.com> - 3:530.41.03-1
- Update to 530.41.03.

* Wed Mar 08 2023 Simone Caronni <negativo17@gmail.com> - 3:530.30.02-1
- Update to 530.30.02.

* Fri Feb 10 2023 Simone Caronni <negativo17@gmail.com> - 3:525.89.02-1
- Update to 525.89.02.

* Fri Jan 20 2023 Simone Caronni <negativo17@gmail.com> - 3:525.85.05-1
- Update to 525.85.05.

* Mon Jan 09 2023 Simone Caronni <negativo17@gmail.com> - 3:525.78.01-1
- Update to 525.78.01.

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 3:525.60.11-2
- Drop nvidia-driver-devel subpackage.
- Trim changelog.

* Tue Nov 29 2022 Simone Caronni <negativo17@gmail.com> - 3:525.60.11-1
- Update to 525.60.11.

* Thu Oct 13 2022 Simone Caronni <negativo17@gmail.com> - 3:520.56.06-1
- Update to 520.56.06.

* Wed Sep 21 2022 Simone Caronni <negativo17@gmail.com> - 3:515.76-1
- Update to 515.76.

* Mon Aug 08 2022 Simone Caronni <negativo17@gmail.com> - 3:515.65.01-1
- Update to 515.65.01.

* Wed Jun 29 2022 Simone Caronni <negativo17@gmail.com> - 3:515.57-1
- Update to 515.57.

* Wed Jun 01 2022 Simone Caronni <negativo17@gmail.com> - 3:515.48.07-1
- Update to 515.48.07.

* Sun May 15 2022 Simone Caronni <negativo17@gmail.com> - 3:515.43.04-2
- Rename libnvidia-vulkan-producer.so versioned library (#128).

* Thu May 12 2022 Simone Caronni <negativo17@gmail.com> - 3:515.43.04-1
- Update to 515.43.04.

* Mon May 02 2022 Simone Caronni <negativo17@gmail.com> - 3:510.68.02-1
- Update to 510.68.02.

* Mon Mar 28 2022 Simone Caronni <negativo17@gmail.com> - 3:510.60.02-1
- Update to 510.60.02.

* Thu Mar 03 2022 Simone Caronni <negativo17@gmail.com> - 3:510.54-3
- nvidia-resume is no longer triggered by nvidia-sleep.sh.

* Fri Feb 25 2022 Simone Caronni <negativo17@gmail.com> - 3:510.54-2
- nvidia-smi dlopens NVML, add explicit dependency to cuda subpackage.

* Mon Feb 14 2022 Simone Caronni <negativo17@gmail.com> - 3:510.54-1
- Update to 510.54.

* Sat Feb 12 2022 Simone Caronni <negativo17@gmail.com> - 3:510.47.03-4
- Drop libva-vdpau-driver hard dependency.

* Mon Feb 07 2022 Simone Caronni <negativo17@gmail.com> - 3:510.47.03-3
- Fix GBM condition.

* Sat Feb 05 2022 Simone Caronni <negativo17@gmail.com> - 3:510.47.03-2
- Drop explicit dependency on egl-wayland, it's auto generated and not needed on
  i686 libs. Minimum version 1.1.7 required.

* Wed Feb 02 2022 Simone Caronni <negativo17@gmail.com> - 3:510.47.03-1
- Update to 510.47.03.
- Use external GBM library.
- Install GBM only on CentOS/RHEL 9+ and Fedora 35. It's also supported in
  CentOS Stream 8 (8.6+/Mesa 21.2), but there's no easy way to check for Stream
  in the SPEC file.
