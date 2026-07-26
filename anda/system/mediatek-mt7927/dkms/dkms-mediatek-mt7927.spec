%global modulename   mediatek-mt7927

Name:                dkms-%{modulename}
Version:             2.13.1
Release:             1%{?dist}
Summary:             DKMS WiFi 7 and Bluetooth 5.4 drivers for MediaTek MT7927 (Filogic 380)
License:             GPL-2.0-only
URL:                 https://github.com/jetm/mediatek-mt7927-dkms
BuildArch:           noarch

Source0:             https://github.com/jetm/mediatek-mt7927-dkms/archive/refs/tags/v%{version}-1.tar.gz
Source1:             LICENSE

BuildRequires:       make
BuildRequires:       curl
BuildRequires:       python3

Requires:            dkms
Requires(post):      dkms
Requires(preun):     dkms

Conflicts:           btusb-mt7925-dkms
Conflicts:           btusb-mt7927-dkms

Packager:            Cypress Reed <cypress@fyralabs.com>

%description
DKMS package for MediaTek MT7927 (Filogic 380) combo WiFi 7 + BT 5.4.

Builds out-of-tree btusb/btmtk (Bluetooth) and mt76 (WiFi) kernel modules
with device IDs and patches not yet in mainline Linux. Supports kernels 6.17+.

When MT7927 support is merged into mainline kernels and linux-firmware,
remove this package to use the in-tree drivers.

%prep
%autosetup -n %{modulename}-dkms-%{version}-1

%build
%__make download
%__make sources SRCDIR=%{_builddir}/%{modulename}-dkms-%{version}-1/_build

%install
%make_install \
    SRCDIR=%{_builddir}/%{modulename}-dkms-%{version}-1/_build \
    DESTDIR=%{buildroot} \
    VERSION=%{version}
cp %{SOURCE1} -t .

%post
dkms add -m %{modulename} -v %{version} -q --rpm_safe_upgrade || :
dkms build -m %{modulename} -v %{version} -q || :
dkms install -m %{modulename} -v %{version} -q --force || :

%preun
dkms remove -m %{modulename} -v %{version} -q --all --rpm_safe_upgrade || :

%files
%license LICENSE
%{_usrsrc}/%{modulename}-%{version}
%dir /usr/lib/firmware/mediatek
%dir /usr/lib/firmware/mediatek/mt7927
/usr/lib/firmware/mediatek/mt7927/BT_RAM_CODE_MT6639_2_1_hdr.bin
/usr/lib/firmware/mediatek/mt7927/WIFI_MT6639_PATCH_MCU_2_1_hdr.bin
/usr/lib/firmware/mediatek/mt7927/WIFI_RAM_CODE_MT6639_2_1.bin

%changelog
* Thu May 21 2026 Willow C Reed <willow@willowidk.dev>
- Port to Terra from https://github.com/jetm/mediatek-mt7927-dkms

* Sun Mar 29 2026 Eder Sánchez <eder.sanchez@pm.me> - 2.9-1
- See CHANGELOG.md for detailed release notes
