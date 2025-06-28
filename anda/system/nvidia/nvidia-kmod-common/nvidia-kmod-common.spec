%global _dracutopts_in  rd.driver.blacklist=nouveau modprobe.blacklist=nouveau
%global _dracutopts_rm  nomodeset gfxpayload=vga=normal nouveau.modeset=0 nvidia-drm.modeset=1 initcall_blacklist=simpledrm_platform_driver_init
%global _dracut_conf_d  %{_prefix}/lib/dracut/dracut.conf.d

# gsp_*.bin: ELF 64-bit LSB executable, UCB RISC-V
%global _binaries_in_noarch_packages_terminate_build 0
%global __brp_strip %{nil}

Name:           nvidia-kmod-common
Version:        575.64
Release:        2%?dist
Summary:        Common file for NVIDIA's proprietary driver kernel modules
Epoch:          3
License:        NVIDIA License
URL:            http://www.nvidia.com/object/unix.html

BuildArch:      noarch

Source0:        http://download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}.run
Source18:       MODULE_VARIANT.txt
Source19:       nvidia-modeset.conf
Source20:       nvidia.conf
Source21:       60-nvidia.rules
Source22:       nvidia-fallback.service
Source23:       10-nvidia-fallback.rules

# UDev rule location (_udevrulesdir) and systemd macros:
BuildRequires:  systemd-rpm-macros

Requires:       dracut
Requires:       nvidia-modprobe
Requires:       nvidia-driver = %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-libs = %{?epoch:%{epoch}:}%{version}
Requires:       (nvidia-open-kmod = %{?epoch:%{epoch}:}%{version} or nvidia-kmod = %{?epoch:%{epoch}:}%{version})
Provides:       nvidia-kmod-common = %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-open-kmod-common = %{?epoch:%{epoch}:}%{version}
Obsoletes:      cuda-nvidia-kmod-common < %{?epoch:%{epoch}:}%{version}

%description
This package provides the common files required by all NVIDIA kernel module
package variants.
 
%prep
sh %{SOURCE0} -x --target nvidia-kmod-%{version}-x86_64
%setup -T -D -n nvidia-kmod-%{version}-x86_64

%install
# Nvidia modesetting support:
install -p -m 0644 -D %{SOURCE19} %{buildroot}%{_sysconfdir}/modprobe.d/nvidia-modeset.conf

# Load nvidia-uvm, enable complete power management:
install -p -m 0644 -D %{SOURCE20} %{buildroot}%{_modprobedir}/nvidia.conf

# UDev rules
# https://github.com/NVIDIA/nvidia-modprobe/blob/master/modprobe-utils/nvidia-modprobe-utils.h#L33-L46
# https://github.com/negativo17/nvidia-kmod-common/issues/11
# https://github.com/negativo17/nvidia-driver/issues/27
install -p -m 644 -D %{SOURCE21} %{buildroot}%{_udevrulesdir}/60-nvidia.rules

# Firmware files:
mkdir -p %{buildroot}%{_prefix}/lib/firmware/nvidia/%{version}/
install -p -m 644 firmware/* %{buildroot}%{_prefix}/lib/firmware/nvidia/%{version}

# Old kernel.conf rewritten as a doc file.
cp %{SOURCE18} .

# Fallback service. Fall back to Nouveau if NVIDIA drivers fail.
# This is actually from RPM Fusion.
install -Dm644 %{SOURCE22} -t %{buildroot}%{_unitdir}
install -Dm644 %{SOURCE23} -t %{buildroot}%{_udevrulesdir}

%pre
# Remove the kernel command line adjustments one last time when doing an upgrade
# from a version that was still setting up the command line parameters:
if [ "$1" -eq "2" ] && [ -x %{_bindir}/nvidia-boot-update ]; then
  %{_bindir}/nvidia-boot-update preun

fi ||:

%triggerin -- nvidia-kmod,nvidia-open-kmod
dracut --regenerate-all --force

%files
%doc MODULE_VARIANT.txt
%{_modprobedir}/nvidia.conf
%dir %{_prefix}/lib/firmware
%dir %{_prefix}/lib/firmware/nvidia
%{_prefix}/lib/firmware/nvidia/%{version}
%config(noreplace) %{_sysconfdir}/modprobe.d/nvidia-modeset.conf
%{_udevrulesdir}/10-nvidia-fallback.rules
%{_udevrulesdir}/60-nvidia.rules
%{_unitdir}/nvidia-fallback.service

%changelog
%autochangelog
