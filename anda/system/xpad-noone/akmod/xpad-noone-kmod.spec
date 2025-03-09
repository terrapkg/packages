%global commit 6970c40930bedd8b58d0764894e0d5f04813b7c5
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20240109
%global ver 1.0
%global modulename xpad-noone
%global debug_package %{nil}
%global buildforkernels akmod
%global _description %{expand:
This is the original upstream xpad driver from the Linux kernel with support for XBox One controllers removed. If you are running the xone driver you may have to replace the xpad kernel module with this one to retain the functionality of XBox and XBox 360 controllers.}

Name:          %{modulename}-kmod
Version:       %{ver}^%{commitdate}git.%{shortcommit}
Release:       1%?dist
License:       GPL-2.0-or-later
Summary:       xpad driver with support for XBox One controllers removed
URL:           https://github.com/medusalix/xpad-noone
Source0:       %{url}/archive/%{commit}/%{modulename}-%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
# Extra support for controllers that register as XBox 360 controllers
Patch0:        0000.patch
BuildRequires: gcc
BuildRequires: kmodtool
BuildRequires: make
BuildRequires: systemd-rpm-macros
Requires:      %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:      %{modulename}-akmod-modules
Requires:      akmods
Conflicts:     dkms-%{modulename}
Packager:      Gilver E. <rockgrub@disroot.org>

%{expand:%(kmodtool --target %{_target_cpu} --repo terra --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description %_description

%prep
%{?kmodtool_check}

kmodtool --target %{_target_cpu} --repo terra --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -n %{modulename}-%{commit} -p1

for kernel_version  in %{?kernel_versions} ; do
  cp -a %{modulename}-%{commit} _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version  in %{?kernel_versions} ; do
  make V=1 %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} VERSION=v%{version} modules
done

%install
for kernel_version in %{?kernel_versions}; do
 mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/%{modulename}.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/%{modulename}.ko
done
%{?akmod_install}

%changelog
* Fri Mar 07 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
