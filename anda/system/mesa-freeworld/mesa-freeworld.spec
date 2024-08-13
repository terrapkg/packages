%global srcname mesa
%global _description These drivers contains video acceleration codecs for decoding/encoding H.264 and H.265 \
algorithms and decoding only VC1 algorithm.
%ifnarch s390x
%global with_hardware 1
%global with_radeonsi 1
%global with_vmware 1
%global with_vulkan_hw 0
#global with_vdpau 1
%global with_va 1
%if !0%{?rhel}
%global with_r300 1
%global with_r600 1
%global with_nine 0
%global with_nvk 0
%global with_omx 0
%global with_opencl 0
%endif
#%%global base_vulkan ,amd
%endif

#%%ifnarch %%{ix86}
%if !0%{?rhel}
%global with_teflon 0
%endif
#%%endif

%ifarch %{ix86} x86_64
%global with_crocus 0
%global with_i915   0
%global with_iris   0
%global with_xa     0
%if !0%{?rhel}
%global with_intel_clc 0
%endif
#%%global intel_platform_vulkan ,intel,intel_hasvk
%endif
#%%ifarch x86_64
%global with_intel_vk_rt 0
#%%endif

%ifarch aarch64 x86_64 %{ix86}
%if !0%{?rhel}
%global with_lima      0
%global with_vc4       0
%endif
%global with_etnaviv   0
%global with_freedreno 0
%global with_kmsro     0
%global with_panfrost  0
%global with_tegra     0
%global with_v3d       0
%global with_xa        0
#%%global extra_platform_vulkan ,broadcom,freedreno,panfrost,imagination-experimental
%endif

%if !0%{?rhel}
%global with_libunwind 1
%global with_lmsensors 1
%endif

%ifarch %{valgrind_arches}
%bcond_without valgrind
%else
%bcond_with valgrind
%endif

#%%global vulkan_drivers swrast%%{?base_vulkan}%%{?intel_platform_vulkan}%%{?extra_platform_vulkan}%%{?with_nvk:,nouveau}

Name:           %{srcname}-freeworld
Summary:        Mesa graphics libraries
%global ver 24.2.0-rc4
Version:        %{lua:ver = string.gsub(rpm.expand("%{ver}"), "-", "~"); print(ver)}
Release:        1%{?dist}
License:        MIT AND BSD-3-Clause AND SGI-B-2.0
URL:            http://www.mesa3d.org

Source0:        https://archive.mesa3d.org/%{srcname}-%{ver}.tar.xz
# src/gallium/auxiliary/postprocess/pp_mlaa* have an ... interestingly worded license.
# Source1 contains email correspondence clarifying the license terms.
# Fedora opts to ignore the optional part of clause 2 and treat that code as 2 clause BSD.
Source1:        Mesa-MLAA-License-Clarification-Email.txt
Source2:        org.mesa3d.vaapi.freeworld.metainfo.xml
Source3:        org.mesa3d.vdpau.freeworld.metainfo.xml

BuildRequires:  meson >= 1.3.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
%if 0%{?with_hardware}
BuildRequires:  kernel-headers
%endif
# We only check for the minimum version of pkgconfig(libdrm) needed so that the
# SRPMs for each arch still have the same build dependencies. See:
# https://bugzilla.redhat.com/show_bug.cgi?id=1859515
BuildRequires:  pkgconfig(libdrm) >= 2.4.97
%if 0%{?with_libunwind}
BuildRequires:  pkgconfig(libunwind)
%endif
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(zlib) >= 1.2.3
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.8
BuildRequires:  pkgconfig(wayland-client) >= 1.11
BuildRequires:  pkgconfig(wayland-server) >= 1.11
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xdamage) >= 1.1
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xcb-glx) >= 1.8.1
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-dri2) >= 1.8
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xshmfence) >= 1.1
BuildRequires:  pkgconfig(dri2proto) >= 2.8
BuildRequires:  pkgconfig(glproto) >= 1.4.14
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xrandr) >= 1.3
BuildRequires:  bison
BuildRequires:  flex
%if 0%{?with_lmsensors}
BuildRequires:  lm_sensors-devel
%endif
%if 0%{?with_vdpau}
BuildRequires:  pkgconfig(vdpau) >= 1.1
%endif
%if 0%{?with_va}
BuildRequires:  pkgconfig(libva) >= 0.38.0
%endif
%if 0%{?with_omx}
BuildRequires:  pkgconfig(libomxil-bellagio)
%endif
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libglvnd) >= 1.3.2
BuildRequires:  llvm-devel >= 7.0.0
%ifarch %{ix86} x86_64
BuildRequires:  clang-devel
BuildRequires:  bindgen
BuildRequires:  pkgconfig(libclc)
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(LLVMSPIRVLib)
%endif
%if 0%{?with_teflon}
BuildRequires:  flatbuffers-devel
BuildRequires:  flatbuffers-compiler
BuildRequires:  xtensor-devel
%endif
%if 0%{?with_opencl} || 0%{?with_nvk}
BuildRequires:  rust-packaging
%endif
%if 0%{?with_nvk}
BuildRequires:  cbindgen
BuildRequires:  (crate(paste) >= 1.0.14 with crate(paste) < 2)
BuildRequires:  (crate(proc-macro2) >= 1.0.56 with crate(proc-macro2) < 2)
BuildRequires:  (crate(quote) >= 1.0.25 with crate(quote) < 2)
BuildRequires:  (crate(syn/clone-impls) >= 2.0.15 with crate(syn/clone-impls) < 3)
BuildRequires:  (crate(unicode-ident) >= 1.0.6 with crate(unicode-ident) < 2)
%endif
%if %{with valgrind}
BuildRequires:  pkgconfig(valgrind)
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-mako
%if 0%{?with_intel_clc}
BuildRequires:  python3-ply
%endif
BuildRequires:  python3-pycparser
BuildRequires:  vulkan-headers
BuildRequires:  glslang
%if 0%{?with_vulkan_hw}
BuildRequires:  pkgconfig(vulkan)
%endif

%description
%{_description}

%if 0%{?with_va}
%package        -n %{srcname}-va-drivers-freeworld
Summary:        Mesa-based VA-API drivers
Requires:       %{srcname}-filesystem%{?_isa} = %{?epoch:%{epoch}:}%{version}
Conflicts:      %{srcname}-va-drivers%{?_isa}

%description    -n %{srcname}-va-drivers-freeworld
%{_description}
%endif

%if 0%{?with_vdpau}
%package        -n %{srcname}-vdpau-drivers-freeworld
Summary:        Mesa-based VDPAU drivers
Requires:       %{srcname}-filesystem%{?_isa} = %{?epoch:%{epoch}:}%{version}
Conflicts:      %{srcname}-vdpau-drivers%{?_isa}

%description 	-n %{srcname}-vdpau-drivers-freeworld
%{_description}
%endif
%prep
%autosetup -n %{srcname}-%{ver} -p1
cp %{SOURCE1} docs/

%build
# ensure standard Rust compiler flags are set
export RUSTFLAGS="%build_rustflags"

# We've gotten a report that enabling LTO for mesa breaks some games. See
# https://bugzilla.redhat.com/show_bug.cgi?id=1862771 for details.
# Disable LTO for now
%define _lto_cflags %{nil}

%meson \
  -Dplatforms=x11,wayland \
  -Ddri3=enabled \
  -Dosmesa=false \
%if 0%{?with_hardware}
  -Dgallium-drivers=swrast,virgl,nouveau%{?with_r300:,r300}%{?with_crocus:,crocus}%{?with_i915:,i915}%{?with_iris:,iris}%{?with_vmware:,svga}%{?with_radeonsi:,radeonsi}%{?with_r600:,r600}%{?with_freedreno:,freedreno}%{?with_etnaviv:,etnaviv}%{?with_tegra:,tegra}%{?with_vc4:,vc4}%{?with_v3d:,v3d}%{?with_kmsro:,kmsro}%{?with_lima:,lima}%{?with_panfrost:,panfrost}%{?with_vulkan_hw:,zink} \
%else
  -Dgallium-drivers=swrast,virgl \
%endif
  -Dgallium-vdpau=%{?with_vdpau:enabled}%{!?with_vdpau:disabled} \
  -Dgallium-omx=%{!?with_omx:bellagio}%{?with_omx:disabled} \
  -Dgallium-va=%{?with_va:enabled}%{!?with_va:disabled} \
  -Dgallium-xa=%{!?with_xa:enabled}%{?with_xa:disabled} \
  -Dgallium-nine=%{!?with_nine:true}%{?with_nine:false} \
  -Dteflon=%{!?with_teflon:true}%{?with_teflon:false} \
  -Dgallium-opencl=%{!?with_opencl:icd}%{?with_opencl:disabled} \
%if 0%{?with_opencl}
  -Dgallium-rusticl=true \
%endif
  -Dvideo-codecs=h264dec,h264enc,h265dec,h265enc,vc1dec,av1dec,av1enc,vp9dec \
  -Dvulkan-drivers=%{?vulkan_drivers} \
  -Dvulkan-layers=device-select \
  -Dshared-glapi=enabled \
  -Dgles1=disabled \
  -Dgles2=disabled \
  -Dopengl=true \
  -Dgbm=disabled \
  -Dglx=dri \
  -Degl=disabled \
  -Dglvnd=false \
%if 0%{?with_intel_clc}
  -Dintel-clc=enabled \
%endif
  -Dintel-rt=%{!?with_intel_vk_rt:enabled}%{?with_intel_vk_rt:disabled} \
  -Dmicrosoft-clc=disabled \
  -Dllvm=enabled \
  -Dshared-llvm=enabled \
  -Dvalgrind=%{?with_valgrind:enabled}%{!?with_valgrind:disabled} \
  -Dbuild-tests=false \
  -Dselinux=true \
%if !0%{?with_libunwind}
  -Dlibunwind=disabled \
%endif
%if !0%{?with_lmsensors}
  -Dlmsensors=disabled \
%endif
  -Dandroid-libbacktrace=disabled \
%ifarch %{ix86}
  -Dglx-read-only-text=true \
%endif
  %{nil}
%meson_build

%install
%meson_install

# install Appdata files
mkdir -p %{buildroot}%{_metainfodir}
install -pm 0644 %{SOURCE2} %{buildroot}%{_metainfodir}
install -pm 0644 %{SOURCE3} %{buildroot}%{_metainfodir}

# libvdpau opens the versioned name, don't bother including the unversioned
rm -vf %{buildroot}%{_libdir}/vdpau/*.so
# likewise glvnd
rm -vf %{buildroot}%{_libdir}/libGLX_mesa.so
rm -vf %{buildroot}%{_libdir}/libEGL_mesa.so
# XXX can we just not build this
rm -vf %{buildroot}%{_libdir}/libGLES*

# glvnd needs a default provider for indirect rendering where it cannot
# determine the vendor
ln -s %{_libdir}/libGLX_mesa.so.0 %{buildroot}%{_libdir}/libGLX_system.so.0

# this keeps breaking, check it early.  note that the exit from eu-ftr is odd.
pushd %{buildroot}%{_libdir}
for i in libOSMesa*.so libGL.so ; do
    eu-findtextrel $i && exit 1
done
popd

# strip unneeded files from va-api and vdpau
rm -rf %{buildroot}%{_datadir}/{drirc.d,glvnd,vulkan}
rm -rf %{buildroot}%{_libdir}/{d3d,EGL,gallium-pipe,libGLX,pkgconfig}
rm -rf %{buildroot}%{_includedir}/{d3dadapter,EGL,GL,KHR}
rm -fr %{buildroot}%{_sysconfdir}/OpenGL
rm -fr %{buildroot}%{_libdir}/libGL.so*
rm -fr %{buildroot}%{_libdir}/libglapi.so*
rm -fr %{buildroot}%{_libdir}/libOSMesa.so*
rm -fr %{buildroot}%{_libdir}/pkgconfig/osmesa.pc
rm -fr %{buildroot}%{_libdir}/libgbm.so*
rm -fr %{buildroot}%{_includedir}/gbm.h
rm -fr %{buildroot}%{_libdir}/libxatracker.so*
rm -fr %{buildroot}%{_includedir}/xa_*.h
rm -fr %{buildroot}%{_libdir}/libMesaOpenCL.so*
rm -fr %{buildroot}%{_libdir}/dri/*_dri.so
rm -fr %{buildroot}%{_libdir}/libvulkan*.so
rm -fr %{buildroot}%{_libdir}/libVkLayer_MESA_device_select.so

%if 0%{?with_vdpau}
%else
rm %buildroot%_datadir/metainfo/org.mesa3d.vdpau.freeworld.metainfo.xml
%endif

%if 0%{?with_va}
%files -n %{srcname}-va-drivers-freeworld
%{_libdir}/dri/nouveau_drv_video.so
%if 0%{?with_r600}
%{_libdir}/dri/r600_drv_video.so
%endif
%if 0%{?with_radeonsi}
%{_libdir}/dri/radeonsi_drv_video.so
%endif
%{_libdir}/dri/virtio_gpu_drv_video.so
%{_metainfodir}/org.mesa3d.vaapi.freeworld.metainfo.xml
%license docs/license.rst
%endif

%if 0%{?with_vdpau}
%files -n %{srcname}-vdpau-drivers-freeworld
%{_libdir}/vdpau/libvdpau_nouveau.so.1*
%if 0%{?with_r600}
%{_libdir}/vdpau/libvdpau_r600.so.1*
%endif
%if 0%{?with_radeonsi}
%{_libdir}/vdpau/libvdpau_radeonsi.so.1*
%endif
%{_libdir}/vdpau/libvdpau_virtio_gpu.so.1*
%{_metainfodir}/org.mesa3d.vdpau.freeworld.metainfo.xml
%license docs/license.rst
%endif

%changelog
* Thu Aug 1 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.1.5-1
- Update to 24.1.5
- Drop upstreamed patch

* Fri Jul 19 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.1.4-2
- add revert-6746d4df-to-fix-av1-slice_data_offset.patch

* Thu Jul 18 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.1.4-1
- Update to 24.1.4
- Drop upstreamed patch

* Mon Jul 01 2024 Leigh Scott <leigh123linux@gmail.com> - 24.1.2-2
- Fix mutter crash when calling eglQueryDmaBufModifiersEXT
- Fix GNOME and KDE crash with some AMD GPUs

* Thu Jun 20 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.1.2-1
- Update to 24.1.2

* Thu Jun 06 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.1.1-1
- Update to 24.1.1

* Thu May 23 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.1.0-1
- Update to 24.1.0

* Fri May 17 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.1.0~rc4-2
- disable teflon on ix86, too

* Thu May 16 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.1.0~rc4-1
- Update to 24.1.0-rc4
- Sync a few more bits with mesa.spec from fedora

* Thu May 9 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.1.0~rc3-1
- Update to 24.1.0-rc3
- Sync with_intel_vk_rt bits with mesa.spec from fedora
- Unconditionally BR clang-devel, bindgen, libclc, SPIRV-Tools, and
  LLVMSPIRVLib which are needed now

* Tue May 7 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.1.0~rc2-1
- Update to 24.1.0-rc2

* Thu Apr 25 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.0.6-1
- Update to 24.0.6

* Thu Apr 11 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.0.5-1
- Update to 24.0.5

* Mon Apr 1 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.0.4-1
- Update to 24.0.4

* Thu Mar 14 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.0.3-1
- Update to 24.0.3

* Wed Mar 6 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.0.2-3
- Disable nvk explicitly to avoid BR on rust-packaging

* Wed Mar 6 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.0.2-2
- Update to 24.0.2

* Thu Feb 22 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.0.0-2
- enable vp9, av1 codecs due to new meson build flag (#6873)

* Fri Feb 02 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.0.0-1
- Update to 24.0.0

* Fri Jan 19 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 24.0.0~rc2-1
- Update to 24.0.0-rc2

* Thu Jan 11 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 23.3.3-1
- Update to 23.3.3

* Wed Jan 3 2024 Thorsten Leemhuis <fedora@leemhuis.info> - 23.3.2-1
- Update to 23.3.2

* Mon Dec 18 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.3.1-1
- Update to 23.3.1

* Fri Dec 15 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.3.0-2
- sync a few bit with fedora's mesa.spec

* Fri Dec 1 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.3.0-1
- Update to 23.3.0

* Thu Nov 30 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.3.0~rc5-1
- Update to 23.3.0-rc5

* Thu Nov 2 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.3.0~rc2-1
- Update to 23.3.0-rc2

* Thu Oct 26 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.3.0~rc1-1
- Update to 23.3.0-rc1

* Tue Oct 10 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.2.1-2
- follow Fedora: backport MR #24045 to fix Iris crashes (RHBZ#2238711)
- temporarily hard require llvm16, as that's what's used by fedora

* Sat Sep 30 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.2.1-1
- Update to 23.2.1

* Wed Sep 6 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.2.0~rc3.1
- Update to 23.2.0-rc3
- sync a few spec file bits with Fedora's mesa package

* Fri Aug 11 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.2.0~rc1.1
- Update to 23.2.0-rc2

* Thu Aug 3 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.1.5-1
- Update to 23.1.5

* Sun Jul 23 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.1.4-1
- Update to 23.1.4

* Fri Jun 23 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.1.3-1
- Update to 23.1.3

* Mon Jun 12 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.1.2-1
- Update to 23.1.2
- sync a few spec file bits with Fedora's mesa package

* Fri May 26 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.1.1-1
- Update to 23.1.1

* Tue May 23 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.1.0-1
- Update to 23.1.0
- sync a few spec file bits with Fedora's mesa package

* Tue Apr 25 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.0.3-1
- Update to 23.0.3

* Thu Apr 20 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.0.2-1.1
- Re-introduce Conflicts (rfbz#6612, kwizart)
- Enforces version to avoid miss-match with fedora (rfbz#6613, kwizart)

* Thu Apr 13 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.0.2-1
- Update to 23.0.2

* Tue Apr 11 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.0.1-2
- Rebuild for LLVM 16

* Sat Mar 25 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.0.1-1
- Update to 23.0.1

* Thu Feb 23 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.0.0-1
- Update to 23.0.0

* Thu Feb 16 2023 Luya Tshimbalanga <luya@fedoraproject.org> - 23.0.0~rc4-2
- Remove trailed .1 in release tag

* Thu Feb 2 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.0.0~rc4-1
- Update to 23.0.0-rc4

* Mon Jan 30 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 23.0.0~rc3-1
- Update to 23.0.0-rc3

* Wed Jan 18 2023 Luya Tshimbalanga <luya@fedoraproject.org> - 22.3.3-2.1
- Drop conflicts with provides

* Tue Jan 17 2023 Luya Tshimbalanga <luya@fedoraproject.org> - 22.3.3-2
- Fix dependencies issues between Fedora and RPM Fusion

* Thu Jan 12 2023 Thorsten Leemhuis <fedora@leemhuis.info> - 22.3.3-1
- Update to 22.3.3

* Wed Jan 4 2023 Luya Tshimbalanga <luya@fedoraproject.org> - 22.3.2-3
- fix typo on conflict condition for vdpau sub-package

* Sun Jan 1 2023 Luya Tshimbalanga <luya@fedoraproject.org> - 22.3.2-2
- Add conflicts to resolve dependencies from Fedora repo on update

* Sat Dec 31 2022 Thorsten Leemhuis <fedora@leemhuis.info> - 22.3.2-1
- Update to 22.3.2

* Mon Dec 19 2022 Thorsten Leemhuis <fedora@leemhuis.info> - 22.3.1-1
- adjust placement of a few files entries to stay in sync with Fedora; while at it
  make it more obvious that the license files are specific to rpmfusion

* Mon Dec 19 2022 Thorsten Leemhuis <fedora@leemhuis.info> - 22.3.1-1
- Update to 22.3.1
- sync a few bits with Fedora's mesa.spec

* Sun Nov 13 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 22.3.0~rc2-2
- Updated to version 22.3.0-rc2.

* Sun Nov 13 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 22.2.3-1
- Updated to version 22.2.3.

* Sun Nov 6 2022 Luya Tshimbalanga <luya@fedoraproject.org> - 22.2.2-1
- Update to 22.2.2

* Thu Oct 13 2022 Luya Tshimbalanga <luya@fedoraproject.org> - 22.2.1-1
- Update to 22.2.1
- Add appdata files for each subpackage

* Wed Oct 5 2022 Luya Tshimbalanga <luya@fedoraproject.org> - 22.2.0-4
- Drop unneeded omx support
- Add missing license for each files

* Sun Oct 2 2022 Luya Tshimbalanga <luya@fedoraproject.org> - 22.2.0-3
- Rename vaapi to va
- Broaden description
- Add Enhancement line
- Clean up spec file

* Sat Oct 1 2022 Luya Tshimbalanga <luya@fedoraproject.org> - 22.2.0-2
- Drop unsupported autospec in rpmfusion infra
- Enable h264, h265 and vc1 codecs
- Re-enable vdpau and omx (OpenMax) support

* Sat Oct 1 2022 Luya Tshimbalanga <luya@fedoraproject.org> - 22.2.0-1
- Initial release
