%global commit f7ecb30c65ee5f7870e921bc0a2354df8e1e8100
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250225
%global ver 1.0
%define buildforkernels akmod
%global debug_package %{nil}
%global modulename t150-driver

Name:           %{modulename}-kmod
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        3%{?dist}
Summary:        Thrustmaster T150 steering wheel kernel module
License:        GPL-2.0-only
URL:            https://github.com/scarburato/t150_driver
Source0:        %{url}/archive/%{commit}.tar.gz#/t150_driver-%{shortcommit}.tar.gz
BuildRequires:  kmodtool
Requires:       akmods
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       %{modulename}-akmod-modules = %{?epoch:%{epoch}:}%{version}
Conflicts:      dkms-%{modulename}

%{expand:%(kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux driver for Thrustmaster T150 Steering Wheel USB.

%prep
%{?kmodtool_check}
kmodtool  --target %{_target_cpu}  --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -p1 -n t150_driver-%{commit}

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -fr hid-t150/* _kmod_build_${kernel_version%%___*}/
done

%build
for kernel_version in %{?kernel_versions}; do
    pushd _kmod_build_${kernel_version%%___*}/
        %make_build -C "${kernel_version##*___}" M=$(pwd) modules
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
* Thu Apr 02 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
