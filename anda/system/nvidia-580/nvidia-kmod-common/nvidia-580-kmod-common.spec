%global _dracut_conf_d  %{_prefix}/lib/dracut/dracut.conf.d

# gsp_*.bin: ELF 64-bit LSB executable, UCB RISC-V
%global _binaries_in_noarch_packages_terminate_build 0
%global __brp_strip %{nil}

Name:           nvidia-580-kmod-common
Version:        580.126.20
Release:        1%?dist
Summary:        Common file for NVIDIA's proprietary driver kernel modules
Epoch:          3
License:        NVIDIA License
URL:            http://www.nvidia.com/object/unix.html

BuildArch:      noarch

Source0:        http://download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}.run
Source17:       nvidia-boot-update
Source18:       nvidia-modeset.conf
Source19:       nvidia.conf
Source20:       60-nvidia.rules
Source21:       99-nvidia.conf

# UDev rule location (_udevrulesdir) and systemd macros:
BuildRequires:  systemd-rpm-macros

Requires:       dracut
Requires:       nvidia-modprobe-580
Requires:       nvidia-driver-580 = %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-580-libs = %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-580-kmod = %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-580-kmod-common = %{?epoch:%{epoch}:}%{version}
Obsoletes:      cuda-nvidia-kmod-common < %{?epoch:%{epoch}:}%{version}

%description
This package provides the common files required by all NVIDIA kernel module
package variants.

%prep
sh %{SOURCE0} -x --target nvidia-kmod-%{version}-x86_64
%setup -T -D -n nvidia-kmod-%{version}-x86_64

%install
# Script for post/preun tasks
install -p -m 0755 -D %{SOURCE17} %{buildroot}%{_bindir}/nvidia-boot-update

# Nvidia modesetting support:
install -p -m 0644 -D %{SOURCE18} %{buildroot}%{_sysconfdir}/modprobe.d/nvidia-modeset.conf

# Load nvidia-uvm, enable complete power management:
install -p -m 0644 -D %{SOURCE19} %{buildroot}%{_modprobedir}/nvidia.conf

# Avoid Nvidia modules getting in the initrd:
install -p -m 0644 -D %{SOURCE21} %{buildroot}%{_dracut_conf_d}/99-nvidia.conf

# UDev rules
# https://github.com/NVIDIA/nvidia-modprobe/blob/master/modprobe-utils/nvidia-modprobe-utils.h#L33-L46
# https://github.com/negativo17/nvidia-kmod-common/issues/11
# https://github.com/negativo17/nvidia-driver/issues/27
install -p -m 644 -D %{SOURCE20} %{buildroot}%{_udevrulesdir}/60-nvidia.rules

# Firmware files:
mkdir -p %{buildroot}%{_prefix}/lib/firmware/nvidia/%{version}/
install -p -m 644 firmware/* %{buildroot}%{_prefix}/lib/firmware/nvidia/%{version}

# Fallback service. Fall back to Nouveau if NVIDIA drivers fail.
# This is actually from RPM Fusion.
%dnl install -Dm644 %{SOURCE22} -t %{buildroot}%{_unitdir}
%dnl install -Dm644 %{SOURCE23} -t %{buildroot}%{_udevrulesdir}

%post
%{_bindir}/nvidia-boot-update post || :

%pre
# Remove the kernel command line adjustments one last time when doing an upgrade
# from a version that was still setting up the command line parameters:
if [ "$1" -eq "2" ] && [ -x %{_bindir}/nvidia-boot-update ]; then
  %{_bindir}/nvidia-boot-update preun || :

fi ||:

%triggerin -- nvidia-kmod,nvidia-open-kmod
dracut --regenerate-all --force || :

%files
%{_dracut_conf_d}/99-nvidia.conf
%{_modprobedir}/nvidia.conf
%dir %{_prefix}/lib/firmware
%dir %{_prefix}/lib/firmware/nvidia
%{_prefix}/lib/firmware/nvidia/%{version}
%{_bindir}/nvidia-boot-update
%config(noreplace) %{_sysconfdir}/modprobe.d/nvidia-modeset.conf
%{_udevrulesdir}/60-nvidia.rules

%changelog
%autochangelog
