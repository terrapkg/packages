%global commit 8187920ed261c7024826f8204cc7bea45153a3da
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260310
%global ver 0.83

%global tminit_commit 8c4547288a6c182ed4ff131e36f710f11a76c4a9
%global tminit_shortcommit %(c=%{tminit_commit}; echo ${c:0:7})

%define buildforkernels akmod
%global debug_package %{nil}
%global modulename hid-tmff2

Name:           %{modulename}-kmod
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Thrustmaster Force Feedback kernel module
License:        GPL-2.0-only
URL:            https://github.com/Kimplul/%{modulename}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{modulename}-%{shortcommit}.tar.gz
Source1:        https://github.com/Kimplul/hid-tminit/archive/%{tminit_commit}.tar.gz#/hid-tminit-%{tminit_shortcommit}.tar.gz
BuildRequires:  kmodtool
Requires:       akmods
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Requires:       %{modulename}-akmod-modules = %{?epoch:%{epoch}:}%{version}
Conflicts:      dkms-%{modulename}

%{expand:%(kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux kernel module for Thrustmaster T300RS, T248 and (experimental) TX, T128,
T598, T-GT II and TS-XW wheels.

%prep
%{?kmodtool_check}
kmodtool  --target %{_target_cpu}  --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -p1 -n %{modulename}-%{commit}

# Populate the hid-tminit submodule
mkdir -p deps/hid-tminit
tar xf %{SOURCE1} --strip-components=1 -C deps/hid-tminit

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -fr Kbuild Makefile src _kmod_build_${kernel_version%%___*}/
    cp -fr deps _kmod_build_${kernel_version%%___*}/
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
    install -p -m 0755 _kmod_build_${kernel_version%%___*}/deps/hid-tminit/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

%changelog
* Thu Apr 02 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
