%define debug_package %{nil}

%global _description %{expand:
libfiber is a high-performance coroutine library designed for building efficient network applications across multiple platforms.
Originating from the coroutine module in the acl project, libfiber supports Linux, FreeBSD, macOS, and Windows operating systems.
The library enables developers to write highly concurrent applications using synchronous programming paradigms while achieving performance comparable to or better than asynchronous frameworks.}

Name:           libfiber-devel
Version:        1.1.0
Release:        1%?dist
URL:            https://deepwiki.com/iqiyi/libfiber
Source0:        https://github.com/iqiyi/libfiber/archive/refs/tags/v%version.tar.gz
Patch0:         add-missing-header.patch
Summary:        The high performance c/c++ coroutine/fiber library for Linux/FreeBSD/MacOS/Windows, supporting select/poll/epoll/kqueue/iouring/iocp/windows GUI
License:        LGPL-3.0
ExclusiveArch:  x86_64

Packager:       Owen Zimmerman <owen@fyralabs.com>

BuildRequires:  gcc-c++ make

%description %_description

%prep
%autosetup -n libfiber-%{version} -p1

%build
%make_build

%install
mkdir -p %{buildroot}%{_includedir}/fiber/
install -Dm644 c/include/fiber/*.h %{buildroot}%{_includedir}/fiber/
install -Dm644 cpp/include/fiber/*.hpp %{buildroot}%{_includedir}/fiber/

%files
%license LICENSE.txt
%doc README.md README_cn.md changes.txt
%{_includedir}/fiber/

%changelog
* Wed Dec 31 2025 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
