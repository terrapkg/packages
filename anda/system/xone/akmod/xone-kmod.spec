%global commit 6b9d59aed71f6de543c481c33df4705d4a590a31
%global date 20241223
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 0.3
%define buildforkernels akmod
%global debug_package %{nil}
%global real_name xone

Name:           %{real_name}-kmod
Version:        0.3^20241223git.6b9d59a
Release:        1%?dist
Summary:        Linux kernel driver for Xbox One and Xbox Series X|S accessories
License:        GPL-2.0-or-later
URL:            https://github.com/dlundqvist/xone
Source0:        %{url}/archive/%{commit}.tar.gz#/xone-%{shortcommit}.tar.gz
BuildRequires:  kmodtool
BuildRequires:  systemd-rpm-macros
Requires:       %{real_name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Packager:       Gilver E. <rockgrub@disroot.org>

%{expand:%(kmodtool --target %{_target_cpu} --repo terra --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux kernel driver for Xbox One and Xbox Series X|S accessories.

%prep
%{?kmodtool_check}
kmodtool  --target %{_target_cpu}  --repo terra --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -p1 -n %{real_name}-%{commit}

/usr/bin/sed -nE '/^BUILT_MODULE_NAME/{s@^.+"(.+)"@\1@; s|-|_|g; p}' dkms.conf > %{real_name}.conf

find . -type f -name '*.c' -exec sed -i "s/#VERSION#/%{version}/" {} \;

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -fr auth bus driver transport Kbuild _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    pushd _kmod_build_${kernel_version%%___*}/
        %make_build -C "${kernel_version##*___}" M=$(pwd) VERSION="v%{version}" modules
    popd
done

%install
install -Dm644 %{real_name}.conf -t %{buildroot}%{_modulesloaddir}

for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -p -m 0755 _kmod_build_${kernel_version%%___*}/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

%files
%{_modulesloaddir}/%{real_name}.conf

%changelog
* Thu Feb 27 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
