%global commit c933525a6efe8229a7129b7b0b66798f19d2bef7
%global commit_date 20250627
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global build_cflags %{__build_flags_lang_c} %{?_distro_extra_cflags} -Wno-alloc-size-larger-than
%global build_cxxflags %{__build_flags_lang_cxx} %{?_distro_extra_cxxflags} -Wno-alloc-size-larger-than
%global __cmake_in_source_build 1
%global ver 1.0.0

Name:           ipu6-camera-hal
Summary:        Hardware abstraction layer for Intel IPU6
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%?dist
License:        Apache-2.0
URL:            https://github.com/intel/ipu6-camera-hal
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        60-intel-ipu6.rules
Source2:        v4l2-relayd-adl
Source3:        v4l2-relayd-tgl
Source4:        ipu6-driver-select.sh
### RPM Fusion | [ipu6-camera-hal] Fix build with gcc15
## https://lists.rpmfusion.org/archives/list/rpmfusion-commits@lists.rpmfusion.org/thread/TDMTM3WHMTHKCIN3XAUVWK3OBARW5SKO
Patch0:         0001-Drop-Werror.patch
BuildRequires:  systemd-rpm-macros
BuildRequires:  ipu6-camera-bins-devel >= 0.0-11
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  expat-devel
BuildRequires:  libdrm-devel
Requires:       ipu6-camera-bins >= 0.0-11
# Fix the stupid issue when changing versioning schemes
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Provides:       %{name} = %{commit_date}.%{shortcommit}-%{release}
%endif
ExclusiveArch:  x86_64
Packager:       Gilver E. <rockgrub@disroot.org>

%description
This package provides the basic Hardware Avstraction Layer (HAL) access APIs for IPU6.

%package devel
Summary:        IPU6 header files for HAL
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ipu6-camera-bins-devel

%description devel
This provides the necessary header files for IPU6 HAL development.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_INSTALL_SYSCONFDIR:PATH="%{_datadir}/defaults/etc" \
       -DBUILD_CAMHAL_ADAPTOR=ON \
       -DBUILD_CAMHAL_PLUGIN=ON \
       -DIPU_VERSIONS="ipu6;ipu6ep;ipu6epmtl" \
       -DUSE_PG_LITE_PIPE=ON
%cmake_build

%install
%cmake_install
# camera-hal will try to use the static libs instead of .so files if present
# Fedora does -devel-static packages, maybe I could do this as well in a different spec so it will not affect builds?
rm %{buildroot}%{_libdir}/libcamhal/plugins/*.a

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/60-intel-ipu6.rules

### v4l2-relayd configuration examples (mtl uses same config as adl)
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_datadir}/defaults/etc/camera/ipu6/v4l2-relayd
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_datadir}/defaults/etc/camera/ipu6ep/v4l2-relayd
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_datadir}/defaults/etc/camera/ipu6epmtl/v4l2-relayd

### Script to switch between proprietary and open IPU6 stacks
install -Dpm 0755 %{SOURCE4} %{buildroot}%{_bindir}/ipu6-driver-select

%posttrans
### Skip triggering if udevd isn't accessible
if [ -S /run/udev/control ]; then
    /usr/bin/udevadm control --reload
    /usr/bin/udevadm trigger /sys/devices/pci0000:00/0000:00:05.0
fi

%files
%doc README.md
%doc SECURITY.md
%license LICENSE
%{_bindir}/ipu6-driver-select
%{_libdir}/libcamhal.so.*
%{_libdir}/libcamhal
%{_datadir}/defaults
%{_udevrulesdir}/60-intel-ipu6.rules

%files devel
%{_includedir}/libcamhal
%{_libdir}/libcamhal.so
%{_libdir}/pkgconfig/libcamhal.pc


%changelog
%autochangelog
