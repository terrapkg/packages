%global commit d890a93105a0aa52028ac49282fa1b579e12566e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260826
%global ver 0.83

# Pinned to the hid-tminit submodule commit of the hid-tmff2 commit above
%global tminit_commit 8c4547288a6c182ed4ff131e36f710f11a76c4a9
%global tminit_shortcommit %(c=%{tminit_commit}; echo ${c:0:7})

%define buildforkernels akmod
%global debug_package %{nil}
%global modulename hid-tmff2

Name:           %{modulename}-kmod
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        3%{?dist}
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

# Pull in the hid-tminit submodule sources. It builds hid-tminit-new and
# usb-tminit-new, required to switch wheels that enumerate as a generic
# "Thrustmaster FFB Wheel" (e.g. T128 Xbox version) into PC mode.
rm -rf deps/hid-tminit
mkdir -p deps/hid-tminit
tar -xf %{SOURCE1} -C deps/hid-tminit --strip-components=1

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -fr Kbuild Makefile src _kmod_build_${kernel_version%%___*}/
    cp -fr deps _kmod_build_${kernel_version%%___*}/
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
    install -p -m 0755 _kmod_build_${kernel_version%%___*}/deps/hid-tminit/*.ko \
        %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done
%{?akmod_install}

%changelog
* Tue Oct 20 2026 Potajito <potajito@gmail.com> - 0.83^20260826git.d890a93-3
- Build and ship hid-tminit-new and usb-tminit-new from the hid-tminit
- dependency (required for wheels needing mode switching, e.g. T128X)
- https://github.com/ublue-os/bazzite/issues/3555

* Thu Apr 02 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
