%global debug_package %{nil}
%global commit 3c1cdd3e634bb4668a900d75efd4d6292b8c7d1d
%global commit_date 20240507
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 1.0.1

Name:           ipu6-camera-bins
Summary:        Binary libraries for Intel IPU6
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        1%?dist
License:        Proprietary
URL:            https://github.com/intel/ipu6-camera-bins
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:  systemd-rpm-macros
BuildRequires:  chrpath
Requires:       gstreamer1-plugin-icamerasrc
Requires:       v4l2-relayd
Requires:       intel-ipu6-kmod
Requires:       intel-vsc-firmware >= 20240513
Obsoletes:      ipu6-camera-bins-firmware < 0.0-11
### For Akmods package
Provides:       intel-ipu6-kmod-common = %{version}
# Fix the stupid issue when changing versioning schemes
%if %{?fedora} <= 42 || %{?rhel} <= 10
Provides:       %{name} = %{commit_date}.%{shortcommit}
%endif
ExclusiveArch:  x86_64
Packager:       Gilver E. <rockgrub@disroot.org>

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
install -Dm755 lib/*.so* -t %{buildroot}%{_libdir}
install -Dm644 lib/*.a -t %{buildroot}%{_libdir}
install -Dm644 lib/pkgconfig/* -t %{buildroot}%{_libdir}/pkgconfig


%files
%license LICENSE
%doc README.md 
%doc SECURITY.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/ia_*
%{_libdir}/pkgconfig/*
%{_libdir}/*.a
%dnl %{_libdir}/*.so


%changelog
%autochangelog
