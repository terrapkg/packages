%global debug_package %{nil}
%global commit 74a01d1208a352ed85d76f959c68200af4ead918
%global commitdate 20230811
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           ivsc-firmware
Summary:        Intel iVSC firmware
URL:            https://github.com/intel/ivsc-firmware
Version:        %{commitdate}.%{shortcommit}
Release:        1%?dist
License:        Proprietary
Source0:        https://github.com/intel/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Requires:       ipu6-camera-bins
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
