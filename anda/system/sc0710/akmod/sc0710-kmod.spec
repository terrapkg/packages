%global commit 56c3cc0748cc66220487aaa63dc621aa1076994d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260418
%global ver 0
%define buildforkernels akmod
%global debug_package %{nil}
%global modulename sc0710

Name:           %{modulename}-kmod
Version:        %{ver}^%{commitdate}git.%{shortcommit}
Release:        1%{?dist}
Summary:        Elgato 4K60 Pro MK.2 / 4K Pro capture card driver
License:        GPL-2.0-only
URL:            https://github.com/Nakildias/sc0710
Source0:        https://github.com/Nakildias/sc0710/archive/%{commit}.tar.gz#/sc0710-%{shortcommit}.tar.gz
BuildRequires:  kmodtool
Requires:       akmods
Requires:       %{modulename} = %{?epoch:%{epoch}:}%{version}
Conflicts:      dkms-%{modulename}
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>

%{expand:%(kmodtool --target %{_target_cpu} --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Elgato 4K60 Pro MK.2 / 4K Pro capture card driver.

%prep
%{?kmodtool_check}
kmodtool  --target %{_target_cpu}  --repo terrapkg.com --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -p1 -n %{modulename}-%{commit}

for kernel_version in %{?kernel_versions}; do
    mkdir _kmod_build_${kernel_version%%___*}
    cp -fr lib Makefile _kmod_build_${kernel_version%%___*}
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
* Fri Apr 03 2026 Kyle Gospodnetich <me@kylegospodneti.ch>
- Initial package
