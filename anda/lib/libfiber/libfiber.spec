%define debug_package %{nil}

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

%description
The libfiber project comes from the coroutine module of the acl project in lib_fiber directory of which.
It can be used on OS platforms including Linux, FreeBSD, macOS, and Windows, which supports select, poll,
epoll, kqueue, iocp, and even Windows GUI messages for different platform. With libfiber, you can write
network application services having the high performance and large concurrent more easily than the traditional
asynchronous framework with event-driven model. What's more, with the help of libfiber, you can even write
network module of the Windows GUI application written by MFC, wtl or other GUI framework on Windows in coroutine way.

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
