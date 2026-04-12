%global commit d8f6e10395b2fa5f036a9f5e0f62a5b910b9edd9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260410
%global ver 0.10.2
%define buildforkernels akmod
%global debug_package %{nil}
%global modulename xpadneo

Name:           %{modulename}-nightly-kmod
Version:        %{ver}^%{commitdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad
License:        GPL-2.0-only AND GPL-3.0-or-later
URL:            https://atar-axis.github.io/xpadneo
Source0:        https://github.com/atar-axis/xpadneo/archive/%{commit}.tar.gz#/xpadneo-%{shortcommit}.tar.gz
BuildRequires:  kmodtool
BuildRequires:  systemd-rpm-macros
Requires:       akmods
Requires:       bluez
Requires:       bluez-tools
Requires:       %{modulename}-nightly-kmod-common = %{?epoch:%{epoch}:}%{version}
Requires:       %{modulename}-nightly-akmod-modules = %{?epoch:%{epoch}:}%{version}
Conflicts:      dkms-%{modulename}
Packager:       Gilver E. <roachy@fyralabs.com>

%{expand:%(kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Advanced Linux Driver for Xbox One Wireless Gamepad.

%prep
%{?kmodtool_check}
kmodtool  --target %{_target_cpu}  --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

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
* Sat Apr 11 2026 Gilver E. <roachy@fyralabs.com> - 0.10.2^45f3982git20260411
- Separated nightly builds into their own packages
* Thu Feb 27 2025 Gilver E. <rockgrub@disroot.org>
- Package refactoring for alternative DKMS package compatibility
