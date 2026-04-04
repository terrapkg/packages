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
Release:    5%{?dist}
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
Patch9:    wl-kmod-011_kernel_4.14_new_kernel_read_function_prototype.patch
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
Patch27:    wl-kmod-029_kernel_6.13_adaptation.patch
Patch28:    wl-kmod-030_kernel_6.14_adaptation.patch
Patch29:    wl-kmod-031_replace_EXTRA_CFLAGS_EXTRA_LDFLAGS_with_ccflags-y_ldflags-y.patch
Patch30:    wl-kmod-032_add_MODULE_DESCRIPTION_macro.patch
Patch31:    wl-kmod-033_disable_objtool_add_warning_unmaintained.patch
Patch32:    wl-kmod-034_kernel_6.15_adaptation_replace_del_timer_with_timer_delete.patch
Patch33:    wl-kmod-035_kernel_6.17_adaptation_fix_functions_prototypes.patch
ExclusiveArch:  i686 x86_64
BuildRequires:  kmodtool
BuildRequires:  elfutils-libelf-devel

%{!?kernels:BuildRequires: gcc, elfutils-libelf-devel}

%{expand:%(kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{name} --filterfile %{SOURCE11} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
These packages contain Broadcom's IEEE 802.11a/b/g/n hybrid Linux device driver for use with Broadcom's BCM4311-, BCM4312-, BCM4313-, BCM4321-, BCM4322-, BCM43142-, BCM43224-, BCM43225-, BCM43227-, BCM43228-, BCM4331-, BCM4360, and -BCM4352-.

NOTE: Please read the LICENSE.txt file in the docs directory before using this driver. You should read the fedora.readme file in the docs directory in order to know how to configure this software if you encounter problems.

%prep
%{?kmodtool_check}
kmodtool --target %{_target_cpu}  --repo terra.fyralabs.com --kmodname %{name} --filterfile %{SOURCE11} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

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
%patch -P 9 -p1 -b .kernel_4.14_new_kernel_read_function_prototype
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
%patch -P 27 -p1 -b .kernel_6.13_adaptation
%patch -P 28 -p1 -b .kernel_6.14_adaptation
%patch -P 29 -p1 -b .EXTRA_CFLAGS_EXTRA_LDFLAGS
%patch -P 30 -p1 -b .MODULE_DESCRIPTION
%patch -P 31 -p1 -b .disable_objtool
%patch -P 32 -p1 -b .kernel_6.15_adaptation
%patch -P 33 -p1 -b .kernel_6.17_adaptation

# Manual patching to build for RHEL - inspired by CentOS wl-kmod.spec
# Actually works for RHEL 6.x and 7.x
%if 0%{?rhel} == 6
 # Define kvl (linux) & kvr (release) for use in "patching" logical
 %define kvl %(echo %{kernel_versions} | cut -d"-" -f1)
 %define kvr %(echo %{kernel_versions} | cut -d"-" -f2 | cut -d"." -f1)

 # Perform "patching" edits to the src/wl/sys/wl_cfg80211_hybrid.c file.
 #  Note: Using this method, as opposed to making a patch, allows
 #        the src.rpm to be compiled under various point release kernels.
 #  Note: Use [ >][>=] where both >= & > are present
 %if "%{kvl}" == "2.6.32"
  %if %{kvr} >= 71
   #  Apply to EL 6.0 point release and later
   %{__sed} -i 's/ >= KERNEL_VERSION(3, 6, 0)/ >= KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} >= 131
   #  Apply to EL 6.1 point release and later (2.6.32-131.0.15)
   #   >  No changes currently needed for EL 6.1 point release
  %endif
  %if %{kvr} >= 220
   #  Apply to EL 6.2 point release and later
   #   >  No changes currently needed for EL 6.2 point release
  %endif
  %if %{kvr} >= 279
   #  Apply to EL 6.3 point release and later
   %{__sed} -i 's/ >= KERNEL_VERSION(2, 6, 36)/ >= KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i 's/ >= KERNEL_VERSION(2, 6, 37)/ >= KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i 's/ >= KERNEL_VERSION(2, 6, 38)/ >= KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i  's/ > KERNEL_VERSION(2, 6, 39)/ > KERNEL_VERSION(2, 6, 31)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i 's/ >= KERNEL_VERSION(2, 6, 39)/ >= KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i 's/ >= KERNEL_VERSION(3, 1, 0)/ >= KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} == 358
   #  Only apply to EL 6.4 point release
   if $(grep -q "/lib/modules/kabi/kabi_whitelist" /usr/lib/rpm/redhat/find-requires.ksyms 2>/dev/null) ; then
    %{__sed} -i 's@/lib/modules/kabi/kabi_whitelist@/lib/modules/kabi-current/kabi_whitelist@g' /usr/lib/rpm/redhat/find-requires.ksyms
   fi
  %endif
  %if %{kvr} >= 358
   #  Apply to EL 6.4 point release and later
   #   >  No changes currently needed for EL 6.4 point release
  %endif
  %if %{kvr} == 431
   #  Only apply to EL 6.5 point release
   if $(grep -q "/lib/modules/kabi/kabi_whitelist" /usr/lib/rpm/redhat/find-requires.ksyms 2>/dev/null) ; then
    %{__sed} -i 's@/lib/modules/kabi/kabi_whitelist@/lib/modules/kabi-current/kabi_whitelist@g' /usr/lib/rpm/redhat/find-requires.ksyms
   fi
  %endif
  %if %{kvr} >= 431
   #  Apply to EL 6.5 point release and later
   %{__sed} -i 's/ >= KERNEL_VERSION(3, 8, 0)/ >= KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i 's/ >= KERNEL_VERSION(3, 9, 0)/ >= KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} == 504
   #  Only apply to EL 6.6 point release
   if $(grep -q "/lib/modules/kabi/kabi_whitelist" /usr/lib/rpm/redhat/find-requires.ksyms 2>/dev/null) ; then
    %{__sed} -i 's@/lib/modules/kabi/kabi_whitelist@/lib/modules/kabi-current/kabi_whitelist@g' /usr/lib/rpm/redhat/find-requires.ksyms
   fi
  %endif
  %if %{kvr} >= 504
   #  Apply to EL 6.6 point release and later
   #   >  No changes currently needed for EL 6.6 point release
  %endif
  %if %{kvr} >= 573
   #  Apply to EL 6.7 point release and later
   %{__sed} -i 's/ >= KERNEL_VERSION(3, 11, 0)/ >= KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i  's/ < KERNEL_VERSION(3, 16, 0)/ < KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i  's/ < KERNEL_VERSION(3, 18, 0)/ < KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i 's/ >= KERNEL_VERSION(3, 15, 0)/ >= KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} >= 642
   #  Apply to EL 6.8 point release and later
   %{__sed} -i 's/ >= KERNEL_VERSION(4, 0, 0)/ >= KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i  's/ < KERNEL_VERSION(4,2,0)/ < KERNEL_VERSION(2, 6, 32)/' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} >= 696
   #  Apply to EL 6.9 point release and later
   #   >  No changes currently needed for EL 6.9 point release
  %endif
  %if %{kvr} >= 754
   #  Apply to EL 6.10 point release and later
   #   >  No changes currently needed for EL 6.10 point release
  %endif
 %endif
%endif
%if 0%{?rhel} == 7
 # Define kvl (linux) & kvr (release) for use in "patching" logical
 %define kvl %(echo %{kernel_versions} | cut -d"-" -f1)
 %define kvr %(echo %{kernel_versions} | cut -d"-" -f2 | cut -d"." -f1)

 # Perform "patching" edits to the src/wl/sys/wl_cfg80211_hybrid.c file.
 #  Note: Using this method, as opposed to making a patch, allows
 #        the src.rpm to be compiled under various point release kernels.
 #  Note: Use [ >][>=] where both >= & > are present
 %if "%{kvl}" == "3.10.0"
  %if %{kvr} == 123
   #  Only apply to EL 7.0 point release
   if $(grep -q "/lib/modules/kabi/kabi_whitelist" /usr/lib/rpm/redhat/find-requires.ksyms 2>/dev/null) ; then
    %{__sed} -i 's@/lib/modules/kabi/kabi_whitelist@/lib/modules/kabi-rhel70/kabi_whitelist@g' /usr/lib/rpm/redhat/find-requires.ksyms
   fi
  %endif
  %if %{kvr} >= 123
   #  Apply to EL 7.0 point release and later
   #   >  No changes currently needed for EL 7.0 point release
  %endif
  %if %{kvr} >= 229
   #  Apply to EL 7.1 point release and later
   %{__sed} -i 's/ >= KERNEL_VERSION(3, 11, 0)/ >= KERNEL_VERSION(3, 10, 0)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i 's/ >= KERNEL_VERSION(3, 15, 0)/ >= KERNEL_VERSION(3, 10, 0)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i  's/ < KERNEL_VERSION(3, 16, 0)/ < KERNEL_VERSION(3, 10, 0)/' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} >= 327
   #  Apply to EL 7.2 point release and later
   %{__sed} -i  's/ < KERNEL_VERSION(3, 18, 0)/ < KERNEL_VERSION(3, 9, 0)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i 's/ >= KERNEL_VERSION(4, 0, 0)/ >= KERNEL_VERSION(3, 10, 0)/' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} >= 514
   #  Apply to EL 7.3 point release and later
   %{__sed} -i  's/ < KERNEL_VERSION(4,2,0)/ < KERNEL_VERSION(3, 9, 0)/' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i 's/ >= KERNEL_VERSION(4, 7, 0)/ >= KERNEL_VERSION(3, 10, 0)/' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} >= 693
   #  Apply to EL 7.4 point release and later
   %{__sed} -i 's/ >= KERNEL_VERSION(4, 8, 0)/ >= KERNEL_VERSION(3, 10, 0)/' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} >= 862
   #  Apply to EL 7.5 point release and later
   %{__sed} -i 's/ <= KERNEL_VERSION(4, 10, 0)/ <= KERNEL_VERSION(3, 9, 0)/' src/wl/sys/wl_linux.c
   %{__sed} -i 's/ >= KERNEL_VERSION(4, 11, 0)/ >= KERNEL_VERSION(3, 10, 0)/g' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i  's/ < KERNEL_VERSION(4, 12, 0)/ < KERNEL_VERSION(3, 10, 0)/g' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i 's/ >= KERNEL_VERSION(4, 12, 0)/ >= KERNEL_VERSION(3, 10, 0)/g' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} >= 957
   #  Apply to EL 7.6 point release and later
   #   >  No changes currently needed for EL 7.6 point release
  %endif
  %if %{kvr} >= 1062
   #  Apply to EL 7.7 point release and later
   %{__sed} -i -e 's@__attribute__((__fallthrough__));.*@/* fall through */@g' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} >= 1127
   #  Apply to EL 7.8 point release and later
   #   >  No changes currently needed for EL 7.8 point release
  %endif
  %if %{kvr} >= 1160
   #  Apply to EL 7.9 point release and later
   #   >  No changes currently needed for EL 7.9 point release
  %endif
 %endif
%endif
%if 0%{?rhel} == 8
 # Define kvl (linux) & kvr (release) for use in "patching" logical
 %define kvl %(echo %{kernel_versions} | cut -d"-" -f1)
 %define kvr %(echo %{kernel_versions} | cut -d"-" -f2 | cut -d"." -f1)

 # Perform "patching" edits to the src/wl/sys/wl_cfg80211_hybrid.c file.
 #  Note: Using this method, as opposed to making a patch, allows
 #        the src.rpm to be compiled under various point release kernels.
 #  Note: Use [ >][>=] where both >= & > are present
 %if "%{kvl}" == "4.18.0"
  %if %{kvr} == 80
   #  Only apply to EL 8.0 point release
   #   >  No changes currently needed for EL 8.0 point release
  %endif
  %if %{kvr} >= 80
   #  Apply to EL 8.0 point release and later
   #   >  No changes currently needed for EL 8.0 point release
  %endif
  %if %{kvr} >= 147
   #  Apply to EL 8.1 point release and later
   #   >  No changes currently needed for EL 8.1 point release
  %endif
  %if %{kvr} >= 193
   #  Apply to EL 8.2 point release and later
   #   >  No changes currently needed for EL 8.2 point release
  %endif
  %if %{kvr} >= 240
   #  Apply to EL 8.3 point release and later
   #   >  No changes currently needed for EL 8.3 point release
  %endif
  %if %{kvr} >= 305
   #  Apply to EL 8.4 point release and later
   #   >  No changes currently needed for EL 8.4 point release
  %endif
  %if %{kvr} >= 348
   #  Apply to EL 8.5 point release and later
   #   >  No changes currently needed for EL 8.5 point release
  %endif
  %if %{kvr} >= 372
   #  Apply to EL 8.6 point release and later
   #   >  No changes currently needed for EL 8.6 point release
  %endif
  %if %{kvr} >= 425
   #  Apply to EL 8.7 point release and later
   #   >  No changes currently needed for EL 8.7 point release
  %endif
  %if %{kvr} >= 477
   #  Apply to EL 8.8 point release and later
   %{__sed} -i 's/ >= KERNEL_VERSION(6, 0, 0)/ >= KERNEL_VERSION(4, 18, 0)/g' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i 's/ >= KERNEL_VERSION(6, 1, 0)/ >= KERNEL_VERSION(4, 18, 0)/g' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} >= 513
   #  Apply to EL 8.9 point release and later
   #   >  No changes currently needed for EL 8.9 point release
  %endif
  %if %{kvr} >= 553
   #  Apply to EL 8.10 point release and later
   #   >  No changes currently needed for EL 8.10 point release
  %endif
 %endif
%endif
%if 0%{?rhel} == 9
 # Define kvl (linux) & kvr (release) for use in "patching" logical
 %define kvl %(echo %{kernel_versions} | cut -d"-" -f1)
 %define kvr %(echo %{kernel_versions} | cut -d"-" -f2 | cut -d"." -f1)

 # Perform "patching" edits to the src/wl/sys/wl_cfg80211_hybrid.c file.
 #  Note: Using this method, as opposed to making a patch, allows
 #        the src.rpm to be compiled under various point release kernels.
 #  Note: Use [ >][>=] where both >= & > are present
 %if "%{kvl}" == "5.14.0"
  %if %{kvr} == 70
   #  Only apply to EL 9.0 point release
   #   >  No changes currently needed for EL 9.0 point release
  %endif
  %if %{kvr} >= 70
   #  Apply to EL 9.0 point release and later
   %{__sed} -i  's/ < KERNEL_VERSION(5, 17, 0)/ < KERNEL_VERSION(5, 14, 0)/g' src/wl/sys/wl_iw.h
   %{__sed} -i 's/ >= KERNEL_VERSION(5, 17, 0)/ >= KERNEL_VERSION(5, 14, 0)/g' src/wl/sys/wl_linux.c
  %endif
  %if %{kvr} >= 162
   #  Apply to EL 9.1 point release and later
   #   >  No changes currently needed for EL 9.1 point release
  %endif
  %if %{kvr} >= 284
   #  Apply to EL 9.2 point release and later
   #   >  No changes currently needed for EL 9.2 point release
  %endif
  %if %{kvr} >= 362
   #  Apply to EL 9.3 point release and later
   %{__sed} -i 's/ >= KERNEL_VERSION(6, [01], 0)/ >= KERNEL_VERSION(5, 14, 0)/g' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
  %if %{kvr} >= 427
   #  Apply to EL 9.4 point release and later
   #   >  No changes currently needed for EL 9.4 point release
  %endif
  %if %{kvr} >= 503
   #  Apply to EL 9.5 point release and later
   #   >  No changes currently needed for EL 9.5 point release
  %endif
  %if %{kvr} >= 570
   #  Apply to EL 9.6 point release and later
   #   >  No changes currently needed for EL 9.6 point release
  %endif
  %if %{kvr} >= 611
   #  Apply to EL 9.7 point release and later
   %{__sed} -i  's/ < KERNEL_VERSION(6, 13, 0)/ < KERNEL_VERSION(5, 14, 0)/g' src/include/linuxver.h
   %{__sed} -i  's/ >= KERNEL_VERSION(6, 14, 0)/ >= KERNEL_VERSION(5, 14, 0)/g' src/wl/sys/wl_cfg80211_hybrid.c
   %{__sed} -i  's/ >= KERNEL_VERSION(6, 17, 0)/ >= KERNEL_VERSION(5, 14, 0)/g' src/wl/sys/wl_cfg80211_hybrid.c
  %endif
 %endif
%endif
%if 0%{?rhel} == 10
 # Define kvl (linux) & kvr (release) for use in "patching" logical
 %define kvl %(echo %{kernel_versions} | cut -d"-" -f1)
 %define kvr %(echo %{kernel_versions} | cut -d"-" -f2 | cut -d"." -f1)

 # Perform "patching" edits to the src/wl/sys/wl_cfg80211_hybrid.c file.
 #  Note: Using this method, as opposed to making a patch, allows
 #        the src.rpm to be compiled under various point release kernels.
 #  Note: Use [ >][>=] where both >= & > are present
 %if "%{kvl}" == "6.12.0"
  %if %{kvr} == 55
   #  Only apply to EL 10.0 point release
   #   >  No changes currently needed for EL 10.0 point release
  %endif
  %if %{kvr} >= 55
   #  Apply to EL 10.0 point release and later
   %{__sed} -i  's/ < KERNEL_VERSION(6, 13, 0)/ < KERNEL_VERSION(6, 12, 0)/g' src/include/linuxver.h
  %endif
  %if %{kvr} >= 124
   #  Apply to EL 10.1 point release and later
   %{__sed} -i  's/ >= KERNEL_VERSION(6, 14, 0)/ >= KERNEL_VERSION(6, 12, 0)/g' src/wl/sys/wl_cfg80211_hybrid.c
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
