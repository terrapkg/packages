Name:           multipass
Version:        1.16.3
Release:        1%?dist
Summary:        Multipass orchestrates virtual Ubuntu instances
License:        GPL-3.0-only
URL:            https://canonical.com/multipass
BuildSystem:    cmake
BuildRequires:  rust-packaging mold 

%description
Multipass is a lightweight VM manager for Linux, Windows and macOS. It's designed for developers who want to spin up a fresh Ubuntu environment with a single command. It uses KVM on Linux, Hyper-V on Windows and QEMU on macOS to run virtual machines with minimal overhead. It can also use VirtualBox on Windows and macOS. Multipass will fetch Ubuntu images for you and keep them up to date.

%prep
%git_clone https://github.com/canonical/multipass

%conf -p
%ifarch aarch64
export VCPKG_FORCE_SYSTEM_BINARIES=1
%endif

%files
%doc README.md SECURITY.md CONTRIBUTING.md
%license LICENSE
