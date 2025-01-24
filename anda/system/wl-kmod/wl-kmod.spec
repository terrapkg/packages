%if 0%{?fedora} || 0%{?rhel} >= 9
%bcond_with kmod
%if %{with kmod}
%global buildforkernels current
%else
%global buildforkernels akmod
%endif
%endif
%global debug_package %{nil}

Name:       wl-kmod
Version:    6.30.223.271
Release:    1%{?dist}
Summary:    Kernel module for Broadcom wireless devices
Group:      System Environment/Kernel
License:    Redistributable, no modification permitted
URL:        https://www.broadcom.com/support/download-search?pg=Legacy+Products&pf=Legacy+Wireless&pn=&pa=&po=&dk=&pl=
Source0:    https://docs.broadcom.com/docs-and-downloads/docs/linux_sta/hybrid-v35-nodebug-pcoem-6_30_223_271.tar.gz
Source1:    https://docs.broadcom.com/docs-and-downloads/docs/linux_sta/hybrid-v35_64-nodebug-pcoem-6_30_223_271.tar.gz
Source11:   wl-kmod-kmodtool-excludekernel-filterfile
Patch0:     wl-kmod-002_kernel_3.18_null_pointer.patch
Patch1:     wl-kmod-003_gcc_4.9_remove_TIME_DATE_macros.patch
Patch2:     wl-kmod-004_kernel_4.3_rdtscl_to_rdtsc.patch
Patch3:     wl-kmod-005_kernel_4.7_IEEE80211_BAND_to_NL80211_BAND.patch
Patch4:     wl-kmod-006_gcc_6_fix_indentation_warnings.patch
Patch5:     wl-kmod-007_kernel_4.8_add_cfg80211_scan_info_struct.patch
Patch6:     wl-kmod-008_fix_kernel_warnings.patch
Patch7:     wl-kmod-009_kernel_4.11_remove_last_rx_in_net_device_struct.patch
Patch8:     wl-kmod-010_kernel_4.12_add_cfg80211_roam_info_struct.patch
Patch9:     wl-kmod-011_kernel_4.14_new_kernel_read_function_prototype.patch
Patch10:    wl-kmod-012_kernel_4.15_new_timer.patch
Patch11:    wl-kmod-013_gcc8_fix_bounds_check_warnings.patch
Patch12:    wl-kmod-014_kernel_read_pos_increment_fix.patch
Patch13:    wl-kmod-015_kernel_5.1_get_ds_removed.patch
Patch14:    wl-kmod-016_fix_unsupported_mesh_point.patch
Patch15:    wl-kmod-017_fix_gcc_fallthrough_warning.patch
Patch16:    wl-kmod-018_kernel_5.6_adaptations.patch
Patch17:    wl-kmod-019_kernel_5.9_segment_eq_removed.patch
Patch18:    wl-kmod-020_kernel_5.10_get_set_fs_removed.patch
Patch19:    wl-kmod-021_kernel_5.17_adaptation.patch
Patch20:    wl-kmod-022_kernel_5.18_adaptation.patch
Patch21:    wl-kmod-023_kernel_6.0_adaptation.patch
Patch22:    wl-kmod-024_kernel_6.1_adaptation.patch
Patch23:    wl-kmod-025_kernel_6.5_adaptation.patch
Patch24:    wl-kmod-026_kernel_6.10_fix_empty_body_in_if_warning.patch
Patch25:    wl-kmod-027_wpa_supplicant-2.11_add_max_scan_ie_len.patch
Patch26:    wl-kmod-028_kernel_6.12_adaptation.patch
ExclusiveArch:  i686 x86_64
BuildRequires:  kmodtool
BuildRequires:  elfutils-libelf-devel

%{!?kernels:BuildRequires: gcc, elfutils-libelf-devel}

%{expand:%(kmodtool --target %{_target_cpu} --repo terra --kmodname %{name} --filterfile %{SOURCE11} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
These packages contain Broadcom's IEEE 802.11a/b/g/n hybrid Linux device driver for use with Broadcom's BCM4311-, BCM4312-, BCM4313-, BCM4321-, BCM4322-, BCM43142-, BCM43224-, BCM43225-, BCM43227-, BCM43228-, BCM4331-, BCM4360, and -BCM4352-.

NOTE: Please read the LICENSE.txt file in the docs directory before using this driver. You should read the fedora.readme file in the docs directory in order to know how to configure this software if you encounter problems.

%prep
%{?kmodtool_check}
kmodtool --target %{_target_cpu}  --repo terra --kmodname %{name} --filterfile %{SOURCE11} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c -T
mkdir %{name}-%{version}-src
pushd %{name}-%{version}-src
%ifarch %{ix86}
 tar xzf %{SOURCE0}
%else
 tar xzf %{SOURCE1}
%endif
%patch -P 0  -p1 -b .kernel_3.18_null_pointer.patch
%patch -P 1  -p1 -b .gcc_4.9_remove_TIME_DATE_macros
%patch -P 2  -p1 -b .kernel_4.3_rdtscl_to_rdtsc.patch
%patch -P 3  -p1 -b .kernel_4.7_IEEE80211_BAND_to_NL80211_BAND
%patch -P 4  -p1 -b .gcc_6_fix_indentation_warnings
%patch -P 5  -p1 -b .kernel_4.8_add_cfg80211_scan_info_struct
%patch -P 6  -p1 -b .fix_kernel_warnings
%patch -P 7  -p1 -b .kernel_4.11_remove_last_rx_in_net_device_struct
%patch -P 8  -p1 -b .kernel_4.12_add_cfg80211_roam_info_struct
%patch -P 9  -p1 -b .kernel_4.14_new_kernel_read_function_prototype
%patch -P 10 -p1 -b .kernel_4.15_new_timer
%patch -P 11 -p1 -b .gcc8_fix_bounds_check_warnings
%patch -P 12 -p1 -b .kernel_read_pos_increment_fix
%patch -P 13 -p1 -b .kernel_5.1_get_ds_removed
%patch -P 14 -p1 -b .fix_unsupported_mesh_point
%patch -P 15 -p1 -b .fix_gcc_fallthrough_warning.patch
%patch -P 16 -p1 -b .kernel_5.6_adaptations.patch
%patch -P 17 -p1 -b .kernel_5.9_segment_eq_removed
%patch -P 18 -p1 -b .kernel_5.10_get_set_fs_removed
%patch -P 19 -p1 -b .kernel_5.17_adaptation
%patch -P 20 -p1 -b .kernel_5.18_adaptation
%patch -P 21 -p1 -b .kernel_6.0_adaptation
%patch -P 22 -p1 -b .kernel_6.1_adaptation
%patch -P 23 -p1 -b .kernel_6.5_adaptation
%patch -P 24 -p1 -b .kernel_6.10_adaptation
%patch -P 25 -p1 -b .wpa_supplicant-2.11_adaptation
%patch -P 26 -p1 -b .kernel_6.12_adaptation

### NOTE: These MUST be added to as new EL versions are released.
%if 0%{?rhel} == 9
 %define kvl %(echo %{kernel_versions} | cut -d"-" -f1)
 %define kvr %(echo %{kernel_versions} | cut -d"-" -f2 | cut -d"." -f1)

### Patching for various point release kernels.
 %if "%{kvl}" == "5.14.0"
  %if %{kvr} == 70
  %endif
  %if %{kvr} >= 70
   %{__sed} -i  's/ < KERNEL_VERSION(5, 17, 0)/ < KERNEL_VERSION(5, 14, 0)/g' src/wl/sys/wl_iw.h
   %{__sed} -i 's/ >= KERNEL_VERSION(5, 17, 0)/ >= KERNEL_VERSION(5, 14, 0)/g' src/wl/sys/wl_linux.c
  %endif
  %if %{kvr} >= 162
  %endif
  %if %{kvr} >= 284
  %endif
  %if %{kvr} >= 362
   %{__sed} -i 's/ >= KERNEL_VERSION(6, [01], 0)/ >= KERNEL_VERSION(5, 14, 0)/g' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} >= 427
  %endif
 %endif
%endif
popd

for kernel_version in %{?kernel_versions} ; do
 cp -a %{name}-%{version}-src _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
 pushd _kmod_build_${kernel_version%%___*}
 make -C ${kernel_version##*___} M=`pwd` modules
 popd
done

%install
rm -rf ${RPM_BUILD_ROOT}
for kernel_version in %{?kernel_versions}; do
 pushd _kmod_build_${kernel_version%%___*}
 mkdir -p ${RPM_BUILD_ROOT}%{kmodinstdir_prefix}${kernel_version%%___*}%{kmodinstdir_postfix}
 install -m 0755 *.ko ${RPM_BUILD_ROOT}%{kmodinstdir_prefix}${kernel_version%%___*}%{kmodinstdir_postfix}
 popd
done

chmod 0755 $RPM_BUILD_ROOT%{kmodinstdir_prefix}*%{kmodinstdir_postfix}/* || :
%{?akmod_install}

%changelog
%autochangelog
