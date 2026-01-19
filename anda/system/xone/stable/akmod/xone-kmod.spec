%define buildforkernels akmod
%global debug_package %{nil}
%global modulename xone

Name:           %{modulename}-kmod
Version:        0.5.2
Release:        1%?dist
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Epoch:          2
%endif
Summary:        Linux kernel driver for Xbox One and Xbox Series X|S accessories
License:        GPL-2.0-or-later
URL:            https://github.com/dlundqvist/xone
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  kmodtool
BuildRequires:  systemd-rpm-macros
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       %{modulename}-akmod-modules = %{?epoch:%{epoch}:}%{version}
Requires:       akmods
Conflicts:      dkms-%{modulename}
Conflicts:      %{modulename}-nightly-kmod
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Obsoletes:      %{name} < %{?epoch:%{epoch}:}0.3.4
%endif
Packager:       Gilver E. <rockgrub@disroot.org>

%{expand:%(kmodtool --target %{_target_cpu} --repo terra.fyralabs.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux kernel driver for Xbox One and Xbox Series X|S accessories.

%prep
%{?kmodtool_check}
kmodtool  --target %{_target_cpu}  --repo terra.fyralabs.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -p1 -n %{modulename}-%{version}

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
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
    install -p -m 0755 _kmod_build_${kernel_version%%___*}/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

%changelog
* Thu Feb 27 2025 Gilver E. <rockgrub@disroot.org>
- Initial package
