%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif

Name:     xpadneo
Version:  0.9.6
Release:  1%{?dist}
Summary:  Advanced Linux Driver for Xbox One Wireless Gamepad
Group:    System Environment/Kernel
License:  GPL-3.0
URL:      https://github.com/atar-axis/xpadneo
Source0:  %url/archive/v%version/%name-%version.tar.gz
Source1:  modules-load-d-xpadneo.conf
Source2:  io.github.xpadneo.metainfo.xml

%global   srcname hid-%name

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  kmodtool
BuildRequires:  systemd-rpm-macros

Requires:       bash
Requires:       bluez bluez-tools

Provides:       %{name}-kmod-common = %{version}-%{release}
Requires:       %{name}-kmod >= %{version}
Obsoletes:      %{name} < 0.9.1-2

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Advanced Linux Driver for Xbox One Wireless Controller

%package kmod
Summary:  Kernel module (kmod) for %{name}
Requires: kernel-devel

%description kmod
This is the first driver for the Xbox One Wireless Gamepad (which is shipped with the Xbox One S).

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q

for kernel_version  in %{?kernel_versions} ; do
  cp -a hid-xpadneo/src _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version  in %{?kernel_versions} ; do
  make V=1 %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} VERSION=v%{version} modules
done

%install
for kernel_version in %{?kernel_versions}; do
  mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
  install -D -m 755 _kmod_build_${kernel_version%%___*}/hid-xpadneo.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
  chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/*.ko
done
%{?akmod_install}

install -Dm644 hid-xpadneo/etc-modprobe.d/xpadneo.conf %{buildroot}%{_modprobedir}/60-xpadneo.conf
install -Dm644 %{SOURCE1} %{buildroot}%{_modulesloaddir}/xpadneo.conf
install -Dm644 hid-xpadneo/etc-udev-rules.d/60-xpadneo.rules %{buildroot}%{_udevrulesdir}/60-xpadneo.rules
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/metainfo/io.github.xpadneo.metainfo.xml

%files
%doc NEWS.md docs/README.md docs/CONFIGURATION.md
%license LICENSE
%{_modprobedir}/60-xpadneo.conf
%{_modulesloaddir}/xpadneo.conf
%{_udevrulesdir}/60-xpadneo.rules
%{_datadir}/metainfo/io.github.xpadneo.metainfo.xml

%changelog
* Wed Oct 12 2022 Jan DrÃ¶gehoff <sentrycraft123@gmail.com> - 0.9.5-1
- Update to 0.9.5

* Mon Jul 04 2022 Jan DrÃ¶gehoff <sentrycraft123@gmail.com> - 0.9.4-1
- Update to 0.9.4

* Sun May 29 2022 Jan DrÃ¶gehoff <sentrycraft123@gmail.com> - 0.9.2-1
- Update to 0.9.2

* Thu Jun 17 2021 Jan DrÃ¶gehoff <sentrycraft123@gmail.com> - 0.9.1-2
- Move from DKMS to Akmods

* Fri May 21 2021 Jan DrÃ¶gehoff <sentrycraft123@gmail.com> - 0.9.1-1
- Update to 0.9.1

* Mon Dec 28 21:58:05 CET 2020 Jan DrÃ¶gehoff <sentrycraft123@gmail.com> - 0.9-2
- remove configure script

* Mon Dec 28 21:01:47 CET 2020 Jan DrÃ¶gehoff <sentrycraft123@gmail.com> - 0.9-1
- Initial Spec
