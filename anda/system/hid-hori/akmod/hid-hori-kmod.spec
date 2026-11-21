%define buildforkernels akmod
%global debug_package %{nil}
%global modulename hid-hori

Name:           %{modulename}-kmod
Version:        0.0.7staging
Release:        1%{?dist}
Summary:        HORI Truck Control System kernel module
License:        GPL-2.0-only
URL:            https://github.com/LinuxGamesTV/hori_control_systems
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  kmodtool
BuildRequires:  elfutils-libelf-devel
Requires:       akmods
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       %{modulename}-akmod-modules = %{?epoch:%{epoch}:}%{version}
Conflicts:      dkms-%{modulename}

%{expand:%(kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null)}

%description
Experimental Linux kernel module for the HORI Truck Control System wheel
and shifter, including force feedback and wheel settings via sysfs.
Requires Linux 6.12 or newer.

%prep
%{?kmodtool_check}
%autosetup -n hori_control_systems-%{version}

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -a Kbuild Makefile *.c *.h usbhid _kmod_build_${kernel_version%%___*}/
done

%build
for kernel_version in %{?kernel_versions}; do
    %make_build -C "${kernel_version##*___}" \
        M="$PWD/_kmod_build_${kernel_version%%___*}" modules
done

%install
for kernel_version in %{?kernel_versions}; do
    install -Dpm644 _kmod_build_${kernel_version%%___*}/%{modulename}.ko \
        %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/%{modulename}.ko
done
%{?akmod_install}

%changelog
* Fri Nov 20 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.0.7staging-1
- Initial package
