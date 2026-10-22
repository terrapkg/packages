%global buildforkernels akmod
%global debug_package %{nil}
%global modulename ayaneo-platform

Name:           %{modulename}-kmod
Version:        0.3.5
Release:        1%{?dist}
Summary:        Platform driver for AYANEO x86 handhelds
License:        GPL-2.0-or-later
URL:            https://github.com/ShadowBlip/%{modulename}
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      x86_64
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  kmodtool
BuildRequires:  elfutils-libelf-devel

Requires:       akmods
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       kernel-devel
Conflicts:      dkms-%{modulename}

%{expand:%(kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{modulename} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null)}

%description
Platform driver for AYANEO x86 handhelds, exposing RGB LED control and
bypass charging through sysfs.

%prep
%{?kmodtool_check}
%setup -q -c -n %{modulename}-%{version}

for kernel_version in %{?kernel_versions}; do
    cp -a %{modulename}-%{version} _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    make %{?_smp_mflags} -C "${kernel_version##*___}" \
        M="$PWD/_kmod_build_${kernel_version%%___*}" modules
done

%install
for kernel_version in %{?kernel_versions}; do
    install -D -m 0644 _kmod_build_${kernel_version%%___*}/%{modulename}.ko \
        %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/%{modulename}.ko
done
%{?akmod_install}

%changelog
* Thu Oct 22 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.3.5-1
- Initial package
