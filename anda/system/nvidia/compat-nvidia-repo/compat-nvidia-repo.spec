Name:           compat-nvidia-repo
Version:        595.58.03
Epoch:          3
Release:        2%{?dist}
Summary:        Compatibility package required by official CUDA packages
License:        NVIDIA License
URL:            https://developer.nvidia.com/cuda-toolkit
Requires:       nvidia-driver >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-cuda >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-cuda-libs >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-libs >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-kmod >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-settings >= %{?epoch:%{epoch}:}%{version}
Provides:       cuda-drivers >= %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-open >= %{?epoch:%{epoch}:}%{version}
# Add any versioned provides:
Provides:       cuda-drivers-560 >= %{?epoch:%{epoch}:}%{version}
Provides:       cuda-drivers-565 >= %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-open-560 >= %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-open-565 >= %{?epoch:%{epoch}:}%{version}
BuildArch:      noarch
Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
Nvidia drivers metapackage required by official CUDA packages. It pulls in all
Nvidia driver components.

%files
# Without an empty files section the package is not created.

%changelog
* Mon Apr 13 2026 Gilver E. <roachy@fyralabs.com> - 3:595.58.03-2
- Update spec for Terra packaging team
