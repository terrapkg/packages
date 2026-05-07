Name:           compat-nvidia-repo-580xx
Version:        580.159.03
Epoch:          3
Release:        1%{?dist}
Summary:        Compatibility package required by official CUDA packages
License:        NVIDIA License
URL:            https://developer.nvidia.com/cuda-toolkit
Requires:       nvidia-driver-580xx >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-580xx-cuda >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-580xx-cuda-libs >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-580xx-libs >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-580xx-kmod >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-settings-580xx >= %{?epoch:%{epoch}:}%{version}
Provides:       cuda-drivers-580xx >= %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-open-580xx >= %{?epoch:%{epoch}:}%{version}
# Add any versioned provides:
Provides:       cuda-drivers-560 >= %{?epoch:%{epoch}:}%{version}
Provides:       cuda-drivers-565 >= %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-open-560 >= %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-open-565 >= %{?epoch:%{epoch}:}%{version}
Provides:       compat-nvidia-repo-580 = %{evr}
BuildArch:      noarch
Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
Nvidia drivers metapackage required by official CUDA packages. It pulls in all
Nvidia driver components.

%files
# Without an empty files section the package is not created.

%changelog
* Mon Apr 13 2026 Gilver E. <roachy@fyralabs.com> - 3:580.142-3
- Update spec for Terra packaging team
