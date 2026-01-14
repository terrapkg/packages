Name:           compat-nvidia-repo-580
Version:        580.126.09
Epoch:          3
Release:        1%?dist
Summary:        Compatibility package required by official CUDA packages
License:        NVIDIA License
URL:            https://developer.nvidia.com/cuda-toolkit

BuildArch:      noarch

Requires:       nvidia-driver-580 >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-580-cuda >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-580-cuda-libs >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-580-libs >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-580-kmod >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-settings-580 >= %{?epoch:%{epoch}:}%{version}

Provides:       cuda-drivers-580 >= %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-open-580 >= %{?epoch:%{epoch}:}%{version}
# Add any versioned provides:
Provides:       cuda-drivers-560 >= %{?epoch:%{epoch}:}%{version}
Provides:       cuda-drivers-565 >= %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-open-560 >= %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-open-565 >= %{?epoch:%{epoch}:}%{version}

%description
Nvidia drivers metapackage required by official CUDA packages. It pulls in all
Nvidia driver components.

%files
# Without an empty files section the package is not created.

%changelog
%autochangelog
