Name:			multipass
Version:		1.16.1
Release:		1%?dist
Summary:		Multipass orchestrates virtual Ubuntu instances
License:		GPL-3.0
URL:			https://canonical.com/multipass

BuildRequires:          cmake gcc-c++ mold ninja-build cmake(fmt) openssl-devel cmake(gRPC) cmake(yaml-cpp) cmake(semver) cmake(Qt6) cmake(Qt6Core) cmake(Qt6Concurrent) cmake(Qt6Network)

%description
Multipass is a lightweight VM manager for Linux, Windows and macOS. It's
designed for developers who want to spin up a fresh Ubuntu environment with a
single command. It uses KVM on Linux, Hyper-V on Windows and QEMU on macOS to
run virtual machines with minimal overhead. It can also use VirtualBox on
Windows and macOS. Multipass will fetch Ubuntu images for you and keep them up
to date.

%prep
%git_clone https://github.com/canonical/%{name}.git v%{version}

%build
export VCPKG_FORCE_SYSTEM_BINARIES=1
%cmake .
%cmake_build

%install
%cmake_install

%files

%changelog
* Mon Oct 27 2025 Jaiden Riordan <jade@fyralabs.com>
- Initial package
