Name:           vulkan-low-latency-layer
Version:        0.2.0
Release:        1%{?dist}
Summary:        Vulkan layer for hardware agnostic input latency reduction
Packager:       Kyle Gospodnetich <me@kylegospodneti.ch>

License:        MIT
URL:            https://github.com/Korthos-Software/low_latency_layer
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  vulkan-headers
BuildRequires:  cmake(VulkanUtilityLibraries)
BuildRequires:  pkgconfig(vulkan)

Requires:       vulkan-loader

%description
A Vulkan layer that reduces click-to-photon latency by
implementing both AMD and NVIDIA's latency reduction technologies,
providing hardware-agnostic implementations of the VK_NV_low_latency2
and VK_AMD_anti_lag device extensions.

%prep
%autosetup -n low_latency_layer-%{version}

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libVkLayer_KORTHOS_LowLatency.so
%{_datadir}/vulkan/implicit_layer.d/low_latency_layer.json

%changelog
* Fri May 22 2026 Kyle Gospodnetich <me@kylegospodneti.ch> - 0.1.0-1
- Initial package
