%global commit fb2827366361d8470c5ae2076e5f5e74584484da
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20261001
%global ver 0.2.1

%define buildforkernels akmod
%global debug_package %{nil}
%global modulename ayaneo-leds

Name:           %{modulename}-kmod
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        LED RGB control for Ayaneo legacy devices
License:        GPL-2.0-or-later
URL:            https://github.com/TiPSilva/%{modulename}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
BuildRequires:  kmodtool
Requires:       akmods
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Packager:       Tiago Silva <tiago.paulo@live.com>

%{expand:%(kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux kernel module to control the RGB rings on legacy AYANEO
devices with the old EC interface.
AYANEO 2S confirmed.
With the same interface waiting confirmation:
AYANEO 2, GEEK, GEEK 1S, AIR, AIR Pro, AIR 1S,
AIR 1S Limited, AIR Plus (Mendocino), SuiPlay0X1.

%prep
%{?kmodtool_check}
kmodtool  --target %{_target_cpu}  --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -p1 -n %{modulename}-%{commit}

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -fr ayaneo-leds.c Makefile _kmod_build_${kernel_version%%___*}/
done

%build
for kernel_version in %{?kernel_versions}; do
    pushd _kmod_build_${kernel_version%%___*}/
        %make_build KDIR="${kernel_version##*___}"
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
* Wed Sep 30 2026 Tiago Silva <tiago.paulo@live.com> - 0.2.1^20260930git.11e5e4c-1
- Initial package
