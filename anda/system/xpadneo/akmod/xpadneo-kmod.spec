%global commit fc1b13afc8dbaf85fc8ea8dadac460cee1ebda06
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20251229
%global ver 0.9.7
%define buildforkernels akmod
%global debug_package %{nil}
%global modulename xpadneo

Name:           %{modulename}-kmod
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        2%{?dist}
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad
License:        GPL-3.0
URL:            https://atar-axis.github.io/xpadneo
Source0:        https://github.com/atar-axis/xpadneo/archive/%{commit}.tar.gz#/xpadneo-%{shortcommit}.tar.gz
BuildRequires:  kmodtool
BuildRequires:  systemd-rpm-macros
Requires:       akmods
Requires:       bluez
Requires:       bluez-tools
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       %{modulename}-akmod-modules = %{?epoch:%{epoch}:}%{version}
Conflicts:      dkms-%{modulename}
Packager:       Gilver E. <roachy@fyralabs.com>

%{expand:%(kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Advanced Linux Driver for Xbox One Wireless Gamepad.

%prep
%{?kmodtool_check}
kmodtool  --target %{_target_cpu}  --repo terra.fyralabs.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -p1 -n %{modulename}-%{commit}

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -fr hid-xpadneo/src/* _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    pushd _kmod_build_${kernel_version%%___*}/
        %make_build -C "${kernel_version##*___}" M=$(pwd) VERSION="v%{version}" modules
    popd
done

%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -p -m 0755 _kmod_build_${kernel_version%%___*}/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

%changelog
* Thu Feb 27 2025 Gilver E. <rockgrub@disroot.org>
- Package refactoring for alternative DKMS package compatibility
