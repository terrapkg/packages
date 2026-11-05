Name:			multipass
Version:		1.16.4
Release:		1%{?dist}
Summary:		Multipass orchestrates virtual Ubuntu instances
License:		GPL-3.0-or-later
URL:			https://canonical.com/multipass

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mold
BuildRequires:  ninja-build
BuildRequires:  cmake(fmt)
BuildRequires:  openssl-devel
BuildRequires:  cmake(gRPC)
BuildRequires:  cmake(yaml-cpp)
BuildRequires:  cmake(semver)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Network)

%description
Multipass is a lightweight VM manager for Linux, Windows and macOS. It's
designed for developers who want to spin up a fresh Ubuntu environment with a
single command. It uses KVM on Linux, Hyper-V on Windows and QEMU on macOS to
run virtual machines with minimal overhead. It can also use VirtualBox on
Windows and macOS. Multipass will fetch Ubuntu images for you and keep them up
to date.

%prep
%git_clone https://github.com/canonical/%{name}.git v%{version}

%conf
export VCPKG_FORCE_SYSTEM_BINARIES=1
export CMAKE_MAKE_PROGRAM=Ninja
%cmake .

%build
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE

%changelog
* Mon Oct 27 2025 Jaiden Riordan <jade@fyralabs.com>
- Initial package
