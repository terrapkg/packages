Name:           msm-firmware-loader
Version:        1.8.0
Release:        1%{?dist}
Summary:        Loads DSP/modem/WiFi firmware from Qualcomm firmware partitions

License:        MIT
URL:            https://gitlab.postmarketos.org/postmarketOS/msm-firmware-loader
Source0:        %{url}/-/archive/%{version}/msm-firmware-loader-%{version}.tar.gz

Patch1:         0001-load-hexagonrpcd-firmware.patch

BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       qbootctl
Requires:       make-dynpart-mappings

Packager:       Owen Zimmerman <owen@fyralabs.com>

%{?systemd_requires}

%description
msm-firmware-loader mounts a Qualcomm device's dedicated firmware partitions
(modem, dsp, bluetooth, persist, vendor, ...) at early boot and symlinks the
blobs it finds into a single tree, which it then points the kernel's
firmware_class loader at. This lets one rootfs boot on multiple devices
without baking in per-device firmware.

%prep
%autosetup -C -p1

%build

%install
install -Dm755 msm-firmware-loader.sh %{buildroot}%{_bindir}/msm-firmware-loader.sh
install -Dm755 msm-firmware-loader-unpack.sh %{buildroot}%{_bindir}/msm-firmware-loader-unpack.sh
install -Dm644 msm-firmware-loader.service %{buildroot}%{_unitdir}/msm-firmware-loader.service
install -Dm644 msm-firmware-loader-unpack.service %{buildroot}%{_unitdir}/msm-firmware-loader-unpack.service

%post
%systemd_post msm-firmware-loader.service msm-firmware-loader-unpack.service

%preun
%systemd_preun msm-firmware-loader.service msm-firmware-loader-unpack.service

%postun
%systemd_postun_with_restart msm-firmware-loader.service msm-firmware-loader-unpack.service

%files
%license LICENSE
%doc README.md
%{_bindir}/msm-firmware-loader.sh
%{_bindir}/msm-firmware-loader-unpack.sh
%{_unitdir}/msm-firmware-loader.service
%{_unitdir}/msm-firmware-loader-unpack.service

%changelog
* Tue Sep 15 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
