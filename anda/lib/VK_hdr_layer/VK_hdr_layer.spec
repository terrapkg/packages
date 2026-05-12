%global commit 57b26b8927b133566be13a7702f74a62109bad15
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260325

Name:           VK_hdr_layer
Version:        0^%{commitdate}git%{shortcommit}
Release:        1%{?dist}
Epoch:          1
Summary:        Vulkan Wayland HDR WSI Layer
License:        MIT
URL:            https://github.com/zamundaaa/VK_hdr_layer
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.58
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(wayland-scanner)
# Temporary solution until upstream builds with newer VKroots
%dnl BuildRequires:  pkgconfig(vkroots)
BuildRequires:  pkgconfig(wayland-client)
# KWin is the main reference supported compositor
Enhances:       kwin-wayland >= 6.3
Obsoletes:      VK_hdr_layer < 1:0^20250416git3b276e6
Packager:       Gilver E. <roachy@fyralabs.com>

%description
Vulkan layer utilizing a small color management/HDR
protocol for experimentation.
The proposed mainline protocol for color management is
wp_color_management.

This implements the following vulkan extensions,
if the protocol is supported by the compositor.

* VK_EXT_swapchain_colorspace
* VK_EXT_hdr_metadata


%prep
%dnl %autosetup -n %{name}-%{commit} -p1
%git_clone %{url}.git %{commit}

%conf
%meson --libdir=%{_libdir}/%{name}

%build
%meson_build

%install
%meson_install --skip-subprojects=vkroots

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}/libVkLayer_hdr_wsi.so
%{_datadir}/vulkan/implicit_layer.d/VkLayer_hdr_wsi.*.json


%changelog
* Sat Apr 18 2026 Gilver E. <roachy@fyralabs.com> - 1:0^20260325git57b26b8-1
- Adopt for Terra

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20250416.3b276e6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20250416.3b276e6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20250416.3b276e6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Apr 21 2025 Neal Gompa <ngompa@fedoraproject.org> - 0~git20250416.3b276e6-1
- Update to git snapshot with support for finalized color management protocol

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20241018.e173f26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git20241018.e173f26-1
- Update to git snapshot
- Install library to private subdirectory

* Sun Sep 08 2024 Neal Gompa <ngompa@fedoraproject.org> - 0~git20240427.e47dc6d-1
- Initial package
