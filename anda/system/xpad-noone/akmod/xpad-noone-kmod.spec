%global commit 6970c40930bedd8b58d0764894e0d5f04813b7c5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20240109
%global ver 1.0
%global real_name xpad-noone
%global _description %{expand:
This is the original upstream xpad driver from the Linux kernel with support for XBox One controllers removed. If you are running the xone driver you may have to replace the xpad kernel module with this one to retain the functionality of XBox and XBox 360 controllers.}

Name:          %{real_name}-kmod
Version:       %{ver}^%{commit_date}git.%{shortcommit}
Release:       1%{?dist}
License:       GPL-2.0-or-later
Summary:       xpad driver with support for XBox One controllers removed
URL:           https://github.com/medusalix/xpad-noone
Source0:       %{url}/archive/%{commit}/%{real_name}-%{commit}.tar.gz#/%{real_name}-%{shortcommit}.tar.gz
# Extra support for controllers that register as XBox 360 controllers
Patch0:        0000.patch
BuildRequires: gcc
BuildRequires: kmodtool
BuildRequires: make
BuildRequires: systemd-rpm-macros
Requires:      %{real_name} = %{?epoch:%{epoch}:}%{version}
Requires:      %{real_name}-akmod-modules
Requires:      akmods
Packager:      Gilver E. <rockgrub@disroot.org>

%{expand:%(kmodtool --target %{_target_cpu} --repo terra --kmodname %{real_name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description %_description

%prep
%{?kmodtool_check}

kmodtool --target %{_target_cpu}  --repo terra --kmodname %{real_name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -n %{real_name}-%{commit} -p1

for kernel_version  in %{?kernel_versions} ; do
  cp -a %{real_name}-%{commit} _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version  in %{?kernel_versions} ; do
  make V=1 %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} VERSION=v%{version} modules
done

%install
for kernel_version in %{?kernel_versions}; do
 mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/%{real_name}.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/%{real_name}.ko
done
%{?akmod_install}

%changelog
* Fri Mar 07 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
