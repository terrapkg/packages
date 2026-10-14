%global appid io.github.fovty.HushMic
# hushmic specifically only resolves these to /usr/lib so we can't use the _libdir macro
%global privlibdir /usr/lib/hushmic
%global ladspadir /usr/lib/ladspa

ExclusiveArch:  x86_64

Name:           hushmic
Version:        0.10.2
Release:        1%{?dist}
Summary:        Real-time microphone noise suppression as a virtual mic
License:        MIT OR Apache-2.0
URL:            https://github.com/Fovty/hushmic
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://huggingface.co/Ceva-IP/DPDFNet/resolve/dd6818d00f50c836fed43a6243ebe49116de5964/onnx/dpdfnet8_48khz_hr.onnx
Source2:        https://huggingface.co/Ceva-IP/DPDFNet/resolve/dd6818d00f50c836fed43a6243ebe49116de5964/onnx/dpdfnet2_48khz_hr.onnx
Source3:        %{url}/releases/download/v%{version}/dpdfnet8_48khz_hr.weights.f32
Source4:        %{url}/releases/download/v%{version}/dpdfnet2_48khz_hr.weights.f32

# hushmic technically needs onnxruntime >=1.23.0, but this one line patch makes it work on as old as 1.18.0.
# f43 and f44 are on older onnxruntime versions so they need this patch to work.
%if 0%{?fedora} == 43 || 0%{?fedora} == 44
Patch0:         hushmic-optimization-level-compat.patch
%endif

BuildRequires:  rust
BuildRequires:  cargo-rpm-macros
BuildRequires:  anda-srpm-macros
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  terra-appstream-helper
BuildRequires:  systemd-rpm-macros

Requires:       pipewire
Requires:       pipewire-utils
Requires:       pipewire-pulseaudio
Requires:       wireplumber
Requires:       hicolor-icon-theme
Requires:       onnxruntime >= 1.18

Packager:       Caleb Jones <caleb@fyralabs.com>

%description
Real-time microphone noise suppression for Linux, as a system-wide virtual mic.


%prep
%autosetup -n HushMic-%{version} -p1
%cargo_prep_online

%build
export HUSHMIC_BUILD_MODEL=%{_datadir}/hushmic/models/dpdfnet8_48khz_hr.onnx
export HUSHMIC_BUILD_DYLIB=%{privlibdir}/libonnxruntime.so
%cargo_build

%install
install -Dm755 target/rpm/hushmic %{buildroot}%{_bindir}/hushmic
install -Dm755 target/rpm/libdpdfnet_ladspa.so %{buildroot}%{ladspadir}/libdpdfnet_ladspa.so

install -d -m755 %{buildroot}%{privlibdir}
ln -s ../../%{_lib}/libonnxruntime.so.1 %{buildroot}%{privlibdir}/libonnxruntime.so

install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/hushmic/models/dpdfnet8_48khz_hr.onnx
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/hushmic/models/dpdfnet2_48khz_hr.onnx
install -Dm644 %{SOURCE3} %{buildroot}%{_datadir}/hushmic/models/dpdfnet8_48khz_hr.weights.f32
install -Dm644 %{SOURCE4} %{buildroot}%{_datadir}/hushmic/models/dpdfnet2_48khz_hr.weights.f32


install -Dm644 packaging/hushmic.desktop %{buildroot}%{_appsdir}/%{appid}.desktop

install -Dm644 packaging/systemd/hushmic.service %{buildroot}%{_userunitdir}/hushmic.service

mkdir -p %{buildroot}%{_iconsdir}/hicolor
cp -a packaging/tray/hicolor/. %{buildroot}%{_iconsdir}/hicolor/
install -Dm644 packaging/hushmic-256.png %{buildroot}%{_hicolordir}/256x256/apps/hushmic.png

%terra_appstream -o packaging/flatpak/%{appid}.metainfo.xml

%cargo_license_summary_online
%{cargo_license_online} > LICENSE.dependencies

%check
%desktop_file_validate %{buildroot}%{_appsdir}/%{appid}.desktop

%post
%systemd_user_post hushmic.service

%preun
%systemd_user_preun hushmic.service

%postun
%systemd_user_postun_with_restart hushmic.service

%files
%license LICENSE-MIT LICENSE-APACHE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/hushmic
%dir %{ladspadir}
%{ladspadir}/libdpdfnet_ladspa.so
%dir %{privlibdir}
%{privlibdir}/libonnxruntime.so
%dir %{_datadir}/hushmic
%{_datadir}/hushmic/models/
%{_appsdir}/%{appid}.desktop
%{_userunitdir}/hushmic.service
%{_hicolordir}/256x256/apps/hushmic.png
%{_hicolordir}/*/status/hushmic*.png
%{_hicolordir}/*/status/hushmic*.svg
%{_metainfodir}/%{appid}.metainfo.xml

%changelog
* Tue Oct 13 2026 Caleb Jones <caleb@fyralabs.com> - 0.10.2
- Initial package
