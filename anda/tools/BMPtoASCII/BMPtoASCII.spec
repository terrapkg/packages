%global commit 1025c80c56706da71c8309806cdd19f1dbc993ce
%global commit_date 20221114
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%define debug_package %{nil}

Name:          BMPtoASCII
Version:       0~%{commit_date}git.%{shortcommit}
Release:       1%{?dist}
Summary:       Converts 24 bit bitmap images to ASCII art
License:       MIT
URL:           https://github.com/xkevio/BMPtoASCII
Source0:       %{url}/archive/%{commit}/BMPtoASCII-%{commit}.tar.gz

BuildSystem:   cmake
BuildRequires: gcc-c++
BuildRequires: cmake
Provides:      bmptoascii

Packager:      Owen Zimmerman <owen@fyralabs.com>

%description
will try to read in .bmp files and
convert them to lovely ASCII art with
the given set of characters ordered
from "fullest" to "empty" (black to white).

%install -a
install -Dm755 %{__cmake_builddir}/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/BMPtoASCII

%changelog
* Fri Nov 13 2026 Owen Zimmerman <owen@fyralabs.com>
- Initial commit
