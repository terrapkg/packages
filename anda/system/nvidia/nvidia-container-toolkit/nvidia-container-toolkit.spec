Name:           nvidia-container-toolkit
Version:        1.17.4
Release:        1%?dist
Summary:        NVIDIA Container Toolkit
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/NVIDIA/nvidia-container-toolkit
Source0:        https://github.com/NVIDIA/%{name}/archive/v%{version}/nvidia-container-toolkit-v%{version}.tar.gz
BuildRequires:  containers-common
BuildRequires:  golang >= 1.16
Requires:       libnvidia-container-tools
Supplements:    (nvidia-driver and moby-engine)
Supplements:    (nvidia-driver and cri-o)
Supplements:    (nvidia-driver and containerd)


%description
Build and run containers leveraging NVIDIA GPUs.

%prep
%autosetup

%build
go build -v \
    -o bin/nvidia-ctk \
    ./cmd/nvidia-ctk

go build -v \
    -o bin/nvidia-container-runtime-hook \
    ./cmd/nvidia-container-runtime-hook

go build -v \
    -o bin/nvidia-container-runtime \
    ./cmd/nvidia-container-runtime


%install
install -D -m 0755 bin/nvidia-ctk %{buildroot}%{_bindir}/nvidia-ctk
install -D -m 0755 bin/nvidia-container-runtime-hook %{buildroot}%{_bindir}/nvidia-container-runtime-hook
install -D -m 0755 bin/nvidia-container-runtime %{buildroot}%{_bindir}/nvidia-container-runtime
mkdir -p %{buildroot}%{_sysconfdir}/nvidia-container-runtime

%post
if rpm -q --quiet moby-engine; then
    if 'docker info -f "{{println .SecurityOptions}}" | grep rootless'; then
      nvidia-ctk runtime configure --runtime=docker --config="$HOME"/.config/docker/daemon.json
        if systemctl --user is-running docker >/dev/null; then
            systemctl --user restart docker
        fi
       nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
    else nvidia-ctk runtime configure --runtime=docker
        if systemctl is-running docker >/dev/null; then
            systemctl restart docker
        fi
    fi
elif rpm -q --quiet containerd; then
   nvidia-ctk runtime configure --runtime=containerd
    if systemctl is-running containerd >/dev/null; then
        systemctl restart containerd
    fi
elif rpm -q --quiet cri-o; then
    nvidia-ctk runtime configure --runtime=crio
     if systemctl is-running crio >/dev/null; then
         systemctl restart crio
     fi
 elif rpm -q --quiet podman; then
     nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
fi

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/nvidia-ctk
%{_bindir}/nvidia-container-runtime
%{_bindir}/nvidia-container-runtime-hook
%dir %{_sysconfdir}/nvidia-container-runtime
%ghost %config(noreplace) %{_sysconfdir}/nvidia-container-runtime/config.toml

%changelog
%autochangelog
