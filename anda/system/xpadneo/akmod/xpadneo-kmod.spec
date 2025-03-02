%global commit 8d20a23e38883f45c78f48c8574ac93945b4cb03
%global date 20241224
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 0.9.7
%define buildforkernels akmod
%global debug_package %{nil}
%global real_name xpadneo

Name:           %{real_name}-kmod
Version:        %{ver}^%{date}git.%{shortcommit}
Release:        1%?dist
Summary:        Advanced Linux Driver for Xbox One Wireless Gamepad
License:        GPL-3.0
URL:            https://atar-axis.github.io/xpadneo
Source0:        https://github.com/atar-axis/xpadneo/archive/%{commit}.tar.gz#/xpadneo-%{shortcommit}.tar.gz
BuildRequires:  kmodtool
BuildRequires:  systemd-rpm-macros
Requires:       bluez
Requires:       bluez-tools
Requires:       %{real_name}-kmod-common = %{?epoch:%{epoch}:}%{version}
Packager:       ShinyGil <rockgrub@disroot.org>

%{expand:%(kmodtool --target %{_target_cpu} --repo terra --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Advanced Linux Driver for Xbox One Wireless Gamepad.

%prep
%{?kmodtool_check}
kmodtool  --target %{_target_cpu}  --repo terra --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -p1 -n %{real_name}-%{commit}

/usr/bin/sed -nE '/^BUILT_MODULE_NAME/{s@^.+"(.+)"@\1@; s|-|_|g; p}' hid-%{real_name}/dkms.conf.in > %{real_name}.conf

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
* Thu Feb 27 2025 ShinyGil <rockgrub@disroot.org>
- Package refactoring for alternative DKMS package compatibility
