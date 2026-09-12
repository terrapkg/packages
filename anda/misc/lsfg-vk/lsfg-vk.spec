Name:           lsfg-vk
Version:        2.0.0
Release:        2%{?dist}
Summary:        Lossless Scaling Frame Generation on Linux
License:        CC-BY-NC-ND-4.0
URL:            https://lsfg-vk.dev
Source0:        https://git.lsfg-vk.dev/lsfg-vk/snapshot/lsfg-vk-%{version}.tar.xz
Packager:       Owen Zimmerman <owen@fyralabs.com>
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
%{summary}.

%package    ui
Summary:    UI for %{name}
Requires:   %{name} = %{evr}
Requires:   qt6-qtdeclarative
Requires:   qt6-qtbase

%description ui
GUI for lsfg-vk.

%prep
%autosetup -C

%conf
%cmake -DLSFGVK_BUILD_UI=ON

%build
%cmake_build

%install
%cmake_install

%post
if ! rpm -q lsfg-vk-ui &>/dev/null; then
    echo "=============================================================="
    echo "If you want the UI for lsfg-vk, you should install lsfg-vk-ui"
    echo "    sudo dnf install lsfg-vk-ui"
    echo "=============================================================="
fi

%files
%license LICENSE.txt
%{_bindir}/lsfg-vk-cli
%{_libdir}/liblsfg-vk-layer.so
%{_datadir}/vulkan/implicit_layer.d/VkLayer_LSFGVK_frame_generation.json

%files ui
%{_bindir}/lsfg-vk-ui
%{_appsdir}/gay.pancake.lsfg-vk-ui.desktop
%{_hicolordir}/256x256/apps/gay.pancake.lsfg-vk-ui.png

%changelog
* Thu Sep 10 2026 Owen Zimmerman <owen@fyralabs.com> - 2.0.0-1
- Initial commit
