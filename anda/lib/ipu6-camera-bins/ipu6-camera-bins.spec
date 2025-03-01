%global debug_package %{nil}
%global commit 3c1cdd3e634bb4668a900d75efd4d6292b8c7d1d
%global commitdate 20240507
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           ipu6-camera-bins
Summary:        Binary libraries for Intel IPU6
Version:        %{commitdate}.%{shortcommit}
Release:        1%?dist
License:        Proprietary
URL:            https://github.com/intel/ipu6-camera-bins
Source0:        https://github.com/intel/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:  systemd-rpm-macros
BuildRequires:  chrpath
#Requires:       gstreamer1-plugin-icamerasrc
Requires:       v4l2-relayd
Requires:       intel-ipu6-kmod
Requires:       intel-vsc-firmware >= 20240513
Obsoletes:      ipu6-camera-bins-firmware < 0.0-11
### For Akmods package
Provides:       intel-ipu6-kmod-common = %{version}
ExclusiveArch:  x86_64

%description
Provides binaries for Intel IPU6, including libraries and firmware.


%package devel
Summary:        IPU6 development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This provides the header files for IPU6 development.

%prep
%setup -q -n %{name}-%{commit}
chrpath --delete lib/*.so.*
sed -i \
    -e "s|libdir=\${exec_prefix}/lib|libdir=\${prefix}/%{_lib}|g" \
    lib/pkgconfig/*.pc

%build

%install
mkdir -p %{buildroot}%{_includedir}/
mkdir -p %{buildroot}%{_libdir}/
cp -pr include/* %{buildroot}%{_includedir}/
cp -pr lib/lib* lib/pkgconfig %{buildroot}%{_libdir}/
chmod 755 %{buildroot}%{_libdir}/$target/*.so*


%files
%license LICENSE
%doc README.md SECURITY.md
%{_libdir}/*.so*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.a
%{_libdir}/*.so*


%changelog
%autochangelog
