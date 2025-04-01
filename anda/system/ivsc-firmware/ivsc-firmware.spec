%global debug_package %{nil}
%global commit 3377801f46b86e03c464bfb03ca3c486e9b0db00
%global commit_date 20250326
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           ivsc-firmware
Summary:        Intel iVSC firmware
URL:            https://github.com/intel/ivsc-firmware
Version:        0^%{commit_date}git.%{shortcommit}
Release:        1%?dist
License:        Proprietary
Source0:        https://github.com/intel/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Requires:       ipu6-camera-bins
# Fix the stupid issue when changing versioning schemes
%if 0%{?fedora} <= 43 || 0%{?rhel} <= 10
Provides:       %{name} = %{commit_date}.%{shortcommit}
%endif
ExclusiveArch:  x86_64

%description
This provides the firmware for Intel iVSC for kernels below 6.10. Provided for potential LTS users.

%prep
%autosetup -n %{name}-%{commit}

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1
mkdir -p %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod
pushd firmware/
for i in *.bin; do
  cp -a "$i" %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1/`echo "$i" | sed 's|\.bin|_a1\.bin|'`;
  cp -a "$i" %{buildroot}%{_prefix}/lib/firmware/vsc/soc_a1_prod/`echo "$i" | sed 's|\.bin|_a1_prod\.bin|'`;
done
popd

%files
%license LICENSE
%{_prefix}/lib/firmware/vsc/

%changelog
%autochangelog
