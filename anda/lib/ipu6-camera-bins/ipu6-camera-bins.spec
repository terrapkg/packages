%global debug_package %{nil}
%global commit 3c1cdd3e634bb4668a900d75efd4d6292b8c7d1d
%global commit_date 20240507
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global ver 1.0.1

Name:           ipu6-camera-bins
Summary:        Libraries for Intel IPU6
Version:        %{ver}^%{commit_date}git.%{shortcommit}
Release:        3%?dist
License:        Proprietary
URL:            https://github.com/intel/ipu6-camera-bins
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:  chrpath
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       gstreamer1-plugin-icamerasrc
Requires:       intel-ipu6-kmod
Requires:       intel-vsc-firmware >= 20240513
Requires:       v4l2-relayd
Obsoletes:      ipu6-camera-bins-firmware < 0.0-11
# < 6.10 is falling out of third party and official support on Fedora
%if 0%{?fedora}
# Versioning scheme quirk
%if 0%{?fedora} <= 43
Obsoletes:      ivsc-firmware < 20250326.3377801-3
%endif
Obsoletes:      ivsc-firmware < 0^20250326git.3377801-3
%endif
### For Akmods package
Provides:       intel-ipu6-kmod-common = %{version}
# Fix the stupid issue when changing versioning schemes
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Provides:       %{name} = %{commit_date}.%{shortcommit}
%endif
ExclusiveArch:  x86_64
Packager:       Gilver E. <rockgrub@disroot.org>

%description
Provides binary libraries for Intel IPU6.

%package devel
Summary:        IPU6 development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Provides:       %{name}-devel = %{commit_date}.%{shortcommit}
%endif

%description devel
This provides the header files for IPU6 development.

%prep
%autosetup -n %{name}-%{commit}
chrpath --delete lib/*.so.0
chmod +x lib/*.so.0
# The firmware is part of linux-firmware!
rm -r lib/firmware

%build

%install
mkdir -p %{buildroot}%{_includedir}/
cp -pr include/* %{buildroot}%{_includedir}/
install -Dm755 lib/*.so* -t %{buildroot}%{_libdir}
install -Dm644 lib/*.a -t %{buildroot}%{_libdir}
install -Dm644 lib/pkgconfig/* -t %{buildroot}%{_libdir}/pkgconfig
pushd %{buildroot}%{_libdir}
  for i in *.so.0; do
    ln -s $i `echo $i | sed -e "s|\.so\.0|\.so|"`
  done
  for i in pkgconfig/*.pc; do
    sed -i -e "s|libdir=\${exec_prefix}/lib|libdir=%{_libdir}|g" "$i"
  done
popd

%files
%license LICENSE
%doc README.md 
%doc SECURITY.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/ipu6*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
%autochangelog
